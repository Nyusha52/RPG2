from item import Item
from knight import Knight
from monster import Monster

def game() -> None:
    """Игра в рыцаря."""
    i = Item()
    k = Knight()
    hp_knight = k.Hp()
    si_knight = i.sword()
    si_knight_sword = si_knight
    Knight.have_weapon['impact_strength_war'] = si_knight
    hp_plus = k.hp_plus()
    knight_type = k.type_attack_knight()

    while Monster.monster_counter < 10 and hp_knight > 0:
        move = i.select_item()
        if move == "apple":
            hp_knight += hp_plus
            print(
                f"ЯБЛОКО, вам прибавлено {hp_plus} жизней,\n"
                f" теперь у вас {hp_knight} жизней"
            )
        if move == "sword":
            if knight_type != "Warrior":
                sword = i.sword()
                print(
                    f"MEЧ .сила удара равна {sword} \n"
                    f"забрать - 1 или отказаться - 2.\n"
                    f"Сейчас сила вашего удара равна {si_knight_sword}"
                )
                number = i.new_thing()
                new_sword = number
                if new_sword == "1":
                    Knight.have_weapon['impact_strength_war'] = sword

            else:
                Knight.have_weapon['impact_strength_war'] = Knight.have_weapon['impact_strength_war'] + 10
                print(
                    f"MEЧ .сила удара увеличена на 10 и равна {si_knight} "
                )

        if move == "archer":
            if knight_type != "Archer":
                archer = i.archer()
                print(
                    f"ЛУК.его сила удара равна {archer} \n"
                    f"забрать - 1 или отказаться - 2.\n"
                    f"Сейчас сила вашего удара равна {Knight.have_weapon['impact_strength_archer']}"
                )
                number = i.new_thing()
                new_archer = number
                if new_archer == "1":
                    Knight.have_weapon['impact_strength_archer'] = archer
            if knight_type == "Archer" and Knight.have_weapon['impact_strength_archer'] != None:
                Knight.have_weapon['impact_strength_archer'] = Knight.have_weapon['impact_strength_archer'] + 10
                print(
                    f"ЛУК.сила удара увеличена на 10 и равна {Knight.have_weapon['impact_strength_archer']} "
                )
            if knight_type == "Archer" and Knight.have_weapon['impact_strength_archer'] == None:
                archer = i.archer()
                print(
                    f"ЛУК.его сила удара равна {archer} \n"
                    f"забрать - 1 или отказаться - 2.\n"
                    f"Сейчас сила вашего удара равна 0"
                )
                number = i.new_thing()
                new_archer = number
                if new_archer == "1":
                    Knight.have_weapon['impact_strength_archer'] = archer
        if move == "arrows":
            if Knight.have_weapon['impact_strength_arrow'] == None:
                print(
                    f"Стрелы. забрать - 1 или отказаться - 2."
                )
                number = i.new_thing()
                if number == "1":
                    Knight.have_weapon['impact_strength_arrow'] = i.arrow()
        if move == "magician book":
            if knight_type != "Magician":
                magician_book = i.magician_book()
                print(
                    f"КНИГА: сила удара равна {magician_book} \n"
                    f"забрать - 1 или отказаться - 2.\n"
                    f"Сейчас сила вашего удара равна {Knight.have_weapon['impact_strength_magician']}"
                )
                number = i.new_thing()
                new_book = number
                if new_book == "1":
                    Knight.have_weapon['impact_strength_magician'] = magician_book
            if knight_type == "Magician" and Knight.have_weapon['impact_strength_magician'] != None:
                Knight.have_weapon['impact_strength_magician'] += 10
                print(
                    f"КНИГА .сила удара увеличена на 10 и равна {Knight.have_weapon['impact_strength_magician']} "
                )
            if knight_type == "Magician" and Knight.have_weapon['impact_strength_magician'] == None:
                magician_book = i.magician_book()
                print(
                    f"КНИГА: сила удара равна {magician_book} \n"
                    f"забрать - 1 или отказаться - 2.\n"
                    f"Сейчас сила вашего удара равна {Knight.have_weapon['impact_strength_magician']}"
                )
                number = i.new_thing()
                new_book = number
                if new_book == "1":
                    Knight.have_weapon['impact_strength_magician'] = magician_book
        if move == "totem":
            print(
                f"ТОТЕМ"
                f"забрать - 1 или отказаться - 2"
            )
            totem = i.new_thing()
            new_totem = totem
            if new_totem == "1":
                i.totem_safe(hp_knight)
                print(
                    f"вы взяли тотем"
                )
        if move == "monster":
            m = Monster()
            hp_monster = m.Hp()
            msi = m.ImpactStrength()
            monster_type = m.type_attack()
            print(
                f"БОЙ. Чудовище, его сила удара равна {msi} \n"
                f"количество его жизней - {hp_monster}. Его тип {monster_type}\n"
                f"сейчас у вас есть {Knight.have_weapon}, ваше количество жизней {hp_knight}\n"
                f"принять БОЙ - 1, убежать - 2 или вернуть ся на сохраненное место - 3.\n"
                f"Вы уже убили {Monster.monster_counter} чудовищ"
            )
            number = i.new_wor()
            wor = number
            if wor == "3":
                if Item.have_totem["hp_knight_totem"] != None:
                    Monster.monster_counter = Item.have_totem["monster_counter_safe"]
                    hp_knight = Item.have_totem["hp_knight_totem"]
                    Knight.have_weapon['impact_strength_magician'] = Item.have_totem["impact_strength_magician"]
                    Knight.have_weapon['impact_strength_archer'] = Item.have_totem["impact_strength_archer"]
                    Knight.have_weapon['impact_strength_arrow'] = Item.have_totem["impact_strength_arrow"]
                    Knight.have_weapon['impact_strength_war'] = Item.have_totem["impact_strength_war"]
                    print ('тотем использован')
                    i.totem_del()
                    print(Item.have_totem["hp_knight_totem"])
                else:
                    print(
                        f"У вас нет тотема"
                    )
                    number = i.new_wor()
                    wor = number
            if wor == "1":
                knight_weapon = k.type_attack_knight_war()
                if knight_weapon == 'Warrior':
                    si_knight = k.have_weapon["impact_strength_war"]
                    print(f"ваше оружие меч {si_knight}")
                if knight_weapon == 'Archer':
                    si_knight = k.have_weapon["impact_strength_archer"]
                    print( f"ваше оружие лук {si_knight}" )
                if knight_weapon == 'Magician':
                    si_knight = k.have_weapon["impact_strength_archer"]
                    print(f"ваше оружие книга {si_knight}")
                while hp_monster > 0 and hp_knight > 0:
                    hp_monster -= si_knight
                    if hp_monster > 0:
                        if monster_type == knight_type:
                            knight_dodged = i.knight_dodged()
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