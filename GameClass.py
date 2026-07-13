import DiceClass as D
import scoresheet as scoshe

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
        self.scoresheet = scoshe.ScoreSheet()

    def game_over_check(self): # this method checks if the game is over and all scoresheet fields are filled
        if None not in self.scoresheet.__dict__.values():
            print("Game Over")

    def game_loop(self): # This method starts the game loop and thus counts down 13 Rounds
        # might be useless as we are using pygame
        while self.__rounds_left != 0:
            self.__rounds_left -= 1
            self._round_loop()

    def _round_loop(self): # This method starts a round loop, which is just a reset of rerolls and not an actual loop
        # might also be useless as we are using pygame
        self.__rerolls_left = 3
        
    def roll_all_dice(self): # This method rolls every die or the locked die will not get rolled can only be rolled a max of 3 times
        if self.__rerolls_left < 0:
            for die in self.dice_list:
                die.roll()
            self.__rerolls_left -=0

    def print_all_dice(self): # This method prints out the eyecount of every die for now only usefull for debugging
        for die in self.dice_list:
            print(die.get_eyes())

if __name__ == "__main__":
    game = Game()
    game.game_loop()
    game.game_over_check()