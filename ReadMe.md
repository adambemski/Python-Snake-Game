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

dis=pygame.display.set_mode((400, 300))  # set screen dimensions
pygame.display.update()  # apply changes in the game window
```

### Waiting for events

