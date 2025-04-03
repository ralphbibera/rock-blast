import pygame
from constants import *
from enum import Enum


class GroupPosition(Enum):
    TOP_LEFT = 0
    TOP_RIGHT = 1
    BOTTOM_LEFT = 2
    BOTTOM_RIGHT = 3


class UI:
    elements = []

    def __init__(self, screen):
        self.screen = screen
        UI.elements.append(self)

    @classmethod
    def render(cls):
        for element in cls.elements:
            element.render()


class Group(UI):
    def __init__(self, screen, cards, group_position: GroupPosition, padding=20, spacing=10):
        super().__init__(screen)
        self.cards = cards
        self.group_position = group_position
        self.padding = padding
        self.spacing = spacing

        self.layout_cards()

    def layout_cards(self):
        screen_width, screen_height = self.screen.get_width(), self.screen.get_height()
        total_group_height = sum(card.get_height() for card in self.cards) + \
            (len(self.cards) - 1) * self.spacing
        total_group_width = Card.WIDTH

        x, y = self.padding, self.padding

        if self.group_position == GroupPosition.TOP_RIGHT:
            x = screen_width - total_group_width - self.padding
        elif self.group_position == GroupPosition.BOTTOM_LEFT:
            y = screen_height - total_group_height - self.padding
        elif self.group_position == GroupPosition.BOTTOM_RIGHT:
            x = screen_width - total_group_width - self.padding
            y = screen_height - total_group_height - self.padding

        for index, card in enumerate(self.cards):
            card.set_position(
                x, y + index * (card.get_height() + self.spacing))

    def render(self):
        for card in self.cards:
            card.render()


class Card():
    WIDTH = 120

    def __init__(self, screen, height=CARD_HEIGHT, font_size=CARD_FONT_SIZE, padding=CARD_PADDING):
        self.screen = screen
        self.text = ""
        self.position = pygame.Rect(0, 0, self.WIDTH, height)
        self.font = pygame.font.Font(None, font_size)
        self.padding = padding

    def render(self):
        pygame.draw.rect(self.screen, "white", self.position, 2)
        lines = self.text.split('\n')
        for i, line in enumerate(lines):
            self.screen.blit(self.font.render(
                line, True, "white"), (self.position.x + self.padding, self.position.y + self.padding + i * self.font.get_linesize()))

    def set_position(self, x, y):
        self.position.topleft = (x, y)

    def update(self, text):
        self.text = text

    def get_height(self):
        return self.position.height
