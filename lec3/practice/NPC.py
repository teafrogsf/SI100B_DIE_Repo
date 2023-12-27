
# -*- coding:utf-8 -*-

from Settings import *
import pygame

# 设置 NPC
class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(GamePath.npc)
        self.image = pygame.transform.scale(self.image,
            (NPCSettings.npcWidth, NPCSettings.npcHeight))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.speed = NPCSettings.npcSpeed
        self.initialPosition = x
        self.direction = 1
        self.patrollingRange = NPCSettings.npcPatrollingRange

    def update(self):
        self.rect = self.rect.move(self.speed * self.direction, 0)
        if abs(self.rect.x - self.initialPosition) > self.patrollingRange:
            self.direction *= -1
            self.image = pygame.transform.flip(self.image, True, False)
    
    def reset_talk_CD(self):
        pass

    def can_talk(self):
        pass

