import random

from base_spaceships import Spaceship


class Simulator:
    @staticmethod
    def _duel_fight(attacker_ship: Spaceship, defender_ship: Spaceship):
        attacker_ship.fire_on(defender_ship);

        if defender_ship.is_alive == True:
            defender_ship.fire_on(attacker_ship)

    def _simulate_fight(self, attackers, defenders):
        for attacker_ship in attackers:
            if attacker_ship.is_alive:
                alive_defenders = [ship for ship in defenders if ship.is_alive]
                if alive_defenders:
                    defender_ship = random.choice(alive_defenders)
                    self._duel_fight(attacker_ship, defender_ship)
