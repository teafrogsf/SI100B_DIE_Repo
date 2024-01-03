# -*- coding:utf-8 -*-

from Settings import *
import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(GamePath.portal)
        self.image = pygame.transform.scale(self.image,
                            (PortalSettings.portalWidth, 
                             PortalSettings.portalHeight))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
    
    def draw(self, window, dx=0, dy=0):
        window.blit(self.image, self.rect)
