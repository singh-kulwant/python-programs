'''
Sanke Game File 1
Author : Kulwant Singh
Date : 27 Aug 2018
'''

import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint

WIDTH = 35
HEIGHT = 20

# sets the maximum x and y coordinate inside the game, so that snake doesnt hit the border
MAX_X = WIDTH - 2
MAX_Y = HEIGHT - 2
SNAKE_LENGTH = 5

SNAKE_X = SNAKE_LENGTH + 1
SNAKE_Y = 3

#this controls the speed of the game
TIMEOUT = 100

class Snake(object):
    def __init__(self):
        self.x = 'Hisss!'

    def method_a(self, foo):
        print (self.x + ' ' + foo)

snake = Snake()
snake.method_a('Says the snake!')

class Body(object):
    def __init__(self):
        self.x = "This is the"

    def method_a(self,foo):
        print(self.x+' '+foo)

body = Body().method_a('Body')

class Food(object):
    def __init__(self):
        self.y = "Yum, tasty! "

    def method_a(self,foo):
        print(self.y+' '+foo)

food = Food().method_a('Food')
    
