import random
from knight import Knight
from monster import Monster
from item import Item



def game() -> None:
    """Игра в рыцаря."""
    item = Item()
    k = Knight()
    hp_knight = k.Hp()
    si_knight = k.ImpactStrength()
    Knight.have_weapon['impact_strength_war'] = si_knight
    hp_plus = k.hp_plus()
    knight_type = k.type_attack_knight()

    while Monster.monster_counter < 10 and hp_knight > 0:
        move = item.select_item()
        if move == "apple":
            hp_knight += hp_plus
            print(
                f"ЯБЛОКО, вам прибавлено {hp_plus} жизней,\n"
                f" теперь у вас {hp_knight} жизней"
            )
        if move == "sword":
            if knight_type != "Warrior":
                sword = item.sword()
                print(
                    f"MEЧ .сила удара равна {sword} \n"
                    f"забрать - 1 или отказаться - 2.\n"
                    f"Сейчас сила вашего удара равна {si_knight}"
                )
                number = item.new_weapon()
                new_sword = number
                if new_sword == "1":
                    si_knight = sword
            else:
                si_knight = si_knight + 10
                print(
                    f"MEЧ .сила удара увеличена на 10 и равна {si_knight} "
                )

        if move == "archer":
            if Knight.have_weapon['impact_strength_archer'] == None:
                si_knight_archer = k.ImpactStrengthArcher()
            if knight_type != "Archer":
                archer = item.archer()
                print(
                    f"ЛУК.его сила удара равна {archer} \n"
                    f"забрать - 1 или отказаться - 2.\n"
                    f"Сейчас сила вашего удара равна {si_knight_archer}"
                )
                number = item.new_weapon()
                new_archer = number
                if new_archer == "1":
                    si_knight_archer = archer
            else:
                si_knight_archer = si_knight_archer + 10
                print(
                    f"ЛУК.сила удара увеличена на 10 и равна {si_knight_archer} "
                )
        if move == "arrows":
            if Knight.have_weapon['impact_strength_archer'] == None:
                print(
                    f"Стрелы. забрать - 1 или отказаться - 2."
                )
                number = item.new_weapon()
                if number == "1":
                    k.ImpactStrengthArrow()
        if move == "magician book":
            if Knight.have_weapon['impact_strength_magician'] == None:
                si_knight_magician = k.ImpactStrengthMagician()
            if knight_type != "Magician":
                magician_book = item.magician_book()
                print(
                    f"КНИГА: сила удара равна {magician_book} \n"
                    f"забрать - 1 или отказаться - 2.\n"
                    f"Сейчас сила вашего удара равна {si_knight}"
                )
                number = item.new_weapon()
                new_book = number
                if new_book == "1":
                    si_knight_magician = magician_book
            else:
                si_knight_magician += 10
                print(
                    f"КНИГА .сила удара увеличена на 10 и равна {si_knight} "
                )
        if move == "totem":
            pass
        if move == "monster":
            m = Monster()
            hp_monster = m.Hp()
            msi = m.ImpactStrength()
            monster_type = m.type_attack()
            print(
                f"БОЙ. Чудовище, его сила удара равна {msi} \n"
                f"количество его жизней - {hp_monster}. Его тип {monster_type}\n"
                f"ваша сила удара {si_knight}, ваше количество жизней {hp_knight}\n"
                f"принять БОЙ - 1 или убежать - 2.\n"
                f"Вы уже убили {Monster.monster_counter} чудовищ"
                f"сейчас у вас есть {Knight.have_weapon}"
            )
            number = item.new_weapon()
            wor = number
            if wor == "1":
                knight_type = k.type_attack_knight_war()
                if knight_type == 'Warrior':
                    si_knight = k.have_weapon["impact_strength_war"]
                    print(f"Вы сменили оружие, на меч {si_knight}")
                if knight_type == 'Archer':
                    si_knight = k.have_weapon["impact_strength_archer"]
                    print( f"Вы сменили оружие, на лук {si_knight}" )
                while hp_monster > 0 and hp_knight > 0:
                    hp_monster -= si_knight
                    if hp_monster > 0:
                        if monster_type == knight_type:
                            knight_dodged = item.knight_dodged()
                            if knight_dodged < 6:
                                print(f"Вы НЕ увернулись от удара")
                                hp_knight = hp_knight - msi
                            else:
                                print(f"Вы увернулись от удара")
                        else:
                            hp_knight = hp_knight - msi
                Monster.monster_counter += 1
    if Monster.monster_counter >= 10 and hp_knight > 0:
        print("ПОБЕДА")
    else:
        print("ПОРАЖЕНИЕ")
    exit()

game()