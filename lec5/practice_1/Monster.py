# -*- coding:utf-8 -*-

from Settings import *
import pygame

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(GamePath.monster)
        self.image = pygame.transform.scale(self.image, 
        (MonsterSettings.monsterWidth, MonsterSettings.monsterHeight))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.HP = MonsterSettings.monsterHP
        self.attack = MonsterSettings.monsterAttack
        self.defense = MonsterSettings.monsterDefense
