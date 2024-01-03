# -*- coding:utf-8 -*-

import pygame
from GameManager import GameManager

def main():
    pygame.init()
    manager = GameManager()

    while True:
        manager.update()
        manager.render()
        pygame.display.flip()

if __name__ == "__main__":
    main()