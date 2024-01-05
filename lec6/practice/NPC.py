# -*- coding:utf-8 -*-

from Settings import *
import pygame

# 设置 NPC
class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(GamePath.npc)
        self.image = pygame.transform.scale(self.image, (NPCSettings.npcWidth, NPCSettings.npcHeight))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.initialPosition = x  # 记录初始位置
        self.speed = NPCSettings.npcSpeed
        self.direction = 1
        self.patrollingRange = 70  # 巡逻范围

        self.talking = False
        self.talkCD = 0 # cooldown of talk

    def update(self):
        if not self.talking:
            self.rect.x += self.speed * self.direction
            if abs(self.rect.x - self.initialPosition) > self.patrollingRange:
                self.direction *= -1  # 反转方向
                self.image = pygame.transform.flip(self.image, True, False)
            if self.talkCD > 0:
                self.talkCD -= 1
    
    def reset_talk_CD(self):
        self.talkCD = NPCSettings.talkCD 

    def can_talk(self):
        return self.talkCD == 0

