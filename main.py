import pygame

import console


black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

console.display_title_screen()
pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()

pygame.display.set_caption('Snake game by Adam Bemski')

x1 = 200
y1 = 200

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

    x1 += x1_change
    y1 += y1_change
    dis.fill(black)  # can be used to change background
    pygame.draw.rect(dis, blue, [x1, y1, 10, 10])
    pygame.display.update()
    clock.tick(30)


pygame.quit()
quit()
