class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """



    def display_puzzle(self, puzzle):
        """Display the blank puzzle space according to the puzzle word.
        
        Args:
            puzzle (string): The Puzzle word.
        """
        blank_space = ""
        for i in puzzle:
            blank_space += "_ "
        return blank_space

    def display_jumper(self, phases, phase_number):
        """Display the phase the jumper is in.

        Args:
            phase_number (int): A number to influence the level.
            phases (list<string>): Representation of the Jumper in all its phases.
        """
        print(phases[phase_number])

    def read_letter(self, prompt):
        """Display a prompt to the player for them to pick a latter between a-z.

        Args:
            prompt (string): A message that gathers input from the user.
        """
        guess = input(prompt)
        return guess