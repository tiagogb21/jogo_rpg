class Potion:
    def __init__(self):
        self._name = ''
        self._effect = ''

    @property
    def name(self):
        return self._name

    @property
    def effect(self):
        return self._effect

    @property.name
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError('Name must be a string')
        self._name = name
    
    @property.effect
    def effect(self, effect):
        if not isinstance(effect, int):
            raise ValueError('Effect must be an integer')
        self._effect = effect
