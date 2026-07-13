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