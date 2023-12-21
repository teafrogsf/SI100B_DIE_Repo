# -*- coding:utf-8 -*-

from Settings import *
import pygame
import Map

class SceneManager:
    def __init__(self, window):
        self.state = GameState.GAME_PLAY_WILD
        self.map = Map.gen_map()
        
        self.window = window
        self.clock = pygame.time.Clock()
        self.cameraX = 0
        self.cameraY = 0
        self.obstacle = Map.build_obstacle()

    def tick(self, fps):
        pass
    
    def get_width(self):
        return WindowSettings.width * WindowSettings.outdoorScale

    def get_height(self):
        return WindowSettings.height * WindowSettings.outdoorScale

    def update_camera(self, player):
        pass

    def render(self):
        pass
