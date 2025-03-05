import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    # Overall class to manage game assets and behaviour.

    def __init__(self):
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        self.clock.tick(60)