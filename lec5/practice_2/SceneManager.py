# -*- coding:utf-8 -*-

from Settings import *
import pygame
import Map
import NPC
import ShoppingBox
import Scene

class SceneManager:
    def __init__(self, window):
        self.scene = Scene.CityScene(window)
        self.window = window

    
    def check_event_shopping(self, player, keys):
        for npc in self.scene.npcs.sprites():
            if npc.talking:
                self.scene.shoppingBox.render()
            if pygame.sprite.collide_rect(npc, player) and npc.can_talk():
                npc.talking = True
                player.talking = True
                self.scene.shoppingBox = ShoppingBox.ShoppingBox(self.window, 
                    GamePath.npc, player, {"A": "+15"})
                self.scene.shoppingBox.render()
            

    def flush_scene(self):
        if self.scene.type == SceneType.CITY:
            self.scene = Scene.WildScene(self.window)
        elif self.scene.type == SceneType.WILD:
            self.scene = Scene.CityScene(self.window)

    def update(self):
        # update npc
        for each in self.scene.npcs.sprites():
            each.update()

    def render(self):
        self.scene.render()

    
