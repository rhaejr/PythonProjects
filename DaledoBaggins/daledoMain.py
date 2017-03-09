import random, sys
import pygame
from pytmx.util_pygame import load_pygame
from map import Map
from character import Character
from test_gui import MainWindow, ImageWidget
from PyQt4 import QtGui



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
pygame.display.set_caption('The Legend of Daledo Baggins')
clock = pygame.time.Clock()

# Level and player character init
level = Map("Maps/0,0.tmx",gameDisplay,tile_size)
player = Character((3, 4),gameDisplay, tile_size, 'Maps/character_animations.tmx', level)




def game_loop():

    while True:

        # Event Handlers
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] != 0 or keys[pygame.K_d]:
            player.move_right()
            # right_pressed = True
        elif keys[pygame.K_LEFT] != 0 or keys[pygame.K_a]:
            player.move_left()
            # left_pressed = True
        elif keys[pygame.K_UP] != 0 or keys[pygame.K_w]:
            player.move_up()
            # up_pressed = True
        elif keys[pygame.K_DOWN] != 0 or keys[pygame.K_s]:
            player.move_down()
            # down_pressed = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    player.read_sign()
                    #     if event.key == pygame.K_RIGHT:
                    #
                    #         player.move_right()
                    #         # player.destination_x += 32
                    #         # player.x_speed = 1
                    #         right_pressed = True
                    #
                    #     if event.key == pygame.K_LEFT:
                    #         player.move_left()
                    #         left_pressed = True
                    #
                    #     if event.key == pygame.K_UP:
                    #         player.move_up()
                    #         up_pressed = True
                    #
                    #     if event.key == pygame.K_DOWN:
                    #         player.move_down()
                    #         down_pressed = True
                    #
                    # if event.type == pygame.KEYUP:
                    #     if event.key == pygame.K_RIGHT:
                    #         right_pressed = False
                    #
                    #     if event.key == pygame.K_LEFT:
                    #         left_pressed = False
                    #
                    #     if event.key == pygame.K_UP:
                    #         up_pressed = False
                    #
                    #     if event.key == pygame.K_DOWN:
                    #         down_pressed = False

        gameDisplay.fill(black)
        level.draw_map()
        player.draw()
        # arculius.draw()
        # level.draw_forground()
        # ai()

        pygame.display.update()
        clock.tick(20)

# pygame.mixer.init()
# pygame.mixer.music.load(sound)
# pygame.mixer.music.play()
# app=QtGui.QApplication(sys.argv)
# w=MainWindow(gameDisplay)
# w.show()
game_loop()

pygame.quit()
quit()
