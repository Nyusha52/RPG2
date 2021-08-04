import random

# чтобы сделать пул рквест

class Knight():
    type = None
    impact_strength_war = None
    impact_strength_archer = None
    impact_strength_magician = None


    def ImpactStrength(self):
        Knight.impact_strength = random.randint(20, 100)
        return Knight.impact_strength

    def ImpactStrengthArcher(self):
        Knight.impact_strength_archer = random.randint(20, 100)
        return Knight.impact_strength_archer

    def ImpactStrengthMagician(self):
        Knight.impact_strength_magician = random.randint(20, 100)
        return Knight.impact_strength_magician

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

        if Knight.impact_strength_archer == None and  Knight.impact_strength_magician == None:
            x = "1"
        if Knight.impact_strength_archer != None and  Knight.impact_strength_magician == None:
            x = input("1 - Warrior, 3 - Archer:")
            while x != "1" and x != "2" and x != "3":
                print("Вы ввели недопустимое значение")
                x = input("1 - Warrior, 3 - Archer:")
        if Knight.impact_strength_archer == None and  Knight.impact_strength_magician != None:
            x = input("1 - Warrior, 2- Magician:")
            while x != "1" and x != "2" and x != "3":
                print("Вы ввели недопустимое значение")
                x = input("1 - Warrior, 2- Magician:")
        if Knight.impact_strength_archer != None and  Knight.impact_strength_magician != None:
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

    def hp_plus(self):
        Knight.hp_plus = random.randint(0, 10)
        return Knight.hp_plus


class Monster():
    monster_counter = 0
    impact_strength_monster = 0
    hp_monster = 0
    type = None

    def ImpactStrength(self):
        Monster.impact_strength_monster = random.randint(5, 10)
        return Monster.impact_strength_monster

    def Hp(self):
        Monster.hp_monster = random.randint(1, 5)
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


class Item():

    def select_item(self):
        item_list = random.choice(("apple", "sword", "monster", "archer", "magician book", "monster", "monster", "monster", "totem"))
        return item_list

    def sword(self):
        sword = random.randint(10, 100)
        return sword

    def magician_book(self):
        magician_book = random.randint(10, 100)
        return magician_book

    def archer(self):
        archer = random.randint(10, 100)
        return archer

    def totem(self):
        pass
        return Item.totem

    def new_weapon(self):
        new_weapon = input("введите 1 или 2:")
        while new_weapon != "1" and new_weapon != "2":
            print("Вы ввели недопустимое значение")
            new_weapon = input("введите 1 или 2:")
        return new_weapon


def game() -> None:
    """Игра в рыцаря."""
    item = Item()
    k = Knight()
    hp_k = k.Hp()
    si_k = k.ImpactStrength()
    Knight.impact_strength_war = si_k
    hp_plus = k.hp_plus()
    type_k = k.type_attack_knight()
    while Monster.monster_counter < 10 and hp_k > 0:
        move = item.select_item()
        if move == "apple":
            hp_k += hp_plus
            print(
                f"ЯБЛОКО, вам прибавлено {hp_plus} жизней,\n"
                f" теперь у вас {hp_k} жизней"
            )
        if move == "sword":
            if type_k != "Warrior":
                sword = item.sword()
                print(
                    f"MEЧ .сила удара равна {sword} \n"
                    f"забрать - 1 или отказаться - 2.\n"
                    f"Сейчас сила вашего удара равна {si_k}"
                )
                number = item.new_weapon()
                new_sword = number
                if new_sword == "1":
                    si_k = sword
            else:
                si_k = si_k + 10
                print(
                    f"MEЧ .сила удара увеличена на 10 и равна {si_k} "
                )

        if move == "archer":
            if Knight.impact_strength_archer == None:
                si_k_archer = k.ImpactStrengthArcher()
            if type_k != "Archer":
                archer = item.archer()
                print(
                    f"ЛУК.его сила удара равна {archer} \n"
                    f"забрать - 1 или отказаться - 2.\n"
                    f"Сейчас сила вашего удара равна {si_k_archer}"
                )
                number = item.new_weapon()
                new_archer = number
                if new_archer == "1":
                    si_k_archer = archer
            else:
                si_k_archer = si_k_archer + 10
                print(
                    f"ЛУК.сила удара увеличена на 10 и равна {si_k_archer} "
                )
        if move == "magician book":
            if Knight.impact_strength_magician == None:
                si_k_magician = k.ImpactStrengthMagician()
            if type_k != "Magician":
                magician_book = item.magician_book()
                print(
                    f"КНИГА: сила удара равна {magician_book} \n"
                    f"забрать - 1 или отказаться - 2.\n"
                    f"Сейчас сила вашего удара равна {si_k}"
                )
                number = item.new_weapon()
                new_book = number
                if new_book == "1":
                    si_k_magician = magician_book
            else:
                si_k_magician += 10
                print(
                    f"КНИГА .сила удара увеличена на 10 и равна {si_k} "
                )
        if move == "totem":
            pass
        if move == "monster":
            m = Monster()
            hp_monster = m.Hp()
            msi = m.ImpactStrength()
            mtype = m.type_attack()
            print(
                f"БОЙ. Чудовище, его сила удара равна {msi} \n"
                f"количество его жизней - {hp_monster}. Его тип {mtype}\n"
                f"ваша сила удара {si_k}, ваше количество жизней {hp_k}\n"
                f"принять БОЙ - 1 или убежать - 2.\n"
                f"Вы уже убили {Monster.monster_counter} чудовищ"
            )
            number = item.new_weapon()
            wor = number
            type_k = k.type_attack_knight_war()
            if wor == "1":
                if mtype == type_k:
                    pass
                    if hp_monster > si_k:
                        hp_k = hp_k - msi * (hp_monster // si_k + 1)
                        Monster.monster_counter += 1
                    else:
                        hp_k = hp_k - msi
                        Monster.monster_counter += 1
                if hp_monster > si_k:
                    hp_k = hp_k - msi * (hp_monster // si_k + 1)
                    Monster.monster_counter += 1
                else:
                    hp_k = hp_k - msi
                    Monster.monster_counter += 1
    if Monster.monster_counter >= 10 and hp_k > 0:
        print("ПОБЕДА")
    else:
        print("ПОРАЖЕНИЕ")
    exit()

game()