import sys

from src.game.exceptions import RestartGameException, GiveUpException


def show_info():
    print("\n📘 Input Guide:")
    print("- Enter WHOLE numbers only (e.g., 10, 42, 123).")
    print("- Decimal numbers like 2.5 or 3.0 are not accepted.")
    print("- Avoid letters or special characters.")
    print("- Forbidden characters include:")
    print("  ! @ # $ % ^ & * ( ) _ = + [ ] { } \\ | ; : ' \" < > ? , /")
    print("- The minimum value must be LESS than the maximum.\n")


def get_single_value(prompt, game_started=False):
    forbidden_chars = "!@#$%^&*()_=+[]{}\\|;:'\"<>?,/"

    while True:
        user_input = input(prompt).strip().lower()

        if user_input == "/info":
            print("\n📘 Input Guide:")
            print("- Enter WHOLE numbers only (e.g., 10, 42, 123).")
            print("- No decimals or special characters.")
            print("- Commands you can use anytime:")
            print("  /info – show this help")
            print("  /restart – restart the game")
            print("  /giveup – give up and reveal the answer")
            print("  /quit – exit the game\n")
            continue

        if user_input == "/quit":
            print("👋 Game exited. See you next time!")
            sys.exit(0)

        if user_input == "/restart":
            raise RestartGameException()

        if user_input == "/giveup":
            if game_started:
                raise GiveUpException()
            else:
                print("⚠️ You can't give up before the game has started.")
                print("👉 You can use /quit to exit or /restart to start over.\n")
                continue

        if not user_input:
            print("😅 You forgot to type something. Try again.\n")
            continue

        forbidden_used = [c for c in user_input if c in forbidden_chars]
        if forbidden_used:
            print(f"🚫 Special characters are not allowed. You used: {' '.join(forbidden_used)}\n")
            continue

        try:
            value = float(user_input)

            if not value.is_integer():
                print("📏 Whole numbers only. No decimals!\n")
                continue

            return int(value)

        except ValueError:
            print("🤖 That doesn't look like a number. Whole numbers only, please!\n")


def get_number_range():
    while True:
        min_val = get_single_value("Enter the MINIMUM whole number of the range: ", game_started=False)
        max_val = get_single_value("Enter the MAXIMUM whole number of the range: ", game_started=False)

        if min_val >= max_val:
            print("🔄 The minimum must be LESS than the maximum. Let's try again.\n")
            continue

        return min_val, max_val
