from dragon import Dragon
from fire import Fire
from random import randint
class FireDragon(Dragon, Fire):
    '''FireDragon class represents a fire dragon inherits from dragon and fire Mixin'''
    def __init__(self):
        super().__init__(name = "Gronkle", max_hp = 15, num_sp = 3)
    def special_attack(self, opponent):
        attack = randint(1,2)
        if attack == 1:
            return self.fireblast(opponent)
        else:
            return self.fireball(opponent)
        