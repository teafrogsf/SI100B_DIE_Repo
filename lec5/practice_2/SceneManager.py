# -*- coding:utf-8 -*-

from Settings import *
import pygame
import Map
import NPC
import ShoppingBox
import Scene

class SceneManager:
    def __init__(self, window):
        self.state = GameState.GAME_PLAY_CITY
        self.scene = Scene.CityScene(window)
        self.window = window

    def get_width(self):
        return WindowSettings.width 

    def get_height(self):
        return WindowSettings.height
    
    def check_event_shopping(self, player, keys):
        pass

    def flush_scene(self):
        pass

    def update(self):
        # update npc
        for each in self.scene.npcs.sprites():
            each.update()

    def render(self):
        pass

    
