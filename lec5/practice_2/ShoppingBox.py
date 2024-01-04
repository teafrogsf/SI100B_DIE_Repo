# -*- coding:utf-8 -*-

from typing import *
from Settings import DialogSettings, ShopSettings, GamePath
import pygame

class ShoppingBox:
    def __init__(self, window, npcPath, player, items,
                 fontSize: int = DialogSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255), 
                 bgColor: Tuple[int, int, int, int] = (0, 0, 0, 150)):
        self.window = window
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.font = pygame.font.Font(None, self.fontSize)\
        
        self.bg = pygame.Surface((ShopSettings.boxWidth, 
                                  ShopSettings.boxHeight),pygame.SRCALPHA)
        self.bg.fill(bgColor)

        self.npc = pygame.image.load(npcPath)
        self.npc = pygame.transform.scale(self.npc,
                (DialogSettings.npcWidth, DialogSettings.npcHeight))
        
        self.player = player
        self.items = items

        self.selectedID = 0


    def buy(self):
        pass
        

    def render(self):
        self.window.blit(self.bg, 
            (ShopSettings.boxStartX, ShopSettings.boxStartY))
        self.window.blit(self.npc,
            (DialogSettings.npcCoordX, DialogSettings.npcCoordY))
        
        offset = 0
        texts = ["Coins: " + str(self.player.money),
                 "HP: " + str(self.player.HP),
                 "Attack: " + str(self.player.attack),
                 "Defence: " + str(self.player.defence)]
        
        for text in texts:
            self.window.blit(self.font.render(text, True, self.fontColor),
                (ShopSettings.textStartX, ShopSettings.textStartY + offset))
            offset += DialogSettings.textVerticalDist