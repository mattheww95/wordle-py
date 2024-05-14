import pytest
from wordle_py import data




def test_read_words():
    test = data.get_data()
    length_file = 5757
    assert length_file == len(test)

