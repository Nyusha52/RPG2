import random
from knight import Knight
from monster import Monster
from item import Item



def game() -> None:
    """Игра в рыцаря."""
    item = Item()
    k = Knight()
    hp_k = k.Hp()
    si_k = k.ImpactStrength()
    Knight.have_weapon['impact_strength_war'] = si_k
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
            if Knight.have_weapon['impact_strength_archer'] == None:
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
            if Knight.have_weapon['impact_strength_magician'] == None:
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
                if type_k == 'Warrior':
                    si_k = k.have_weapon["impact_strength_war"]
                    print(f"Вы сменили оружие, на меч {si_k}")
                if type_k == 'Archer':
                    si_k = k.have_weapon["impact_strength_archer"]
                    print( f"Вы сменили оружие, на лук {si_k}" )
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