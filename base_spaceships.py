class Spaceship:
    is_alive = True

    def __init__(self, attack=100, defense=100):
        self.attack = attack
        self.defense = defense

    def take_damages(self, damage):
        if damage < 0:
            raise ValueError("Damage cannot be negative.")
        self.defense -= damage
        if self.defense <= 0:
            self.defense = 0
            self.is_alive = False

    def fire_on(self, target):
        """
        Fire on another spaceship and apply damages.

        :param target: The target spaceship to attack.
        :type target: Spaceship
        """
        target.take_damages(self.attack)


class Battleship(Spaceship):
    def __init__(self, attack, defense):
        super().__init__(attack, defense)

    """
    A class representing a battleship, inheriting from Spaceship.
    """


class Fighter(Spaceship):
    def __init__(self, attack, defense):
        super().__init__(attack, defense)

    """
    A class representing a fighter, inheriting from Spaceship.
    """
