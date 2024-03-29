from base_spaceships import Battleship, Fighter, Spaceship


class BattleshipKiller(Spaceship):
    def fire_on(self, target: Spaceship):
        if target.__class__.__base__.__name__ == "Battleship" or target.__class__.__name__ == "Battleship":
            target.take_damages(self.attack * 2)
        else:
            target.take_damages(self.attack)
        return target


class FighterKiller(Spaceship):
    def fire_on(self, target: Spaceship):
        if target.__class__.__base__.__name__ == "Fighter" or target.__class__.__name__ == "Fighter":
            target.take_damages(self.attack * 2)
        else:
            target.take_damages(self.attack)
        return target


class Interceptor(Fighter, FighterKiller):
    def __init__(self, attack=180, defense=1000) -> None:
        super().__init__(attack, defense)


class Bomber(Fighter, BattleshipKiller):
    def __init__(self, attack=150, defense=2000) -> None:
        super().__init__(attack, defense)


class Cruiser(Battleship):
    def __init__(self, attack=800, defense=3000) -> None:
        super().__init__(attack, defense)


class Frigate(Battleship, FighterKiller):
    def __init__(self, attack=500, defense=2500) -> None:
        super().__init__(attack, defense)


class Destroyer(Battleship, BattleshipKiller):
    def __init__(self, attack=650, defense=5000) -> None:
        super().__init__(attack, defense)