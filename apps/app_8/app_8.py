import pygame
from pygame import mixer
import sys, os
import math
import time
from dotenv import load_dotenv
from utils import map_coords, distance, play_sound
import colors as COLORS

load_dotenv()
# Initialize Pygame
pygame.init()
# Initialize the mixer
mixer.init()

# Get the current display height and width
infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h
# SCREEN_WIDTH = int(os.getenv('SCREEN_WIDTH'))
# SCREEN_HEIGHT = int(os.getenv('SCREEN_HEIGHT'))
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
PIXEL_TO_MM = 0.4478  # Adjust this variable as needed

def run(screen):
    running = True

    home_button_center = (150, 100)
    home_button_radius = 50

    clear_button_rect = pygame.Rect((SCREEN_SIZE[0] // 2 - 150, SCREEN_SIZE[1] - 150, 300, 70))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                mapped_x, mapped_y = map_coords(x, y)

                if distance((mapped_x, mapped_y), home_button_center) <= home_button_radius:
                    running = False
                    play_sound('audio/back.wav')

        screen.fill(COLORS.BLACK)
        # for line in permanent_lines:
        #     draw_line_with_measurement(screen, line[0], line[1])
        # if start_point:
        #     x, y = pygame.mouse.get_pos()
        #     mapped_x, mapped_y = map_coords(x, y)
        #     draw_line_with_measurement(screen, start_point, (mapped_x, mapped_y))
        # pygame.draw.circle(screen, COLORS.RED, home_button_center, home_button_radius)
        # font = pygame.font.Font(None, 36)
        # text_surface = font.render('Home', True, COLORS.WHITE)
        # screen.blit(text_surface, (home_button_center[0] - 30, home_button_center[1] - 20))
        # pygame.draw.rect(screen, COLORS.RED, clear_button_rect)
        # text_surface = font.render('Clear', True, COLORS.WHITE)
        # screen.blit(text_surface, (SCREEN_SIZE[0] // 2 - 30, SCREEN_SIZE[1] - 140))

        # Draw the Home button
        pygame.draw.circle(screen, COLORS.NAVY_BLUE, home_button_center, home_button_radius)
        pygame.draw.circle(screen, COLORS.LIGHT_BLUE, home_button_center, home_button_radius, 5)
        font = pygame.font.Font(None, 36)
        text_surface = font.render('Home', True, COLORS.WHITE)
        text_rect = text_surface.get_rect(center=home_button_center)
        screen.blit(text_surface, text_rect)

        pygame.display.flip()

if __name__ == '__main__':
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Weather App')
    run(screen)