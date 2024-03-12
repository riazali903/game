from player import Player
from weapon import Weapon
import threading
import time


class Boss(Player):
    def __init__(self, name, weapon=Weapon('kk', 20, 15), health=int(70), ammo=int(50), power="Super Strength"):
        """ the health and ammo parameters are optional here as they have default values so even if removed,
         values can be obtained from player class"""
        super().__init__(name, health=int(100), ammo=int(50))
        self.power = power
        self.weapon = weapon
        healing_thread = threading.Thread(target=self.auto_heal, daemon=True)
        healing_thread.start()

    def user_power(self):
        """ Display a message indicating the boss is using its special power"""
        print('Boss is using its special power')

    def heal(self, healing_points=10):
        """ Increases the boss health by specified healing points """
        if self.health < 100:
            self.health += healing_points
            if self.health > 100:
                self.health = 100
        return self.health

    def auto_heal(self):
        while self.health <= 100:
            print(f'auto healing from {self.health} to {self.heal()}')
            self.heal()
            time.sleep(1)
            # healing_thread = threading.Thread(target=self.heal(), daemon=True)
            # healing_thread.start()


if __name__ == '__main__':
    boss2 = Boss('Ali')
    print(boss2.health)
    boss2.hit(5)
    time.sleep(3)
    print('health after hit',boss2.health)
    boss2.hit(50)
    time.sleep(2)

    # boss2.auto_heal()

    print('health after auto heal',boss2.health)

    # boss2.hit(20)
    # time.sleep(3)
    # print(boss2.health)
    # print(boss2.weapon)