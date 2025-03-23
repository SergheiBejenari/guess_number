import pytest

from src.game.engine import GuessNumberGame
from src.game.exceptions import RestartGameException, GiveUpException


# Test setup_game correctly sets values

def test_setup_game_sets_range(monkeypatch):
    monkeypatch.setattr("src.game.engine.get_number_range", lambda: (10, 20))
    game = GuessNumberGame()
    game.setup_game()

    assert game.min_val == 10
    assert game.max_val == 20
    assert 10 <= game.number_to_guess <= 20


# Test that guess returns an int in range

def test_get_user_guess_valid(monkeypatch):
    game = GuessNumberGame()
    game.min_val = 1
    game.max_val = 100

    monkeypatch.setattr("builtins.input", lambda _: "42")
    guess = game.get_user_guess()
    assert guess == 42


# Test /giveup triggers GiveUpException after game started

def test_giveup_during_guess(monkeypatch):
    game = GuessNumberGame()
    game.min_val = 1
    game.max_val = 100

    monkeypatch.setattr("builtins.input", lambda _: "/giveup")

    with pytest.raises(GiveUpException):
        game.get_user_guess()


# Test /restart during guess

def test_restart_during_guess(monkeypatch):
    game = GuessNumberGame()
    game.min_val = 1
    game.max_val = 100

    monkeypatch.setattr("builtins.input", lambda _: "/restart")

    with pytest.raises(RestartGameException):
        game.get_user_guess()


# Test invalid non-numeric input

def test_non_numeric_guess(monkeypatch, capsys):
    inputs = iter(["hello", "50"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    game = GuessNumberGame()
    game.min_val = 1
    game.max_val = 100

    guess = game.get_user_guess()
    captured = capsys.readouterr()

    assert "doesn't look like a number" in captured.out
    assert guess == 50
