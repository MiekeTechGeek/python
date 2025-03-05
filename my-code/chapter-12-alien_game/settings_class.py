from ship import Ship
from bullet import Bullet

class Settings:
    # A class to store all settings for Alien Invasion.

    def __init__(self):
        # Initialize the game's settings.
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        # Ship settings
        self.ship_speed = 1.5

import pygame

from settings import Settings

class AlienInvasion:
    # Overall class to manage game assets and behaviour.

    def __init__(self):
        # Initialize the game, and create game resources.
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        self.clock.tick(60)