# In spaceships.py

from base_spaceships import Fighter, Battleship

class Interceptor(Fighter):
    def __init__(self):
        super().__init__(attack=180, defense=1000)

    def fire_on(self, target):
        if isinstance(target, Fighter):
            target.take_damages(2 * self.attack)
        else:
            target.take_damages(self.attack)

class Bomber(Fighter):
    def __init__(self):
        super().__init__(attack=150, defense=2000)

    def fire_on(self, target):
        if isinstance(target, Battleship):
            target.take_damages(2 * self.attack)
        else:
            target.take_damages(self.attack)

class Cruiser(Battleship):
    def __init__(self):
        super().__init__(attack=800, defense=3000)

class Frigate(Battleship):
    def __init__(self):
        super().__init__(attack=500, defense=2500)

    def fire_on(self, target):
        if isinstance(target, Fighter):
            target.take_damages(2 * self.attack)
        else:
            target.take_damages(self.attack)

class Destroyer(Battleship):
    def __init__(self):
        super().__init__(attack=650, defense=5000)

    def fire_on(self, target):
        if isinstance(target, Battleship):
            target.take_damages(2 * self.attack)
        else:
            target.take_damages(self.attack)
