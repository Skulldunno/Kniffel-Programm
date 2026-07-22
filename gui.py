import pygame
import widgets
import GameClass
import skinsets
import random
import sys


class Gui:
    def __init__(self):
        if sys.platform == "win32":
            import ctypes
            myappid = 'kniffelspiel.subid.version.1'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        
        pygame.init()

        pygame.display.set_icon(pygame.image.load("./assets/icon.png"))
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Kniffel Programm")

        self.game_manager = GameClass.Game()

        self.current_screen = StartScreen(self, self.game_manager)

        self.iconchanger = IconChanger()

    def change_screen(self, new_screen):
        self.current_screen = new_screen

    def start(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                self.current_screen.handle_events(event)

            self.current_screen.update()
            self.current_screen.draw(self.screen)

            #self.iconchanger.increment_frame_counter()
            #pygame.display.set_icon(self.iconchanger.icon_list[self.iconchanger.icon_index])

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


class IconChanger:
    def __init__(self):
        icon_one_png = pygame.image.load("assets/icon_one.png")
        icon_two_png = pygame.image.load("assets/icon_two.png")
        icon_three_png = pygame.image.load("assets/icon_three.png")
        icon_four_png = pygame.image.load("assets/icon_four.png")
        icon_five_png = pygame.image.load("assets/icon_five.png")
        icon_six_png = pygame.image.load("assets/icon_six.png")

        self.icon_list = [
            icon_one_png,
            icon_two_png, 
            icon_three_png,
            icon_four_png,
            icon_five_png,
            icon_six_png
            ]
        self.icon_index = 5
        self.frame_counter = 0

    def change_index(self):
        alt = self.icon_index
        while alt == self.icon_index:
            self.icon_index = random.randint(0, 5)       

    def increment_frame_counter(self):
        if self.frame_counter == 60:
            self.frame_counter = 0
            self.change_index()
        else:
            self.frame_counter += 1


class Screen:
    def __init__(self, manager, game_manager):
        self.manager = manager
        self.game_manager = game_manager

    def handle_events(self, event):
        pass

    def update(self):
        pass

    def draw(self, surface):
        pass

class StartScreen(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

        self.title_lable = widgets.Label("KNIFFEL", (400, 37.5), 80)

        self.highscore_rect = pygame.Rect((50, 85, 700, 75))
        self.highscore_label = widgets.Label("HIGHSCORE", (400, 122.5), 60)

        self.highscores_rect = pygame.Rect((200, 170, 400, 500))
        self.highscores_view = widgets.HighscoreView(game_manager.load_highscore())

        self.start_singelplayer_button = widgets.Button("Einzelspieler", (115, 700, 275, 60))
        self.start_singelplayer_button.set_action(self.start_singleplayer)

        self.start_multiplayer_button = widgets.Button("Mehrspieler", (410, 700, 275, 60))
        self.start_multiplayer_button.set_action(self.start_multiplayer)

    def start_singleplayer(self):
        self.game_manager = GameClass.Game()
        self.manager.change_screen(GameScreenSinglerplayer(self.manager, self.game_manager))

    def start_multiplayer(self):
        self.game_manager = GameClass.GameMultiplayer()
        self.manager.change_screen(GameScreenMultiplayer(self.manager, self.game_manager))

    def handle_events(self, event):
        self.start_singelplayer_button.handle_event(event)
        self.start_multiplayer_button.handle_event(event)

    def draw(self, surface):
        surface.fill((255, 255, 255))

        pygame.draw.line(surface, (0, 0, 0), (0, 75), (800, 75), 2)
        self.title_lable.draw(surface)

        pygame.draw.rect(surface, (0, 0, 0), self.highscore_rect, 2, 20)
        self.highscore_label.draw(surface)

        pygame.draw.rect(surface, (0, 0, 0), self.highscores_rect, 2, 20)
        self.highscores_view.draw(surface)

        self.start_singelplayer_button.draw(surface)
        self.start_multiplayer_button.draw(surface)

class GameScreenSinglerplayer(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

        self.title_lable = widgets.Label("Kniffel Gewinnkarte", (400, 37.5), 40)
        self.upper_left_rect = pygame.Rect((0, 75, 400, 275))
        self.ones_label = widgets.Label("nur Einser zählen", (100, 95), 26)
        self.arrow_ones = widgets.ArrowRight((200, 95), 30)
        self.ones_button = widgets.Button("", (235, 82.5, 140, 25))
        self.ones_button.set_action(self.enter_ones)
        self.twos_label = widgets.Label("nur Zweier zählen", (100, 125), 26)
        self.arrow_twos = widgets.ArrowRight((200, 125), 30)
        self.twos_button = widgets.Button("", (235, 112.5, 140, 25))
        self.twos_button.set_action(self.enter_twos)
        self.threes_label = widgets.Label("nur Dreier zählen", (100, 155), 26)
        self.arrow_threes = widgets.ArrowRight((200, 155), 30)
        self.three_button = widgets.Button("", (235, 142.5, 140, 25))
        self.three_button.set_action(self.enter_three)
        self.fours_label = widgets.Label("nur Vierer zählen", (100, 185), 26)
        self.arrow_fours = widgets.ArrowRight((200, 185), 30)
        self.fours_button = widgets.Button("", (235, 172.5, 140, 25))
        self.fours_button.set_action(self.enter_fours)
        self.fives_label = widgets.Label("nur Fünfer zählen", (100, 215), 26)
        self.arrow_fives = widgets.ArrowRight((200, 215), 30)
        self.fives_button = widgets.Button("", (235, 202.5, 140, 25))
        self.fives_button.set_action(self.enter_fives)
        self.sixes_label = widgets.Label("nur Sechser zählen", (100, 245), 26)
        self.arrow_sixes = widgets.ArrowRight((200, 245), 30)
        self.sixes_button = widgets.Button("", (235, 232.5, 140, 25))
        self.sixes_button.set_action(self.enter_sixes)
        self.upper_sum_wo_bonus_label = widgets.Label("gesamt", (100, 275), 26)
        self.upper_sum_wo_bonus_arrow = widgets.ArrowRight((200, 275), 30)
        self.upper_sum_wo_bonus_show = widgets.ShowLabel(str(self.game_manager.score_upper_part()), (305, 275, 140, 25))
        self.bonus_label = widgets.Label("Bonus bei 63", (100, 305), 26)
        self.bonus_arrow = widgets.ArrowRight((200, 305), 30)
        self.bonus_show = widgets.ShowLabel(str(self.game_manager.scoresheet.bonus), (305, 305, 140, 25))
        self.upper_sum_label = widgets.Label("gesamt oberer Teil", (100, 335), 26)
        self.upper_sum_arrow = widgets.ArrowRight((200, 335), 30)
        self.upper_sum_show = widgets.ShowLabel(str(self.game_manager.score_upper_part() + self.game_manager.scoresheet.bonus), (305, 335, 140, 25))

        self.upper_right_rect = pygame.Rect((400, 75, 400, 275))
        self.roll_dice_board = pygame.Rect((420, 95, 265, 175))
        self.safe_dice_board = pygame.Rect((705, 95, 75, 175))
        self.roll_one_lamp = widgets.Lamp((420, 290, 40, 40), border_radius=20, width=2)
        self.roll_two_lamp = widgets.Lamp((470, 290, 40, 40), border_radius=20, width=2)
        self.roll_three_lamp = widgets.Lamp((520, 290, 40, 40), border_radius=20, width=2)
        self.roll_dices_button = widgets.Button("Würfeln", (580, 290, 200, 40))
        self.roll_dices_button.set_action(self.roll_all_dice)

        self.std_skinset = skinsets.StandartSkinset()
        self.blue_skinset = skinsets.BlueSkinset()
        self.roman_skinset = skinsets.RomanSkinset()
        self.anti_skinset = skinsets.AntiSkinset()

        self.skinchanger = skinsets.SkinChanger()
        self.skinchanger.add_skinset("black", self.std_skinset)
        self.skinchanger.add_skinset("blue", self.blue_skinset)
        self.skinchanger.add_skinset("roman", self.roman_skinset)
        self.skinchanger.add_skinset("anti", self.anti_skinset)

        self.skinchanger.set_current_skinset(self.game_manager.settings.get_value("skinset"))

        self.dice_one = widgets.KlickableDice(0, (430, 145, 32, 32), (725, 99, 32, 32), self.skinchanger.get_current_skinset())
        self.dice_two = widgets.KlickableDice(0, (485, 220, 32, 32), (725, 133, 32, 32), self.skinchanger.get_current_skinset())
        self.dice_three = widgets.KlickableDice(0, (525, 180, 32, 32), (725, 167, 32, 32), self.skinchanger.get_current_skinset())
        self.dice_four = widgets.KlickableDice(0, (615, 230, 32, 32), (725, 201, 32, 32), self.skinchanger.get_current_skinset())
        self.dice_five = widgets.KlickableDice(0, (590, 130, 32, 32), (725, 235, 32, 32), self.skinchanger.get_current_skinset())

        self.skinchanger.add_dice(self.dice_one)
        self.skinchanger.add_dice(self.dice_two)
        self.skinchanger.add_dice(self.dice_three)
        self.skinchanger.add_dice(self.dice_four)
        self.skinchanger.add_dice(self.dice_five)

        self.rolls_lamp_line = widgets.LampLine()
        self.rolls_lamp_line.add_lamp(self.roll_one_lamp)
        self.rolls_lamp_line.add_lamp(self.roll_two_lamp)
        self.rolls_lamp_line.add_lamp(self.roll_three_lamp)

        self.lower_left_rect = pygame.Rect((0, 350, 400, 350))
        self.three_of_a_kind_label = widgets.Label("Dreierpasch", (100, 365), 26)
        self.three_of_a_kind_arrow = widgets.ArrowRight((200, 365), 30)
        self.three_of_a_kind_button = widgets.Button("", (235, 353.5, 140, 25))
        self.three_of_a_kind_button.set_action(self.enter_three_of_a_kind)
        self.four_of_a_kind_label = widgets.Label("Viererpasch", (100, 395), 26)
        self.four_of_a_kind_arrow = widgets.ArrowRight((200, 395), 30)
        self.four_of_a_kind_button = widgets.Button("", (235, 383.5, 140, 25))
        self.four_of_a_kind_button.set_action(self.enter_four_of_a_kind)
        self.full_house_label = widgets.Label("Full-House", (100, 425), 26)
        self.full_house_arrow = widgets.ArrowRight((200, 425), 30)
        self.full_house_button = widgets.Button("", (235, 412.5, 140, 25))
        self.full_house_button.set_action(self.enter_full_house)
        self.small_road_label = widgets.Label("Kleine Straße", (100, 455), 26 )
        self.small_road_arrow = widgets.ArrowRight((200, 455), 30)
        self.small_road_button = widgets.Button("", (235, 442.5, 140, 25))
        self.small_road_button.set_action(self.enter_small_road)
        self.big_road_label = widgets.Label("Große Straße", (100, 485), 26)
        self.big_road_arrow = widgets.ArrowRight((200, 485), 30)
        self.big_road_button = widgets.Button("", (235, 472.5, 140, 25))
        self.big_road_button.set_action(self.enter_big_road)
        self.kniffel_label = widgets.Label("Kniffel", (100, 515), 26)
        self.kniffel_arrow = widgets.ArrowRight((200, 515), 30)
        self.kniffel_button = widgets.Button("", (235, 502.5, 140, 25))
        self.kniffel_button.set_action(self.enter_kniffel)
        self.chance_label = widgets.Label("Chance", (100, 545), 26)
        self.chance_arrow = widgets.ArrowRight((200, 545), 30)
        self.chance_button = widgets.Button("",(235, 532.5, 140, 25))
        self.chance_button.set_action(self.enter_chance)
        self.lower_sum_label = widgets.Label("gesamt unterer Teil", (100, 575), 26)
        self.lower_sum_arrow = widgets.ArrowRight((200, 575), 30)
        self.lower_sum_show = widgets.ShowLabel(str(self.game_manager.score_lower_part()), (305, 575, 140, 25))
        self.upper_sum_low_label = widgets.Label("gesamt oberer Teil", (100, 605), 26)
        self.upper_sum_low_arrow = widgets.ArrowRight((200, 605), 30)
        self.upper_sum_low_show = widgets.ShowLabel(str(self.game_manager.score_upper_part() + self.game_manager.scoresheet.bonus), (305, 605, 140, 25))
        self.extra_kniffel_label = widgets.Label("Punkte Extra Kniffel", (100, 635), 26)
        self.extra_kniffel_arrow = widgets.ArrowRight((200, 635), 30)
        self.extra_kniffel_show = widgets.ShowLabel(str(self.game_manager.scoresheet.kniffel_bonus), (305, 635, 140, 25))
        self.end_sum_label = widgets.Label("Endsumme", (100, 665), 26)
        self.end_sum_arrow = widgets.ArrowRight((200, 665), 30)
        self.end_sum_show = widgets.ShowLabel("", (305, 665, 140, 25))

        self.lower_right_rect = pygame.Rect((400, 350, 400, 350))
        self.error_messages_rect = pygame.Rect((420, 370, 360, 310))
        self.three_of_a_kind_explanation_label = widgets.Label("Dreierpasch = 3 gleiche", (600, 390))
        self.four_of_a_kind_explanation_label = widgets.Label("Viererpasch = 4 gleiche", (600, 420))
        self.full_house_explanation_label = widgets.Label("Full House = z.B. 4 4 4 1 1", (600, 450))
        self.small_road_explanation_label = widgets.Label("Kleine Straße = z.B. 1 2 3 4", (600, 480))
        self.big_road_explanation_label = widgets.Label("Große Straße = z.B. 1 2 3 4 5", (600, 510))

        self.std_skinset.skinset_button = skinsets.SkinsetButton((430, 540, 32, 32), "dice_six.png")
        self.std_skinset.skinset_button.set_action(self.change_skinset_to_black)
        self.blue_skinset.skinset_button = skinsets.SkinsetButton((472, 540, 32, 32), "dice_six_blue.png")
        self.blue_skinset.skinset_button.set_action(self.change_skinset_to_blue)
        self.roman_skinset.skinset_button = skinsets.SkinsetButton((514, 540, 32, 32), "roman_VI.png")
        self.roman_skinset.skinset_button.set_action(self.change_skinset_to_roman)
        self.anti_skinset.skinset_button = skinsets.SkinsetButton((556, 540, 32, 32), "anti_six.png")
        self.anti_skinset.skinset_button.set_action(self.change_skinset_to_anti)

        self.start_new_game_button = widgets.Button("Start new Game", (200, 712.5, 195, 75))
        self.start_new_game_button.set_action(self.restart_game)
        self.home_button = widgets.Button("Home", (405, 712.5, 195, 75), font_size=40)
        self.home_button.set_action(self.quit_game)

    def change_skinset_to_black(self):
        self.skinchanger.set_current_skinset("black")
        self.game_manager.settings.set_value("skinset", "black")
        self.skinchanger.update_skinset()

    def change_skinset_to_blue(self):
        self.skinchanger.set_current_skinset("blue")
        self.game_manager.settings.set_value("skinset", "blue")
        self.skinchanger.update_skinset()

    def change_skinset_to_roman(self):
        self.skinchanger.set_current_skinset("roman")
        self.game_manager.settings.set_value("skinset", "roman")
        self.skinchanger.update_skinset()

    def change_skinset_to_anti(self):
        self.skinchanger.set_current_skinset("anti")
        self.game_manager.settings.set_value("skinset", "anti")
        self.skinchanger.update_skinset()
    
    def reset_dice(self):
        self.dice_one = widgets.KlickableDice(0, (430, 145, 32, 32), (725, 99, 32, 32), self.skinchanger.get_current_skinset())
        self.dice_two = widgets.KlickableDice(0, (485, 220, 32, 32), (725, 133, 32, 32), self.skinchanger.get_current_skinset())
        self.dice_three = widgets.KlickableDice(0, (525, 180, 32, 32), (725, 167, 32, 32), self.skinchanger.get_current_skinset())
        self.dice_four = widgets.KlickableDice(0, (615, 230, 32, 32), (725, 201, 32, 32), self.skinchanger.get_current_skinset())
        self.dice_five = widgets.KlickableDice(0, (590, 130, 32, 32), (725, 235, 32, 32), self.skinchanger.get_current_skinset())

        self.skinchanger.dice_list = []

        self.skinchanger.add_dice(self.dice_one)
        self.skinchanger.add_dice(self.dice_two)
        self.skinchanger.add_dice(self.dice_three)
        self.skinchanger.add_dice(self.dice_four)
        self.skinchanger.add_dice(self.dice_five)

    def enter_ones(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.scoresheet.ones = 5
            self.game_manager.score_bonus()
            self.game_manager.reset_rerolls()
        else:
            self.game_manager.ones()
        self.ones_button.text = str(self.game_manager.scoresheet.ones)
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.ones_button.set_action(None)
        self.game_manager.unlock_all_dice()
        self.ones_button.hover_color = (255, 255, 255)
        self.update_sums_upper()
        if self.game_manager.game_over_check():
            self.show_results()

    def enter_twos(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.scoresheet.twos = 10
            self.game_manager.score_bonus()
            self.game_manager.reset_rerolls()
        else:
            self.game_manager.twos()
        self.twos_button.text = str(self.game_manager.scoresheet.twos)
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.twos_button.set_action(None)
        self.game_manager.unlock_all_dice()
        self.twos_button.hover_color = (255, 255, 255)
        self.update_sums_upper()
        if self.game_manager.game_over_check():
            self.show_results()

    def enter_three(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.scoresheet.threes = 15
            self.game_manager.score_bonus()
            self.game_manager.reset_rerolls()
        else:
            self.game_manager.threes()
        self.three_button.text = str(self.game_manager.scoresheet.threes)
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.three_button.set_action(None)
        self.game_manager.unlock_all_dice()
        self.three_button.hover_color = (255, 255, 255)
        self.update_sums_upper()
        if self.game_manager.game_over_check():
            self.show_results()

    def enter_fours(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.scoresheet.fours = 20
            self.game_manager.score_bonus()
            self.game_manager.reset_rerolls()
        else:
            self.game_manager.fours()
        self.fours_button.text = str(self.game_manager.scoresheet.fours)
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.fours_button.set_action(None)
        self.game_manager.unlock_all_dice()
        self.fours_button.hover_color = (255, 255, 255)
        self.update_sums_upper()
        if self.game_manager.game_over_check():
            self.show_results()

    def enter_fives(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.scoresheet.fives = 25
            self.game_manager.score_bonus()
            self.game_manager.reset_rerolls()
        else:
            self.game_manager.fives()
        self.fives_button.text = str(self.game_manager.scoresheet.fives)
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.fives_button.set_action(None)
        self.game_manager.unlock_all_dice()
        self.fives_button.hover_color = (255, 255, 255)
        self.update_sums_upper()
        if self.game_manager.game_over_check():
            self.show_results()

    def enter_sixes(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.scoresheet.sixes = 30
            self.game_manager.score_bonus()
            self.game_manager.reset_rerolls()
        else:
            self.game_manager.sixes()
        self.sixes_button.text = str(self.game_manager.scoresheet.sixes)
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.sixes_button.set_action(None)
        self.game_manager.unlock_all_dice()
        self.sixes_button.hover_color = (255, 255, 255)
        self.update_sums_upper()
        if self.game_manager.game_over_check():
            self.show_results()

    def enter_three_of_a_kind(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.scoresheet.check_kniffel(self.game_manager.dice_list):
            pass
        self.game_manager.three_of_a_kind()
        self.three_of_a_kind_button.text = str(self.game_manager.scoresheet.three_of_a_kind)
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.three_of_a_kind_button.set_action(None)
        self.game_manager.unlock_all_dice()
        self.three_of_a_kind_button.hover_color = (255, 255, 255)
        self.update_sums_lower()
        if self.game_manager.game_over_check():
            self.show_results()

    def enter_four_of_a_kind(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.scoresheet.check_kniffel(self.game_manager.dice_list):
            pass
        self.game_manager.four_of_a_kind()
        self.four_of_a_kind_button.text = str(self.game_manager.scoresheet.four_of_a_kind)
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.four_of_a_kind_button.set_action(None)
        self.game_manager.unlock_all_dice()
        self.four_of_a_kind_button.hover_color = (255, 255, 255)
        self.update_sums_lower()
        if self.game_manager.game_over_check():
            self.show_results()

    def enter_full_house(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.scoresheet.full_house  = 25
            self.game_manager.reset_rerolls()
        else:
            self.game_manager.full_house()
        self.full_house_button.text = str(self.game_manager.scoresheet.full_house)
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.full_house_button.set_action(None)
        self.game_manager.unlock_all_dice()
        self.full_house_button.hover_color = (255, 255, 255)
        self.update_sums_lower()
        if self.game_manager.game_over_check():
            self.show_results()

    def enter_small_road(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.scoresheet.small_straight = 30
            self.game_manager.reset_rerolls()
        else:
            self.game_manager.small_straight()
        self.small_road_button.text = str(self.game_manager.scoresheet.small_straight)
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.small_road_button.set_action(None)
        self.game_manager.unlock_all_dice()
        self.small_road_button.hover_color = (255, 255, 255)
        self.update_sums_lower()
        if self.game_manager.game_over_check():
            self.show_results()

    def enter_big_road(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.scoresheet.large_straight = 40
            self.game_manager.reset_rerolls()
        else:
            self.game_manager.large_straight()
        self.big_road_button.text = str(self.game_manager.scoresheet.large_straight)
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.big_road_button.set_action(None)
        self.game_manager.unlock_all_dice()
        self.big_road_button.hover_color = (255, 255, 255)
        self.update_sums_lower()
        if self.game_manager.game_over_check():
            self.show_results()

    def enter_kniffel(self):
        if self.game_manager.get_rerolls() == 3:
            return
        self.game_manager.kniffel()
        self.kniffel_button.text = str(self.game_manager.scoresheet.kniffel)
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.kniffel_button.set_action(None)
        self.game_manager.unlock_all_dice()
        self.kniffel_button.hover_color = (255, 255, 255)
        self.update_sums_lower()
        if self.game_manager.game_over_check():
            self.show_results()

    def enter_chance(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.scoresheet.check_kniffel(self.game_manager.dice_list):
            pass
        self.game_manager.chance()
        self.chance_button.text = str(self.game_manager.scoresheet.chance)
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.chance_button.set_action(None)
        self.game_manager.unlock_all_dice()
        self.chance_button.hover_color = (255, 255, 255)
        self.update_sums_lower()
        if self.game_manager.game_over_check():
            self.show_results()

    def show_results(self):
        self.manager.change_screen(ResultScreenSinglerplayer(self.manager, self.game_manager))

    def roll_all_dice(self):
        self.game_manager.roll_all_dice()
        self.dice_one.set_eyes(self.game_manager.dice_list[0].get_eyes())
        self.dice_two.set_eyes(self.game_manager.dice_list[1].get_eyes())
        self.dice_three.set_eyes(self.game_manager.dice_list[2].get_eyes())
        self.dice_four.set_eyes(self.game_manager.dice_list[3].get_eyes())
        self.dice_five.set_eyes(self.game_manager.dice_list[4].get_eyes())
        self.rolls_lamp_line.turn_number_of_lamps_on(3 - self.game_manager.get_rerolls())
    
    def restart_game(self):
        self.game_manager = GameClass.Game()
        self.manager.change_screen(GameScreenSinglerplayer(self.manager, self.game_manager))

    def quit_game(self):
        self.manager.change_screen(StartScreen(self.manager, self.game_manager))

    def handle_events(self, event):
        self.start_new_game_button.handle_event(event)
        self.home_button.handle_event(event)
        self.dice_one.handle_event(event, self.game_manager, 0)
        self.dice_two.handle_event(event, self.game_manager, 1)
        self.dice_three.handle_event(event, self.game_manager, 2)
        self.dice_four.handle_event(event, self.game_manager, 3)
        self.dice_five.handle_event(event, self.game_manager, 4)
        self.roll_dices_button.handle_event(event)
        self.ones_button.handle_event(event)
        self.twos_button.handle_event(event)
        self.three_button.handle_event(event)
        self.fours_button.handle_event(event)
        self.fives_button.handle_event(event)
        self.sixes_button.handle_event(event)
        self.three_of_a_kind_button.handle_event(event)
        self.four_of_a_kind_button.handle_event(event)
        self.full_house_button.handle_event(event)
        self.small_road_button.handle_event(event)
        self.big_road_button.handle_event(event)
        self.chance_button.handle_event(event)
        self.kniffel_button.handle_event(event)
        self.std_skinset.skinset_button.handle_event(event)
        self.blue_skinset.skinset_button.handle_event(event)
        self.roman_skinset.skinset_button.handle_event(event)
        self.anti_skinset.skinset_button.handle_event(event)

    def update_sums_upper(self):
        self.upper_sum_wo_bonus_show.text = str(self.game_manager.score_upper_part())
        self.upper_sum_show.text = str(self.game_manager.score_upper_part() + self.game_manager.scoresheet.bonus)
        self.bonus_show.text = str(self.game_manager.scoresheet.bonus)
        self.upper_sum_low_show.text = str(self.game_manager.score_upper_part() + self.game_manager.scoresheet.bonus)
        self.extra_kniffel_show.text = str(self.game_manager.scoresheet.kniffel_bonus)

    def update_sums_lower(self):
        self.lower_sum_show.text = str(self.game_manager.score_lower_part())
        self.upper_sum_low_show.text = str(self.game_manager.score_upper_part() + self.game_manager.scoresheet.bonus)
        self.extra_kniffel_show.text = str(self.game_manager.scoresheet.kniffel_bonus)

    def draw(self, surface):
        surface.fill((255, 255, 255))

        pygame.draw.line(surface, (0, 0, 0), (0, 75), (800, 75), 2)
        self.title_lable.draw(surface)

        pygame.draw.rect(surface, (0, 0, 0), self.upper_left_rect, 1)
        self.ones_label.draw(surface)
        self.arrow_ones.draw(surface)
        self.ones_button.draw(surface)
        self.twos_label.draw(surface)
        self.arrow_twos.draw(surface)
        self.twos_button.draw(surface)
        self.threes_label.draw(surface)
        self.arrow_threes.draw(surface)
        self.three_button.draw(surface)
        self.fours_label.draw(surface)
        self.arrow_fours.draw(surface)
        self.fours_button.draw(surface)
        self.fives_label.draw(surface)
        self.arrow_fives.draw(surface)
        self.fives_button.draw(surface)
        self.sixes_label.draw(surface)
        self.arrow_sixes.draw(surface)
        self.sixes_button.draw(surface)
        self.upper_sum_wo_bonus_label.draw(surface)
        self.upper_sum_wo_bonus_arrow.draw(surface)
        self.upper_sum_wo_bonus_show.draw(surface)
        self.bonus_label.draw(surface)
        self.bonus_arrow.draw(surface)
        self.bonus_show.draw(surface)
        self.upper_sum_label.draw(surface)
        self.upper_sum_arrow.draw(surface)
        self.upper_sum_show.draw(surface)

        pygame.draw.rect(surface, (0, 0, 0), self.upper_right_rect, 1)
        pygame.draw.rect(surface, (0, 0, 0), self.roll_dice_board, 2, 20)
        pygame.draw.rect(surface, (0, 0, 0), self.safe_dice_board, 2, 20)
        self.roll_one_lamp.draw(surface)
        self.roll_two_lamp.draw(surface)
        self.roll_three_lamp.draw(surface)
        self.roll_dices_button.draw(surface)

        self.dice_one.draw(surface)
        self.dice_two.draw(surface)
        self.dice_three.draw(surface)
        self.dice_four.draw(surface)
        self.dice_five.draw(surface)

        pygame.draw.rect(surface, (0, 0, 0), self.lower_left_rect, 1)
        self.three_of_a_kind_label.draw(surface)
        self.three_of_a_kind_arrow.draw(surface)
        self.three_of_a_kind_button.draw(surface)
        self.four_of_a_kind_label.draw(surface)
        self.four_of_a_kind_arrow.draw(surface)
        self.four_of_a_kind_button.draw(surface)
        self.full_house_label.draw(surface)
        self.full_house_arrow.draw(surface)
        self.full_house_button.draw(surface)
        self.small_road_label.draw(surface)
        self.small_road_arrow.draw(surface)
        self.small_road_button.draw(surface)
        self.big_road_label.draw(surface)
        self.big_road_arrow.draw(surface)
        self.big_road_button.draw(surface)
        self.kniffel_label.draw(surface)
        self.kniffel_arrow.draw(surface)
        self.kniffel_button.draw(surface)
        self.chance_label.draw(surface)
        self.chance_arrow.draw(surface)
        self.chance_button.draw(surface)
        self.lower_sum_label.draw(surface)
        self.lower_sum_arrow.draw(surface)
        self.lower_sum_show.draw(surface)
        self.upper_sum_low_label.draw(surface)
        self.upper_sum_low_arrow.draw(surface)
        self.upper_sum_low_show.draw(surface)
        self.extra_kniffel_label.draw(surface)
        self.extra_kniffel_arrow.draw(surface)
        self.extra_kniffel_show.draw(surface)
        self.end_sum_label.draw(surface)
        self.end_sum_arrow.draw(surface)
        self.end_sum_show.draw(surface)

        pygame.draw.rect(surface, (0, 0, 0), self.lower_right_rect, 1)
        pygame.draw.rect(surface, (0, 0, 0), self.error_messages_rect, 2, 20)
        self.three_of_a_kind_explanation_label.draw(surface)
        self.four_of_a_kind_explanation_label.draw(surface)
        self.full_house_explanation_label.draw(surface)
        self.small_road_explanation_label.draw(surface)
        self.big_road_explanation_label.draw(surface)
        pygame.draw.line(surface, (0, 0, 0), (420, 530), (779, 530), 2)
        self.std_skinset.skinset_button.draw(surface)
        self.blue_skinset.skinset_button.draw(surface)
        self.roman_skinset.skinset_button.draw(surface)
        self.anti_skinset.skinset_button.draw(surface)

        pygame.draw.line(surface, (0, 0, 0), (0, 700), (800, 700), 2)
        self.start_new_game_button.draw(surface)
        self.home_button.draw(surface)

class ResultScreenSinglerplayer(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

        self.title_label = widgets.Label("Kniffel", (400, 37.5), 80)
        self.highscore_show = widgets.ShowLabel("Highscore", (400, 125, 670, 75), 60)
        self.highscore_value_show = widgets.ShowLabel(str(self.game_manager.load_highscore()[0]["Score"]), (400, 215, 670, 90), 60)
        self.points_show = widgets.ShowLabel(str(self.game_manager.get_tally_total()), (400, 420, 700, 300), 200)
        self.name_input = widgets.TextField((175, 580, 450, 100))
        self.start_new_game_button = widgets.Button("Start New Game", (100, 700, 200, 50))
        self.start_new_game_button.set_action(self.start_new_game)
        self.home_button = widgets.Button("Home", (500, 700, 200, 50))
        self.home_button.set_action(self.go_home)

    def start_new_game(self):
        self.save_highscore()
        self.game_manager = GameClass.Game()
        self.manager.change_screen(GameScreenSinglerplayer(self.manager, self.game_manager))

    def go_home(self):
        self.save_highscore()
        self.manager.change_screen(StartScreen(self.manager, self.game_manager))

    def save_highscore(self):
        if self.name_input.text.strip() != "":
            self.game_manager.save_highscore(self.name_input.text)

    def handle_events(self, event):
        self.start_new_game_button.handle_event(event)
        self.home_button.handle_event(event)
        self.name_input.handle_event(event)

    def draw(self, surface):
        surface.fill((255, 255, 255))

        pygame.draw.line(surface, (0, 0, 0), (0, 75), (800, 75), 2)
        self.title_label.draw(surface)
        self.highscore_show.draw(surface)
        self.highscore_value_show.draw(surface)
        self.points_show.draw(surface)
        self.name_input.draw(surface)
        self.start_new_game_button.draw(surface)
        self.home_button.draw(surface)

class GameScreenMultiplayer(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

        self.title_lable = widgets.Label("Kniffel Gewinnkarte", (400, 37.5), 40)
        self.upper_left_rect = pygame.Rect((0, 60, 400, 290))

        self.p1_label = widgets.Label("P1", (270, 72))
        self.p2_label = widgets.Label("P2", (340, 72))

        self.ones_label = widgets.Label("nur Einser zählen", (100, 95), 26)
        self.arrow_ones = widgets.ArrowRight((200, 95), 30)
        self.p1_ones_button = widgets.Button("", (235, 82.5, 67.5, 25))
        self.p1_ones_button.set_action(self.enter_ones)
        self.p2_ones_button = widgets.Button("", (307.5, 82.5, 67.5, 25))
        self.p2_ones_button.set_action(self.enter_ones)

        self.twos_label = widgets.Label("nur Zweier zählen", (100, 125), 26)
        self.arrow_twos = widgets.ArrowRight((200, 125), 30)
        self.p1_twos_button = widgets.Button("", (235, 112.5, 67.5, 25))
        self.p1_twos_button.set_action(self.enter_twos)
        self.p2_twos_button = widgets.Button("", (307.5, 112.5, 67.5, 25))
        self.p2_twos_button.set_action(self.enter_twos)

        self.threes_label = widgets.Label("nur Dreier zählen", (100, 155), 26)
        self.arrow_threes = widgets.ArrowRight((200, 155), 30)
        self.p1_three_button = widgets.Button("", (235, 142.5, 67.5, 25))
        self.p1_three_button.set_action(self.enter_three)
        self.p2_three_button = widgets.Button("", (307.5, 142.5, 67.5, 25))
        self.p2_three_button.set_action(self.enter_three)

        self.fours_label = widgets.Label("nur Vierer zählen", (100, 185), 26)
        self.arrow_fours = widgets.ArrowRight((200, 185), 30)
        self.p1_fours_button = widgets.Button("", (235, 172.5, 67.5, 25))
        self.p1_fours_button.set_action(self.enter_fours)
        self.p2_fours_button = widgets.Button("", (307.5, 172.5, 67.5, 25))
        self.p2_fours_button.set_action(self.enter_fours)

        self.fives_label = widgets.Label("nur Fünfer zählen", (100, 215), 26)
        self.arrow_fives = widgets.ArrowRight((200, 215), 30)
        self.p1_fives_button = widgets.Button("", (235, 202.5, 67.5, 25))
        self.p1_fives_button.set_action(self.enter_fives)
        self.p2_fives_button = widgets.Button("", (307.5, 202.5, 67.5, 25))
        self.p2_fives_button.set_action(self.enter_fives)

        self.sixes_label = widgets.Label("nur Sechser zählen", (100, 245), 26)
        self.arrow_sixes = widgets.ArrowRight((200, 245), 30)
        self.p1_sixes_button = widgets.Button("", (235, 232.5, 67.5, 25))
        self.p1_sixes_button.set_action(self.enter_sixes)
        self.p2_sixes_button = widgets.Button("", (307.5, 232.5, 67.5, 25))
        self.p2_sixes_button.set_action(self.enter_sixes)

        self.upper_sum_wo_bonus_label = widgets.Label("gesamt", (100, 275), 26)
        self.upper_sum_wo_bonus_arrow = widgets.ArrowRight((200, 275), 30)
        self.p1_upper_sum_wo_bonus_show = widgets.ShowLabel(str(0), (268.75, 275, 67.5, 25))
        self.p2_upper_sum_wo_bonus_show = widgets.ShowLabel(str(0), (341.25, 275, 67.5, 25))

        self.bonus_label = widgets.Label("Bonus bei 63", (100, 305), 26)
        self.bonus_arrow = widgets.ArrowRight((200, 305), 30)
        self.p1_bonus_show = widgets.ShowLabel(str(0), (268.75, 305, 67.5, 25))
        self.p2_bonus_show = widgets.ShowLabel(str(0), (341.25, 305, 67.5, 25))

        self.upper_sum_label = widgets.Label("gesamt oberer Teil", (100, 335), 26)
        self.upper_sum_arrow = widgets.ArrowRight((200, 335), 30)
        self.p1_upper_sum_show = widgets.ShowLabel(str(0), (268.75, 335, 67.5, 25))
        self.p2_upper_sum_show = widgets.ShowLabel(str(0), (341.25, 335, 67.5, 25))

        self.upper_right_rect = pygame.Rect((400, 60, 400, 290))
        self.roll_dice_board = pygame.Rect((420, 95, 265, 175))
        self.safe_dice_board = pygame.Rect((705, 95, 75, 175))
        self.roll_one_lamp = widgets.Lamp((420, 290, 40, 40), border_radius=20, width=2)
        self.roll_two_lamp = widgets.Lamp((470, 290, 40, 40), border_radius=20, width=2)
        self.roll_three_lamp = widgets.Lamp((520, 290, 40, 40), border_radius=20, width=2)
        self.roll_dices_button = widgets.Button("Würfeln", (580, 290, 200, 40))
        self.roll_dices_button.set_action(self.roll_all_dice)

        self.std_skinset = skinsets.StandartSkinset()
        self.blue_skinset = skinsets.BlueSkinset()
        self.roman_skinset = skinsets.RomanSkinset()
        self.anti_skinset = skinsets.AntiSkinset()

        self.skinchanger = skinsets.SkinChanger()
        self.skinchanger.add_skinset("black", self.std_skinset)
        self.skinchanger.add_skinset("blue", self.blue_skinset)
        self.skinchanger.add_skinset("roman", self.roman_skinset)
        self.skinchanger.add_skinset("anti", self.anti_skinset)

        self.skinchanger.set_current_skinset(self.game_manager.settings.get_value("skinset"))

        self.dice_one = widgets.KlickableDice(0, (430, 145, 32, 32), (725, 99, 32, 32), self.skinchanger.get_current_skinset())
        self.dice_two = widgets.KlickableDice(0, (485, 220, 32, 32), (725, 133, 32, 32), self.skinchanger.get_current_skinset())
        self.dice_three = widgets.KlickableDice(0, (525, 180, 32, 32), (725, 167, 32, 32), self.skinchanger.get_current_skinset())
        self.dice_four = widgets.KlickableDice(0, (615, 230, 32, 32), (725, 201, 32, 32), self.skinchanger.get_current_skinset())
        self.dice_five = widgets.KlickableDice(0, (590, 130, 32, 32), (725, 235, 32, 32), self.skinchanger.get_current_skinset())

        self.skinchanger.add_dice(self.dice_one)
        self.skinchanger.add_dice(self.dice_two)
        self.skinchanger.add_dice(self.dice_three)
        self.skinchanger.add_dice(self.dice_four)
        self.skinchanger.add_dice(self.dice_five)

        self.rolls_lamp_line = widgets.LampLine()
        self.rolls_lamp_line.add_lamp(self.roll_one_lamp)
        self.rolls_lamp_line.add_lamp(self.roll_two_lamp)
        self.rolls_lamp_line.add_lamp(self.roll_three_lamp)

        self.lower_left_rect = pygame.Rect((0, 350, 400, 350))
        self.three_of_a_kind_label = widgets.Label("Dreierpasch", (100, 365), 26)
        self.three_of_a_kind_arrow = widgets.ArrowRight((200, 365), 30)
        self.p1_three_of_a_kind_button = widgets.Button("", (235, 353.5, 67.5, 25))
        self.p1_three_of_a_kind_button.set_action(self.enter_three_of_a_kind)
        self.p2_three_of_a_kind_button = widgets.Button("", (307.5, 353.5, 67.5, 25))
        self.p2_three_of_a_kind_button.set_action(self.enter_three_of_a_kind)

        self.four_of_a_kind_label = widgets.Label("Viererpasch", (100, 395), 26)
        self.four_of_a_kind_arrow = widgets.ArrowRight((200, 395), 30)
        self.p1_four_of_a_kind_button = widgets.Button("", (235, 383.5, 67.5, 25))
        self.p1_four_of_a_kind_button.set_action(self.enter_four_of_a_kind)
        self.p2_four_of_a_kind_button = widgets.Button("", (307.5, 383.5, 67.5, 25))
        self.p2_four_of_a_kind_button.set_action(self.enter_four_of_a_kind)

        self.full_house_label = widgets.Label("Full-House", (100, 425), 26)
        self.full_house_arrow = widgets.ArrowRight((200, 425), 30)
        self.p1_full_house_button = widgets.Button("", (235, 412.5, 67.5, 25))
        self.p1_full_house_button.set_action(self.enter_full_house)
        self.p2_full_house_button = widgets.Button("", (307.5, 412.5, 67.5, 25))
        self.p2_full_house_button.set_action(self.enter_full_house)

        self.small_road_label = widgets.Label("Kleine Straße", (100, 455), 26 )
        self.small_road_arrow = widgets.ArrowRight((200, 455), 30)
        self.p1_small_road_button = widgets.Button("", (235, 442.5, 67.5, 25))
        self.p1_small_road_button.set_action(self.enter_small_road)
        self.p2_small_road_button = widgets.Button("", (307.5, 442.5, 67.5, 25))
        self.p2_small_road_button.set_action(self.enter_small_road)

        self.big_road_label = widgets.Label("Große Straße", (100, 485), 26)
        self.big_road_arrow = widgets.ArrowRight((200, 485), 30)
        self.p1_big_road_button = widgets.Button("", (235, 472.5, 67.5, 25))
        self.p1_big_road_button.set_action(self.enter_big_road)
        self.p2_big_road_button = widgets.Button("", (307.5, 472.5, 67.5, 25))
        self.p2_big_road_button.set_action(self.enter_big_road)

        self.kniffel_label = widgets.Label("Kniffel", (100, 515), 26)
        self.kniffel_arrow = widgets.ArrowRight((200, 515), 30)
        self.p1_kniffel_button = widgets.Button("", (235, 502.5, 67.5, 25))
        self.p1_kniffel_button.set_action(self.enter_kniffel)
        self.p2_kniffel_button = widgets.Button("", (307.5, 502.5, 67.5, 25))
        self.p2_kniffel_button.set_action(self.enter_kniffel)

        self.chance_label = widgets.Label("Chance", (100, 545), 26)
        self.chance_arrow = widgets.ArrowRight((200, 545), 30)
        self.p1_chance_button = widgets.Button("",(235, 532.5, 67.5, 25))
        self.p1_chance_button.set_action(self.enter_chance)
        self.p2_chance_button = widgets.Button("",(307.5, 532.5, 67.5, 25))
        self.p2_chance_button.set_action(self.enter_chance)

        self.lower_sum_label = widgets.Label("gesamt unterer Teil", (100, 575), 26)
        self.lower_sum_arrow = widgets.ArrowRight((200, 575), 30)
        self.p1_lower_sum_show = widgets.ShowLabel(str(self.game_manager.score_lower_part()), (268.75, 575, 67.5, 25))
        self.p2_lower_sum_show = widgets.ShowLabel(str(self.game_manager.score_lower_part()), (341.25, 575, 67.5, 25))

        self.upper_sum_low_label = widgets.Label("gesamt oberer Teil", (100, 605), 26)
        self.upper_sum_low_arrow = widgets.ArrowRight((200, 605), 30)
        self.p1_upper_sum_low_show = widgets.ShowLabel(str(self.game_manager.score_upper_part() + self.game_manager.active_scoresheet.bonus), (268.75, 605, 67.5, 25))
        self.p2_upper_sum_low_show = widgets.ShowLabel(str(self.game_manager.score_upper_part() + self.game_manager.active_scoresheet.bonus), (341.25, 605, 67.5, 25))

        self.extra_kniffel_label = widgets.Label("Punkte Extra Kniffel", (100, 635), 26)
        self.extra_kniffel_arrow = widgets.ArrowRight((200, 635), 30)
        self.p1_extra_kniffel_show = widgets.ShowLabel(str(self.game_manager.active_scoresheet.kniffel_bonus), (268.75, 635, 67.5, 25))
        self.p2_extra_kniffel_show = widgets.ShowLabel(str(self.game_manager.active_scoresheet.kniffel_bonus), (341.25, 635, 67.5, 25))

        self.end_sum_label = widgets.Label("Endsumme", (100, 665), 26)
        self.end_sum_arrow = widgets.ArrowRight((200, 665), 30)
        self.p1_end_sum_show = widgets.ShowLabel("", (268.75, 665, 67.5, 25))
        self.p2_end_sum_show = widgets.ShowLabel("", (341.25, 665, 67.5, 25))

        self.lower_right_rect = pygame.Rect((400, 350, 400, 350))
        self.error_messages_rect = pygame.Rect((420, 370, 360, 310))
        self.three_of_a_kind_explanation_label = widgets.Label("Dreierpasch = 3 gleiche", (600, 390))
        self.four_of_a_kind_explanation_label = widgets.Label("Viererpasch = 4 gleiche", (600, 420))
        self.full_house_explanation_label = widgets.Label("Full House = z.B. 4 4 4 1 1", (600, 450))
        self.small_road_explanation_label = widgets.Label("Kleine Straße = z.B. 1 2 3 4", (600, 480))
        self.big_road_explanation_label = widgets.Label("Große Straße = z.B. 1 2 3 4 5", (600, 510))

        self.std_skinset.skinset_button = skinsets.SkinsetButton((430, 540, 32, 32), "dice_six.png")
        self.std_skinset.skinset_button.set_action(self.change_skinset_to_black)
        self.blue_skinset.skinset_button = skinsets.SkinsetButton((472, 540, 32, 32), "dice_six_blue.png")
        self.blue_skinset.skinset_button.set_action(self.change_skinset_to_blue)
        self.roman_skinset.skinset_button = skinsets.SkinsetButton((514, 540, 32, 32), "roman_VI.png")
        self.roman_skinset.skinset_button.set_action(self.change_skinset_to_roman)
        self.anti_skinset.skinset_button = skinsets.SkinsetButton((556, 540, 32, 32), "anti_six.png")
        self.anti_skinset.skinset_button.set_action(self.change_skinset_to_anti)

        self.start_new_game_button = widgets.Button("Start new Game", (200, 712.5, 195, 75))
        self.start_new_game_button.set_action(self.restart_game)
        self.home_button = widgets.Button("Home", (405, 712.5, 195, 75), font_size=40)
        self.home_button.set_action(self.quit_game)

        p1_object_list = [self.p1_ones_button, self.p1_twos_button, self.p1_three_button, self.p1_fours_button, self.p1_fives_button, self.p1_sixes_button,
                          self.p1_upper_sum_wo_bonus_show, self.p1_bonus_show, self.p1_upper_sum_show,
                          self.p1_three_of_a_kind_button, self.p1_four_of_a_kind_button, self.p1_small_road_button, self.p1_big_road_button,
                          self.p1_full_house_button, self.p1_kniffel_button, self.p1_chance_button,
                          self.p1_upper_sum_low_show, self.p1_lower_sum_show, self.p1_extra_kniffel_show, self.p1_end_sum_show]

        p2_object_list = [self.p2_ones_button, self.p2_twos_button, self.p2_three_button, self.p2_fours_button, self.p2_fives_button, self.p2_sixes_button,
                          self.p2_upper_sum_wo_bonus_show, self.p2_bonus_show, self.p2_upper_sum_show,
                          self.p2_three_of_a_kind_button, self.p2_four_of_a_kind_button, self.p2_small_road_button, self.p2_big_road_button,
                          self.p2_full_house_button, self.p2_kniffel_button, self.p2_chance_button,
                          self.p2_upper_sum_low_show, self.p2_lower_sum_show, self.p2_extra_kniffel_show, self.p2_end_sum_show]

        self.column_controller = widgets.MultiplayerColumnControl(p1_object_list, p2_object_list)

    def change_skinset_to_black(self):
        self.skinchanger.set_current_skinset("black")
        self.game_manager.settings.set_value("skinset", "black")
        self.skinchanger.update_skinset()

    def change_skinset_to_blue(self):
        self.skinchanger.set_current_skinset("blue")
        self.game_manager.settings.set_value("skinset", "blue")
        self.skinchanger.update_skinset()

    def change_skinset_to_roman(self):
        self.skinchanger.set_current_skinset("roman")
        self.game_manager.settings.set_value("skinset", "roman")
        self.skinchanger.update_skinset()

    def change_skinset_to_anti(self):
        self.skinchanger.set_current_skinset("anti")
        self.game_manager.settings.set_value("skinset", "anti")
        self.skinchanger.update_skinset()

    def roll_all_dice(self):
        self.game_manager.roll_all_dice()
        self.dice_one.set_eyes(self.game_manager.dice_list[0].get_eyes())
        self.dice_two.set_eyes(self.game_manager.dice_list[1].get_eyes())
        self.dice_three.set_eyes(self.game_manager.dice_list[2].get_eyes())
        self.dice_four.set_eyes(self.game_manager.dice_list[3].get_eyes())
        self.dice_five.set_eyes(self.game_manager.dice_list[4].get_eyes())
        self.rolls_lamp_line.turn_number_of_lamps_on(3 - self.game_manager.get_rerolls())

    def reset_dice(self):
        self.dice_one = widgets.KlickableDice(0, (430, 145, 32, 32), (725, 99, 32, 32), self.skinchanger.get_current_skinset())
        self.dice_two = widgets.KlickableDice(0, (485, 220, 32, 32), (725, 133, 32, 32), self.skinchanger.get_current_skinset())
        self.dice_three = widgets.KlickableDice(0, (525, 180, 32, 32), (725, 167, 32, 32), self.skinchanger.get_current_skinset())
        self.dice_four = widgets.KlickableDice(0, (615, 230, 32, 32), (725, 201, 32, 32), self.skinchanger.get_current_skinset())
        self.dice_five = widgets.KlickableDice(0, (590, 130, 32, 32), (725, 235, 32, 32), self.skinchanger.get_current_skinset())

        self.skinchanger.dice_list = []

        self.skinchanger.add_dice(self.dice_one)
        self.skinchanger.add_dice(self.dice_two)
        self.skinchanger.add_dice(self.dice_three)
        self.skinchanger.add_dice(self.dice_four)
        self.skinchanger.add_dice(self.dice_five)

    def enter_ones(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.active_scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.active_scoresheet.ones = 5
            self.game_manager.score_bonus()
            self.game_manager.reset_rerolls()
        else:
            self.game_manager.ones()
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.game_manager.unlock_all_dice()

        if self.game_manager.p1_turn:
            ones_button = self.p1_ones_button
        else:
            ones_button = self.p2_ones_button

        ones_button.text = str(self.game_manager.active_scoresheet.ones)
        ones_button.set_action(None)
        ones_button.hover_color = (255, 255, 255)

        self.update_sums_upper()
        self.switch_turn()

        if self.game_manager.game_over_check():
            self.show_results()

    def enter_twos(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.active_scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.active_scoresheet.twos = 10
            self.game_manager.score_bonus()
            self.game_manager.reset_rerolls()
        else:
            self.game_manager.twos()
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.game_manager.unlock_all_dice()

        if self.game_manager.p1_turn:
            twos_button = self.p1_twos_button
        else:
            twos_button = self.p2_twos_button

        twos_button.text = str(self.game_manager.active_scoresheet.twos)
        twos_button.set_action(None)
        twos_button.hover_color = (255, 255, 255)

        self.update_sums_upper()
        self.switch_turn()

        if self.game_manager.game_over_check():
            self.show_results()

    def enter_three(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.active_scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.active_scoresheet.threes = 15
            self.game_manager.score_bonus()
            self.game_manager.reset_rerolls()
        else:
            self.game_manager.threes()
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.game_manager.unlock_all_dice()

        if self.game_manager.p1_turn:
            three_button = self.p1_three_button
        else:
            three_button = self.p2_three_button

        three_button.text = str(self.game_manager.active_scoresheet.threes)
        three_button.set_action(None)
        three_button.hover_color = (255, 255, 255)

        self.update_sums_upper()
        self.switch_turn()

        if self.game_manager.game_over_check():
            self.show_results()

    def enter_fours(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.active_scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.active_scoresheet.fours = 20
            self.game_manager.score_bonus()
            self.game_manager.reset_rerolls()
        else:
            self.game_manager.fours()
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.game_manager.unlock_all_dice()

        if self.game_manager.p1_turn:
            fours_button = self.p1_fours_button
        else:
            fours_button = self.p2_fours_button

        fours_button.text = str(self.game_manager.active_scoresheet.fours)
        fours_button.set_action(None)
        fours_button.hover_color = (255, 255, 255)

        self.update_sums_upper()
        self.switch_turn()

        if self.game_manager.game_over_check():
            self.show_results()

    def enter_fives(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.active_scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.active_scoresheet.fives = 25
            self.game_manager.score_bonus()
            self.game_manager.reset_rerolls()
        else:
            self.game_manager.fives()
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.game_manager.unlock_all_dice()

        if self.game_manager.p1_turn:
            fives_button = self.p1_fives_button
        else:
            fives_button = self.p2_fives_button

        fives_button.text = str(self.game_manager.active_scoresheet.fives)
        fives_button.set_action(None)
        fives_button.hover_color = (255, 255, 255)

        self.update_sums_upper()
        self.switch_turn()

        if self.game_manager.game_over_check():
            self.show_results()

    def enter_sixes(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.active_scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.active_scoresheet.sixes = 30
            self.game_manager.score_bonus()
            self.game_manager.reset_rerolls()
        else:
            self.game_manager.sixes()
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.game_manager.unlock_all_dice()

        if self.game_manager.p1_turn:
            sixes_button = self.p1_sixes_button
        else:
            sixes_button = self.p2_sixes_button

        sixes_button.text = str(self.game_manager.active_scoresheet.sixes)
        sixes_button.set_action(None)
        sixes_button.hover_color = (255, 255, 255)

        self.update_sums_upper()
        self.switch_turn()

        if self.game_manager.game_over_check():
            self.show_results()
    
    def enter_three_of_a_kind(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.active_scoresheet.check_kniffel(self.game_manager.dice_list):
            pass
        self.game_manager.three_of_a_kind()
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.game_manager.unlock_all_dice()

        if self.game_manager.p1_turn:
            three_of_a_kind_button = self.p1_three_of_a_kind_button
        else:
            three_of_a_kind_button = self.p2_three_of_a_kind_button

        three_of_a_kind_button.text = str(self.game_manager.active_scoresheet.three_of_a_kind)
        three_of_a_kind_button.set_action(None)
        three_of_a_kind_button.hover_color = (255, 255, 255)

        self.update_sums_lower()
        self.switch_turn()

        if self.game_manager.game_over_check():
            self.show_results()

    def enter_four_of_a_kind(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.active_scoresheet.check_kniffel(self.game_manager.dice_list):
            pass
        self.game_manager.four_of_a_kind()
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.game_manager.unlock_all_dice()

        if self.game_manager.p1_turn:
            four_of_a_kind_button = self.p1_four_of_a_kind_button
        else:
            four_of_a_kind_button = self.p2_four_of_a_kind_button

        four_of_a_kind_button.text = str(self.game_manager.active_scoresheet.four_of_a_kind)
        four_of_a_kind_button.set_action(None)
        four_of_a_kind_button.hover_color = (255, 255, 255)

        self.update_sums_lower()
        self.switch_turn()

        if self.game_manager.game_over_check():
            self.show_results()
    
    def enter_full_house(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.active_scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.active_scoresheet.full_house = 25
            self.game_manager.reset_rerolls()
        else:
            self.game_manager.full_house()
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.game_manager.unlock_all_dice()

        if self.game_manager.p1_turn:
            full_house_button = self.p1_full_house_button
        else:
            full_house_button = self.p2_full_house_button

        full_house_button.text = str(self.game_manager.active_scoresheet.full_house)
        full_house_button.set_action(None)
        full_house_button.hover_color = (255, 255, 255)

        self.update_sums_lower()
        self.switch_turn()

        if self.game_manager.game_over_check():
            self.show_results()
    
    def enter_small_road(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.active_scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.active_scoresheet.small_straight = 30
            self.game_manager.reset_rerolls()
        else:
            self.game_manager.small_straight()
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.game_manager.unlock_all_dice()

        if self.game_manager.p1_turn:
            small_road_button = self.p1_small_road_button
        else:
            small_road_button = self.p2_small_road_button

        small_road_button.text = str(self.game_manager.active_scoresheet.small_straight)
        small_road_button.set_action(None)
        small_road_button.hover_color = (255, 255, 255)

        self.update_sums_lower()
        self.switch_turn()

        if self.game_manager.game_over_check():
            self.show_results()

    def enter_big_road(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.active_scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.active_scoresheet.large_straight = 40
            self.game_manager.reset_rerolls()
        else:
            self.game_manager.large_straight()
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.game_manager.unlock_all_dice()

        if self.game_manager.p1_turn:
            big_road_button = self.p1_big_road_button
        else:
            big_road_button = self.p2_big_road_button

        big_road_button.text = str(self.game_manager.active_scoresheet.large_straight)
        big_road_button.set_action(None)
        big_road_button.hover_color = (255, 255, 255)

        self.update_sums_lower()
        self.switch_turn()

        if self.game_manager.game_over_check():
            self.show_results()

    def enter_kniffel(self):
        if self.game_manager.get_rerolls() == 3:
            return
        self.game_manager.kniffel()
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.game_manager.unlock_all_dice()

        if self.game_manager.p1_turn:
            kniffel_button = self.p1_kniffel_button
        else:
            kniffel_button = self.p2_kniffel_button

        kniffel_button.text = str(self.game_manager.active_scoresheet.kniffel)
        kniffel_button.set_action(None)
        kniffel_button.hover_color = (255, 255, 255)

        self.update_sums_lower()
        self.switch_turn()

        if self.game_manager.game_over_check():
            self.show_results()

    def enter_chance(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.active_scoresheet.check_kniffel(self.game_manager.dice_list):
            pass
        self.game_manager.chance()
        self.rolls_lamp_line.turn_all_off()
        self.reset_dice()
        self.game_manager.unlock_all_dice()

        if self.game_manager.p1_turn:
            chance_button = self.p1_chance_button
        else:
            chance_button = self.p2_chance_button

        chance_button.text = str(self.game_manager.active_scoresheet.chance)
        chance_button.set_action(None)
        chance_button.hover_color = (255, 255, 255)

        self.update_sums_lower()
        self.switch_turn()

        if self.game_manager.game_over_check():
            self.show_results()

    def update_sums_upper(self):
        if self.game_manager.p1_turn:
            upper_sum_wo_bonus_show = self.p1_upper_sum_wo_bonus_show
            upper_sum_show = self.p1_upper_sum_show
            bonus_show = self.p1_bonus_show
            upper_sum_low_show = self.p1_upper_sum_low_show
            extra_kniffel_show = self.p1_extra_kniffel_show
        else:
            upper_sum_wo_bonus_show = self.p2_upper_sum_wo_bonus_show
            upper_sum_show = self.p2_upper_sum_show
            bonus_show = self.p2_bonus_show
            upper_sum_low_show = self.p2_upper_sum_low_show
            extra_kniffel_show = self.p2_extra_kniffel_show

        upper_sum_wo_bonus_show.text = str(self.game_manager.score_upper_part())
        upper_sum_show.text = str(self.game_manager.score_upper_part() + self.game_manager.active_scoresheet.bonus)
        bonus_show.text = str(self.game_manager.active_scoresheet.bonus)
        upper_sum_low_show.text = str(self.game_manager.score_upper_part() + self.game_manager.active_scoresheet.bonus)
        extra_kniffel_show.text = str(self.game_manager.active_scoresheet.kniffel_bonus)

    def update_sums_lower(self):
        if self.game_manager.p1_turn:
            lower_sum_show = self.p1_lower_sum_show
            upper_sum_low_show = self.p1_upper_sum_low_show
            extra_kniffel_show = self.p1_extra_kniffel_show
        else:
            lower_sum_show = self.p2_lower_sum_show
            upper_sum_low_show = self.p2_upper_sum_low_show
            extra_kniffel_show = self.p2_extra_kniffel_show

        lower_sum_show.text = str(self.game_manager.score_lower_part())
        upper_sum_low_show.text = str(self.game_manager.score_upper_part() + self.game_manager.active_scoresheet.bonus)
        extra_kniffel_show.text = str(self.game_manager.active_scoresheet.kniffel_bonus)

    def switch_turn(self):
        self.game_manager.switch_turn()
        self.column_controller.switch_column()
        self.game_manager.switch_active_scoresheet()

    def restart_game(self):
        self.game_manager = GameClass.GameMultiplayer()
        self.manager.change_screen(GameScreenMultiplayer(self.manager, self.game_manager))

    def quit_game(self):
        self.game_manager = GameClass.Game()
        self.manager.change_screen(StartScreen(self.manager, self.game_manager))

    def show_results(self):
        self.manager.change_screen(ResultScreenMultiplayer(self.manager, self.game_manager))

    def handle_events(self, event):
        self.start_new_game_button.handle_event(event)
        self.home_button.handle_event(event)
        self.dice_one.handle_event(event, self.game_manager, 0)
        self.dice_two.handle_event(event, self.game_manager, 1)
        self.dice_three.handle_event(event, self.game_manager, 2)
        self.dice_four.handle_event(event, self.game_manager, 3)
        self.dice_five.handle_event(event, self.game_manager, 4)
        self.roll_dices_button.handle_event(event)
        self.p1_ones_button.handle_event(event)
        self.p2_ones_button.handle_event(event)
        self.p1_twos_button.handle_event(event)
        self.p2_twos_button.handle_event(event)
        self.p1_three_button.handle_event(event)
        self.p2_three_button.handle_event(event)
        self.p1_fours_button.handle_event(event)
        self.p2_fours_button.handle_event(event)
        self.p1_fives_button.handle_event(event)
        self.p2_fives_button.handle_event(event)
        self.p1_sixes_button.handle_event(event)
        self.p2_sixes_button.handle_event(event)
        self.p1_three_of_a_kind_button.handle_event(event)
        self.p2_three_of_a_kind_button.handle_event(event)
        self.p1_four_of_a_kind_button.handle_event(event)
        self.p2_four_of_a_kind_button.handle_event(event)
        self.p1_full_house_button.handle_event(event)
        self.p2_full_house_button.handle_event(event)
        self.p1_small_road_button.handle_event(event)
        self.p2_small_road_button.handle_event(event)
        self.p1_big_road_button.handle_event(event)
        self.p2_big_road_button.handle_event(event)
        self.p1_chance_button.handle_event(event)
        self.p2_chance_button.handle_event(event)
        self.p1_kniffel_button.handle_event(event)
        self.p2_kniffel_button.handle_event(event)
        self.std_skinset.skinset_button.handle_event(event)
        self.blue_skinset.skinset_button.handle_event(event)
        self.roman_skinset.skinset_button.handle_event(event)
        self.anti_skinset.skinset_button.handle_event(event)

    def draw(self, surface):
        surface.fill((255, 255, 255))

        pygame.draw.line(surface, (0, 0, 0), (0, 60), (800, 60), 2)
        self.title_lable.draw(surface)

        self.p1_label.draw(surface)
        self.p2_label.draw(surface)

        pygame.draw.rect(surface, (0, 0, 0), self.upper_left_rect, 1)
        self.ones_label.draw(surface)
        self.arrow_ones.draw(surface)
        self.p1_ones_button.draw(surface)
        self.p2_ones_button.draw(surface)
        self.twos_label.draw(surface)
        self.arrow_twos.draw(surface)
        self.p1_twos_button.draw(surface)
        self.p2_twos_button.draw(surface)
        self.threes_label.draw(surface)
        self.arrow_threes.draw(surface)
        self.p1_three_button.draw(surface)
        self.p2_three_button.draw(surface)
        self.fours_label.draw(surface)
        self.arrow_fours.draw(surface)
        self.p1_fours_button.draw(surface)
        self.p2_fours_button.draw(surface)
        self.fives_label.draw(surface)
        self.arrow_fives.draw(surface)
        self.p1_fives_button.draw(surface)
        self.p2_fives_button.draw(surface)
        self.sixes_label.draw(surface)
        self.arrow_sixes.draw(surface)
        self.p1_sixes_button.draw(surface)
        self.p2_sixes_button.draw(surface)
        self.upper_sum_wo_bonus_label.draw(surface)
        self.upper_sum_wo_bonus_arrow.draw(surface)
        self.p1_upper_sum_wo_bonus_show.draw(surface)
        self.p2_upper_sum_wo_bonus_show.draw(surface)
        self.bonus_label.draw(surface)
        self.bonus_arrow.draw(surface)
        self.p1_bonus_show.draw(surface)
        self.p2_bonus_show.draw(surface)
        self.upper_sum_label.draw(surface)
        self.upper_sum_arrow.draw(surface)
        self.p1_upper_sum_show.draw(surface)
        self.p2_upper_sum_show.draw(surface)

        pygame.draw.rect(surface, (0, 0, 0), self.upper_right_rect, 1)
        pygame.draw.rect(surface, (0, 0, 0), self.roll_dice_board, 2, 20)
        pygame.draw.rect(surface, (0, 0, 0), self.safe_dice_board, 2, 20)
        self.roll_one_lamp.draw(surface)
        self.roll_two_lamp.draw(surface)
        self.roll_three_lamp.draw(surface)
        self.roll_dices_button.draw(surface)

        self.dice_one.draw(surface)
        self.dice_two.draw(surface)
        self.dice_three.draw(surface)
        self.dice_four.draw(surface)
        self.dice_five.draw(surface)

        pygame.draw.rect(surface, (0, 0, 0), self.lower_left_rect, 1)
        self.three_of_a_kind_label.draw(surface)
        self.three_of_a_kind_arrow.draw(surface)
        self.p1_three_of_a_kind_button.draw(surface)
        self.p2_three_of_a_kind_button.draw(surface)
        self.four_of_a_kind_label.draw(surface)
        self.four_of_a_kind_arrow.draw(surface)
        self.p1_four_of_a_kind_button.draw(surface)
        self.p2_four_of_a_kind_button.draw(surface)
        self.full_house_label.draw(surface)
        self.full_house_arrow.draw(surface)
        self.p1_full_house_button.draw(surface)
        self.p2_full_house_button.draw(surface)
        self.small_road_label.draw(surface)
        self.small_road_arrow.draw(surface)
        self.p1_small_road_button.draw(surface)
        self.p2_small_road_button.draw(surface)
        self.big_road_label.draw(surface)
        self.big_road_arrow.draw(surface)
        self.p1_big_road_button.draw(surface)
        self.p2_big_road_button.draw(surface)
        self.kniffel_label.draw(surface)
        self.kniffel_arrow.draw(surface)
        self.p1_kniffel_button.draw(surface)
        self.p2_kniffel_button.draw(surface)
        self.chance_label.draw(surface)
        self.chance_arrow.draw(surface)
        self.p1_chance_button.draw(surface)
        self.p2_chance_button.draw(surface)
        self.lower_sum_label.draw(surface)
        self.lower_sum_arrow.draw(surface)
        self.p1_lower_sum_show.draw(surface)
        self.p2_lower_sum_show.draw(surface)
        self.upper_sum_low_label.draw(surface)
        self.upper_sum_low_arrow.draw(surface)
        self.p1_upper_sum_low_show.draw(surface)
        self.p2_upper_sum_low_show.draw(surface)
        self.extra_kniffel_label.draw(surface)
        self.extra_kniffel_arrow.draw(surface)
        self.p1_extra_kniffel_show.draw(surface)
        self.p2_extra_kniffel_show.draw(surface)
        self.end_sum_label.draw(surface)
        self.end_sum_arrow.draw(surface)
        self.p1_end_sum_show.draw(surface)
        self.p2_end_sum_show.draw(surface)

        pygame.draw.rect(surface, (0, 0, 0), self.lower_right_rect, 1)
        pygame.draw.rect(surface, (0, 0, 0), self.error_messages_rect, 2, 20)
        self.three_of_a_kind_explanation_label.draw(surface)
        self.four_of_a_kind_explanation_label.draw(surface)
        self.full_house_explanation_label.draw(surface)
        self.small_road_explanation_label.draw(surface)
        self.big_road_explanation_label.draw(surface)
        pygame.draw.line(surface, (0, 0, 0), (420, 530), (779, 530), 2)
        self.std_skinset.skinset_button.draw(surface)
        self.blue_skinset.skinset_button.draw(surface)
        self.roman_skinset.skinset_button.draw(surface)
        self.anti_skinset.skinset_button.draw(surface)

        pygame.draw.line(surface, (0, 0, 0), (0, 700), (800, 700), 2)
        self.start_new_game_button.draw(surface)
        self.home_button.draw(surface)

class ResultScreenMultiplayer(Screen):
    def __init__(self, manager, game_manager):
        super().__init__(manager, game_manager)

        self.title_label = widgets.Label("Kniffel", (400, 37.5), 80)
        self.highscore_show = widgets.ShowLabel("Highscore", (400, 125, 670, 75), 60)
        self.highscore_value_show = widgets.ShowLabel(str(self.game_manager.load_highscore()[0]["Score"]), (400, 215, 670, 90), 60)      # Werte aus multiplayer gamemanager

        self.p1_points_show = widgets.ShowLabel(str(self.game_manager.get_p1_tally_total()), (220, 420, 340, 300), 200)          # Werte aus multiplayer gamemanager
        self.p1_name_input = widgets.TextField((50, 580, 340, 100))

        self.p2_points_show = widgets.ShowLabel(str(self.game_manager.get_p2_tally_total()), (580, 420, 340, 300), 200)          # Werte aus multiplayer gamemanager
        self.p2_name_input = widgets.TextField((410, 580, 340, 100))

        self.start_new_game_button = widgets.Button("Start New Game", (100, 700, 200, 50))
        self.start_new_game_button.set_action(self.start_new_game)
        self.home_button = widgets.Button("Home", (500, 700, 200, 50))
        self.home_button.set_action(self.go_home)

    def start_new_game(self):
        self.save_highscore()
        self.game_manager = GameClass.GameMultiplayer()
        self.manager.change_screen(GameScreenMultiplayer(self.manager, self.game_manager))

    def go_home(self):
        self.save_highscore()
        self.manager.change_screen(StartScreen(self.manager, self.game_manager))

    def save_highscore(self):
        if self.p1_name_input.text.strip() != "":
            self.game_manager.save_highscore(self.p1_name_input.text, self.game_manager.get_p1_tally_total())

        if self.p2_name_input.text.strip() != "":
            self.game_manager.save_highscore(self.p2_name_input.text, self.game_manager.get_p2_tally_total())

    def handle_events(self, event):
        self.start_new_game_button.handle_event(event)
        self.home_button.handle_event(event)
        self.p1_name_input.handle_event(event)
        self.p2_name_input.handle_event(event)

    def draw(self, surface):
        surface.fill((255, 255, 255))

        pygame.draw.line(surface, (0, 0, 0), (0, 75), (800, 75), 2)
        self.title_label.draw(surface)
        self.highscore_show.draw(surface)
        self.highscore_value_show.draw(surface)
        self.p1_points_show.draw(surface)
        self.p1_name_input.draw(surface, 60)
        self.p2_points_show.draw(surface)
        self.p2_name_input.draw(surface, 60)
        self.start_new_game_button.draw(surface)
        self.home_button.draw(surface)