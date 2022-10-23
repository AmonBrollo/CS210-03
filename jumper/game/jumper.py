class Jumper:
    """A figure with a parachute to indicate what level the player is on. 
    
    The responsibility of the jumper is to show how many wrong guesses the player has 
    left.
    Attributes:
        _phase_1 (string): Representation of the Jumper in phase 1
        _phase_2 (string): Representation of the Jumper in phase 2
        _phase_3 (string): Representation of the Jumper in phase 3
        _phase_4 (string): Representation of the Jumper in phase 4
        _phase_5 (string): Representation of the Jumper in phase 5
    """

_phase_1 = "\n  ___ \n /___\ \n \   / \n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^"
_phase_2 = "\n /___\ \n \   / \n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^"
_phase_3 = "\n \   / \n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^"
_phase_4 = "\n  \ / \n   0 \n  /|\ \n  / \ \n \n^^^^^^^"
_phase_5 = "\n   x \n  /|\ \n  / \ \n \n^^^^^^^"