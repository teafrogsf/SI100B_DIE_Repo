# -*- coding:utf-8 -*-
from Settings import *
import pygame
from random import random,randint

class Block(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.transform.scale(image, 
            (SceneSettings.tileWidth, SceneSettings.tileHeight))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


def gen_map():
    images = [pygame.image.load(tile) for tile in GamePath.groundTiles]
    images = [pygame.transform.scale(image, (SceneSettings.tileWidth, SceneSettings.tileHeight)) for image in images]

    mapObj = []
    for i in range(SceneSettings.tileXnum):
        tmp = []
        for j in range(SceneSettings.tileYnum):
            tmp.append(images[randint(0, len(images) - 1)])
        mapObj.append(tmp)
    
    return mapObj

def build_obstacles():

    image = pygame.image.load(GamePath.tree)
    obstacles = pygame.sprite.Group()

    midX = SceneSettings.tileXnum // 2
    midY = SceneSettings.tileYnum // 2

    for i in range(SceneSettings.tileXnum):
        for j in range(SceneSettings.tileYnum):
            if random() < SceneSettings.obstacleDensity and \
                ((i not in range(midX - 3, midX + 4))\
                or (j not in range(midY - 3, midY + 4)))\
                and (i > midX or j > midY):
                obstacles.add(Block(image, 
                    SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))
                
    return obstacles

