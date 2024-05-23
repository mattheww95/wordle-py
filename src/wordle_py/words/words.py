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

    def __init__(self, seed_value: Optional[int]=None) -> None:
        self.seed = seed_value
        self.words = data.get_data()
        self.word = self.__word_init()
        self.word_len = len(self.word)
        self.characters: set[str] = set([i for i in self.word])
        self.guesses = []
        self.alphabet_string = {chr(i): Style.RESET_ALL for i in range(65,91)}
        self.matched = False
    
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

    
    def guess(self, string: str) -> List[Tuple[str, Status]]:
        """
        Return a coloured string to display to the screen
        """

        if string == self.word:
            self.matched = True
            #return Fore.GREEN + string + Style.RESET_ALL
            return [(i, Status.CORRECT) for i in string]
        return_string = []
        for q, v in zip(string, self.word):
            if q == v:
                self.alphabet_string[q] = f"{Style.BRIGHT}{Fore.YELLOW}"
                return_string.append((q, Status.CORRECT))
            elif q in self.characters:
                self.alphabet_string[q] = f"{Style.BRIGHT}{Fore.YELLOW}"
                return_string.append((q, Status.CONTAINED))
            else:
                self.alphabet_string[q] = f"{Style.BRIGHT}{Fore.CYAN}"
                return_string.append((q, Status.WRONG))
        return return_string



