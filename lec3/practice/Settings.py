
# -*- coding:utf-8 -*-

from enum import Enum

class WindowSettings:
    name = "Thgink Luos"
    width = 1280
    height = 720
    outdoorScale = 1.5 # A necessary scale to allow camera movement in outdoor scenes

class PlayerSettings:
    playerSpeed = 5
    playerWidth = 60
    playerHeight = 55

class NPCSettings:
    npcSpeed = 1
    npcWidth = 60
    npcHeight = 60
    npcPatrollingRange = 70
    npcTalkCD = 30           # 1s

class SceneSettings:
    tileXnum = 36
    tileYnum = 18
    tileWidth = tileHeight = 40
    obstacleDensity = 0.1

class DialogSettings:
    boxWidth = 800
    boxHeight = 180
    boxStartX = WindowSettings.width // 4           # Coordinate X of the box
    boxStartY = WindowSettings.height // 3 * 2 + 20 # Coordinate Y of the box

    textSize = 48 # Default font size
    textStartX = WindowSettings.width // 4 + 10         # Coordinate X of the first line of dialog
    textStartY = WindowSettings.height // 3 * 2 + 30    # Coordinate Y of the first line of dialog
    textVerticalDist = textSize // 4 * 3                # Vertical distance of two lines

    alpha = 150

    npcWidth = WindowSettings.width // 5
    npcHeight = WindowSettings.height // 3
    npcCoordX = 0
    npcCoordY = WindowSettings.height * 2 // 3 - 20

class GamePath:
    # player/npc related path
    npc = r".\assets\npc\npc.png"
    player = [
        r".\assets\player\1.png", 
        r".\assets\player\2.png", 
        r".\assets\player\3.png", 
        r".\assets\player\4.png", 
    ]

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