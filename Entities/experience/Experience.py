from jogo_rpg.Entities.experience.Level import levels_data

class Experience:
    def __init__(self, level):
        self.level = level
        self.experience = 0

    @property
    def experience_required_to_next_level(self):
        return 100 * 2 ** (self.level - 1)

    def is_leveled_up(self):
        return self.experience >= self.experience_required_to_next_level

    def gain_experience(self, amount):
        self.experience += amount
        self.level_up()

    def level_up(self):
        next_level_data = levels_data.get(self.level + 1)
        if next_level_data:
            self.level = next_level_data.level
            print(f"Leveled up to level {self.level}!")

experience_data = {level: Experience(level) for level in range(1, 11)}
