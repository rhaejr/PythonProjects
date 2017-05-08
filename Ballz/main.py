import random, sys
import pygame



# color variables
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

background = black
# screen sizes
tile_size = 64
ball_space = 32
gap = 4
block_size = tile_size - (gap * 2)
tiles_h = 7
tiles_v = 8
display_width = (tile_size * tiles_h)
display_height = (tile_size * tiles_v) + ball_space
blocks = []

# Init
pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Ballz')
clock = pygame.time.Clock()



class Block:
    def __init__(self, x, y ,color, hits=1):
        self.x = x
        self.y = y
        self.w = block_size
        self.h = block_size
        self.color = color
        self.hits = hits

    def draw(self):
        if self.hits <= 0:
            self.destroy()
        pygame.draw.rect(gameDisplay, self.color, [self.x, self.y, self.w, self.h])

    def destroy(self):
        self.color = background

class Ball:
    def __init__(self, x, y ,color):
        self.x = x
        self.y = y
        self.w = block_size
        self.h = block_size
        self.color = color

def block_placer():
    global blocks
    for i in range(tiles_v):
        l = []
        for j in range(tiles_h):
            if i != 0 and i != tiles_v - 1:
                block = Block(tile_size*j+gap, tile_size*i+gap, white)
                l.append(block)
        blocks.append(l)
def draw_blocks():
    for i in blocks:
        for block in i:
            block.draw()
block_placer()




def game_loop():
    while True:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('space')


        gameDisplay.fill(black)
        draw_blocks()

        pygame.display.update()
        clock.tick(20)
game_loop()

pygame.quit()
quit()
