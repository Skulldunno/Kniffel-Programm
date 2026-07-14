import random

class Dice:
    def __init__(self):
        self.__eyes = 1
        self.__locked = False

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
