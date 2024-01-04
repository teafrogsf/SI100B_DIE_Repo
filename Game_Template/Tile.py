# -*- coding:utf-8 -*-

import pygame

from Settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0, width=SceneSettings.tileWidth, height=SceneSettings.tileHeight):
        super().__init__()
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, window, dx=0, dy=0):
        rect = self.rect
        rect = rect.move(dx, dy)
        window.blit(self.image, rect)
