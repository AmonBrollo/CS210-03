class Jumper:
    """A figure with a parachute to indicate what level the player is on. 
    
    The responsibility of the jumper is to show how many wrong guesses the player has 
    left.
    Attributes:
        phase_number (int): A number to keep track of the phases.
        phases (list<string>): Representation of the Jumper in all its phases.
    """
    def __init__(self):
        """Constructs a new Jumper.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        self.phase_number = 0
        self.phases = ["\n  ___ \n /___\ \n \   / \n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^", 
        "\n /___\ \n \   / \n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^", 
        "\n \   / \n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^", 
        "\n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^", "\n   x \n  /|\ \n  / \ \n \n^^^^^^^"]

    def update_jumper(self, phase_number):
        """Update the jumper to the next level.
        
        Args:
            self (Jumper): An instance of Jumper.
            phase_number (int): A number to influence the level.
        """
        phase_number += 1
        return phase_number
