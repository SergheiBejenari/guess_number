import random

from src.game.exceptions import RestartGameException, GiveUpException
from src.cli.input_utils import get_number_range
from src.game.messages import success_message, hint_message, temperature_hint


class GuessNumberGame:
    def __init__(self):
        self.min_val = None
        self.max_val = None
        self.number_to_guess = None
        self.attempts = 0

    def setup_game(self):
        self.min_val, self.max_val = get_number_range()
        self.number_to_guess = random.randint(self.min_val, self.max_val)

    def get_user_guess(self):
        while True:
            try:
                user_input = input(f"Enter your guess ({self.min_val}–{self.max_val}): ").strip().lower()

                if user_input == "/info":
                    print("ℹ️  Enter a WHOLE number in the range, or use /quit /restart /giveup.")
                    continue

                if user_input == "/quit":
                    print("👋 Game exited. See you next time!")
                    exit(0)

                if user_input == "/restart":
                    raise RestartGameException()

                if user_input == "/giveup":
                    raise GiveUpException()

                guess = float(user_input)

                if not guess.is_integer():
                    print("📏 Whole numbers only. Try again!")
                    continue

                guess = int(guess)

                if guess < self.min_val or guess > self.max_val:
                    print(f"🚧 Your guess is out of range! Stay between {self.min_val} and {self.max_val}.")
                    continue

                return guess

            except ValueError:
                print("🤖 That doesn't look like a number. Please enter a whole number.")

    def play(self):
        while True:
            # 👉 Reset the game state
            self.min_val = None
            self.max_val = None
            self.number_to_guess = None
            self.attempts = 0

            try:
                # 🌱 Start a new game
                self.setup_game()
                print(f"\n🎯 I've picked a number between {self.min_val} and {self.max_val}. Can you guess it?\n")

                previous_distance = None
                non_progress_streak = 0

                while True:
                    guess = self.get_user_guess()
                    self.attempts += 1

                    distance = abs(guess - self.number_to_guess)

                    if previous_distance is not None:
                        if distance < previous_distance:
                            print("🔥 You're getting warmer!")
                            non_progress_streak = 0
                        elif distance > previous_distance:
                            print("❄️ You're getting colder...")
                            non_progress_streak += 1
                        else:
                            print("😐 Same distance as before.")
                            non_progress_streak += 1
                    else:
                        non_progress_streak = 1

                    previous_distance = distance
                    temperature_hint(distance)

                    if guess == self.number_to_guess:
                        success_message(self.attempts)
                        break

                    direction = "Higher" if guess < self.number_to_guess else "Lower"
                    if non_progress_streak >= 3:
                        print("❗ Seems like you're not getting any closer...")
                        hint_message(direction)
                        non_progress_streak = 0

                break  # Exit the outer loop if the game was successfully completed

            except RestartGameException:
                print("🔁 Game is restarting...\n")
                continue  # Restart everything from the beginning

            except GiveUpException:
                print(f"😢 Don't worry. The correct number was: {self.number_to_guess}")
                break  # End the game after giving up
