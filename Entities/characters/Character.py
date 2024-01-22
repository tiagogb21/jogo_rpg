class Character:
    def __init__(self):
        self._life = ''
        self._attack = 0
        self._defense = 0
    
    @property
    def life(self):
        return self._life
    
    @property
    def attack(self):
        return self._attack
    
    @property
    def defense(self):
        return self._defense
    
    @property.life
    def life(self, life):
        if not isinstance(life, int):
            raise ValueError('Life must be an integer')
        self._life = life
    
    @property.attack
    def attack(self, attack):
        if not isinstance(attack, int):
            raise ValueError('Attack must be an integer')
        self._attack = attack
    
    @property.defense
    def defense(self, defense):
        if not isinstance(defense, int):
            raise ValueError('Defense must be an integer')
        self._defense = defense
    
    def receive_damage(self, damage):
        if(self.life - damage <= 0):
            self.life = 0
        else:
            self.life -= damage
