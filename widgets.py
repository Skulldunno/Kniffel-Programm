import pygame

class Label:
    def __init__(self, text, position, font_size=32, color=(0, 0, 0)):
        self.text = text
        self.position = position
        self.color = color

        self.font = pygame.font.Font(None, font_size)
        self.image = self.font.render(
            self.text,
            True,
            self.color
        )

        self.rect = self.image.get_rect(center=position)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class ShowLabel:
    def __init__(self, text, rect, font_size=32, color=(0, 0, 0)):
        self.text = text
        self.position = (rect[0], rect[1])
        self.color = color

        self.label_rect = pygame.Rect(rect[0] - (rect[2]/2), rect[1] - (rect[3]/2), rect[2], rect[3])

        self.font = pygame.font.Font(None, font_size)
        self.image = self.font.render(
            self.text,
            True,
            self.color
        )

        self.rect = self.image.get_rect(center=(rect[0], rect[1]))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.label_rect, 2, 20)
        surface.blit(self.image, self.rect)      

class Lamp:
    def __init__(self, rect, color_off=(255, 255, 255), color_on=(255, 0, 0), state = False, border_radius=-1, width=1):
        self.rect = pygame.Rect(rect)
        self.border_radius = border_radius
        self.color_off = color_off
        self.color_on = color_on
        self.state = state
        self.width = width
    
    def draw(self, surface):
        if self.state:
            pygame.draw.rect(surface, self.color_on, self.rect, border_radius=self.border_radius)
            pygame.draw.rect(surface, (0, 0, 0), self.rect, self.width, self.border_radius)
        else:
            pygame.draw.rect(surface, self.color_off, self.rect, border_radius=self.border_radius)
            pygame.draw.rect(surface, (0, 0, 0), self.rect, self.width, self.border_radius)

    def switch_state(self):
        if self.state:
            self.state = False
        else:
            self.state = True

class LampLine:
    def __init__(self):
        self.__lamp_list = []

    def add_lamp(self, lamp: Lamp):
        if type(lamp) == Lamp:
            self.__lamp_list.append(lamp)

    def remove_lamp(self, lamp: Lamp):
        if type(lamp) == Lamp and lamp in self.__lamp_list:
            self.__lamp_list.remove(lamp)

    def turn_all_on(self):
        for lamps in self.__lamp_list:
            lamps.state = True

    def turn_all_off(self):
        for lamps in self.__lamp_list:
            lamps.state = False

    def turn_lamp_on(self, lamp: Lamp):
        if type(lamp) == Lamp:
            for lamps in self.__lamp_list:
                if lamps == lamp:
                    lamp.state = True

    def turn_lamp_off(self, lamp: Lamp):
        if type(lamp) == Lamp:
            for lamps in self.__lamp_list:
                if lamps == lamp:
                    lamp.state = False

    def turn_number_of_lamps_on(self, number: int):
        if number > len(self.__lamp_list):
            return print(f"turn_number_of_lamps_on({number}): the number given is higher than the number of available lamps")
        else:
            for lamp in range(number):
                self.__lamp_list[lamp].state = True

    def turn_number_of_lamps_off(self, number: int):
        if number > len(self.__lamp_list):
            return print(f"turn_number_of_lamps_off({number}): the number given is higher than the number of available lamps")
        else:
            for lamp in range(number):
                self.__lamp_list[lamp].state = False

class Button:
    def __init__(self, text, rect, color=(255, 255, 255), hover_color=(171, 171, 171), text_color=(0, 0, 0), font_size=32):
        self.text = text
        self.rect = pygame.Rect(rect)

        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color

        self.font = pygame.font.Font(None, font_size)

        self.action = None

    def set_action(self, action):
        self.action = action

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):

                if self.action:
                    self.action()

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()

        # Hover-Effekt
        if self.rect.collidepoint(mouse_pos):
            color = self.hover_color
        else:
            color = self.color

        pygame.draw.rect(
            surface,
            color,
            self.rect,
            border_radius=20
        )

        pygame.draw.rect(
            surface,
            (0, 0, 0),
            self.rect,
            2,
            20
        )

        text_image = self.font.render(
            self.text,
            True,
            self.text_color
        )

        text_rect = text_image.get_rect(
            center=self.rect.center
        )

        surface.blit(
            text_image,
            text_rect
        )

