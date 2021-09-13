import random

from knight import Knight
from monster import Monster


class Item():
    """Создание переменных для одной игры."""

    have_totem = {
        "monster_counter_safe": None,
        "hp_knight_totem": None,
        "impact_strength_magician": None,
        "impact_strength_archer": None,
        "impact_strength_arrow": None,
        "impact_strength_war": None}

    def select_item(self) -> str:
        """Выбор того, что будет происходить на слудующем ходу."""
        item_list = random.choice(("apple", "arrows", "sword", "archer",
                                   "magician book", "monster", "monster",
                                   "monster", "totem"))
        return item_list

    def sword(self) -> int:
        """Новая сила удара меча."""
        sword = random.randint(10, 100)
        return sword

    def magician_book(self) -> int:
        """Новая сила удара книги."""
        magician_book = random.randint(10, 100)
        return magician_book

    def archer(self) -> int:
        """Новая сила удара лука."""
        archer = random.randint(10, 100)
        return archer

    def arrow(self) -> bool:
        """Выдаем рыцарю стрелы."""
        arrow = True
        return arrow

    def totem_safe(self, y: int) -> list:
        """Сохранение параметров игры при взятии тотема."""
        Item.have_totem["monster_counter_safe"] = Monster.monster_counter
        Item.have_totem["hp_knight_totem"] = y
        Item.have_totem["impact_strength_magician"] = Knight.have_weapon['impact_strength_magician']
        Item.have_totem["impact_strength_archer"] = Knight.have_weapon['impact_strength_archer']
        Item.have_totem["impact_strength_arrow"] = Knight.have_weapon['impact_strength_arrow']
        Item.have_totem["impact_strength_war"] = Knight.have_weapon['impact_strength_war']
        return [Item.have_totem["monster_counter_safe"], Item.have_totem["hp_knight_totem"],
                Item.have_totem["impact_strength_magician"], Item.have_totem["impact_strength_archer"],
                Item.have_totem["impact_strength_arrow"], Item.have_totem["impact_strength_war"]]

    def totem_del(self) -> list:
        """Удаление параметров при использовании тотема."""
        Item.have_totem["monster_counter_safe"] = None
        Item.have_totem["hp_knight_totem"] = None
        Item.have_totem["impact_strength_magician"] = None
        Item.have_totem["impact_strength_archer"] = None
        Item.have_totem["impact_strength_arrow"] = None
        Item.have_totem["impact_strength_war"] = None
        return [Item.have_totem["monster_counter_safe"], Item.have_totem["hp_knight_totem"],
                Item.have_totem["impact_strength_magician"], Item.have_totem["impact_strength_archer"],
                Item.have_totem["impact_strength_arrow"], Item.have_totem["impact_strength_war"]]

    def new_wor(self) -> str:
        """Биться с монстром или убежать."""
        new_weapon = input("введите 1, 2 или 3:")
        while new_weapon != "1" and new_weapon != "2" and new_weapon != "3":
            print("Вы ввели недопустимое значение")
            new_weapon = input("введите 1, 2 или 3:")
        return new_weapon

    def new_thing(self) -> str:
        """Выбор - брать новое оружие или нет."""
        new_thing = input("введите 1 или 2:")
        while new_thing != "1" and new_thing != "2":
            print("Вы ввели недопустимое значение")
            new_thing = input("введите 1 или 2:")
        return new_thing

    def knight_dodged(self) -> int:
        """Вероятность укланения рыцаря от атаки монстра."""
        knight_dodged = random.randint(0, 10)
        return knight_dodged
