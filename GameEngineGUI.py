import pygame
from constants import *


def start_button_hovered(mouse):
    return SCREEN_WIDTH / 2 - 100 <= mouse[0] <= SCREEN_WIDTH / 2 + 100 \
           and SCREEN_HEIGHT / 2 + 190 <= mouse[1] <= SCREEN_HEIGHT / 2 + 250


def rock_logo_hovered(mouse):
    return 55 <= mouse[0] <= 150 and 80 <= mouse[1] <= 165


def paper_logo_hovered(mouse):
    return 230 <= mouse[0] <= 340 and 70 <= mouse[1] <= 170


def scissors_logo_hovered(mouse):
    return 145 <= mouse[0] <= 275 and 205 <= mouse[1] <= 300


class GameGUI:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0

        self.title = True

        # pygame attributes
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.time.set_timer(pygame.USEREVENT, 1500)

        # images
        self.background = pygame.image.load("img/background.png")
        self.title_logo = pygame.image.load("img/rps_logo-removebg.png")
        self.original_rock_logo = pygame.image.load("img/rock.png")
        self.rock_logo = pygame.image.load("img/rock.png")
        self.original_scissors_logo = pygame.image.load("img/scissors.png")
        self.scissors_logo = pygame.image.load("img/scissors.png")
        self.original_paper_logo = pygame.transform.scale(pygame.image.load("img/paper.png"),
                                                          (pygame.image.load("img/paper.png").get_rect().width * 0.9,
                                                           pygame.image.load("img/paper.png").get_rect().height * 0.9))
        self.paper_logo = pygame.transform.scale(pygame.image.load("img/paper.png"),
                                                 (pygame.image.load("img/paper.png").get_rect().width * 0.9,
                                                  pygame.image.load("img/paper.png").get_rect().height * 0.9))

        self.rps_images = [self.rock_logo, self.paper_logo, self.scissors_logo]
        self.computer_flip_index = ROCK_INDEX

        self.player_picked_choice = None

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
            if self.player_picked_choice is None:
                self.check_if_player_picked_a_choice(event)
            self.change_flip_index(event)

    def check_if_event_is_quit(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    def check_if_start_button_is_pressed(self, event):
        # checks if a mouse is clicked
        if self.title and event.type == pygame.MOUSEBUTTONDOWN:
            # if the mouse is clicked on the button, then start the game
            if start_button_hovered(pygame.mouse.get_pos()):
                self.title = False
                print("Start button pressed. Begin the game.")

    def check_if_player_picked_a_choice(self, event):
        self.check_if_player_chose_rock(event)
        self.check_if_player_chose_paper(event)
        self.check_if_player_chose_scissors(event)

    def check_if_player_chose_rock(self, event):
        if not self.title and event.type == pygame.MOUSEBUTTONDOWN:
            if rock_logo_hovered(pygame.mouse.get_pos()):
                self.rock_logo = pygame.transform.smoothscale(self.original_rock_logo,
                                                              (self.original_rock_logo.get_rect().width * 0.9,
                                                               self.original_rock_logo.get_rect().height * 0.9))
                self.player_picked_choice = ROCK_INDEX
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if not self.title and event.type == pygame.MOUSEBUTTONUP:
            if rock_logo_hovered(pygame.mouse.get_pos()):
                self.rock_logo = pygame.transform.smoothscale(self.original_rock_logo,
                                                              (self.original_rock_logo.get_rect().width,
                                                               self.original_rock_logo.get_rect().height))

    def check_if_player_chose_paper(self, event):
        if not self.title and event.type == pygame.MOUSEBUTTONDOWN:
            if paper_logo_hovered(pygame.mouse.get_pos()):
                self.paper_logo = pygame.transform.smoothscale(self.original_paper_logo,
                                                               (self.original_paper_logo.get_rect().width * 0.9,
                                                                self.original_paper_logo.get_rect().height * 0.9))
                self.player_picked_choice = PAPER_INDEX
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if not self.title and event.type == pygame.MOUSEBUTTONUP:
            if paper_logo_hovered(pygame.mouse.get_pos()):
                self.paper_logo = pygame.transform.smoothscale(self.original_paper_logo,
                                                               (self.original_paper_logo.get_rect().width,
                                                                self.original_paper_logo.get_rect().height))

    def check_if_player_chose_scissors(self, event):
        if not self.title and event.type == pygame.MOUSEBUTTONDOWN:
            if scissors_logo_hovered(pygame.mouse.get_pos()):
                self.scissors_logo = pygame.transform.smoothscale(self.original_scissors_logo,
                                                                  (self.original_scissors_logo.get_rect().width * 0.9,
                                                                   self.original_scissors_logo.get_rect().height * 0.9))
                self.player_picked_choice = SCISSORS_INDEX
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if not self.title and event.type == pygame.MOUSEBUTTONUP:
            if scissors_logo_hovered(pygame.mouse.get_pos()):
                self.scissors_logo = pygame.transform.smoothscale(self.original_scissors_logo,
                                                                  (self.original_scissors_logo.get_rect().width,
                                                                   self.original_scissors_logo.get_rect().height))

    def change_flip_index(self, event):
        if event.type == pygame.USEREVENT:
            self.computer_flip_index = (self.computer_flip_index + 1) % 3

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
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            self.draw_title_button(LIGHT_ORANGE)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
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
        self.draw_player_choices()
        self.flip_through_computer_images()
        self.draw_choice_that_player_picked()

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

    def draw_player_choices(self):
        if self.player_picked_choice is not None:
            return
        mouse = pygame.mouse.get_pos()
        if rock_logo_hovered(mouse) or paper_logo_hovered(mouse) or scissors_logo_hovered(mouse):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        self.screen.blit(self.rock_logo, (40, 70))
        self.screen.blit(self.paper_logo, (220, 65))
        self.screen.blit(self.scissors_logo, (140, 200))

    def draw_choice_that_player_picked(self):
        if self.player_picked_choice is None:
            return
        self.screen.blit(self.rps_images[self.player_picked_choice], (140, 250))

    def flip_through_computer_images(self):
        self.screen.blit(self.rps_images[self.computer_flip_index], (535, 250))
