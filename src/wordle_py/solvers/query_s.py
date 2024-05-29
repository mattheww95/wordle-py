"""
Basic attempt at a simple solver for wordle

Matthew Wells: 2024-05-22
"""

from wordle_py.words.words import Words, Status
import pandas as pd
from typing import Optional, List, Tuple


class QuerySolver:
    """
    A simple solver based off of querying the data table
    """

    def __init__(self, words: Words) -> None:
        self.words_obj = words
        self.data = self.words_obj.words.copy(deep=True)

    def select_word(self, words: Optional[pd.DataFrame]=None) -> str:
        """
        Select an initial start word
        """
        data = self.data if words is None else self.data
        start_word = None
        for idx in data.index:
            if len(idx) == len(set(idx)):
                start_word = idx
                break
        start_word = idx
        return start_word


    def update_dataframe(self, guess: List[Tuple[str, Status]], data_in: Optional[pd.DataFrame]=None):
        """
        update the dataframe for the updated test
        """
        data = self.data if data_in is None else data_in
        data.drop(index="".join([i[0] for i in guess]), inplace=True)
        for k, v in enumerate(guess):
            status = v[1]
            letter = v[0]
            if status == Status.WRONG:
                data = data[~data.index.str.contains(letter)]
            elif status == Status.CONTAINED:
                data = data[data.index.str.contains(letter)]
            else:
                data = data[data[k] == letter]
        return data

    def solve_word(self) -> str:
        """
        solver the wordle word
        """
        guesses = 0
        while True:
            guess_word = self.select_word(self.data)
            guess_out = self.words_obj.guess(guess_word, False)
            if self.words_obj.word_correct(guess_out):
                break
            self.data = self.update_dataframe(guess_out, self.data)
            guesses += 1
        return f"Program {self.__class__.__name__} solved puzzle in {guesses} guesses"


if __name__ == "__main__":
    words = Words(42)
    qs = QuerySolver(words)
    out_str = qs.solve_word()
    print(out_str)

