import copy


class Player:
    def __init__(self):
        self._strength, self._agility, self._intelligence, self._speed = 0, 0, 0, 0
        self.current_weapon = [None, None]

    def __lshift__(self, other):
        if self.current_weapon[0] is None and self.current_weapon[1] is None:
            if other.is_one_handed():
                self.current_weapon = [other, None]
            else:
                self.current_weapon = [other, other]
        else:
            if self.current_weapon[0] and self.current_weapon[1] is None:
                if self.current_weapon[0].is_one_handed() and other.is_one_handed():
                    self.current_weapon[1] = other
                else:
                    self.current_weapon = [other, other]
                    # wrong
            elif self.current_weapon[1] and self.current_weapon[0] is None:
                if self.current_weapon[1].is_one_handed() and other.is_one_handed():
                    self.current_weapon[1] = other
                else:
                    self.current_weapon = [other, other]
                    # wrong
            elif self.current_weapon[0] and self.current_weapon[1]:
                if self.current_weapon[0].is_one_handed() and other.is_one_handed():
                    self.current_weapon = [other, None]
                else:
                    self.current_weapon = [other, other]

    def strength(self):
        return sum([i.strength() for i in self.current_weapon if i])

    def agility(self):
        return sum([i.agility() for i in self.current_weapon if i])

    def intelligence(self):
        return sum([i.intelligence() for i in self.current_weapon if i])

    def speed(self):
        if not len([i for i in self.current_weapon if i]):
            return 0
        return sum([i.speed() for i in self.current_weapon if i]) // len([i for i in self.current_weapon if i])

    def take_up_weapon(self, weapon):
        self << weapon

    def throw_a_weapon(self):
        self.current_weapon = [None, None]

    def __neg__(self):
        self.throw_a_weapon()

    def __str__(self):
        weapon_count = len([i for i in self.current_weapon if i])
        if self.current_weapon[0] and not self.current_weapon[0].is_one_handed() or \
                self.current_weapon[1] and not self.current_weapon[1].is_one_handed():
            weapon_count = 1
        return f"Player[{weapon_count}](" \
            f"Strength: {self.strength()}, " \
            f"Agility: {self.agility()}, " \
            f"Intelligence: {self.intelligence()}, " \
            f"Speed: {self.speed()} )"


class Weapon:
    def __init__(self, one_handed=True, strength=0, agility=0, intelligence=0, speed=0):
        self.one_handed = one_handed
        self._strength = strength
        self._agility = agility
        self._intelligence = intelligence
        self._speed = speed

    def is_one_handed(self):
        return self.one_handed

    def strength(self):
        return self._strength

    def agility(self):
        return self._agility

    def intelligence(self):
        return self._intelligence

    def speed(self):
        return self._speed

    def copy(self):
        return Weapon(self.one_handed, self._strength, self._agility, self._intelligence, self._speed)

    def __mul__(self, number):
        return Weapon(self.one_handed, self._strength, self._agility, self._intelligence, self._speed * number)

    def __imul__(self, number):
        return Weapon(self.one_handed, self._strength, self._agility, self._intelligence, self._speed * number)

    def __add__(self, scd):
        return Weapon(False, self._strength + scd._strength,
                      self._agility + scd._agility,
                      self._intelligence + scd._intelligence,
                      self._speed + scd._speed)

    def __iadd__(self, scd):
        return self + other

    def __str__(self):
        hand_count = 1 if self.one_handed else 2
        return f"Weapon{[hand_count]}(strength: {self.strength()}, agility: {self.agility()}," + \
               f"intelligence: {self.intelligence()}, speed: {self.speed()})"


weapon1 = Weapon(strength=2, speed=5)
weapon2 = Weapon(intelligence=5, speed=1)
weapon3 = weapon1 + weapon2

print(weapon1)
print(weapon2)
print(weapon3)
print('---')
player = Player()
player.take_up_weapon(weapon1)
print(player, end='\n---\n')
player.take_up_weapon(weapon2)
print(player, end='\n---\n')
player.throw_a_weapon()
print(player, end='\n---\n')
player << weapon1
player << weapon2
player << weapon3
print(player, end='\n---\n')
-player
print(player, end='\n---\n')