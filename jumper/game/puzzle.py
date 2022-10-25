import random


class Puzzle:
    """A random word generated for the player to guess.
    
    The responsibility of the Puzzle is to generate a random word for the player to guess and display the
    puzzle being solved.
    Attributes:
        words (list<string>): A list of words 
    """

    def __init__(self):
        """Constructs a new Puzzle.
        
        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self.words = ["easy","photography","baby","episode","withdraw","qualified","watch","trustee",
        "ghostwriter","thread","overeat","perfume","roar","impound","primary","listen","helmet",
        "revolutionary","west","sister"]

    def get_word(self,words):
        """Get a random word from the list of words.
        
        Args:
            self (Puzzle): An instance of Puzzle.
            words (list<string>): A list of words.
        """
        word = random.choice(words)
        return word

    def update_puzzle(self, blank_space, word, letter):
        """Update the puzzle's blank spaces according to the player's guess.
        
        Args:
            self (Puzzle): An instance of Puzzle.
            blank_space (string): The blank spaces displaying to the player.
            word (string): The puzzle word randomly generated.
            letter (string): The player's guess.
        """
        blank_space = ""
        for i in word:
            if i == letter:        
                blank_space += f"{letter} "
            else: blank_space += "_ "

        return blank_space