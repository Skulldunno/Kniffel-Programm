import random

class Dice:
    def __init__(self, eyes = 1, locked = False):
        self.__eyes = eyes
        self.__locked = locked

    def roll(self): # This Method rolls the die and gives random number from 1 to 6
        if self.__locked == False:
            self.__eyes = random.randint(1,6)

    def get_eyes(self): # This Method gets the eye count
        return self.__eyes
    
    def lock_unlock(self): # This Method either locks or unlocks the die based on the previous state
        if self.__locked == False:
            self.__locked = True
        else:
            self.__locked = False

if __name__ == "__main__":
    dice1 = Dice()
    dice2 = Dice()
    dice3 = Dice()

    dice1.roll()
    dice2.roll()
    dice3.roll()

    print(f"{dice1.get_eyes()} {dice2.get_eyes()} {dice3.get_eyes()}")

    dice2.lock_unlock()
    dice1.roll()
    dice2.roll()
    dice3.roll()

    print(f"{dice1.get_eyes()} {dice2.get_eyes()} {dice3.get_eyes()}")

    dice1.roll()
    dice2.roll()
    dice3.roll()

    print(f"{dice1.get_eyes()} {dice2.get_eyes()} {dice3.get_eyes()}")

    dice1.roll()
    dice2.roll()
    dice3.roll()

    print(f"{dice1.get_eyes()} {dice2.get_eyes()} {dice3.get_eyes()}")

    dice2.lock_unlock()
    dice1.roll()
    dice2.roll()
    dice3.roll()

    print(f"{dice1.get_eyes()} {dice2.get_eyes()} {dice3.get_eyes()}")

    dice1.roll()
    dice2.roll()
    dice3.roll()

    print(f"{dice1.get_eyes()} {dice2.get_eyes()} {dice3.get_eyes()}")