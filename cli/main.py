from game.engine import GuessNumberGame
from game.messages import welcome_message


def main():
    welcome_message()
    game = GuessNumberGame()
    game.play()


if __name__ == "__main__":
    main()
