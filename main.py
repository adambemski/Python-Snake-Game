import random
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


def game_session():
    x1 = conf.x1
    y1 = conf.y1

    x1_change = 0
    y1_change = 0

    clock = pygame.time.Clock()

    food_x = round(random.randrange(0, conf.display_horizontal_size_x - conf.snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, conf.display_vertical_size_y - conf.snake_size) / 10.0) * 10.0

    game_over = False
    game_quit = False

    while game_over is False:
        while game_quit is True:
            dis.fill(conf.black)
            message("Game Over - Press q for quit or c for replay", conf.red, font_style,
                    conf.display_horizontal_size_x,
                    conf.display_vertical_size_y)
            pygame.display.update()
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        print('The End...')
                        game_over = True
                        game_quit = False
                    if event.key == pygame.K_c:
                        print('New game!')
                        game_session()  # recursive call of entire game

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
            game_quit = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(conf.black)  # allow change background
        pygame.draw.rect(dis, conf.red, [food_x, food_y, conf.snake_size, conf.snake_size])
        pygame.draw.rect(dis, conf.blue, [x1, y1, conf.snake_size, conf.snake_size])
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            print("Food eaten!")

        clock.tick(conf.game_speed)

    pygame.quit()
    quit()


if __name__ == "__main__":
    game_session()
