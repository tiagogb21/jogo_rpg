class Equipment:
    def __init__(self):
        self._name = ''
        self._durability = 100

    @property
    def name(self):
        return self._name
    
    @property
    def durability(self):
        return self._durability
    
    @property.name
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError('Name must be a string')
        self._name = name
    
    @property.durability
    def durability(self, durability):
        if not isinstance(durability, int):
            raise ValueError('Durability must be an integer')
        self._durability = durability
