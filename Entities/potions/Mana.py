from Potion import Potion

class Mana(Potion):
    def __init__(self):
        super().__init__()
        self._mana_power = 0

    @property
    def mana_power(self):
        return self._mana_power

    @property.mana_power
    def mana_power(self, mana_power):
        if not isinstance(mana_power, str):
            raise ValueError('Mana power must be a number')
        self._mana_power = mana_power
