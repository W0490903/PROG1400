import random

# Step 1: Define the Weapon class
class Weapon:
    def __init__(self, name, damage, ammo_capacity):
        self.name = name
        self.damage = damage
        self.ammo_capacity = ammo_capacity
        self.ammo_remaining = ammo_capacity

    def shoot(self):
        if self.ammo_remaining > 0:
            print(f"{self.name} fired! -{self.damage} damage")
            self.ammo_remaining -= 1
        else:
            print("Out of ammo!")

# Step 2: Define the Player class
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = None

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage. Current health: {self.health}")

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} equipped {weapon.name}")

    def shoot(self):
        if self.weapon:
            self.weapon.shoot()
        else:
            print(f"{self.name} has no weapon!")

# Step 3: Define the Game class
class FirstPersonShooterGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play_round(self):
        print("New Round!")
        self.player1.shoot()
        self.player2.take_damage(self.player1.weapon.damage)

        self.player2.shoot()
        self.player1.take_damage(self.player2.weapon.damage)

# Step 4: Instantiate objects and play the game
if __name__ == "__main__":
    # Create weapons
    assault_rifle = Weapon("Assault Rifle", damage=10, ammo_capacity=30)
    shotgun = Weapon("Shotgun", damage=20, ammo_capacity=8)

    # Create players
    player1 = Player("Player 1", health=100)
    player2 = Player("Player 2", health=100)

    # Equip weapons
    player1.equip_weapon(assault_rifle)
    player2.equip_weapon(shotgun)

    # Create the game
    fps_game = FirstPersonShooterGame(player1, player2)

    # Play a round
    fps_game.play_round()
