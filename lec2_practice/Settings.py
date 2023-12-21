# -*- coding:utf-8 -*-

from enum import Enum

class WindowSettings:
    name = "Thgink Luos Ton"
    width = 1280
    height = 720
    outdoorScale = 1.5 # A necessary scale to allow camera movement in outdoor scenes

class PlayerSettings:
    playerSpeed = 5
    playerWidth = 60
    playerHeight = 55

class SceneSettings:
    tileXnum = 48
    tileYnum = 27
    tileWidth = tileHeight = 40

class GamePath:
    player = r".\assets\player\1.png"

    groundTiles = [
        r".\assets\tiles\ground1.png", 
        r".\assets\tiles\ground2.png", 
        r".\assets\tiles\ground3.png", 
        r".\assets\tiles\ground4.png", 
        r".\assets\tiles\ground5.png", 
        r".\assets\tiles\ground6.png", 
    ]

    tree = r".\assets\tiles\tree.png"

class GameState(Enum):
    MAIN_MENU = 1
    GAME_LOADING = 2
    GAME_OVER = 3
    GAME_WIN = 4
    GAME_PAUSE = 5
    GAME_PLAY_WILD = 6