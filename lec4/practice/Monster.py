# -*- coding:utf-8 -*-

from Settings import *
import pygame

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
