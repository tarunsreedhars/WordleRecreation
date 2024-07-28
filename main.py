import random
import pygame
from wordle import load_dict, determine_unguessed_letters, determine_color
from graphics import setup_screen, draw_background, draw_guesses
from config import WIDTH, HEIGHT, ALPHABET, DICT_GUESSES_FILE, DICT_ANSWERS_FILE

class Main:

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont("comicsans", (WIDTH - 4 * 10 - 2 * 250) // 5)
        self.font_small = pygame.font.SysFont("comicsans", ((WIDTH - 4 * 10 - 2 * 250) // 5) // 2)
        self.dict_guesses = load_dict(DICT_GUESSES_FILE)
        self.dict_answers = load_dict(DICT_ANSWERS_FILE)
        self.answer = random.choice(self.dict_answers)
        self.input = ""
        self.guesses = []
        self.unguessed = ALPHABET
        self.game_over = False
        self.screen = setup_screen(WIDTH, HEIGHT)

    def run(self):
        animating = True
        while animating:
            draw_background(self.screen, self.unguessed, self.font_small)
            draw_guesses(self.screen, self.guesses, self.input, self.answer, self.font)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    animating = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        animating = False
                    elif event.key == pygame.K_BACKSPACE:
                        if len(self.input) > 0:
                            self.input = self.input[:-1]
                    elif event.key == pygame.K_RETURN:
                        if len(self.input) == 5 and self.input in self.dict_guesses:
                            self.guesses.append(self.input)
                            self.unguessed = determine_unguessed_letters(self.guesses)
                            self.game_over = True if self.input == self.answer else False
                            self.input = ""
                    elif event.key == pygame.K_SPACE:
                        self.reset_game()
                    elif len(self.input) < 5 and not self.game_over:
                        self.input += event.unicode.upper()

    def reset_game(self):
        self.answer = random.choice(self.dict_answers)
        self.guesses = []
        self.unguessed = ALPHABET
        self.input = ""
        self.game_over = False

if __name__ == "__main__":
    game = Main()
    game.run()
