from base_spaceships import Spaceship
from spaceships import Interceptor, Frigate, Bomber


class Simulator(Spaceship):
    @staticmethod
    def _duel_fight(attacker, defender):
        while attacker.is_alive and defender.is_alive:
            defender.defense -= attacker.attack
            if defender.defense <= 0:
                defender.is_alive = False
                break
            attacker.defense -= defender.attack
            if attacker.defense <= 0:
                attacker.is_alive = False
                break

# Make sure you have the Spaceship class defined in spaceships.py.
