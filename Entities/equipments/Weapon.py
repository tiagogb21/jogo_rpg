class Weapon:
    def __init__(self):
        self._damage = 0
        self._attack_speed = 0

    @property
    def damage(self):
        return self._damage
    
    @property
    def attack_speed(self):
        return self._attack_speed
    
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
