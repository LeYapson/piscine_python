class Spaceship:
    is_alive = True

    def __init__(self, attack=0, defense=0):
        self.attack = attack
        self.defense = defense

    def take_damages(self, damage):
        """
        Apply damage to the spaceship's defense.

        :param damage: The amount of damage to apply.
        :type damage: int

        :raises ValueError: If damage is negative.
        """
        if damage < 0:
            raise ValueError("Damage cannot be negative.")

        self.defense -= damage
        if self.defense <= 0:
            self.defense = 0
            self.is_alive = False

class Battleship(Spaceship):
    """
    A class representing a battleship, inheriting from Spaceship.
    """

class Fighter(Spaceship):
    """
    A class representing a fighter, inheriting from Spaceship.
    """
