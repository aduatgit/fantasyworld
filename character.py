from classes import *
from abc import ABC
import time
import random

class Character(ABC):
    def __init__(self, name: str, age: int, gender: str, _class: Class, race="Human") -> None:
        self.name: str = name
        self.age: int = age
        self.gender: str = gender
        self._class: Class = _class
        self.race: str = race
        self.max_health: int = 250
        self.curr_health: int = self.max_health
        self.armor: int = 0
        self.current_xp: int = 0
        self.level: int = 1
        self.crit_chance: float = 0.9
        self.crit_dmg: int = 2

    #Takes an ability string and an target Character as input
    #Prints the attack action to the console and calls the takeDamage() method of the target
    def attack(self, ability, target):
        if ability in self._class.abilities:
            crit_dmg, crit = self._calculateCrit(self._class.abilities[ability])
            print(f"{self} {self._class.ability_verb[ability]} {target}!")
            if crit:
                time.sleep(1)
                print(f"{ability} critically strikes!")
            time.sleep(1)
            target._takeDamage(crit_dmg, self)

    def __str__(self) -> str:
        return f"{self.name} the {self._class}"
    
    #Takes an int input of the damage a character is taking
    #If the character is of the warrior class, rage is generated
    #This method should only be invoked by other methods, such as attack()
    def _takeDamage(self, dmg, other):
        post_mit_dmg = dmg - self.armor
        self.curr_health -= post_mit_dmg
        print(f"{self} took {post_mit_dmg} damage!")
        time.sleep(1)
        if self.curr_health <= 0:
            self._deathAction(other)
        else:
            print(f"{self} has {self.curr_health} health left!")
            time.sleep(1)
            if self._class.getClassName() == "Warrior" and self._class.curr_rage < self._class.max_rage:
                print(f"{self} {self._class.gainRage(post_mit_dmg)}")
                time.sleep(1)
    
    def _calculateCrit(self, dmg):
        if random.randrange(0,99) < self.crit_chance*100:
            return dmg*self.crit_dmg, True
        return dmg, False

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
        "{self} has been vanquished by the forces of {target}.",
        "Alas, {self} has fallen in battle to {target}. Better luck next time.",
        "{target} has claimed the soul of {self}. Game over.",
        "{self} fought bravely against {target}, but it was not enough.",
        "{self}'s journey ends here at the hands of {target}. May {self} find peace in the afterlife.",
        "{self} was bested by the monsters, led by {target}. Try again?",
        "{self}'s adventure comes to a tragic end due to {target}.",
        "{self} has succumbed to the wounds inflicted by {target}. Rest in peace.",
        "The battle was fierce, but {self} was overpowered by {target}.",
        "{self} was a worthy opponent, but fate was not on {self}'s side against {target}."
        ]

        message = death_messages[random.randint(0,9)].format(self=self, target=other)
        print(f"{self.name} has 0 hp left!")
        time.sleep(1)
        print(message)
        time.sleep(1)