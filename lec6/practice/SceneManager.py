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
                if keys[pygame.K_w]:
                    self.scene.shoppingBox.selectedID = max(0, 
                        self.scene.shoppingBox.selectedID - 1)
                elif keys[pygame.K_s]:
                    self.scene.shoppingBox.selectedID = min(4, 
                        self.scene.shoppingBox.selectedID + 1)
                elif keys[pygame.K_RETURN]:
                    if self.scene.shoppingBox.selectedID == 4:
                        npc.talking = False
                        npc.reset_talk_CD()
                        player.talking = False
                        self.scene.shoppingBox = None
                    else:
                        self.scene.shoppingBox.buy() 
            if self.scene.shoppingBox:    
                self.scene.shoppingBox.render()
            elif pygame.sprite.collide_rect(npc, player) and npc.can_talk():
                npc.talking = True
                player.talking = True
                self.scene.shoppingBox = ShoppingBox.ShoppingBox(self.window, 
                    GamePath.npc, player, 
            {"Attack +1": "Coin -15", "Defence +1": "Coin -15",
             "HP +1": "Coin -15", "???": "HP -5", "Exit": ""})
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

    
