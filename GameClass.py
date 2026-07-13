import DiceClass as D

class Game:
    def __init__(self):
        self.__rerolls_left = 3
        self.__rounds_left = 13
        dice1 = D.Dice()
        dice2 = D.Dice()
        dice3 = D.Dice()
        dice4 = D.Dice()
        dice5 = D.Dice()
        self.dice_list = (dice1, dice2, dice3, dice4, dice5)

    def game_loop(self): # This method starts the game loop and thus counts down 13 Rounds
        while self.__rounds_left != 0:
            self.__rounds_left -= 1
            self.round_loop()

    def round_loop(self): # This method starts a round loop and repeats at max 3 times
        for i in range(self.__rerolls_left):
            pass

    def roll_all_dice(self): # This method rolls every die or the locked die will not get rolled
        for die in self.dice_list:
            die.roll()
    
    def print_all_dice(self): # This method prints out the eyecount of every die for now only usefull for debugging
        for die in self.dice_list:
            print(die.get_eyes())

if __name__ == "__main__":
    game1 = Game()
    game1.game_loop()
    game1.print_all_dice()
    game1.roll_all_dice()
    game1.print_all_dice()