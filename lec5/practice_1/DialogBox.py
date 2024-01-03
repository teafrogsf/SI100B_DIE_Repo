# -*- coding:utf-8 -*-

from typing import *
from Settings import DialogSettings, GamePath
import pygame

class DialogBox:
    def __init__(self, window, npcPath: str, texts: list, 
                 fontSize: int = DialogSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255), 
                 bgColor: Tuple[int, int, int, int] = (0, 0, 0, 
                                    DialogSettings.boxAlpha)):
        self.window = window
        self.texts = texts

        self.fontSize = fontSize
        self.fontColor = fontColor
        self.font = pygame.font.Font(None, self.fontSize)

        self.bg = pygame.Surface((DialogSettings.boxWidth,
            DialogSettings.boxHeight), pygame.SRCALPHA)
        self.bg.fill(bgColor)

        self.npc = pygame.image.load(npcPath)
        self.npc = pygame.transform.scale(self.npc, (DialogSettings.npcWidth,
                                    DialogSettings.npcHeight))
    
    def render(self):
        self.window.blit(self.bg, (DialogSettings.boxStartX,
            DialogSettings.boxStartY))
        self.window.blit(self.npc, (DialogSettings.npcCoordX,
            DialogSettings.npcCoordY))
        
        offset = 0
        for text in self.texts:
            self.window.blit(self.font.render(text,
                True, self.fontColor),
                (DialogSettings.textStartX, DialogSettings.textStartY + offset))
            offset += DialogSettings.textVerticalDist
        
