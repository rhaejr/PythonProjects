import random
import pygame
from pytmx.util_pygame import load_pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, pos, gameDisplay, tile_size, animations, level):
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
        self.rect.x = pos[0] * tile_size
        self.rect.y = pos[1] * tile_size
        self.x = pos[0]
        self.y = pos[1]

        self.pos = pos
        self.destination_x = self.rect.x
        self.destination_y = self.rect.y
        self.x_speed = 0
        self.y_speed = 0

        self.is_moving = False
        self.dist = 0
        self.facing = (0, 0)
        self.gameDisplay = gameDisplay
        self.tile_size = tile_size
        self.animation_file = animations
        self.animations = load_pygame(self.animation_file)
        self.level = level

    def draw(self):
        self.move()
        self.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        x = 0
        y = 0
        if self.destination_x != self.rect.x or self.destination_y != self.rect.y:

            self.rect.x += self.x_speed
            self.rect.y += self.y_speed
            self.is_moving = True

            if self.destination_x != self.rect.x:
                self.dist = abs(self.rect.x - self.destination_x)
            if self.destination_y != self.rect.y:
                self.dist = abs(self.rect.y - self.destination_y)

            if self.x_speed < 0:
                y = 1
            elif self.x_speed > 0:
                y = 3
            elif self.y_speed > 0:
                y = 2
            elif self.y_speed < 0:
                y = 0

            if self.dist == 30:
                x = 1
            elif self.dist == 26 or self.dist == 28:
                x = 2
            elif self.dist == 22 or self.dist == 24:
                x = 3
            elif self.dist == 18 or self.dist == 20:
                x = 4
            elif self.dist == 14 or self.dist == 16:
                x = 5
            elif self.dist == 10 or self.dist == 12:
                x = 6
            elif self.dist == 6 or self.dist == 8:
                x = 7
            elif self.dist == 2 or self.dist == 4:
                x = 8

            print(self.dist)

            self.image = self.animate(x, y, 0)

        else:
            self.x_speed = 0
            self.y_speed = 0
            self.x = int(self.destination_x / self.tile_size)
            self.y = int(self.destination_y / self.tile_size)
            self.is_moving = False

    def check_adjacent(self, x, y):
        # if (self.rect.x + x, self.rect.y + y) in level.events:
        for obj in self.level.events:
            if (self.x + x, self.y + y) == obj:
                self.exit_level(x, y)
                return False
        for sign in self.level.signs:
            if (self.x + x, self.y + y) == sign:
                # read_sign(x, y)
                return False
        if (self.x + x, self.y + y) in self.level.collisions:
            return False

        return True
        # self.move(x, y)

    def move_down(self):
        if not self.is_moving:
            self.image = self.animate(0, 2, 0)
            self.facing = (0, 1)
            # if self.rect.y < tiles - 1:
            if self.check_adjacent(0, 1):
                # self.move(0, 1)
                self.destination_y += 32
                self.y_speed = 2

    def move_up(self):
        if not self.is_moving:
            self.image = self.animate(0, 0, 0)
            self.facing = (0, -1)
            if self.check_adjacent(0, -1):
                # self.move(0, -1)
                self.destination_y += -32
                self.y_speed = -2

    def move_left(self):
        if not self.is_moving:
            self.image = self.animate(0, 1, 0)
            self.facing = (-1, 0)
            if self.check_adjacent(-1, 0):
                # self.move(-1, 0)
                self.destination_x += -32
                self.x_speed = -2

    def move_right(self):
        if not self.is_moving:
            self.image = self.animate(0, 3, 0)
            self.facing = (1, 0)
            if self.check_adjacent(1, 0):
                self.destination_x += 32
                self.x_speed = 2

    def animate(self, x, y, layer):
        animation = self.animations.get_tile_image(x, y, layer)
        animation = pygame.transform.smoothscale(animation, (self.tile_size, self.tile_size))
        return animation

    def read_sign(self):
        x = self.facing[0]
        y = self.facing[1]
        for obj in self.level.data.objects:
            if obj.name is not None:
                if (int(obj.x / self.tile_size), int(obj.y / self.tile_size)) == (self.x + x, self.y + y):
                    print(obj.properties['line1'])
                    print(obj.properties['line2'])

    def exit_level(self, x, y):
        for obj in self.level.data.objects:
            if obj.name != None:
                if ((int(obj.x / self.tile_size), int(obj.y / self.tile_size))) == (self.x + x, self.y + y):
                    transition = (obj.properties['transition'],
                                  (int(obj.properties['transition_startx']), int(obj.properties['transition_starty'])))
                    self.level.__init__(transition[0], self.gameDisplay, self.tile_size)
                    self.__init__(transition[1], self.gameDisplay, self.tile_size, self.animation_file, self.level)