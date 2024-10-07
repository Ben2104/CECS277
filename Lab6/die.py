import random
class Die:
    '''
    Represents a single Die. Defaults to 6-sided die
    Attributes: 
    side(int): number of sides on the die
    value(int): the value of the rolled die.
    '''
    def __init__(self, side = 6):
        self._side = side
        self._value = self.roll()
    def roll(self):
        self._value = random.randint(1, 6)
        return self._value
    def __str__(self):
        return str(self._value)
    def __lt__(self, other):
        return self._value < other._value
    def __eq__(self, other):
        return self._value == other._value
    def __sub__(self, other):
        return self._value - other._value