import random


class Puzzle:
    """A random word generated for the player to guess.
    
    The responsibility of the Puzzle is to generate a random word for the player to guess and display the
    puzzle being solved.
    Attributes:
        _words (list<string>): A list of words 
    """

    def __init__(self):
        """Constructs a new Puzzle.
        
        Args:
            self (Puzzle): An instance if Puzzle.
        """
        self._words = ["easy","photography","baby","episode","withdraw","qualified","watch","trustee",
        "ghostwriter","thread","overeat","perfume","roar","impound","primary","listen","helmet",
        "revolutionary","west","sister"]