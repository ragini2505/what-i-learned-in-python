class characters:
    def __init__(self , name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        
    def attack_enemy(self):
        print(f'{self.name} attacks with power {self.attack}')
        

warrior = characters('Thor', 100, 50)
mage = characters('Galdalf',80,70)

warrior.attack_enemy()
mage.attack_enemy()            