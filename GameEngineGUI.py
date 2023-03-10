import pygame
from constants import *


def start_button_hovered(mouse):
    return SCREEN_WIDTH / 2 - 100 <= mouse[0] <= SCREEN_WIDTH / 2 + 100 \
           and SCREEN_HEIGHT / 2 + 190 <= mouse[1] <= SCREEN_HEIGHT / 2 + 250


class GameGUI:
    def __init__(self):
        """
        This function initializes a new instance of the GameGUI class with both
        the player's and computer's scores set to zero.
        """
        self.player_score = 0
        self.computer_score = 0

        self.title = True

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
        self.player_score_text = self.title_font.render(str(self.player_score), False, DARK_BLUE)
        self.computer_score_text = self.title_font.render(str(self.computer_score), False, DARK_BLUE)


    def start_game(self):
        clock = pygame.time.Clock()

        while True:
            self.handle_pygame_events()

            # Do logical updates here.
            # ...

            self.draw_screens()

            # Render the graphics here.
            # ...

            pygame.display.flip()  # Refresh on-screen display
            clock.tick(60)  # wait until next frame (at 60 FPS)

    def handle_pygame_events(self):
        # Process player inputs.
        for event in pygame.event.get():
            self.check_if_event_is_quit(event)
            self.check_if_start_button_is_pressed(event)

    def check_if_event_is_quit(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    def check_if_start_button_is_pressed(self, event):
        # checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if the mouse is clicked on the button, then start the game
            if start_button_hovered(pygame.mouse.get_pos()):
                self.title = False
                print("Start button pressed. Begin the game.")

    def draw_screens(self):
        if self.title:
            self.draw_title_screen()
        else:
            self.draw_play_screen()

    def draw_title_screen(self):
        if not self.title:
            return

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
        self.screen.blit(self.button_text, (test_x_pos, test_y_pos))

    def draw_play_screen(self):
        pygame.display.flip()
        self.screen.blit(self.background, (0, 0))

        # draw line down the middle
        # pygame.draw.rect(self.screen, DARK_ORANGE, [SCREEN_WIDTH / 2, 0, 10, SCREEN_HEIGHT])
        self.draw_dashed_line_down_the_middle()
        self.draw_scores_on_screen()

    def draw_dashed_line_down_the_middle(self):
        num_dashed_lines = 30
        y_pos = 5
        for i in range(num_dashed_lines):
            pygame.draw.rect(self.screen, RED, [SCREEN_WIDTH / 2, y_pos, 5, 10])
            y_pos += 20

    def draw_scores_on_screen(self):
        test_x_pos_player = SCREEN_WIDTH / 4
        test_y_pos = 20
        self.screen.blit(self.player_score_text, (test_x_pos_player, test_y_pos))

        test_x_pos_computer = 3 * SCREEN_WIDTH / 4
        self.screen.blit(self.computer_score_text, (test_x_pos_computer, test_y_pos))
