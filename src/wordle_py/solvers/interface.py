"""
Interface for various solver, for methods and properties they 
must implement.

Matthew Wells: 2024-05-28
"""


from abc import ABC, abstractmethod
from wordle_py.words.words import Words, Status
from typing import List, Tuple

class Solver(ABC):
    """
    Interface for each class to invoke
    """


    def __init__(self, words: Words) -> None:
        self.words = words


    def process_guess(self, guess: List[Tuple[str, Status]]) -> Bool:
        """
        Process the guess to determine if it is correct or not
        """
        bools_list = [True if i[1] == Status.CORRECT else False for i in guess]
        if all(bool_list):
            return True
        return False
