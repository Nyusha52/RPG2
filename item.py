import random


class Item():

    def select_item(self):
        item_list = random.choice(("apple", "arrows", "sword", "archer", "magician book", "monster", "monster", "monster", "totem"))
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

    def arrow(self):
        arrow = True
        return arrow

    def totem(self):
        pass
        return Item.totem

    def new_weapon(self):
        new_weapon = input("введите 1 или 2:")
        while new_weapon != "1" and new_weapon != "2":
            print("Вы ввели недопустимое значение")
            new_weapon = input("введите 1 или 2:")
        return new_weapon

    def knight_dodged(self):
        knight_dodged = random.randint(0, 10)
        return knight_dodged