import pygame


class SkinChanger:
    def __init__(self):
        self.__current_skinset = None
        self.skinsets = {}
        self.dice_list = []

    def add_skinset(self, id_string, skinset):
        self.skinsets[id_string] = skinset

    def add_dice(self, dice):
        self.dice_list.append(dice)

    def set_current_skinset(self, skinset):
        self.__current_skinset = skinset

    def update_skinset(self):
        for die in self.dice_list:
            die.pngs = self.skinsets[self.__current_skinset].pngs

    def get_current_skinset(self):
        return self.skinsets[self.__current_skinset].pngs

class SkinsetButton:
    def __init__(self, rect, png):
        self.png = png
        self.rect = rect

    def set_action(self, action):
        self.action = action

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            rect = pygame.Rect(rect)
            if rect.collidepoint(event.pos):
                if self.action:
                    self.action()

    def draw(self, surface):
        png = pygame.image.load(f"assets/{self.png}")
        png = pygame.transform.scale(png, (32, 32))
        surface.blit(png, (self.rect[0], self.rect[1]))

class SkinSet:
    def __init__(self):
        self.pngs = {}
        self.skinset_button = None

class StandartSkinset(SkinSet):
    def __init__(self):
        super().__init__()

        self.pngs = {
            0 : "empty.png",
            1 : "dice_one.png",
            2 : "dice_two.png",
            3 : "dice_three.png",
            4 : "dice_four.png",
            5 : "dice_five.png",
            6 : "dice_six.png"
        }

class BlueSkinset(SkinSet):
    def __init__(self):
        super().__init__()

        self.pngs = {
            0 : "empty.png",
            1 : "dice_one_blue.png",
            2 : "dice_two_blue.png",
            3 : "dice_three_blue.png",
            4 : "dice_four_blue.png",
            5 : "dice_five_blue.png",
            6 : "dice_six_blue.png"
        }
