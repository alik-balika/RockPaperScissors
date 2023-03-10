import pygame
from constants import *


def start_button_hovered(mouse):
    return SCREEN_WIDTH / 2 - 100 <= mouse[0] <= SCREEN_WIDTH / 2 + 100 \
           and SCREEN_HEIGHT / 2 + 190 <= mouse[1] <= SCREEN_HEIGHT / 2 + 250


def check_if_event_is_quit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        raise SystemExit


def check_if_start_button_is_pressed(event):
    # checks if a mouse is clicked
    if event.type == pygame.MOUSEBUTTONDOWN:
        # if the mouse is clicked on the button, then start the game
        if start_button_hovered(pygame.mouse.get_pos()):
            print("Start button pressed. Begin the game.")


def handle_pygame_events():
    # Process player inputs.
    for event in pygame.event.get():
        check_if_event_is_quit(event)
        check_if_start_button_is_pressed(event)




class GameGUI:
    def __init__(self):
        """
        This function initializes a new instance of the GameGUI class with both
        the player's and computer's scores set to zero.
        """
        self.player_score = 0
        self.computer_score = 0

        # pygame attributes
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # images
        self.background = pygame.image.load("img/background.png")
        self.title_logo = pygame.image.load("img/rps_logo-removebg.png")

        # fonts
        pygame.font.init()
        self.title_font = pygame.font.SysFont(GAME_FONT, TITLE_FONT_SIZE, bold=True)
        self.title_text = self.title_font.render('Rock, Paper, Scissors!', False, DARK_BLUE)
        self.button_font = pygame.font.SysFont(GAME_FONT, REGULAR_FONT_SIZE)
        self.button_text = self.button_font.render('Begin!', False, DARK_BLUE)

    def start_game(self):
        clock = pygame.time.Clock()

        while True:
            handle_pygame_events()

            # Do logical updates here.
            # ...

            self.draw_title_screen()

            # Render the graphics here.
            # ...

            pygame.display.flip()  # Refresh on-screen display
            clock.tick(60)  # wait until next frame (at 60 FPS)

    def draw_title_screen(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.title_logo, (250, 200))
        self.screen.blit(self.title_text, (180, 50))

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        # if mouse is hovered on a button it
        # changes to lighter shade
        if start_button_hovered(mouse):
            self.draw_title_button(LIGHT_ORANGE)
        else:
            self.draw_title_button(DARK_ORANGE)

        self.draw_title_button_text()

    def draw_title_button(self, color):
        pygame.draw.rect(self.screen, color,
                         [SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 190, BUTTON_WIDTH, BUTTON_HEIGHT],
                         border_radius=3)

    def draw_title_button_text(self):
        test_x_pos = SCREEN_WIDTH / 2 - 25
        test_y_pos = SCREEN_HEIGHT / 2 + 210
        # superimposing the text onto our button
        self.screen.blit(self.button_text, (test_x_pos, test_y_pos))