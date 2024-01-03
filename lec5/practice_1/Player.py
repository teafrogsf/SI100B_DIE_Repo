# -*- coding:utf-8 -*-

from Settings import *
import pygame
import os

# 设置角色动画
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = [pygame.transform.scale(pygame.image.load(img), 
                            (PlayerSettings.playerWidth, PlayerSettings.playerHeight)) for img in GamePath.player]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = PlayerSettings.playerSpeed
        self.talking = False

        self.HP = PlayerSettings.playerHP
        self.attack = PlayerSettings.playerAttack
        self.defense = PlayerSettings.playerDefence

    def update(self, keys, scene):
        if self.talking:
            # 如果不移动，显示静态图像
            self.index = 0
            self.image = self.images[self.index]
        else:
            # Update Player Position
            dx = 0
            dy = 0
            if keys[pygame.K_w] and self.rect.top > 0 :
                dy -= self.speed
            if keys[pygame.K_s] and self.rect.bottom < WindowSettings.height:
                dy += self.speed
            if keys[pygame.K_a] and self.rect.left > 0:
                dx -= self.speed
            if keys[pygame.K_d] and self.rect.right < WindowSettings.width:
                dx += self.speed
                
            self.rect = self.rect.move(dx, dy)
            if pygame.sprite.spritecollide(self, scene.obstacles, False):
                # 遇到障碍物，取消移动
                self.rect = self.rect.move(-dx, -dy)

            # 更新角色动画
            if any(keys):
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]


    def draw(self, window):
        window.blit(self.image, self.rect)