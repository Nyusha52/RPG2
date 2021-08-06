import random


class Monster():
    monster_counter = 0
    impact_strength_monster = 0
    hp_monster = 0
    type = None

    def ImpactStrength(self):
        Monster.impact_strength_monster = random.randint(5, 20)
        return Monster.impact_strength_monster

    def Hp(self):
        Monster.hp_monster = random.randint(50, 100)
        return Monster.hp_monster

    def type_attack(self):
        monster = random.choice(('Warrior', 'Magician', 'Archer'))
        if monster == 'Warrior':
            type = 'Warrior'
        if monster == 'Magician':
            type = 'Magician'
        if monster == 'Archer':
           type = 'Archer'
        return type