
class Weapon:
    def __init__(self,name,damage,ammo_consumption):
        self.name = name
        self.damage = damage
        self.ammo_consumption = ammo_consumption

    def attack(self):
        """ Returns the damage dealt by the weapon"""
        return self.damage


