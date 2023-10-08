from classes import *
from classes import Class
import time

class Character():
    def __init__(self, name: str, age: int, gender: bool, _class: Class, race="Human") -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self._class = _class
        self.race = race
        self.max_health = 250
        self.curr_health = self.max_health
        self.armor = 0
        self.current_xp = 0
        self.level = 1
        self.crit_chance = 0.1
        self.crit_dmg = 2

    def attack(self, ability, target):
        if ability in self._class.abilities:
            print(f"{self.name} {self._class.ability_verb[ability]} {target.name}!")
            time.sleep(1)
            target.takeDamage(self._class.abilities[ability])

    def takeDamage(self, dmg):
        post_mit_dmg = dmg - self.armor
        self.curr_health -= post_mit_dmg
        print(f"{self.name} took {post_mit_dmg} damage!")
        time.sleep(1)
        if self.curr_health <= 0:
            print(f"{self.name} has 0 hp!")
            time.sleep(1)
            print(f"{self.name} dies! Unlucky!")
        else:
            print(f"{self.name} has {self.curr_health} health left!")
            time.sleep(1)
            if self._class.getClassName() == "Warrior":
                print(f"{self.name} " + self._class.gainRage(post_mit_dmg))
                


class Player(Character):
    def __init__(self, name: str, age: int, gender: bool, _class: Class, race="Human") -> None:
        super().__init__(name, age, gender, _class, race)

class Enemy(Character):
    def __init__(self, name: str, age: int, gender: bool, _class: Class, race="Orc", level=1, xp_drop=25) -> None:
        super().__init__(name, age, gender, _class, race)
        self.level = level
        self.xp_drop = xp_drop