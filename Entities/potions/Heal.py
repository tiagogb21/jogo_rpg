from Potion import Potion

class Heal(Potion):
    def __init__(self):
        super().__init__()
        self._healing_power = 0

    @property
    def healing_power(self):
        return self._healing_power

    @property.healing_power
    def healing_power(self, healing_power):
        if not isinstance(healing_power, str):
            raise ValueError('Healing power must be a number')
        self._healing_power = healing_power
