from base_spaceships import Fighter, Battleship


class BattleshipKiller(Battleship):
    def __init__(self, attack, defense):
        super().__init__(attack, defense)

    def fire_on(self, target):
        if target is None:
            raise ValueError("The target cannot be None.")
        if isinstance(target, Battleship):
            target.take_damages(self.attack * 2)
        else:
            if isinstance(target, Fighter):
                target.take_damages(self.attack)


class FighterKiller(Fighter):
    def __init__(self, attack, defense):
        super().__init__(attack, defense)

    def fire_on(self, target):
        if target is None:
            raise ValueError("The target cannot be None.")
        if isinstance(target, Fighter):
            target.take_damages(self.attack * 2)
        else:
            if isinstance(target, Battleship):
                target.take_damages(self.attack)


class Interceptor(FighterKiller, Fighter):
    def __init__(self):
        super().__init__(attack=180, defense=1000)
        self.attack = 180


class Bomber(BattleshipKiller, Fighter):
    def __init__(self):
        super().__init__(attack=150, defense=2000)
        self.attack = 150


class Cruiser(Battleship):
    def __init__(self):
        super().__init__(attack=800, defense=3000)
        self.attack = 800


class Frigate(FighterKiller, Battleship):
    def __init__(self):
        super().__init__(attack=500, defense=2500)
        self.attack = 500


class Destroyer(BattleshipKiller, Battleship):
    def __init__(self):
        super().__init__(attack=650, defense=5000)
        self.attack = 650
