import random

import pygame
from constants import *
from utils import calculate_winner_of_round


class GameGUI:
    def __init__(self):
        # game attributes
        self.player_score = 0
        self.computer_score = 0

        self.current_screen = TITLE_SCREEN

        # pygame attributes
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.time.set_timer(pygame.USEREVENT, 1500)

        # images
        self.background = pygame.image.load("img/background.png")
        self.title_logo = pygame.image.load("img/rps_logo-removebg.png")
        self.rock_logo = pygame.image.load("img/rock.png")
        self.scissors_logo = pygame.image.load("img/scissors.png")
        self.paper_logo = pygame.transform.scale(pygame.image.load("img/paper.png"),
                                                 (pygame.image.load("img/paper.png").get_rect().width * 0.9,
                                                  pygame.image.load("img/paper.png").get_rect().height * 0.9))

        self.rps_images = [self.rock_logo, self.paper_logo, self.scissors_logo]
        self.computer_flip_index = ROCK_INDEX

        self.player_picked_choice = None
        self.computer_picked_choice = None

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
            self.draw_screens()
            pygame.display.flip()  # Refresh on-screen display
            clock.tick(60)

    def handle_pygame_events(self):
        # Process player inputs.
        for event in pygame.event.get():
            self.check_if_event_is_quit(event)
            self.check_if_start_button_is_pressed(event)
            self.check_if_player_picked_a_choice(event)
            self.change_flip_index(event)
            self.reset_choice_indices_and_calculate_score(event)
            self.check_if_end_button_is_pressed(event)

    def check_if_event_is_quit(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    def check_if_start_button_is_pressed(self, event):
        if self.current_screen == TITLE_SCREEN and event.type == pygame.MOUSEBUTTONDOWN:
            if self.game_component_hovered(pygame.mouse.get_pos(), START_BUTTON_DIMENSIONS):
                self.current_screen = PLAY_SCREEN

    def check_if_player_picked_a_choice(self, event):
        if self.player_picked_choice is not None:
            return
        self.check_if_player_chose(ROCK_INDEX, ROCK_LOGO_DIMENSIONS, event)
        self.check_if_player_chose(PAPER_INDEX, PAPER_LOGO_DIMENSIONS, event)
        self.check_if_player_chose(SCISSORS_INDEX, SCISSORS_LOGO_DIMENSIONS, event)

    def check_if_player_chose(self, logo_index, dimensions, event):
        if self.current_screen == PLAY_SCREEN and event.type == pygame.MOUSEBUTTONDOWN:
            if self.game_component_hovered(pygame.mouse.get_pos(), dimensions):
                self.assign_player_choice_and_computer_choice(logo_index)
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                pygame.time.set_timer(pygame.USEREVENT + EVENT_FOR_WAITING_AFTER_CHOICE, 2000, loops=1)

    def assign_player_choice_and_computer_choice(self, player_choice):
        self.player_picked_choice = player_choice
        self.computer_picked_choice = random.randint(0, NUM_OPTIONS)

    def change_flip_index(self, event):
        if event.type == pygame.USEREVENT:
            self.computer_flip_index = (self.computer_flip_index + 1) % 3

    def reset_choice_indices_and_calculate_score(self, event):
        if event.type == pygame.USEREVENT + EVENT_FOR_WAITING_AFTER_CHOICE:
            self.calculate_scores()

    def calculate_scores(self):
        player_choice = COMPUTER_MOVES[self.player_picked_choice]
        computer_choice = COMPUTER_MOVES[self.computer_picked_choice]

        winner = calculate_winner_of_round(player_choice, computer_choice)

        if winner == "Player":
            self.player_score += 1
        elif winner == "Computer":
            self.computer_score += 1

        if self.player_score == SCORE_TO_REACH or self.computer_score == SCORE_TO_REACH:
            self.current_screen = END_SCREEN

        self.computer_picked_choice = None
        self.player_picked_choice = None

    def check_if_end_button_is_pressed(self, event):
        if self.current_screen == END_SCREEN and event.type == pygame.MOUSEBUTTONDOWN:
            if self.game_component_hovered(pygame.mouse.get_pos(), START_BUTTON_DIMENSIONS):
                self.player_score = 0
                self.computer_score = 0
                self.current_screen = PLAY_SCREEN

    def draw_screens(self):
        self.draw_title_screen()
        self.draw_play_screen()
        self.draw_end_screen()

    def draw_title_screen(self):
        if self.current_screen != TITLE_SCREEN:
            return

        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.title_logo, (250, 200))
        self.screen.blit(self.title_text, (180, 50))

        self.draw_button_at_bottom_of_screen()
        self.draw_title_button_text()

    def draw_button_at_bottom_of_screen(self):
        mouse = pygame.mouse.get_pos()

        if self.game_component_hovered(mouse, START_BUTTON_DIMENSIONS):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            self.draw_button(LIGHT_ORANGE, START_BUTTON_DIMENSIONS[0], START_BUTTON_DIMENSIONS[2])
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.draw_button(DARK_ORANGE, START_BUTTON_DIMENSIONS[0], START_BUTTON_DIMENSIONS[2])

    def draw_button(self, color, x, y):
        pygame.draw.rect(self.screen, color,
                         [x, y, BUTTON_WIDTH, BUTTON_HEIGHT],
                         border_radius=3)

    def draw_title_button_text(self):
        test_x_pos = SCREEN_WIDTH / 2 - 25
        test_y_pos = SCREEN_HEIGHT / 2 + 210
        self.screen.blit(self.button_text, (test_x_pos, test_y_pos))

    def draw_play_screen(self):
        if self.current_screen != PLAY_SCREEN:
            return
        pygame.display.flip()
        self.screen.blit(self.background, (0, 0))
        self.player_score_text = self.title_font.render(str(self.player_score), False, DARK_BLUE)
        self.computer_score_text = self.title_font.render(str(self.computer_score), False, DARK_BLUE)

        self.draw_dashed_line_down_the_middle()
        self.draw_scores_on_screen()
        self.draw_player_choices()
        self.flip_through_computer_images()

        if self.player_picked_choice is not None and self.computer_picked_choice is not None:
            self.draw_choice_at_position(self.player_picked_choice, 140, 250)
            self.draw_choice_at_position(self.computer_picked_choice, 535, 250)

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
        if self.game_component_hovered(mouse, ROCK_LOGO_DIMENSIONS) or \
                self.game_component_hovered(mouse, PAPER_LOGO_DIMENSIONS) or \
                self.game_component_hovered(mouse, SCISSORS_LOGO_DIMENSIONS):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        self.screen.blit(self.rock_logo, (40, 70))
        self.screen.blit(self.paper_logo, (220, 65))
        self.screen.blit(self.scissors_logo, (140, 200))

    def flip_through_computer_images(self):
        if self.computer_picked_choice is not None:
            return
        self.screen.blit(self.rps_images[self.computer_flip_index], (535, 250))

    def draw_choice_at_position(self, choice_index, x, y):
        self.screen.blit(self.rps_images[choice_index], (x, y))

    def draw_end_screen(self):
        if self.current_screen != END_SCREEN:
            return
        self.screen.blit(self.background, (0, 0))

        x_pos = 25
        if self.player_score == SCORE_TO_REACH:
            x_pos = 100
            game_over_message = "Congrats! You won the game!"
        else:
            game_over_message = "That's too bad. Better luck next time!"

        end_text = self.title_font.render(game_over_message, False, DARK_BLUE)
        self.screen.blit(end_text, (x_pos, 250))

        self.draw_button_at_bottom_of_screen()
        self.draw_end_button_text()

    def draw_end_button_text(self):
        end_button_text = self.button_font.render("Play again?", False, DARK_BLUE)
        test_x_pos = SCREEN_WIDTH / 2 - 40
        test_y_pos = SCREEN_HEIGHT / 2 + 210
        self.screen.blit(end_button_text, (test_x_pos, test_y_pos))

    def game_component_hovered(self, mouse, component_dimensions):
        return component_dimensions[0] <= mouse[0] <= component_dimensions[1] and \
               component_dimensions[2] <= mouse[1] <= component_dimensions[3]
