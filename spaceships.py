from base_spaceships import Fighter, Battleship


class BattleshipKiller:
    def __init__(self, attack):
        self.attack = attack

    def fire_on(self, target):
        if isinstance(target, Battleship):
            target.defense -= self.attack * 2
        else:
            target.defense -= self.attack


class FighterKiller:
    def __init__(self, attack):
        self.attack = attack

    def fire_on(self, target):
        if isinstance(target, Fighter):
            target.defense -= self.attack * 2
        else:
            target.defense -= self.attack


class Interceptor(Fighter, FighterKiller):
    def __init__(self):
        super().__init__(attack=180, defense=1000)


class Bomber(Fighter, BattleshipKiller):
    def __init__(self):
        super().__init__(attack=150, defense=2000)


class Cruiser(Battleship, FighterKiller):
    def __init__(self):
        super().__init__(attack=800, defense=3000)


class Frigate(Battleship, FighterKiller):
    def __init__(self):
        super().__init__(attack=500, defense=2500)


class Destroyer(Battleship, BattleshipKiller):
    def __init__(self):
        super().__init__(attack=650, defense=5000)
