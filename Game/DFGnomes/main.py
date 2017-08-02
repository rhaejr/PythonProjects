import random, sys
import pygame
from df_map import Map




# color variables
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# screen sizes
tile_size = 32
tiles = 18
display_width = (tile_size * tiles)
display_height = (tile_size * tiles)

# Init
pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('DF Gnomes')
clock = pygame.time.Clock()
game_map = Map()

init_pos = 0,0,0


def game_loop():
    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] != 0 or keys[pygame.K_d]:
        elif keys[pygame.K_LEFT] != 0 or keys[pygame.K_a]:
        elif keys[pygame.K_UP] != 0 or keys[pygame.K_w]:
        elif keys[pygame.K_DOWN] != 0 or keys[pygame.K_s]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    pygame.display.update()
    clock.tick(20)

def move(x,y,z):
    x_pos,y_pos, z_pos = init_pos

    print(game_map.map_tiles[x_pos + x][y_pos + y][z_pos + z])

game_loop()

pygame.quit()
quit()
