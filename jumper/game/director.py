from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        jumper (Jumper): The game's jumper.
        puzzle (Puzzle): The game's puzzle.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._is_playing = True
        self._puzzle = Puzzle()
        self._terminal_service = TerminalService()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
    
    def _get_inputs(self):
        """Display Jumper and the puzzle. Ask for player's guess.

        Args:
            self (Director): An instance of Director.
        """
        #display_puzzle
        #self._terminal_service.display_jumper(jumper_phase)
        guess = self._terminal_service.read_letter(f"\nGuess a letter [a-z]: ")

    def _do_updates(self):
        """Check if player's guess matches the puzzle word. Update the puzzle and jumper
        accordingly.

        Args:
            self (Director): An instance of Director.
        """
        #if player_guess = true, update puzzle word to show correct letters
        #if not, proceed to jumper's next phase

    def check_game_over(is_playing, jumper, word, guess):
        None