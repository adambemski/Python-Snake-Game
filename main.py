import time

import pygame

import conf
import console


def message(msg, color, font_type, dis_width, dis_height):
    shown_text = font_type.render(msg, True, color)
    dis.blit(shown_text, [dis_width/4, dis_height/2])


console.display_title_screen()
pygame.init()
font_style = pygame.font.SysFont(None, 50)  # can be set after initialized pygame module

dis = pygame.display.set_mode((conf.display_horizontal_size_x, conf.display_vertical_size_y))
pygame.display.update()

pygame.display.set_caption('Snake game by Adam Bemski')

x1 = conf.x1
y1 = conf.y1

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

game_over = False
while game_over is False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0

    if x1 >= conf.display_horizontal_size_x or x1 < 0 \
            or y1 >= conf.display_vertical_size_y or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(conf.black)  # allow change background
    pygame.draw.rect(dis, conf.blue, [x1, y1, conf.snake_size, conf.snake_size])
    pygame.display.update()
    clock.tick(conf.game_speed)

message("Game Over", conf.red, font_style, conf.display_horizontal_size_x, conf.display_vertical_size_y)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()
