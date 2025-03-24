def welcome_message():
    print("🎉 Welcome to the 'Guess the Number' game!")


def success_message(attempts):
    print(f"🎉 Congratulations! You guessed the number in {attempts} attempt(s)!")


def hint_message(direction):
    print(f"❗ Try {direction}!")


def temperature_hint(distance):
    if distance == 0:
        return  # Exact match — don't say anything
    elif distance <= 2:
        print("🔥🔥 You're BURNING HOT!")
    elif distance <= 5:
        print("🔥 You're HOT!")
    elif distance <= 10:
        print("🌤 You're WARM.")
    elif distance <= 20:
        print("🧊 It's getting COLD.")
    else:
        print("❄️ You're FREEZING cold!")
