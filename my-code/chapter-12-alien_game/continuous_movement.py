import pygame


class Ship:
    # A class to manage the ship.

    def __init__(self, ai_game):
        # Initialize the ship and set its starting position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)
        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update the ship's position based on the movement flag.
        # Update the ship's x value, not the rect.
        if self.moving_right:
            self.x += self.settings.ship_speed
            self.rect.x += 1
        if self.moving_left:
            self.x -= self.settings.ship_speed
            self.rect.x -= 1

        # Update rect object from self.x.
        self.rect.x = self.x

    

    