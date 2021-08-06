import random


class Knight():
    type = None
    attak = None
    have_weapon = {'impact_strength_war' : None, 'impact_strength_archer' : None, 'impact_strength_magician' : None, 'impact_strength_arrow' : None,}
   
    def ImpactStrength(self):
        Knight.have_weapon["impact_strength_war"] = random.randint(20, 100)
        return Knight.have_weapon["impact_strength_war"]

    def ImpactStrengthArcher(self):
        Knight.have_weapon["impact_strength_archer"] = random.randint(20, 100)
        return Knight.have_weapon["impact_strength_archer"]

    def ImpactStrengthArrow(self):
        Knight.have_weapon["impact_strength_arrow"] = True
        return Knight.have_weapon["impact_strength_arrow"]


    def ImpactStrengthMagician(self):
        Knight.have_weapon["impact_strength_magician"] = random.randint(20, 100)
        return Knight.have_weapon["impact_strength_magician"]

    def Hp(self):
        Knight.hp = random.randint(50, 100)
        return Knight.hp

    def type_attack_knight(self):
        print("Выберете тип атаки")
        x = input("1 - Warrior, 2- Magician, 3 - Archer:")
        while x != "1" and x != "2" and x != "3":
            print("Вы ввели недопустимое значение")
            x = input("1 - Warrior, 2- Magician, 3 - Archer:")
        if x == '1':
            Knight.type = 'Warrior'
        if x == '2':
            Knight.type = 'Magician'
        if x == '3':
            Knight.type = 'Archer'
        return Knight.type

    def type_attack_knight_war(self):

        if (Knight.have_weapon['impact_strength_archer'] == None or Knight.have_weapon['impact_strength_arrow'] == None) and  Knight.have_weapon['impact_strength_magician'] == None:
            x = "1"
        if Knight.have_weapon['impact_strength_archer'] != None and Knight.have_weapon['impact_strength_arrow'] != None and  Knight.have_weapon['impact_strength_magician'] == None:
            x = input("1 - Warrior, 3 - Archer:")
            while x != "1" and x != "2" and x != "3":
                print("Вы ввели недопустимое значение")
                x = input("1 - Warrior, 3 - Archer:")
        if (Knight.have_weapon['impact_strength_archer'] == None or Knight.have_weapon['impact_strength_arrow'] == None) and  Knight.have_weapon['impact_strength_magician'] != None:
            x = input("1 - Warrior, 2- Magician:")
            while x != "1" and x != "2" and x != "3":
                print("Вы ввели недопустимое значение")
                x = input("1 - Warrior, 2- Magician:")
        if Knight.have_weapon['impact_strength_archer'] != None and Knight.have_weapon['impact_strength_arrow'] != None and  Knight.have_weapon['impact_strength_magician'] != None:
            x = input("1 - Warrior, 2- Magician, 3 - Archer:")
            while x != "1" and x != "2" and x != "3":
                print("Вы ввели недопустимое значение")
                x = input("1 - Warrior, 2- Magician, 3 - Archer:")
        if x == '1':
            Knight.attak = 'Warrior'
        if x == '2':
            Knight.attak = 'Magician'
        if x == '3':
            Knight.attak = 'Archer'
        return Knight.attak

    def hp_plus(self):
        Knight.hp_plus = random.randint(0, 10)
        return Knight.hp_plus