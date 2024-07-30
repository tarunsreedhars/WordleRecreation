import pygame
from config import (
    GREY,
    GREEN,
    YELLOW,
    WIDTH,
    HEIGHT,
    T_MARGIN,
    LR_MARGIN,
    SQ_SIZE,
    MARGIN,
    B_MARGIN,
)
from wordle import determine_color
from pygame.font import Font
from pygame.surface import Surface
from typing import Any, List, Union


def setup_screen(width: int, height: int) -> Surface:
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Wordle...")
    return screen


def draw_background(screen: Surface, unguessed: str, font_small: Font):
    screen.fill("white")
    letters = font_small.render(unguessed, False, GREY)
    surface = letters.get_rect(center=(WIDTH // 2, T_MARGIN // 2))
    screen.blit(letters, surface)


def draw_guesses(screen: Surface, guesses: List[Union[Any, str]], input_text: str, answer: str, font: Font):
    y = T_MARGIN
    for i in range(6):
        x = LR_MARGIN
        for j in range(5):
            square = pygame.Rect(x, y, SQ_SIZE, SQ_SIZE)
            pygame.draw.rect(screen, GREY, square, width=2, border_radius=10)
            if i < len(guesses):
                color = determine_color(guesses[i], j, answer)
                pygame.draw.rect(screen, color, square)
                letter = font.render(guesses[i][j], False, (255, 255, 255))
                surface = letter.get_rect(center=(x + SQ_SIZE // 2, y + SQ_SIZE // 2))
                screen.blit(letter, surface)
            if i == len(guesses) and j < len(input_text):
                letter = font.render(input_text[j], False, GREY)
                surface = letter.get_rect(center=(x + SQ_SIZE // 2, y + SQ_SIZE // 2))
                screen.blit(letter, surface)
            x += SQ_SIZE + MARGIN
        y += SQ_SIZE + MARGIN
    if len(guesses) == 6 and guesses[5] != answer:
        letters = font.render(answer, False, GREY)
        surface = letters.get_rect(center=(WIDTH // 2, HEIGHT - B_MARGIN // 2 - MARGIN))
        screen.blit(letters, surface)
