import pygame

import console


blue = (0, 0, 255)
red = (255, 0, 0)

console.display_title_screen()
pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()

pygame.display.set_caption('Snake game by Adam Bemski')
game_over = False
while game_over is False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pygame.draw.rect(dis, blue, [200, 150, 10, 10])
    pygame.display.update()

pygame.quit()
quit()
