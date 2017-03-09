import random

import pygame
import pytmx
from pytmx.util_pygame import load_pygame

# color variables
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# screen sizes
tile_size = 32
tiles = 16
display_width = (tile_size * tiles)
display_height = (tile_size * tiles)

# Init
pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('2D Game')
clock = pygame.time.Clock()

tiled_map = load_pygame('Maps/test.tmx')

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, is_barrier, image):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = image
        # self.image = pygame.transform.smoothscale(self.image, (tile_size, tile_size))
        # self.image = pygame.Surface([tile_size, tile_size])
        # self.image.fill(green)
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.is_barrier = is_barrier


class Character(pygame.sprite.Sprite):
    def __init__(self, pos):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load('lpc_barbarian.png')
        self.image = pygame.transform.smoothscale(self.image, (tile_size, tile_size))
        # self.image = pygame.Surface([tile_size, tile_size])
        # self.image.fill(black)
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

    def draw(self):
        gameDisplay.blit(self.image, (self.rect.x, self.rect.y))



    def move(self, x, y):
        pos = (self.rect.x, self.rect.y)
        # self.rect.x, self.rect.y = world[int(self.rect.x/tile_size) + x][int(self.rect.y/tile_size) + y].rect.x, world[int(self.rect.x/tile_size) + x][int(self.rect.y/tile_size) + y].rect.y
        for i in range(len(world)):
            for j in range(len(world[i])):
                if pos == (world[i][j].rect.x, world[i][j].rect.y):
                    if world[i][j].is_barrier == False:
                        try:
                            self.rect.x = world[i + x][j + y].rect.x
                            self.rect.y = world[i + x][j + y].rect.y
                        except IndexError:
                            self.rect.x, self.rect.y = pos


    def move_down(self):
        self.move(0, 1)

    def move_up(self):
        if self.rect.y != 0:
            self.move(0, -1)

    def move_left(self):
        if self.rect.x != 0:
            self.move(-1, 0)

    def move_right(self):
        self.move(1, 0)


def mapper():
    m = [[0 for x in range(tiles)] for x in range(tiles)]
    for layer in tiled_map.layers:
        for x, y, image in layer.tiles():
            # gameDisplay.blit(image, (x*tile_size, y*tile_size))
            m[x][y] = Tile((x * tile_size, y * tile_size), False,image)
        return m



def draw_map():
    for i in range(len(world)):
        for j in range(len(world[i])):
            gameDisplay.blit(world[i][j].image, (world[i][j].rect.x, world[i][j].rect.y))


world = mapper()
# print(world)

player = Character((world[1][1].rect.x, world[1][1].rect.y))


def game_loop():
    while True:
        # Event Handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.move_right()

                if event.key == pygame.K_LEFT:
                    player.move_left()

                if event.key == pygame.K_UP:
                    player.move_up()

                if event.key == pygame.K_DOWN:
                    player.move_down()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if world.rect.collidepoint(pygame.mouse.get_pos()):
            #         print(pygame.mouse.get_pos())

        gameDisplay.fill(white)
        # mapper()
        draw_map()
        player.draw()

        pygame.display.update()
        clock.tick(30)


game_loop()

pygame.quit()
quit()
