from random import randint
class Fire:
    '''Mixin class Fire represents the special attacks'''
    def fireblast(self, opponent):
        '''fireblast method'''
        self.decrement_special_attacks()
        if self.special_attacks < 0:
            return f"{self.name} tries to fireblast at {opponent.name}, but it is all out of energy."
        dmg = randint(5,9)
        opponent.take_damage(dmg)
        return f"{self.name} fireblast at {opponent.name} for {dmg} damage!"
    def fireball(self, opponent):
        '''fireball method'''
        self.decrement_special_attacks()
        if self.special_attacks < 0:
            return f"{self.name} tries to fireball at {opponent.name}, but it is all out of energy."
        dmg = randint(4,8)
        opponent.take_damage(dmg)
        return f"{self.name} fireball at {opponent.name} for {dmg} damage!"
