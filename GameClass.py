import DiceClass as D
import scoresheet as scoshe

class Game:
    def __init__(self):
        self.__rerolls_left = 3
        self.__kniffel_rolled = False
        dice1 = D.Dice()
        dice2 = D.Dice()
        dice3 = D.Dice()
        dice4 = D.Dice()
        dice5 = D.Dice()
        self.dice_list = (dice1, dice2, dice3, dice4, dice5)
        self.scoresheet = scoshe.ScoreSheet()

    def game_over_check(self): # this method checks if the game is over and all scoresheet fields are filled
        if None not in self.scoresheet.__dict__.values():
            self.score_bonus()
            self.tally_total()
            print("Game Over")

    def reset_rerolls(self): # This method resets the rerolls. should be triggered every round
        self.__rerolls_left = 3
        
    def roll_all_dice(self): # This method rolls every die or the locked die will not get rolled. can only be rolled a max of 3 times
        if self.__rerolls_left < 0:
            for die in self.dice_list:
                die.roll()
            self.__rerolls_left -= 1

    def print_all_dice(self): # This method prints out the eyecount of every die. for now only usefull for debugging
        for die in self.dice_list:
            print(die.get_eyes())

    def score_upper_part(self):
        upper_part = [self.scoresheet.ones + self.scoresheet.twos + self.scoresheet.threes + self.scoresheet.fours + self.scoresheet.fives + self.scoresheet.sixes]
        for number in upper_part:
            if type(number) == int:
                total += number
        return total

    def score_bonus(self):
        if self.score_upper_part() >= 63 :
            self.scoresheet.bonus = 35
        else:
            self.scoresheet.bonus = 0

    def ones(self): # this method is to be used by the button for ones
        self.scoresheet.ones = self.scoresheet.score_upper(self.dice_list, 1)
        self.reset_rerolls()

    def twos(self): # this method is to be used by the button for twos
        self.scoresheet.twos = self.scoresheet.score_upper(self.dice_list, 2)
        self.reset_rerolls()

    def threes(self): # this method is to be used by the button for threes
        self.scoresheet.threes = self.scoresheet.score_upper(self.dice_list, 3)
        self.reset_rerolls()
    
    def fours(self): # this method is to be used by the button for fours
        self.scoresheet.fours = self.scoresheet.score_upper(self.dice_list, 4)
        self.reset_rerolls()
    
    def fives(self): # this method is to be used by the button for fives
        self.scoresheet.fives = self.scoresheet.score_upper(self.dice_list, 5)
        self.reset_rerolls()
    
    def sixes(self): # this method is to be used by the button for sixes
        self.scoresheet.sixes = self.scoresheet.score_upper(self.dice_list, 6)
        self.reset_rerolls()
    
    def three_of_a_kind(self): # this method is to be used by the button for three of a kind
        self.scoresheet.three_of_a_kind = self.scoresheet.score_three_of_a_kind(self.dice_list)
        self.reset_rerolls()

    def four_of_a_kind(self): # this method is to be used by the button for four of a kind
        self.scoresheet.four_of_a_kind = self.scoresheet.score_four_of_a_kind(self.dice_list)
        self.reset_rerolls()
    
    def full_house(self): # this method is to be used by the button for full house
        self.scoresheet.full_house = self.scoresheet.score_full_house(self.dice_list)
        self.reset_rerolls()

    def small_straight(self): # this method is to be used by the button for small straight
        self.scoresheet.small_straight = self.scoresheet.score_small_straight(self.dice_list)
        self.reset_rerolls()

    def large_straight(self): # this method is to be used by the button for large straight
        self.scoresheet.large_straight = self.scoresheet.score_large_straight(self.dice_list)
        self.reset_rerolls()

    def kniffel(self): # this method is to be used by the button for kniffel
        self.scoresheet.kniffel = self.scoresheet.score_kniffel(self.dice_list)
        self.reset_rerolls()

    def chance(self): # this method is to be used by the button for chance
        self.scoresheet.chance = self.scoresheet.score_chance(self.dice_list)
        self.reset_rerolls()

    # This Method is meant to lock or unlock the die of corresponding number and used for the buttons of these die
    def lock_unlock_die(self, number):
        self.dice_list[number - 1].lock_unlock()
    
    def tally_total(self):
        x = self.scoresheet.__dict__
        return
if __name__ == "__main__":
    game = Game()
    game.game_over_check()
    game.tally_total()