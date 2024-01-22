from jogo_rpg.Entities.Player import Player
from jogo_rpg.Entities.Monster import Monster, MonsterName

class Game:

    def __init__(self):
        self._player = None
        self._monster = None

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self):
        self._player = Player(
            input('What is your name? '),
            100,
            20,
            20,
        )

    @property
    def monster(self):
        return self._monster

    @monster.setter
    def monster(self):
        self._monster = Monster(
            MonsterName.BAT,
            50,
            15,
            15,
        )
