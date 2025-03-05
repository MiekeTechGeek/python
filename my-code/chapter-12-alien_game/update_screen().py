import sys
from typing import Self
import pygame


def run_game(self):
    # Start the main loop for the game.
    while True:
        self._check_events()
        self.ship.update()
        self._update_bullets()
        self._update_screen()
        self.clock.tick(60)

def _check_events(self):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def _update_bullets(self):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    self.bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in self.bullets.copy():
        if bullet.rect.bottom <= 0:
            self.bullets.remove(bullet)

def _update_screen(self):
    # Update images on the screen, and flip to the new screen.
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()

    pygame.display.flip()

def update(self):
    """Update the ship's position based on movement flags."""
    # Update the ship's x value, not the rect.
    if self.moving_right and self.rect.right < self.screen_rect.right:
       self.x += self.settings.ship_speed
    if self.moving_left and self.rect.left > 0:
       self.x -= self.settings.ship_speed
       
    # Update rect object from self.x.
    self.rect.x = self.x 