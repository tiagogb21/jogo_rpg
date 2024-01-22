from jogo_rpg.Entities.characters.Character import Character
from jogo_rpg.Entities.experience.Experience import Experience

class Player(Character):
    def __init__(self):
        self._name = ''
        self._experience = Experience(0)

    @property
    def name(self):
        return self._name

    @property
    def experience(self):
        return self._experience.experience

    @property.name
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError('Name must be a string')
        self._name = name

    def display_player_details(self):
        return f"Nome: {self.name()}\nVida: {self.life()}\nNível: {self.level()}"

    def gain_experience(self, amount):
        self._experience.gain_experience(amount)
        self.level_up()
    
    def level_up(self):
        if self._experience.is_leveled_up():
            print(f"{self.name} subiu para o nível {self._experience.level}!")