
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
    playerHP = 20
    playerAttack = 5
    playerDefence = 1
    playerMoney = 0

class NPCSettings:
    npcSpeed = 1
    npcWidth = 60
    npcHeight = 60
    talkCD = 30           # 1s

class MonsterSettings:
    monsterWidth = 60
    monsterHeight = 60
    monsterHP = 10
    monsterAttack = 3
    monsterDefense = 1


class SceneSettings:
    tileXnum = 36
    tileYnum = 18
    tileWidth = tileHeight = 40
    obstacleDensity = 0.1

class DialogSettings:
    boxWidth = 800
    boxHeight = 180
    boxAlpha = 150
    boxStartX = WindowSettings.width // 4           # Coordinate X of the box
    boxStartY = WindowSettings.height // 3 * 2 + 20 # Coordinate Y of the box

    textSize = 48 # Default font size
    textStartX = WindowSettings.width // 4 + 10         # Coordinate X of the first line of dialog
    textStartY = WindowSettings.height // 3 * 2 + 30    # Coordinate Y of the first line of dialog
    textVerticalDist = textSize // 4 * 3                # Vertical distance of two lines

    npcWidth = WindowSettings.width // 5
    npcHeight = WindowSettings.height // 3
    npcCoordX = 0
    npcCoordY = WindowSettings.height * 2 // 3 - 20

class BattleSettings:
    boxWidth = WindowSettings.width * 3 // 4 
    boxHeight = WindowSettings.height * 3 // 4 
    boxAlpha = 200
    boxStartX = WindowSettings.width // 8           # Coordinate X of the box
    boxStartY = WindowSettings.height // 8
    textSize = 48 # Default font size
    textStartX = WindowSettings.width // 4 
    textPlayerStartX = WindowSettings.width // 4          # Coordinate X of the first line of dialog
    textMonsterStartX = WindowSettings.width // 2 +100   
    textStartY = WindowSettings.height // 3         # Coordinate Y of the first line of dialog
    textVerticalDist = textSize // 4 * 3            # Vertical distance of two lines

    playerWidth = WindowSettings.width // 6
    playerHeight = WindowSettings.height // 3
    playerCoordX = WindowSettings.width // 8
    playerCoordY = WindowSettings.height // 2

    monsterWidth = WindowSettings.width // 6
    monsterHeight = WindowSettings.height // 3
    monsterCoordX = WindowSettings.width * 5 // 8
    monsterCoordY = WindowSettings.height // 2 

    
    animationCount = 15

    stepSpeed = 20

class GamePath:
    # player/npc related path
    player = [
        r".\assets\player\1.png", 
        r".\assets\player\2.png", 
        r".\assets\player\3.png", 
        r".\assets\player\4.png", 
    ]
    npc = r".\assets\npc\npc.png"
    monster = r".\assets\npc\monster\1.png"

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