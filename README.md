# 🎯 Guess the Number (CLI Game)

A fun, interactive console game where the computer picks a secret number, and you try to guess it!  
The game gives you helpful feedback like "cold", "warm", "hot", and more, based on how close your guess is.

---

## 🚀 How to Play

1. Run the game:
   ```bash
   python -m cli.main
   ```

2. Enter a **minimum** and **maximum** whole number for the range (e.g., 1–100).

3. Try to guess the number — the game will guide you:
    - ❄️ "Freezing cold"
    - 🧊 "Cold"
    - 🌤 "Warm"
    - 🔥 "Hot"
    - 🔥🔥 "Burning hot"

4. You’ll also get:
    - ✅ Messages like **"You’re getting warmer!"** if you’re moving in the right direction
    - ❌ Warnings like **"You're getting colder..."** if you're moving away from the number
    - 📣 After 3 bad guesses in a row, the game gives you a directional hint: **Try Higher / Lower**

---

## 💬 Available Commands (can be entered at any time)

| Command     | Description                           |
|-------------|---------------------------------------|
| `/info`     | Show help and input rules             |
| `/restart`  | Restart the game from the beginning   |
| `/giveup`   | Show the correct number and end game  |
| `/quit`     | Exit the game immediately             |

---

## 🧠 Example Gameplay

```
Enter the MINIMUM: 1  
Enter the MAXIMUM: 100  

🎯 I've picked a number between 1 and 100. Can you guess it?

Enter your guess (1–100): 90  
❄️ You're FREEZING cold!

Enter your guess (1–100): 70  
🔥 You're getting warmer!  
🧊 It's getting COLD.

Enter your guess (1–100): /giveup  
😢 Don't worry. The correct number was: 42
```

---

## ⚙️ Requirements

- Python 3.7+
- No external libraries required

---

## 📁 Project Structure

```
guess_number_game/
├── cli/
│   ├── main.py               # Entry point
│   └── input_utils.py        # User input and validation
├── game/
│   ├── engine.py             # Game logic
│   ├── messages.py           # Output messages
│   └── exceptions.py         # Custom exceptions for commands
├── tests/
│   └── test_engine.py        # Tests for game logic
├── requirements.txt
└── README.md
```

---

## ✅ To Do / Ideas

- Add color output using `colorama`
- Add difficulty presets: `/easy`, `/hard`
- Track history of guesses
- Add `/debug` mode to reveal the secret number
- ✨ Create a GIF animation of the game for GitHub

---

## 💖 Have fun & happy guessing!
