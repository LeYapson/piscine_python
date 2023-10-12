class Spaceship:
    def __init__(self, attack, defense):
        self.attack = attack
        self.defense = defense

class BattleshipKiller:
    def fire_on(self, spaceship):
        if isinstance(spaceship, Battleship):
            spaceship.defense -= spaceship.defense * 2
        else:
            spaceship.defense -= spaceship.defense

class FighterKiller:
    def fire_on(self, spaceship):
        if isinstance(spaceship, Fighter):
            spaceship.defense -= spaceship.defense * 2
        else:
            spaceship.defense -= spaceship.defense

class Interceptor(BattleshipKiller, Spaceship):
    pass

class Cruiser(FighterKiller, Spaceship):
    pass

class Bomber(BattleshipKiller, Spaceship):
    pass

class Destroyer(FighterKiller, Spaceship):
    pass

class Battleship(Spaceship):
    pass

class Fighter(Spaceship):
    pass

