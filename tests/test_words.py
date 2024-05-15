import pytest
from wordle_py.words.words import Words


@pytest.fixture(scope="class")
def words():
    return Words(seed_value=42)


selected_words ="buzzy".upper()

def test_random_word(words):
    rnd_words = words.random_word()
    assert rnd_words == list(selected_words)


def test__word_init(words):
    assert words.word == selected_words
    

def test_characters(words):
    assert words.characters == set([*selected_words])
