"""
Select and query words for look up.

2024-05-10: Matthew Wells
"""
from colorama import Fore, Style, Back
from typing import Optional, List, Tuple
from wordle_py import data
from random import randrange, seed
from functools import partial
from enum import Enum, auto


class Status(Enum):
    CORRECT = auto()
    CONTAINED = auto()
    WRONG = auto()


class Words:
    """
    Query words for usage and look them up where needed
    """
    __capital_letters_range = range(65,91)
    def __init__(self, seed_value: Optional[int]=None) -> None:
        self.seed = seed_value
        self.words = data.get_data()
        self.word = self.__word_init()
        self.word_len = len(self.word)
        self.characters: set[str] = set([i for i in self.word])
        self.alphabet_string = {chr(i): Style.RESET_ALL for i in self.__capital_letters_range}

    def __len__(self) -> int:
        return len(self.words)

    def get_alphabet(self):
        return f"{Style.RESET_ALL}".join([f"{v}{k}" for k, v in self.alphabet_string.items()]) + Style.RESET_ALL

    def __word_init(self):
        """
        Get words and initialze their index for querying
        """
        return "".join(self.random_word())

    def random_word(self) -> List[str]:
        """
        Select a random word from the corpus
        """
        if self.seed:
            seed(self.seed)
        idx = randrange(0, len(self))
        return list(self.words.iloc[idx, list(range(len(self.words.columns)))])
    
    def word_exists(self, string: str) -> bool:
        """
        Check if a selected word exists 
        """
        if string not in self.words.index:
            return False
        return True

    def word_correct(self, guess: List[Tuple[str, Status]]) -> bool:
        """
        """
        bool_list = [True if i[1] == Status.CORRECT else False for i in guess]
        if all(bool_list):
            return True
        return False

    def terminal_string(self, values: List[Tuple[str, Status]]):
        """
        Create the string for the terminal
        """
        terminal_colours = {
                Status.CORRECT: partial(self.__format_string, 
                                        style=Style.BRIGHT,
                                        colour=Fore.GREEN),
                Status.CONTAINED: partial(self.__format_string,
                                          style=Style.BRIGHT,
                                          colour=Fore.YELLOW),
                Status.WRONG: partial(self.__format_string,
                                      style=Style.RESET_ALL,
                                      colour=Style.RESET_ALL)
        }

        return f"{''.join([terminal_colours[i[1]](value=i[0]) for i in values])}{Style.RESET_ALL}"

    
    @staticmethod
    def __format_string(style, colour, value) -> str:
        """
        """
        return f"{style}{colour}{value}{Style.RESET_ALL}"

    
    def guess(self, string: str, update_colours: bool=True) -> List[Tuple[str, Status]]:
        """
        Return a coloured string to display to the screen
        """

        if string == self.word:
            return [(i, Status.CORRECT) for i in string]
        return_string = []
        for q, v in zip(string, self.word):
            coloured_string = None
            if q == v:
                coloured_string = f"{Style.BRIGHT}{Fore.YELLOW}"
                return_string.append((q, Status.CORRECT))
            elif q in self.characters:
                coloured_string = f"{Style.BRIGHT}{Fore.YELLOW}"
                return_string.append((q, Status.CONTAINED))
            else:
                coloured_string = f"{Style.BRIGHT}{Fore.CYAN}"
                return_string.append((q, Status.WRONG))
            if update_colours:
                self.alphabet_string[q] = coloured_string
        return return_string



