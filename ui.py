import pygame


# def draw_card(screen, text, color, position):
#     font = pygame.font.SysFont(None, 36)
#     text_surface = font.render(text, True, color)
#     screen.blit(text_surface, (position[0] + 10, position[1] + 10))
#     pygame.draw.rect(screen, "white", [position[0], position[1],
#                      text_surface.get_width() + 20, text_surface.get_height() + 20], 2)


# def draw_item(screen, text, color, position):
#     # font = pygame.font.SysFont(None, 36)
#     rectangle = pygame.Rect(position[0], position[1], 50, 50)
#     pygame.draw.rect(screen, "white", rectangle, 2)
#     # text_surface = font.render(text, True, color)
#     # screen.blit(text_surface, (position[0] + 20, position[1] + 20))
#     # pygame.draw.rect(screen, "white", [position[0], position[1],
#     #                  text_surface.get_width() + 20, text_surface.get_height() + 20], 2)


class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 36)

    def card(self, text, position):
        text_surface = self.font.render(text, True, "white")
    
    def group(self, gap, items):

