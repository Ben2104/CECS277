from dragon import Dragon
from flying import Flying
from random import randint

class Flying_Dragon(Dragon, Flying):
    '''Represents the Flying Dragon'''

    def __init__(self):
        '''Sets initial flying dragon stats'''
        super().__init__("Timberjack", 10, 3)
        

    def special_attack(self, opponent):
        '''Uses a random special move from FlyingMixin'''
        move_choice = randint(0, 1)
        if move_choice == 0:
            return self.swoop(opponent)
        elif move_choice == 1:
            return self.windblast(opponent)
        else:
            # This should never occur
            print("An error has occured with Flying Dragon.")