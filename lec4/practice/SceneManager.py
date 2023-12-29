# -*- coding:utf-8 -*-

from Settings import *
import pygame
import Map
import NPC
import Monster
import DialogBox
import BattleBox

class SceneManager:
    def __init__(self, window):
        self.state = GameState.GAME_PLAY_WILD
        self.map = Map.gen_map()

        self.npcs = pygame.sprite.Group()
        self.npcs.add(NPC.NPC(WindowSettings.width // 4, WindowSettings.height // 4 + 80))

        
        self.obstacles = Map.build_obstacles()
        
        self.window = window

        self.monsters = pygame.sprite.Group()
        self.monsters.add(Monster.Monster(WindowSettings.width // 4, WindowSettings.height // 4 + 180))
        self.battleBox = None

    def get_width(self):
        return WindowSettings.width 

    def get_height(self):
        return WindowSettings.height
    
    def check_event_talking(self, player, keys):
        # check for all npcs
        for npc in self.npcs.sprites():
            # 结束对话
            if npc.talking and keys[pygame.K_RETURN]:
                npc.talking = False
                player.talking = False
                npc.reset_talk_CD()
            # 保持对话
            elif pygame.sprite.collide_rect(player, npc) and npc.can_talk():
                npc.talking = True
                player.talking = True
                dialogBoxTemp = DialogBox.DialogBox(self.window, GamePath.npc,
                    ["Happy","2023!"])
                dialogBoxTemp.render()

    def check_event_battle(self, player, keys):
        if self.battleBox is None:
            for monster in self.monsters.sprites():
                if pygame.sprite.collide_rect(player, monster):
                    self.battleBox = BattleBox.BattleBox(self.window, 
                                        player, monster)
                    self.battleBox.render()
        else:
            self.battleBox.render()


    def update(self):
        # update npc
        for each in self.npcs.sprites():
            each.update()

    def render(self):
        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                self.window.blit(self.map[i][j], 
                                 (SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))
        self.obstacles.draw(self.window)
        self.npcs.draw(self.window)
        self.monsters.draw(self.window)

    
