# -*- coding:utf-8 -*-

from typing import *
from Settings import BattleSettings, GamePath
import pygame

class BattleBox:
    def __init__(self, window, player, monster, fontSize: int = BattleSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255), 
                 bgColor: Tuple[int, int, int, int] = (0, 0, 0, BattleSettings.boxAlpha)):
        # 初始化窗口和字体
        self.window = window

        self.fontSize = fontSize
        self.fontColor = fontColor
        self.font = pygame.font.Font(None, self.fontSize)

        self.bg = pygame.Surface((BattleSettings.boxWidth,
            BattleSettings.boxHeight), pygame.SRCALPHA)
        self.bg.fill(bgColor)
    
        # 初始化相关角色的参数，没有实际操作的权力
        self.player = player
        self.playerHP = player.HP
        self.playerImg = pygame.transform.scale(player.image, 
            (BattleSettings.playerWidth, BattleSettings.playerHeight))
        
        self.playerX = BattleSettings.playerCoordX
        self.playerY = BattleSettings.playerCoordY

        self.monster = monster
        self.monsterHP = monster.HP
        self.monsterImg = pygame.transform.scale(monster.image, 
            (BattleSettings.monsterWidth, BattleSettings.monsterHeight))
        
        self.monsterX = BattleSettings.monsterCoordX
        self.monsterY = BattleSettings.monsterCoordY

        # 默认玩家先手

        self.attacker = 0

        # 区分放动画状态和攻击结算状态

        self.isPlayingAnimation = True
        self.currentAnimationCount = 0

        # 移动方向

        self.dir = 1

        # 是否结束

        self.isFinished = False

    def get_result(self):
        if self.attacker == 0:
            self.attacker = 1
            self.dir = -1
        else:
            self.attacker = 0
            self.dir = 1

        self.isPlayingAnimation = True

    def render(self):
        # 绘制背景和文字
        
        self.window.blit(self.bg, (BattleSettings.boxStartX,
                                   BattleSettings.boxStartY))
        self.window.blit(self.playerImg, (self.playerX,
                                          self.playerY))
        self.window.blit(self.monsterImg, (self.monsterX,
                                           self.monsterY))
        
        text = "player HP: " + str(self.playerHP)
        self.window.blit(self.font.render(text, True, self.fontColor),
        (BattleSettings.textPlayerStartX, BattleSettings.textStartY))

        text = "monster HP: " + str(self.monsterHP)
        self.window.blit(self.font.render(text, True, self.fontColor),
        (BattleSettings.textMonsterStartX, BattleSettings.textStartY))

        # 绘制战斗过程

        if self.isPlayingAnimation:
            if self.currentAnimationCount < BattleSettings.animationCount:
                currentDir = self.dir
            else:
                currentDir = self.dir * -1

            if self.attacker == 0:
                self.playerX += currentDir * BattleSettings.stepSpeed
            else:
                self.monsterX += currentDir * BattleSettings.stepSpeed

            self.currentAnimationCount += 1

            if self.currentAnimationCount == BattleSettings.animationCount * 2:
                self.isPlayingAnimation = False
                self.currentAnimationCount = 0

        # 战斗判定以及结算
                
        else:
            self.get_result()

        # 战斗结束
        
