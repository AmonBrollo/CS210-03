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
        self.words = ["e a s y " ,"p h o t o g r a p h y ","b a b y ","e p i s o d e ","w i t h d r a w ",
        "q u a l i f i e d ","w a t c h ","t r u s t e e ","g h o s t w r i t e r ","t h r e a d ",
        "o v e r e a t ","p e r f u m e ","r o a r ","i m p o u n d ","p r i m a r y ",
        "l i s t e n ","h e l m e t ","r e v o l u t i o n a r y ","w e s t ","s i s t e r "]

    def get_word(self,words):
        """Get a random word from the list of words.
        
        Args:
            self (Puzzle): An instance of Puzzle.
            words (list<string>): A list of words.
        """
        word = random.choice(words)
        return word

    def update_puzzle(self, blank_space, guess):
        """Update the puzzle's blank spaces according to the player's guess.
        
        Args:
            self (Puzzle): An instance of Puzzle.
            blank_space (string): The blank spaces displaying to the player.
            word (string): The puzzle word randomly generated.
            letter (string): The player's guess.
        """
        for i in blank_space:
            if i == guess:
                i = guess

        return blank_space