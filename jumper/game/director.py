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
        self._puzzle_word = self._puzzle.get_word(self._puzzle.words)
        self._blank_space = self._terminal_service.display_puzzle(self._puzzle_word)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._check_game_over(self._puzzle_word, self._jumper.jumper)
    
    def _get_inputs(self):
        """Display Jumper and the puzzle. Ask for player's guess.

        Args:
            self (Director): An instance of Director.
        """
        print(f"\n{self._blank_space}")
        self._terminal_service.display_jumper(self._jumper.phases,self._jumper.phase_number)
        self.guess = self._terminal_service.read_letter(f"\nGuess a letter [a-z]: ")
        return self.guess

    def _do_updates(self):
        """Check if player's guess matches the puzzle word. Update the puzzle and jumper
        accordingly.

        Args:
            self (Director): An instance of Director.
        """
        check = self._check_guess(self._puzzle_word, self.guess)
        if check:
            self._puzzle.update_puzzle(self.blank_space, self._puzzle_word, self.guess)
        else: self._jumper.update_jumper(self._jumper.phase_number)

    def _check_guess(self, _puzzle_word, guess):
        """Check if the player's guess matches one of the letter in the puzzle.
        
        Args:
            self (Director): An instance of Director.
            puzzle_word (Puzzle): The word randomly chosen for the puzzle.
            guess (TerminalService): The letter of input from the player. 
        """
        for i in range(len(_puzzle_word)):
            if i == guess:
                return True
            else: return False

    def _check_game_over(self, puzzle, jumper):
        """Check if the player's guess matches one of the letter in the puzzle.
        
        Args:
            self (Director): An instance of Director.
            puzzle (Puzzle): The word randomly chosen for the puzzle.
            jumper (Jumper): The jumper including its balloon.
        """
        if self.blank_space == puzzle:
            print("Congratulations, you won!\nThanks for playing!")
            self._is_playing = False
        elif jumper == self._jumper.jumper_phase_5:
            print("Game Over. You lost!")            
            self._is_playing = False
        else: None        