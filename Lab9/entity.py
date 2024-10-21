import abc

class Entity(abc.ABC):
    '''
        Enity class represent an abstract enity such as hero and dragon
    '''
    def __init__(self, name, max_hp):
        '''Initialize the name, max_hp, and hp of the enity'''
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
    @property
    def name(self):
        '''Setter for name'''
        return self._name
    @property
    def hp(self):
        '''Setter for hp'''
        return self._hp
    def take_damage(self, dmg):
        '''subtract the hp from taking dmg'''
        self._hp -= dmg
        if self._hp < 0: 
            self._hp = 0  
    def __str__(self) -> str:
        '''Represent for name and hp/maxhp of the enity'''
        return f"{self._name}: {self._hp}/{self._max_hp} "
    @abc.abstractmethod
    def basic_attack(self, opponent):
        pass
    @abc.abstractmethod
    def special_attack(self, opponent):
        pass
