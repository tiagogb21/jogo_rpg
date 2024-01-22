from Equipment import Equipment

class Weapon(Equipment):
    def __init__(self):
        self._defense_rating = 0

    @property
    def defense_rating(self):
        return self._defense_rating
    
    @property.defense_rating
    def defense_rating(self, defense_rating):
        if not isinstance(defense_rating, int):
            raise ValueError('defense_rating must be an integer')
        self._defense_rating = defense_rating