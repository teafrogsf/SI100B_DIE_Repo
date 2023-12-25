# -*- coding:utf-8 -*-

from Settings import *
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(GamePath.player)
        self.image = pygame.transform.scale(self.image, (PlayerSettings.playerWidth, PlayerSettings.playerHeight))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = PlayerSettings.playerSpeed

    def update(self, keys, scene):
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        elif keys[pygame.K_s] and self.rect.bottom < WindowSettings.height:
            self.rect.y += self.speed
        elif keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        elif keys[pygame.K_d] and self.rect.right < WindowSettings.width:
            self.rect.x += self.speed

    def fix_to_middle(self, dx, dy):
        self.rect.x -= dx
        self.rect.y -= dy
