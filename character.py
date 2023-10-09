from classes import *
from classes import Class
from abc import ABC
import time
import random

class Character(ABC):
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

    #Takes an ability string and an target Character as input
    #Prints the attack action to the console and calls the takeDamage() method of the target
    def attack(self, ability, target):
        if ability in self._class.abilities:
            print(f"{self.name} {self._class.ability_verb[ability]} {target.name}!")
            time.sleep(1)
            target._takeDamage(self._class.abilities[ability], self)


    #Takes an int input of the damage a character is taking
    #If the character is of the warrior class, rage is generated
    #This method should only be invoked by other methods, such as attack()
    def _takeDamage(self, dmg, other):
        post_mit_dmg = dmg - self.armor
        self.curr_health -= post_mit_dmg
        print(f"{self.name} took {post_mit_dmg} damage!")
        time.sleep(1)
        if self.curr_health <= 0:
            self._deathAction(other)
        else:
            print(f"{self.name} has {self.curr_health} health left!")
            time.sleep(1)
            if self._class.getClassName() == "Warrior" and self._class.curr_rage < self._class.max_rage:
                print(f"{self.name} {self._class.gainRage(post_mit_dmg)}")
                time.sleep(1)
    
    def _deathAction(self, other):
        pass


class Player(Character):
    def __init__(self, name: str, age: int, gender: bool, _class: Class, race="Human") -> None:
        super().__init__(name, age, gender, _class, race)

class Enemy(Character):
    def __init__(self, name: str, age: int, gender: bool, _class: Class, race="Orc", level=1, xp_drop=25) -> None:
        super().__init__(name, age, gender, _class, race)
        self.level = level
        self.xp_drop = xp_drop

    def _deathAction(self, other):
        death_messages = [
        "{self.name} has been vanquished by the forces of {target.name}.",
        "Alas, {self.name} has fallen in battle to {target.name}. Better luck next time.",
        "{target.name} has claimed the soul of {self.name}. Game over.",
        "{self.name} fought bravely against {target.name}, but it was not enough.",
        "{self.name}'s journey ends here at the hands of {target.name}. May {self.name} find peace in the afterlife.",
        "{self.name} was bested by the monsters, led by {target.name}. Try again?",
        "{self.name}'s adventure comes to a tragic end due to {target.name}.",
        "{self.name} has succumbed to the wounds inflicted by {target.name}. Rest in peace.",
        "The battle was fierce, but {self.name} was overpowered by {target.name}.",
        "{self.name} was a worthy opponent, but fate was not on {self.name}'s side against {target.name}."
        ]
        message = death_messages[random.randint(0,9)].format(self=self, target=other)
        print(f"{self.name} has 0 hp left!")
        time.sleep(1)
        print(message)
        time.sleep(1)