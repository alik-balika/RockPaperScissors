import pygame


class GameGUI:
    def __init__(self):
        """
        This function initializes a new instance of the GameGUI class with both
        the player's and computer's scores set to zero.
        """
        self.player_score = 0
        self.computer_score = 0

    def start_game(self):
        pygame.init()

        screen = pygame.display.set_mode((1280, 720))

        clock = pygame.time.Clock()

        while True:
            # Process player inputs.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

            # Do logical updates here.
            # ...

            screen.fill("purple")  # Fill the display with a solid color

            # Render the graphics here.
            # ...

            pygame.display.flip()  # Refresh on-screen display
            clock.tick(60)  # wait until next frame (at 60 FPS)
