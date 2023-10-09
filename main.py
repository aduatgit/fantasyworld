from character import *
import time

def main():
    char1 = Player("John", 3, True, Archer())
    print(f"Successfully created character {char1}!")
    time.sleep(1)
    char2 = Enemy("Oleg", 30, False, Warrior())
    char2.dead = True
    print(f"Successfully created character {char2}!")
    time.sleep(1)
    char1.attack("Shoot", char2)
    char1.attack("Shoot", char2)
    char1.attack("Shoot", char2)

main()