class Weapon:
    def __init__(self, name, damage, radius):
        self.name = name
        self.damage = damage
        self.radius = radius

    def hit(self, actor, target):
        if target.is_alive():
            if ((target.pos_x - actor.pos_x)**2 + (target.pos_y - actor.pos_y)**2)**0.5 > self.radius:
                print(f"Враг слишком далеко для оружия {self}")
            else:
                print(f"Врагу нанесен урон оружием {self} в размере {self.damage}")
                target.get_damage(actor.current_weapon.damage)
        else:
            print("Враг уже повержен")

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x, self.pos_y = pos_x, pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        return bool(self.hp)

    def get_damage(self, amount):
        if self.hp <= amount:
            self.hp = 0
        else:
            self.hp -= amount

    def get_coords(self):
        return self.pos_x, self.pos_y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        self.current_weapon = weapon
        super().__init__(pos_x, pos_y, hp)

    def hit(self, target):
        if isinstance(target, MainHero):
            self.current_weapon.hit(self, target)
        else:
            print("Могу ударить только Главного героя")

    def __str__(self):
        return f"Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.current_weapon}"


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        self.name = name
        self.weapon = []
        self.current_weapon = None
        self.max_hp = 200
        super().__init__(pos_x, pos_y, hp)

    def hit(self, target):
        if not self.weapon:
            print("Я безоружен")
        elif isinstance(target, BaseEnemy):
            self.current_weapon.hit(self, target)
        else:
            print("Могу ударить только Врага")

    def add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            print(f"Подобрал {weapon}")
            if not self.current_weapon:
                self.current_weapon = weapon
                self.weapon += [weapon]
            else:
                self.weapon += [weapon]
        else:
            print("Это не оружие")

    def next_weapon(self):
        if not self.current_weapon:
            print("Я безоружен")
        elif len(self.weapon) == 1:
            print("У меня только одно оружие")
        else:
            if self.weapon.index(self.current_weapon) + 1 >= len(self.weapon):
                index = len(self.weapon) - self.weapon.index(self.current_weapon)
                self.current_weapon = self.weapon[index]
            else:
                self.current_weapon = self.weapon[self.weapon.index(self.current_weapon) - 1]
                print(f"Сменил оружие на {self.current_weapon}")

    def heal(self, amount):
        if self.hp + amount >= self.max_hp:
            self.hp = 200
        else:
            self.hp += amount
        print(f"Полечился, теперь здоровья {self.hp}")