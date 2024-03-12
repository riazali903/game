from player import Player
from weapon import Weapon

class Enemy(Player):
    def __init__(self,name,health=int(100),ammo=int(50),agility='High'):
        super().__init__(name,health=int(100),ammo=int(50))
        self.agility = agility
        self.weapon = Weapon('KK', 30, 20)
        # self.weapon = weapon

    def evade(self):
        """ Returns a message indicating the enemy is evading the attack """
        return "The enemy is envading the attack"

    def heal(self, healing_points):
        """ Enemy cannot heal"""
        return self.health
    def get_health(self):
        """ override player's get_health method """
        return self.health

if __name__ == "__main__":
    ene = Enemy('Nayab',100,50)
    print(ene.get_health())
    print(ene.weapon)
    ene.hit(30)
    ene.heal(20)

    print(ene.get_health())