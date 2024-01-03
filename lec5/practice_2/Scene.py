import pygame
import Map
from random import randint

from enum import Enum
from Settings import *
from NPC import *
from Portal import *

class Scene():
    def __init__(self, window):
        pass

    def render(self):
        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                self.window.blit(self.map[i][j], 
                                 (SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))
                
        self.obstacles.draw(self.window)
        self.npcs.draw(self.window)
        self.portals.draw(self.window)
        
class CityScene(Scene):
    def __init__(self, window):
        super().__init__(window)

    def gen_CITY(self):
        pass


class WildScene(Scene):
    def __init__(self, window):
        super().__init__(window)

    def gen_WILD(self):
       pass