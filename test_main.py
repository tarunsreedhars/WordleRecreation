# test_main.py
import pygame
import pytest
from unittest.mock import patch, Mock
from main import Main

@pytest.fixture
def game_instance():
    return Main()

def test_initialization(game_instance):
    assert game_instance.input == ""
    assert game_instance.guesses == []
    assert game_instance.unguessed == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert game_instance.game_over == False

@patch('main.random.choice')
def test_reset_game(mock_random_choice, game_instance):
    mock_random_choice.return_value = "SLATE"
    game_instance.reset_game()
    assert game_instance.answer == "SLATE"
    assert game_instance.input == ""
    assert game_instance.guesses == []
    assert game_instance.unguessed == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert game_instance.game_over == False
