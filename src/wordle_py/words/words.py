"""
Select and query words for look up.

2024-05-10: Matthew Wells
"""
from colorama import Fore, Style
from typing import Optional
from wordle_py import data
from random import randrange, seed


class Words:
    """
    Query words for usage and look them up where needed
    """

    def __init__(self, seed_value: Optional[int]=None) -> None:
        self.seed = seed_value
        self.words = data.get_data()
        self.word = self.__word_init()
        self.word_len = len(self.word)
        self.characters: list[str] = set([i for i in self.word])
        self.guesses = []
        self.matched = False
    
    def __len__(self) -> int:
        return len(self.words)

    def __word_init(self):
        """
        Get words and initialze their index for querying
        """
        return "".join(self.random_word())

    def random_word(self) -> list[str]:
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

    
    def guess(self, string: str) -> str:
        """
        Return a coloured string to display to the screen
        """

        if string == self.word:
            self.matched = True
            return Fore.GREEN + string + Style.RESET_ALL
        return_string = []
        for q, v in zip(string, self.word):
            if q == v:
                return_string.append(f"{Fore.GREEN}{q}{Style.RESET_ALL}")
            elif q in self.characters:
                return_string.append(f"{Fore.YELLOW}{q}{Style.RESET_ALL}")
            else:
                return_string.append(q)
        return_string.append(Style.RESET_ALL)
        return "".join(return_string)













