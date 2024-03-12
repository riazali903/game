from weapon import Weapon


class Player:
    def __init__(self, name, health=int(100), ammo=int(50), weapon = Weapon('KK', 10, 15)):
        self.name = name
        self.health = health
        self.ammo = ammo
        self.weapon = weapon
        # self.weapon = weapon

    def reload(self, ammo_count):
        """ Reloads the player's ammo with the given amount """
        self.ammo += ammo_count

    def hit(self, damage):
        """ Reduces the player's health by the specified damage"""
        print(f'i have been hit by {damage}')
        self.health -= damage

    def get_health(self):
        """ Returns the current health of the player"""
        return self.health

    def heal(self, healing_points):
        """ gain health by specified healing points"""
        self.health += healing_points

    def fire(self):
        """ Decreases the player's ammo by 1 and returns a message
            indicating a short fired """
        self.ammo -= 1
        return "Short fired "


if __name__ == "__main__":
    weapon1 = Weapon("TT",20,20)
    player1 = Player('Riaz', health=90, ammo=45,weapon=weapon1)
    print(player1.get_health())
    print(player1.fire())
    print(player1.ammo)
    print(player1.weapon)
