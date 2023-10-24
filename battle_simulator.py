from base_spaceships import Battleship, Spaceship
from fleet import Fleet
import random


class Simulator:
    def __init__(self, att_fleet: Fleet, def_fleet: Fleet):
        '''Constructeur de la classe Simulator'''
        '''Le constructeur prend deux arguments : la flotte attaquante et la flotte défendante. Ces flottes sont stockées en tant qu'attributs de la classe.'''
        self.att_fleet = att_fleet
        self.def_fleet = def_fleet

    def fight(self):
        '''La méthode fight est responsable de simuler la bataille. Elle effectue trois étapes de combat : d'abord entre les battleships des deux flottes, puis entre les fighters, et enfin entre tous les vaisseaux survivants (combattants et cuirassés). Cette méthode utilise la méthode _simulate_fight pour chaque étape.'''
        self._simulate_fight(
            self.att_fleet.alive_battleships, self.def_fleet.alive_battleships
        )
        self._simulate_fight(
            self.att_fleet.alive_fighters, self.def_fleet.alive_fighters
        )
        self._simulate_fight(self.att_fleet.alive_ships, self.def_fleet.alive_ships)

    def get_report(self) -> dict:
        '''La méthode get_report renvoie un rapport sous forme de dictionnaire. Ce rapport contient les rapports des deux flottes, identifiés par leur nom.'''
        return {
            self.att_fleet.name: self.att_fleet.report,
            self.def_fleet.name: self.def_fleet.report,
        }

    def _duel_fight(attacker: Spaceship, defender: Spaceship):
        """La méthode _duel_fight simule un duel entre deux vaisseaux, l'attaquant et le défenseur. Elle appelle la méthode fire_on de l'attaquant pour infliger des dégâts au défenseur. Si le défenseur survit, il riposte en appelant fire_on sur l'attaquant."""
        attacker.fire_on(defender)
        if defender.is_alive:
            defender.fire_on(attacker)

    def _simulate_fight(self, attackers: list[Spaceship], defenders: list[Spaceship]):
        """La méthode _simulate_fight simule un combat entre deux listes de vaisseaux, les attaquants et les défenseurs. Elle vérifie d'abord si les listes d'attaquants et de défenseurs ne sont pas vides. Ensuite, elle sélectionne un attaquant vivant au hasard et un défenseur vivant au hasard parmi les listes respectives. Elle utilise ensuite la méthode _duel_fight pour simuler le combat entre ces deux vaisseaux."""
        if len(attackers) == 0 or len(defenders) == 0:
            return
        for attacker in attackers:
            if attacker.is_alive:
                defender = random.choice(defenders)
                Simulator._duel_fight(attacker, defender)