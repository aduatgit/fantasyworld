from abc import ABC

class Class(ABC):
    def __init__(self, main_stat, health_multiplier, ressource_type, base_armor, armor_type, class_name) -> None:
        self._main_stat = main_stat
        self._health_multiplier = health_multiplier
        self._ressource_type = ressource_type
        self._base_armor = base_armor
        self._armor_type = armor_type
        self._class_name = class_name
        self.abilities = {}
        self.ability_verb = {
            "Slash": "slashes",
            "Shoot": "shoots",
            "Fireball": "casts fireball at"
        }

    def getHealthMultiplier(self):
        return self._health_multiplier

    def getBaseArmor(self):
        return self._base_armor
    
    def getMainStatType(self):
        return self._main_stat
    
    def getRessourceType(self):
        return self._ressource_type
    
    def getClassName(self):
        return self._class_name
    
class Warrior(Class):
    slash_base = 80

    def __init__(self) -> None:
        super().__init__("Strength", 1.2, "Rage", 100, "Plate", "Warrior")
        self.max_rage = 100
        self.curr_rage = 0
        self.abilities = {
            "Slash": self.slash()
        }

    def gainRage(self, amount):
        if self.curr_rage == self.max_rage:
            return
        elif self.curr_rage + amount > self.max_rage:
            gained_rage = self.max_rage - self.curr_rage
            self.curr_rage = self.max_rage
            return f"gained {gained_rage} rage!"
        else:
            self.curr_rage += amount
            return f"gained {amount} rage!"

    def slash(self):
        return self.slash_base
        
class Archer(Class):
    shoot_base = 100

    def __init__(self) -> None:
        super().__init__("Agility", 1, "Arrows", 65, "Leather", "Archer")
        self._arrows = 0
        self.abilities = {
            "Shoot": self.shoot()
        }

    def getArrows(self):
        return self._arrows
    
    def shoot(self):
        return self.shoot_base

class Mage(Class):
    fireball_base = 120

    def __init__(self) -> None:
        super().__init__("Intellect", 0.8, "Mana", 30, "Cloth", "Mage")
        self.mana = 0
        self.abilities = {
            "Fireball": self.fireball()
        }

    def fireball(self):
        return self.fireball_base