# In spaceships.py

from base_spaceships import Fighter, Battleship

class BattleshipKiller:
    def fire_on(self, target):
        if isinstance(target, Battleship):
            target.take_damages(2 * self.attack)
        else:
            target.take_damages(self.attack)

class FighterKiller:
    def fire_on(self, target):
        if isinstance(target, Fighter):
            target.take_damages(2 * self.attack)
        else:
            target.take_damages(self.attack)
# In spaceships.py

class Interceptor(FighterKiller, Fighter):
    def __init__(self):
        super().__init__(attack=180, defense=1000)

class Bomber(BattleshipKiller, Fighter):
    def __init__(self):
        super().__init__(attack=150, defense=2000)

class Destroyer(FighterKiller, Battleship):
    def __init__(self):
        super().__init__(attack=650, defense=5000)
