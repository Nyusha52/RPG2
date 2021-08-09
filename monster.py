import random


class Monster():
    """Создание монстра."""

    monster_counter = 0
    impact_strength_monster = 0
    hp_monster = 0
    # type = None

    def ImpactStrength(self) -> int:
        """Сила удара монстра."""
        Monster.impact_strength_monster = random.randint(5, 20)
        return Monster.impact_strength_monster

    def Hp(self) -> int:
        """Здоровье монстра."""
        Monster.hp_monster = random.randint(50, 100)
        return Monster.hp_monster

    def type_attack(self) -> str:
        """Тип монстра."""
        monster = random.choice(('Warrior', 'Magician', 'Archer'))
        if monster == 'Warrior':
            type = 'Warrior'
        if monster == 'Magician':
            type = 'Magician'
        if monster == 'Archer':
            type = 'Archer'
        return type
