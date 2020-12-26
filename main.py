import pygame

import console


console.display_title_screen()
pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()

pygame.display.set_caption('Snake game by Adam Bemski')
game_over = False
while game_over is False:
    for event in pygame.event.get():
        print(event)  # prints out all the actions made on the screen

pygame.quit()
quit()
