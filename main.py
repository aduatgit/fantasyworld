from character import *
import time

def main():
    char1 = Character("John", 3, True, Archer())
    print(f"Successfully created character {char1.name}!")
    time.sleep(1)
    char2 = Enemy("Oleg", 30, False, Warrior())
    print(f"Successfully created character {char2.name}!")
    time.sleep(1)
    char1.attack("Shoot", char2)

main()