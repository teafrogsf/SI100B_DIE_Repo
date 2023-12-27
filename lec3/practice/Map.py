# -*- coding:utf-8 -*-
from Settings import *
import pygame
from random import random,randint

class Block(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()


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
    pass    

