# -*- coding:utf-8 -*-

from Settings import *
import pygame
import Map
import DialogBox
import NPC

class SceneManager:
    def __init__(self, window):
        self.state = GameState.GAME_PLAY_WILD
        self.map = Map.gen_map()

        self.npcs = pygame.sprite.Group()
        self.npcs.add(NPC.NPC(WindowSettings.width // 4, WindowSettings.height // 4 + 80))

        self.obstacles = Map.build_obstacles()
        
        self.window = window

    def get_width(self):
        return WindowSettings.width 

    def get_height(self):
        return WindowSettings.height
    
    def check_event_talking(self, player, keys):
        for npc in self.npcs:
            if npc.talking and keys[pygame.K_RETURN]:
                npc.talking = False
                player.talking = False
                npc.reset_talk_CD()
            elif npc.can_talk() and pygame.sprite.collide_rect(npc, player):
                npc.talking = True
                player.talking = True

    def update(self):
        for npc in self.npcs:
            npc.update()

    def render(self):
        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                self.window.blit(self.map[i][j], 
                    (SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))
        self.obstacles.draw(self.window)
        self.npcs.draw(self.window)

    
