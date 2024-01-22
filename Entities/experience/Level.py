class Level:
    def __init__(self, hp, atk, defense):
        self._hp = hp
        self._atk = atk
        self._defense = defense

    @property
    def hp(self):
        return self._hp

    @property
    def atk(self):
        return self._atk

    @property
    def defense(self):
        return self._defense

levels_data = {
    1: Level(100, 10, 5),
    2: Level(120, 12, 6),
    3: Level(150, 15, 8),
    4: Level(200, 20, 10),
    5: Level(300, 30, 15),
    6: Level(400, 40, 20),
    7: Level(500, 50, 25),
    8: Level(600, 60, 30),
    9: Level(700, 70, 35),
    10: Level(800, 80, 40),
}
