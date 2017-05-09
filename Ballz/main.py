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
rects = []

# Init
pygame.init()
font = pygame.font.SysFont('Ariel', 16)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Ballz')
clock = pygame.time.Clock()
image = pygame.image.load('Ball1.png')



class Block():
    def __init__(self, rect,color, hits=1):

        self.rect = rect
        self.w = block_size
        self.h = block_size
        self.color = color
        self.hits = hits
        self.t_color = red



    def draw(self):
        if self.hits <= 0:
            self.destroy()
        pygame.draw.rect(gameDisplay, self.color, self.rect)
        text = font.render(str(self.hits), True, self.t_color)
        w = int(text.get_rect().width / 2)
        h = int(text.get_rect().height / 2)
        gameDisplay.blit(text, (self.rect.x + (block_size / 2) - w, self.rect.y +(block_size / 2) - h))

    def destroy(self):
        self.color = background
        self.t_color = background

# class Ball(pygame.Rect):
#     def __init__(self, color, x, y, speed=0):
#         super().__init__()
#         self.x = x
#         self.y = y
#         self.w = block_size
#         self.h = block_size
#         self.color = color
#         self.speed = speed
#
#     # pygame.draw.circle(Surface, color, pos, radius, width=0)
#     def draw(self):
#         self.y += self.speed
#         pygame.draw.circle(gameDisplay, self.color, (self.x, self.y), 10)

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, display):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        # self.image = pygame.transform.smoothscale(self.image, (tile_size, tile_size))
        # self.image = pygame.Surface([tile_size, tile_size])
        # self.image.fill(black)
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = speed
        self.y_speed = speed
        self.display = display

    def draw(self):
        self.move()
        self.display.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        if self.rect.y < 0 or self.rect.y + 11 > display_height:
            self.y_speed = -self.y_speed
        if self.rect.x < 0 or self.rect.x + 11 > display_width:
            self.x_speed = -self.x_speed
        self.rect.y += self.y_speed
        self.rect.x += self.x_speed

def block_placer():
    global blocks
    for i in range(tiles_v):
        l = []
        for j in range(tiles_h):
            if i != 0 and i != tiles_v - 1:
                rect = pygame.Rect(tile_size*j+gap, tile_size*i+gap,block_size,block_size)
                h = random.choice([0,1,3,5])
                block = Block(rect, white, hits=h)
                l.append(block)
        blocks.append(l)
def draw_blocks(b):
    for i in blocks:
        for block in i:
            if block.rect.colliderect(b):
                if block.hits > 0:
                    block.hits -= 1
                    collision_side(b, block)
            block.draw()

def collision_side(ball, block):
    up = ball.rect.y
    down = ball.rect.y + 12
    left = ball.rect.x
    right = ball.rect.x + 12

    if block.rect.collidepoint(ball.rect.x - (ball.x_speed *3),up) or  block.rect.collidepoint(ball.rect.x - (ball.x_speed *3),down):
        ball.y_speed = -ball.y_speed
    elif block.rect.collidepoint(left,ball.rect.y - (ball.y_speed *3)) or block.rect.collidepoint(right,ball.rect.y - (ball.y_speed *3)):
        ball.x_speed = -ball.x_speed
    else:
        ball.y_speed = -ball.y_speed
        ball.x_speed = -ball.x_speed
block_placer()
# ball = Ball(red, int(display_width / 2), int(display_height - 15))

ball = Ball(int(display_width / 2), int(display_height - 15), 0, gameDisplay)



def game_loop():
    while True:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball.x_speed = -10
                    ball.y_speed = -2
                    print('space')

        gameDisplay.fill(black)
        draw_blocks(ball)
        ball.draw()
        pygame.display.update()
        clock.tick(60)
game_loop()

pygame.quit()
quit()
