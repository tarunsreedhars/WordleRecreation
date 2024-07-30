# test_wordle.py
import pytest
from wordle import load_dict, determine_unguessed_letters, determine_color
from config import GREY, GREEN, YELLOW


@pytest.fixture
def sample_guesses():
    return ["CRANE", "SLATE"]


@pytest.fixture
def sample_answer():
    return "SLATE"


def test_load_dict(tmp_path):
    dict_file = tmp_path / "test_dict.txt"
    dict_file.write_text("crane\nslate\nstone")

    words = load_dict(dict_file)
    assert words == ["CRANE", "SLATE", "STONE"]


def test_determine_unguessed_letters(sample_guesses):
    unguessed = determine_unguessed_letters(sample_guesses)
    assert unguessed == "BDFGHIJKMOPQUVWXYZ"
