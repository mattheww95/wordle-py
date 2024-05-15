"""
Render the word displayed
"""
import sys
from colorama import just_fix_windows_console
from wordle_py.words.words import Words
from typing import Optional, List

class Renderer:
    """
    Render the word for display
    """
    
    def __init__(self, word: Words) -> None:
        just_fix_windows_console()
        self.__words = word
        self.guess_limit = self.__words.word_len
        self.guesses = []

    def print_guesses(self, guesses: List[str]) -> None:
        """
        Print guess to screen
        """
        print(f"Guesses that remain: {self.guess_limit - len(self.guesses)}")
        for guess in self.guesses:
            print(guess)

    def game_loop(self):
        guesses = 0
        while guesses < self.guess_limit:
            print("Selected Letters", self.__words.get_alphabet())
            self.get_guess()
            if self.__words.matched or guesses == self.guess_limit -1:
                end_message = "You got the word!" if self.__words.matched else f"Sorry, the word to guess was {self.__words.word}"
                print(end_message)
                sys.exit(0)
            guesses += 1


    def get_input(self) -> str:
        """
        Get the users input from the terminal
        """
        input_passed: Optional[str] = None

        while input_passed is None:
            usr_input = input(f"Enter a guess ({self.__words.word_len} characters): ").upper()
            if self.__words.word_len != len(usr_input):
                equality = "short" if self.__words.word_len > len(usr_input) else "long"
                print(f"Guess {usr_input} is too {equality}. Please guess a word of length {self.__words.word_len}")
            elif not set(usr_input).issubset(self.__words.alphabet_string.keys()):
                print(f"Invalid characters entered, Please only enter wors containing the following characters {''.join(self.__words.alphabet_string.keys())}")
            elif not self.__words.word_exists(usr_input):
                print(f"Word entered {usr_input} is not a valid word.")
            else:
                input_passed = usr_input

        return input_passed

    def get_guess(self) -> None:
        """
        Display a string to the terminal with the appropriate colours

        TODO have this function take in string
        """
        usr_input = self.get_input()
        test_value = self.__words.guess(usr_input)
        self.guesses.append(test_value)
        self.print_guesses(self.guesses)

if __name__ == "__main__":
    selection = Words(seed_value=42)
    renderer = Renderer(selection)
    renderer.game_loop()










