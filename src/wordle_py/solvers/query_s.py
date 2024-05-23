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

    def select_word(self, words: Optional[Words]=None) -> str:
        """
        Select an initial start word
        """

        data = self.words_obj.words if words is None else words.words
        start_word = None
        for idx in data.index:
            if len(idx) == len(set(idx)):
                start_word = idx
                break
        start_word = idx
        return start_word

    def process_guess(self, guess: List[Tuple[str, Status]], words: Optional[Words]=None) -> Optional[pd.DataFrame]:
        """
        Process a guess to determine to filter the word list
        """
        data = self.words_obj.words if words is None else words.words
        bool_list = [True if i[1] == Status.CORRECT else False for i in guess]
        if all(bool_list):
            print(f"word found! {guess}")
            return None

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

    def solve_word(self):
        """
        solver the wordle word
        """
        while not self.words_obj.matched:
            guess_word = self.select_word()
            guess_out = self.words_obj.guess(guess_word)
            self.words_obj.words = self.process_guess(guess_out)




if __name__ == "__main__":
    words = Words(42)
    qs = QuerySolver(words)
    qs.solve_word()

