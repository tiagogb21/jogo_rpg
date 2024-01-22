from enum import Enum
from jogo_rpg.Entities.Character import Character

class MonsterName(Enum):
    BAT = 'morcego'
    WOLF = 'lobo'
    SNAKE = 'cobra'
    SPIDER = 'aranha'
    DRAGON = 'dragão'

class Monster(Character):
    def __init__(self):
        _name = ''
        experience = 0

    @property
    def name(self):
        return self._name

    @property.name
    def name(self, monster_name):
        if not isinstance(monster_name, MonsterName):
            raise ValueError('name must be of name monster')
        self._name = monster_name

    def display_monster_details(self):
        return f"Nome: {self.name()}\nVida: {self.life()}\nNível: {self.level()}"