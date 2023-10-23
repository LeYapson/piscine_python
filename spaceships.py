from base_spaceships import Fighter, Battleship


class BattleshipKiller(Battleship):
    def __init__(self):
        super().__init__(attack=150, defense=2000)

    def fire_on(self, target):
        if target is None:
            raise ValueError("The target cannot be None.")
        if isinstance(target, Battleship):
            target.take_damages(self.attack * 2)
        else:
            if isinstance(target, Fighter):
                target.take_damages(self.attack)


class FighterKiller(Fighter):
    def __init__(self):
        super().__init__(attack=150, defense=2000)

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
        super().__init__()


class Bomber(BattleshipKiller, Fighter):
    def __init__(self):
        super().__init__()


class Cruiser(Battleship):
    def __init__(self):
        super().__init__()


class Frigate(FighterKiller, Battleship):
    def __init__(self):
        super().__init__()


class Destroyer(BattleshipKiller, Battleship):
    def __init__(self):
        super().__init__()
