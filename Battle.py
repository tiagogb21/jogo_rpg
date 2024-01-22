import random

class Battle:
    LOSS_FACTOR = 0.05

    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def attack(self, target):
        damage = random.randint(self.level() * 2, self.level() * 4)
        target.receive_damage(damage)
        print(f"{self.name()} atacou {target.name()} e causou {damage} de dano!")
    
    def special_attack(self, target):
        damage = random.randint(self.level() * 5, self.level() * 8)
        target.receive_damage(damage)
        print(f"{self.name()} usou a habilidade especial {self.skill()} em {target.name()} e causou {damage} de dano!")

    def fight(self):
        while self.player_life > 0 or self.monster_life > 0:
            choose = input("Escolha: 1 - ataque normal, 2 - ataque especial")

            if(choose == '1'):
                self.player.attack(self.monster)
            elif(choose == '1'):
                self.player.special_attack(self.monster)

            self.monster.attack(self.player)

            if(self.player_life == 0):
                print(f"O jogador {self.player} morreu!")
                lost_experience = self.player.experience * Battle.LOSS_FACTOR
                self.player.experience -= lost_experience
                print(f"Perdeu {lost_experience} exp")
                break

            if(self.monster_life == 0):
                print(f"{self.monster.type} derrotado!")
                experience_gained = self.monster.experience
                self.player.gain_experience(self.monster.experience)
                print(f"{self.player} ganhou {experience_gained} exp")

                if self.player.check_level_up():
                    print(f"{self.player.name} subiu para o nível {self.player.level}!")
                
                self.player.display_player_details()
                break
