
class Weapon:
    def __init__(self, name, damage, ammo_consumption):
        self.name = name
        self.damage = damage
        self.ammo_consumption = ammo_consumption

    def __str__(self):
        return f'{self.name} {self.damage} {self.ammo_consumption}'

    def attack(self):
        """ Returns the damage dealt by the weapon"""
        return self.damage