class ArrowRight:
    def __init__(self, position, length, color=(0, 0, 0)):
        self.position = (position[0] - (length/2), position[1])
        self.end_position = (self.position[0] + length, self.position[1])
        self.length = length
        self.color = color
    
    def draw(self, surface):
        pygame.draw.line(surface, self.color, self.position, (self.position[0]  + self.length, self.position[1]), 2)
        pygame.draw.line(surface, self.color, self.end_position, (self.end_position[0] - 10, self.end_position[1] - 10), 2)
        pygame.draw.line(surface, self.color, self.end_position, (self.end_position[0] - 10, self.end_position[1] + 10), 2)

class KlickableDice:
    def __init__(self, eyes, roll_rect, alt_rect):
        self.roll_rect = roll_rect
        self.alt_rect = alt_rect
        self.eyes = eyes
        self.pos_roll = True
        self.pngs = {
            1 : "dice_one.png",
            2 : "dice_two.png",
            3 : "dice_three.png",
            4 : "dice_four.png",
            5 : "dice_five.png",
            6 : "dice_six.png"
        }
        self.png = self.pngs[eyes]

    def set_action(self, action):
        self.action = action

    def handle_event(self, event):
        if self.pos_roll:
            rect = self.roll_rect
        else:
            rect = self.alt_rect

        if event.type == pygame.MOUSEBUTTONDOWN:
            rect = pygame.Rect(rect)
            if rect.collidepoint(event.pos):
                self.switch_rect()
    
    def draw(self, surface):
        if self.pos_roll:
            rect = self.roll_rect
        else:
            rect = self.alt_rect

        png = pygame.image.load(f"assets/{self.png}")
        png = pygame.transform.scale(png, (32, 32))
        surface.blit(png, (rect[0], rect[1]))

    def switch_rect(self):
        if self.pos_roll:
            self.pos_roll = False
        else:
            self.pos_roll = True

    def set_eyes(self, eyes):
        self.eyes = eyes

class TextField:
    def __init__(self, rect):
        self.active_input = False
        self.placeholder = "Name eingeben"
        self.text = ""
        self.rect = rect
        self.text_font = pygame.font.SysFont(None, 80)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and self.active_input:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            rect = pygame.Rect(self.rect)
            if rect.collidepoint(event.pos):
                if self.active_input:
                    self.active_input = False
                else:
                    self.active_input = True

    def draw(self, surface):
        rect = pygame.Rect(self.rect)

        pygame.draw.rect(surface, (255, 255, 255), rect)
        pygame.draw.rect(surface, (0, 0, 0), rect, 2, 20)
        if self.active_input:
            name_surface = self.text_font.render(self.text, True, (0, 0, 0))
        elif self.text != "":
            name_surface = self.text_font.render(self.text, True, (0, 0, 0))
        else:
            name_surface = self.text_font.render(self.placeholder, True, (0, 0, 0))
        surface.blit(name_surface, (rect.x + 10, rect.y + 20))

class HighscoreView:
    def __init__(self, highscores = [{'Name': 'Nick', 'Score': 3}, {'Name': 'Nick', 'Score': 2}, {'Name': 'Nick', 'Score': 2}, {'Name': '---', 'Score': 0}, {'Name': '---', 'Score': 0}, {'Name': '---', 'Score': 0}, {'Name': '---', 'Score': 0}, {'Name': '---', 'Score': 0}, {'Name': '---', 'Score': 0}, {'Name': '---', 'Score': 0}]):
        self.highscores = highscores
        self.name_labels = []
        self.arrows = []
        self.score_labels = []

        y_adder = 0

        for entrys in self.highscores:
            name = entrys['Name']
            score = entrys['Score']

            self.name_labels.append(Label(name, (300, 195 + y_adder), 60))
            self.arrows.append(ArrowRight((400, 195 + y_adder), 30))
            self.score_labels.append(Label(str(score), (500, 195 + y_adder), 60))
            y_adder += 50

    def draw(self, surface):
        for label in self.name_labels:
            label.draw(surface)
        
        for arrow in self.arrows:
            arrow.draw(surface)

        for label in self.score_labels:
            label.draw(surface)
