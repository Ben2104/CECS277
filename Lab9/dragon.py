from entity import Entity
import random
import abc
class Dragon(Entity, abc.ABC):
    '''A dragon class that represents an abstract dragon'''
    def __init__(self, name, max_hp, num_sp):
        super().__init__(name, max_hp)
        self._special_attacks = num_sp
    
    @property
    def special_attacks(self):
        return self._special_attacks
    def decrement_special_attacks(self):
        self._special_attacks -= 1
        if self._special_attacks < 0:
            self.special_attacks = 0
    def basic_attack(self, opponent):
        dmg = random.randint(3,7)
        opponent.take_damage(dmg)
        return f"{self._name} smashes you with its tail for {dmg} damge"
    @abc.abstractmethod
    def special_attack(self, opponent):
        pass
    def __str__(self) -> str:
        enity_str = super().__str__()
        return f"{enity_str} \nSpecial attacks remaining: {self._special_attacks}"

