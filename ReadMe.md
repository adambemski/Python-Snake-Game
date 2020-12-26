#  Snake Game

- Snake Game implementation in Python 3.

Examples based on:
- [edureka](https://www.edureka.co/blog/snake-game-with-pygame/)

## Table of contents
* [Running app](#running-app)
* [Working principle](#working-principle)

## Running app

It is recommended to run this project over virtual environment. Run following commands in your terminal:
```powershell
python -m venv snake-game
cd ./snake-game
./Scripts/activate
mkdir code
cd ./code
# here clone this repository
pip install -r requirements.txt
python ./main.py
```

## Working principle

### Creating screen

To create screen use following pygame methods:
```python
import pygame

pygame.init()  # initialize pygame module

dis = pygame.display.set_mode((400, 300))  # set screen dimensions
pygame.display.update()  # apply changes in the game window
```

### Waiting for events

While loop can avoid instant closing of game window:
```python
game_over = False
while game_over is False:
    for event in pygame.event.get():
        print(event)  # prints out all the actions made on the screen
```
Here above console will print every event which will occur inside game window (like cursor movement or button press).

In order to close game window after clicking window cross button exchange body of while loop:
```python
game_over=False
while game_over is False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
```

### Create the sake

Snake here will created as rectangle - over use draw.rect() method.

Firstly define colours inside our game (in RGB schema).
```python
blue = (0, 0, 255)
red = (255, 0, 0)
```
In the next step inside while loop put call of draw.rect() and update() methods:
```python
while game_over is False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pygame.draw.rect(dis, blue, [200, 150, 10, 10])
    pygame.display.update()
```
