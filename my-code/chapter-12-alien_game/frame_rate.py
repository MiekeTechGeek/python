import pygame


def __init__(self):
    # Initialize the game, and create game resources.
    pygame.init()
    self.clock = pygame.time.Clock()
    
def run_game(self):
    # Start the man loop for the game.
    while True:
        pygame.display.flip()
        self.clock.tick(60)