# -*- coding:utf-8 -*-

from Settings import *
import pygame

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
        self.defence = PlayerSettings.playerDefence
        
        self.money = PlayerSettings.playerMoney

    def attr_update(self, addCoins = 0, addHP = 0, addAttack = 0, addDefence = 0):
        if self.money + addCoins < 0:
            return
        if self.HP + addHP < 0:
            return
        self.money += addCoins
        self.HP += addHP
        self.attack += addAttack
        self.defence += addDefence


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

            # 传送事件
            if pygame.sprite.spritecollide(self, scene.portals, 
                                    False, pygame.sprite.collide_mask):
                pygame.event.post(pygame.event.Event(GameEvent.EVENT_SWITCH))

            # 更新角色动画
            if any(keys):
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]


    def draw(self, window):
        window.blit(self.image, self.rect)