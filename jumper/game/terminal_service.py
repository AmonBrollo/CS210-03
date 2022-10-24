class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """



    def display_puzzle(puzzle):
        """"Display the blank puzzle space according to the puzzle word
        
        Args:
            puzzle (string): The Puzzle word.

        """
        blank_space = ""
        for i in len(puzzle):
            blank_space += "_"
        return blank_space