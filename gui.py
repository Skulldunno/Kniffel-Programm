import pygame
import widgets
import GameClass


class Gui:
    def __init__(self):
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
            #pygame.display.set_icon(pygame.image.load(f"./assets/{self.iconchanger.icon_list[self.iconchanger.icon_index]}"))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


class IconChanger:
    def __init__(self):
        self.icon_list = [
            "icon_one.png",
            "icon_two.png", 
            "icon_three.png",
            "icon_four.png",
            "icon_five.png",
            "icon_six.png"
            ]
        self.icon_index = 5
        self.frame_counter = 0

    def increment_index(self):
        if self.icon_index == 5:
            self.icon_index = 0
        else:
            self.icon_index += 1

    def increment_frame_counter(self):
        if self.frame_counter == 60:
            self.frame_counter = 0
            self.increment_index()
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

        self.start_button = widgets.Button("Start", (225, 700, 350, 60))
        self.start_button.set_action(self.start_game)

    def start_game(self):
        self.game_manager = GameClass.Game()
        self.manager.change_screen(GameScreen(self.manager, self.game_manager))

    def handle_events(self, event):
        self.start_button.handle_event(event)

    def draw(self, surface):
        surface.fill((255, 255, 255))

        pygame.draw.line(surface, (0, 0, 0), (0, 75), (800, 75), 2)
        self.title_lable.draw(surface)

        pygame.draw.rect(surface, (0, 0, 0), self.highscore_rect, 2, 20)
        self.highscore_label.draw(surface)

        pygame.draw.rect(surface, (0, 0, 0), self.highscores_rect, 2, 20)
        self.highscores_view.draw(surface)

        self.start_button.draw(surface)

class GameScreen(Screen):
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

        self.dice_one = widgets.KlickableDice(0, (430, 145, 32, 32), (725, 99, 32, 32))
        self.dice_two = widgets.KlickableDice(0, (485, 220, 32, 32), (725, 133, 32, 32))
        self.dice_three = widgets.KlickableDice(0, (525, 180, 32, 32), (725, 167, 32, 32))
        self.dice_four = widgets.KlickableDice(0, (615, 230, 32, 32), (725, 201, 32, 32))
        self.dice_five = widgets.KlickableDice(0, (590, 130, 32, 32), (725, 235, 32, 32))

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

        self.start_new_game_button = widgets.Button("Start new Game", (200, 712.5, 195, 75))
        self.start_new_game_button.set_action(self.restart_game)
        self.home_button = widgets.Button("Home", (405, 712.5, 195, 75), font_size=40)
        self.home_button.set_action(self.quit_game)
    
    def reset_dice(self):
        self.dice_one = widgets.KlickableDice(0, (430, 145, 32, 32), (725, 99, 32, 32))
        self.dice_two = widgets.KlickableDice(0, (485, 220, 32, 32), (725, 133, 32, 32))
        self.dice_three = widgets.KlickableDice(0, (525, 180, 32, 32), (725, 167, 32, 32))
        self.dice_four = widgets.KlickableDice(0, (615, 230, 32, 32), (725, 201, 32, 32))
        self.dice_five = widgets.KlickableDice(0, (590, 130, 32, 32), (725, 235, 32, 32))

    def enter_ones(self):
        if self.game_manager.get_rerolls() == 3:
            return
        if self.game_manager.scoresheet.check_kniffel(self.game_manager.dice_list):
            pass
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
            pass
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
            pass
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
            pass
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
            pass
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
            pass
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
        if self.game_manager.scoresheet.check_kniffel(self.game_manager.dice_list):
            self.game_manager.scoresheet.kniffel = 50
            self.game_manager.reset_rerolls()
        else:
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
        self.manager.change_screen(ResultScreen(self.manager, self.game_manager))

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
        self.manager.change_screen(GameScreen(self.manager, self.game_manager))

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

    def update_sums_upper(self):
        self.upper_sum_wo_bonus_show.text = str(self.game_manager.score_upper_part())
        self.upper_sum_show.text = str(self.game_manager.score_upper_part() + self.game_manager.scoresheet.bonus)
        self.bonus_show.text = str(self.game_manager.scoresheet.bonus)
        self.upper_sum_low_show.text = str(self.game_manager.score_upper_part() + self.game_manager.scoresheet.bonus)

    def update_sums_lower(self):
        self.lower_sum_show.text = str(self.game_manager.score_lower_part())
        self.upper_sum_low_show.text = str(self.game_manager.score_upper_part() + self.game_manager.scoresheet.bonus)

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

        pygame.draw.line(surface, (0, 0, 0), (0, 700), (800, 700), 2)
        self.start_new_game_button.draw(surface)
        self.home_button.draw(surface)

class ResultScreen(Screen):
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
        self.game_manager = GameClass.Game()
        self.manager.change_screen(GameScreen(self.manager, self.game_manager))

    def go_home(self):
        self.manager.change_screen(StartScreen(self.manager, self.game_manager))

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