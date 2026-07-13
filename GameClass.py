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
        self.scoresheet = scoshe.ScoreSheet("nick")

    def game_over_check(self): # this method checks if the game is over and all scoresheet fields are filled
        if None not in self.scoresheet.__dict__.values():
            print("Game Over")

    def game_loop(self): # This method starts the game loop and thus counts down 13 Rounds
        # might be useless as we are using pygame
        while self.__rounds_left != 0:
            self.__rounds_left -= 1
            self._round_loop()

    def _round_loop(self): # This method starts a round loop
        #for i in range(self.__rerolls_left):
        #   pass
        # This will not be a standard loop we need to make it so the reroll button must be 
        # pressed atleast once and can be pressed 2 additional times
        # after rolling atleast once can the decision wether or not you want to fill in a field be made
        # only after that does the round loop end
        pass
        
    def roll_all_dice(self): # This method rolls every die or the locked die will not get rolled
        for die in self.dice_list:
            die.roll()
    
    def print_all_dice(self): # This method prints out the eyecount of every die for now only usefull for debugging
        for die in self.dice_list:
            print(die.get_eyes())

if __name__ == "__main__":
    game = Game()
    game.game_loop()
    game.game_over_check()