from player import Player
from weapon import Weapon

class Boss(Player):
    def __init__(self,name,weapon=Weapon('kk',20,15),health=int(100),ammo=int(50),power="Super Strength"):
        super().__init__(name,health=int(100),ammo=int(50))
        self.power = power
        self.weapon = Weapon('KK', 30, 20)

    def user_power(self):
        """ Display a message indicating the boss is using its special power"""
        print('Boss is using its special power')

    def heal(self,healing_points=10):
        """ Increases the boss health by specified healing points """
        self.health += healing_points