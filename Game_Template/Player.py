# -*- coding:utf-8 -*-

import pygame

from Settings import *
from Attributes import *

class Player(pygame.sprite.Sprite, Collidable):
    def __init__(self, x, y):
        # Must initialize everything one by one here
        pygame.sprite.Sprite.__init__(self)
        Collidable.__init__(self)

        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def attr_update(self, addCoins = 0, addHP = 0, addAttack = 0, addDefence = 0):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def reset_pos(self, x=WindowSettings.width // 2, y=WindowSettings.height // 2):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def try_move(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update(self, width,height):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####


    def draw(self, window, dx=0, dy=0):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
