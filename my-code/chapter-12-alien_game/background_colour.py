import sys
import pygame


def __init__(self):
    pygame.display.set_caption("Alien Invasion")

    # Set the background colour.
    self.bg_color = (230, 230, 230)

def run_game(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Redraw the screen during each pass through the loop.
    self.screen.fill(self.bg_color)

    # Make the most recently drawn screen visible.
    pygame.display.flip()
    self.clock.tick(60)