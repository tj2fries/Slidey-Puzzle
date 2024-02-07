import pygame
import math
import random
pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption('Breadventure')
floorTileImg = pygame.image.load('Floor Tile.png')
brickBlockImg = pygame.image.load('Brick Block.png')
breadArtImg = pygame.transform.scale((pygame.image.load('Bread Art.png')), (320, 320))
pygame.display.set_icon(breadArtImg)
font = pygame.font.Font('freesansbold.ttf', 20)
bigFont = pygame.font.Font('freesansbold.ttf', 50)
startScreenText = ['In the distant Kingdom of',
                   'Ryerule, the dark lord',
                   'Moldemort has cast a curse',
                   'placing the kingdom into an',
                   'eternal night. It is up to you,',
                   'Sir Bread of Breadington to',
                   'find Moldemort in his lair and',
                   'slay the fiend. Be on your',
                   'guard! For many adventurers',
                   'have become eternally lost in',
                   'his maze-like lair. It is of the upmost importance that you',
                   'prevail, for if you do not, the Kingdom of Ryerule is doomed!']
breadFrontIdleImg = pygame.transform.scale(pygame.image.load('Bread Front Idle.png'), (80, 80))
breadFrontWalk1Img = pygame.transform.scale(pygame.image.load('Bread Front Walk 1.png'), (80, 80))
breadFrontWalk2Img = pygame.transform.scale(pygame.image.load('Bread Front Walk 2.png'), (80, 80))
breadBackIdleImg = pygame.transform.scale(pygame.image.load('Bread Back Idle.png'), (80, 80))
breadBackWalk1Img = pygame.transform.scale(pygame.image.load('Bread Back Walk 1.png'), (80, 80))
breadBackWalk2Img = pygame.transform.scale(pygame.image.load('Bread Back Walk 2.png'), (80, 80))
breadBackSlash1Img = pygame.transform.scale(pygame.image.load('Bread Back Slash 1.png'), (80, 80))
breadBackSlash2Img = pygame.transform.scale(pygame.image.load('Bread Back Slash 2.png'), (80, 80))
breadBackSlash3Img = pygame.transform.scale(pygame.image.load('Bread Back Slash 3.png'), (80, 80))
breadBackSlash4Img = pygame.transform.scale(pygame.image.load('Bread Back Slash 4.png'), (80, 80))
breadFrontSlash1Img = pygame.transform.scale(pygame.image.load('Bread Front Slash 1.png'), (80, 80))
breadFrontSlash2Img = pygame.transform.scale(pygame.image.load('Bread Front Slash 2.png'), (80, 80))
breadFrontSlash3Img = pygame.transform.scale(pygame.image.load('Bread Front Slash 3.png'), (80, 80))
breadFrontSlash4Img = pygame.transform.scale(pygame.image.load('Bread Front Slash 4.png'), (80, 80))
breadRightIdleImg = pygame.transform.scale(pygame.image.load('Bread Right Idle.png'), (80, 80))
breadRightWalk1Img = pygame.transform.scale(pygame.image.load('Bread Right Walk 1.png'), (80, 80))
breadRightWalk2Img = pygame.transform.scale(pygame.image.load('Bread Right Walk 2.png'), (80, 80))
breadRightSlash1Img = pygame.transform.scale(pygame.image.load('Bread Right Slash 1.png'), (80, 80))
breadRightSlash2Img = pygame.transform.scale(pygame.image.load('Bread Right Slash 2.png'), (80, 80))
breadRightSlash3Img = pygame.transform.scale(pygame.image.load('Bread Right Slash 3.png'), (80, 80))
breadRightSlash4Img = pygame.transform.scale(pygame.image.load('Bread Right Slash 4.png'), (80, 80))
breadLeftIdleImg = pygame.transform.scale(pygame.image.load('Bread Left Idle.png'), (80, 80))
breadLeftWalk1Img = pygame.transform.scale(pygame.image.load('Bread Left Walk 1.png'), (80, 80))
breadLeftWalk2Img = pygame.transform.scale(pygame.image.load('Bread Left Walk 2.png'), (80, 80))
breadLeftSlash1Img = pygame.transform.scale(pygame.image.load('Bread Left Slash 1.png'), (80, 80))
breadLeftSlash2Img = pygame.transform.scale(pygame.image.load('Bread Left Slash 2.png'), (80, 80))
breadLeftSlash3Img = pygame.transform.scale(pygame.image.load('Bread Left Slash 3.png'), (80, 80))
breadLeftSlash4Img = pygame.transform.scale(pygame.image.load('Bread Left Slash 4.png'), (80, 80))
deadBreadImg = pygame.transform.scale(pygame.image.load('Dead Bread.png'), (80, 80))
breadImgs = [breadFrontIdleImg, breadFrontSlash1Img, breadFrontSlash2Img, breadFrontSlash3Img, breadFrontSlash4Img,
             breadFrontWalk1Img, breadFrontWalk2Img, breadBackIdleImg, breadBackSlash1Img, breadBackSlash2Img,
             breadBackSlash3Img, breadBackSlash4Img, breadBackWalk1Img, breadBackWalk2Img, breadRightIdleImg,
             breadRightSlash1Img, breadRightSlash2Img, breadRightSlash3Img, breadRightSlash4Img, breadRightWalk1Img,
             breadRightWalk2Img, breadLeftIdleImg, breadLeftSlash1Img, breadLeftSlash2Img, breadLeftSlash3Img,
             breadLeftSlash4Img, breadLeftWalk1Img, breadLeftWalk2Img, deadBreadImg]
startButtonImg = pygame.image.load('Start Button.png')
startButtonHoverImg = pygame.image.load('Start Button Hover.png')
tutorialButtonImg = pygame.image.load('Tutorial Button.png')
tutorialButtonHoverImg = pygame.image.load('Tutorial Button Hover.png')
greyDoorImg = pygame.image.load('Grey Door.png')
redDoorImg = pygame.image.load('Red Door.png')
goldDoorImg = pygame.image.load('Gold Door.png')
greyKeyImg = pygame.image.load('Grey Key.png')
redKeyImg = pygame.image.load('Red Key.png')
goldKeyImg = pygame.image.load('Gold Key.png')
arrowImg = pygame.image.load('arrow.png')
pauseScreenImg = pygame.image.load('Pause Screen.png')
startScreenButtonImg = pygame.transform.scale(pygame.image.load('Start Screen Button.png'), (252, 90))
startScreenButtonHoverImg = pygame.transform.scale(pygame.image.load('Start Screen Button Hover.png'), (252, 90))
continueButtonImg = pygame.transform.scale(pygame.image.load('Continue Button.png'), (252, 90))
continueButtonHoverImg = pygame.transform.scale(pygame.image.load('Continue Button Hover.png'), (252, 90))
fadeOutScreenImg = pygame.image.load('Fade Out Screen.png')
enemyDeathAnimation1Img = pygame.image.load('Enemy Death Animation.png')
enemyDeathAnimation2Img = pygame.transform.scale(pygame.image.load('Enemy Death Animation.png'), (60, 60))
enemyDeathAnimation2Img.set_alpha(225)
enemyDeathAnimation3Img = pygame.transform.scale(pygame.image.load('Enemy Death Animation.png'), (80, 80))
enemyDeathAnimation3Img.set_alpha(195)
enemyDeathAnimation4Img = pygame.transform.scale(pygame.image.load('Enemy Death Animation.png'), (100, 100))
enemyDeathAnimation4Img.set_alpha(135)
enemyDeathAnimation5Img = pygame.transform.scale(pygame.image.load('Enemy Death Animation.png'), (120, 120))
enemyDeathAnimation5Img.set_alpha(105)
enemyDeathAnimation6Img = pygame.transform.scale(pygame.image.load('Enemy Death Animation.png'), (140, 140))
enemyDeathAnimation6Img.set_alpha(75)
enemyDeathAnimation7Img = pygame.transform.scale(pygame.image.load('Enemy Death Animation.png'), (160, 160))
enemyDeathAnimation7Img.set_alpha(45)
enemyDeathAnimation8Img = pygame.transform.scale(pygame.image.load('Enemy Death Animation.png'), (180, 180))
enemyDeathAnimation8Img.set_alpha(15)
goblinFront1Img = pygame.transform.scale(pygame.image.load('Goblin Front 1.png'), (80, 80))
goblinFront2Img = pygame.transform.scale(pygame.image.load('Goblin Front 2.png'), (80, 80))
goblinBack1Img = pygame.transform.scale(pygame.image.load('Goblin Back 1.png'), (80, 80))
goblinBack2Img = pygame.transform.scale(pygame.image.load('Goblin Back 2.png'), (80, 80))
goblinRight1Img = pygame.transform.scale(pygame.image.load('Goblin Right 1.png'), (80, 80))
goblinRight2Img = pygame.transform.scale(pygame.image.load('Goblin Right 2.png'), (80, 80))
goblinLeft1Img = pygame.transform.scale(pygame.image.load('Goblin Left 1.png'), (80, 80))
goblinLeft2Img = pygame.transform.scale(pygame.image.load('Goblin Left 2.png'), (80, 80))
goblinImgs = [goblinFront1Img, goblinFront2Img, goblinBack1Img, goblinBack2Img, goblinRight1Img, goblinRight2Img,
              goblinLeft1Img, goblinLeft2Img, enemyDeathAnimation1Img, enemyDeathAnimation2Img, enemyDeathAnimation3Img,
              enemyDeathAnimation4Img, enemyDeathAnimation5Img, enemyDeathAnimation6Img, enemyDeathAnimation7Img,
              enemyDeathAnimation8Img]
heartImg = pygame.image.load('heart.png')
spider1Img = pygame.image.load('Spider 1.png')
spider2Img = pygame.image.load('Spider 2.png')
spider3Img = pygame.image.load('Spider 3.png')
spiderImgs = [spider1Img, spider2Img, spider3Img, enemyDeathAnimation1Img, enemyDeathAnimation2Img,
              enemyDeathAnimation3Img, enemyDeathAnimation4Img, enemyDeathAnimation5Img, enemyDeathAnimation6Img,
              enemyDeathAnimation7Img, enemyDeathAnimation8Img]
ghost1Img = pygame.transform.scale(pygame.image.load('Ghost 1.png'), (80, 80))
ghost2Img = pygame.transform.scale(pygame.image.load('Ghost 2.png'), (80, 80))
ghost3Img = pygame.transform.scale(pygame.image.load('Ghost 3.png'), (80, 80))
ghostAttack1Img = pygame.transform.scale(pygame.image.load('Ghost Attack 1.png'), (80, 80))
ghostAttack2Img = pygame.transform.scale(pygame.image.load('Ghost Attack 2.png'), (80, 80))
ghostImgs = [ghost1Img, ghost2Img, ghost3Img, ghost2Img, ghostAttack1Img, ghostAttack2Img, enemyDeathAnimation1Img,
             enemyDeathAnimation2Img, enemyDeathAnimation3Img, enemyDeathAnimation4Img, enemyDeathAnimation5Img,
             enemyDeathAnimation6Img, enemyDeathAnimation7Img, enemyDeathAnimation8Img]
movingRight = False
movingLeft = False
movingUp = False
movingDown = False
attacking = False
started = False
paused = False
gameOver = False
speed = 5
breadCostume = 0
goblinCostume = 0
mouseX = 0
mouseY = 0
hitWall = False
placerX = 0
placerY = 0
floorX = 0
floorY = 0
roomMove = False
graphCode = []
locksLeft = 0
layerOffset = 0
greyKeyInventory = 0
redKeyInventory = 0
goldKeyInventory = 0
pauseTransparency = 0
fadeTransparency = 0
fadeOut = False
dungeonX = 0
dungeonY = 0
wrongWay = False
checker = 0
redKeyPlaced = False
blockedRoutes = 0
greyDoorCount = 0
greyKeyCount = 0
isRedDoor = False
inTutorial = False
bossRoom = False


class Bread:
    def __init__(self):
        self.x = 280
        self.y = 280
        self.attackAnimation = 0
        self.walkAnimation = 0
        self.diagonal = False
        self.hold = False
        self.hp = 5
        self.HT = 24
        self.HB = 28
        self.HRL = 18
        self.VR = 34
        self.VL = 32
        self.VTB = 11

    def move(self):
        global breadCostume
        if movingRight and movingLeft:
            self.hold = True
        if movingUp and movingDown:
            self.hold = True
        if not self.hold:
            if movingRight and movingUp:
                self.x += speed * (math.sqrt(2) / 2)
                self.y -= speed * (math.sqrt(2) / 2)
                self.diagonal = True
            elif movingRight and movingDown:
                self.x += speed * (math.sqrt(2) / 2)
                self.y += speed * (math.sqrt(2) / 2)
                self.diagonal = True
            elif movingLeft and movingUp:
                self.x -= speed * (math.sqrt(2) / 2)
                self.y -= speed * (math.sqrt(2) / 2)
                self.diagonal = True
            elif movingLeft and movingDown:
                self.x -= speed * (math.sqrt(2) / 2)
                self.y += speed * (math.sqrt(2) / 2)
                self.diagonal = True
        if not self.diagonal:
            if movingRight:
                self.x += speed
            if movingLeft:
                self.x -= speed
            if movingUp:
                self.y -= speed
            if movingDown:
                self.y += speed
        if not hitWall:
            if movingUp and not movingDown:
                if breadCostume == 14 or breadCostume == 21:
                    breadCostume = 13
                if self.walkAnimation < 2:
                    self.walkAnimation += 1
                else:
                    self.walkAnimation = 0
                    if breadCostume == 13:
                        breadCostume = 12
                    else:
                        breadCostume = 13
            elif movingDown and not movingUp:
                if breadCostume == 14 or breadCostume == 21:
                    breadCostume = 6
                if self.walkAnimation < 2:
                    self.walkAnimation += 1
                else:
                    self.walkAnimation = 0
                    if breadCostume == 6:
                        breadCostume = 5
                    else:
                        breadCostume = 6
            elif movingRight and not movingLeft:
                if self.walkAnimation < 2:
                    self.walkAnimation += 1
                else:
                    self.walkAnimation = 0
                    if breadCostume == 20:
                        breadCostume = 19
                    else:
                        breadCostume = 20
            elif movingLeft and not movingRight:
                if self.walkAnimation < 2:
                    self.walkAnimation += 1
                else:
                    self.walkAnimation = 0
                    if breadCostume == 27:
                        breadCostume = 26
                    else:
                        breadCostume = 27
            elif movingUp and movingDown and movingRight and movingLeft:
                if 4 < breadCostume < 7:
                    breadCostume = 0
                elif 11 < breadCostume < 14:
                    breadCostume = 7
                elif 18 < breadCostume < 21:
                    breadCostume = 14
                elif 25 < breadCostume < 28:
                    breadCostume = 21
            elif movingUp and movingDown:
                if 4 < breadCostume < 7:
                    breadCostume = 0
                elif 11 < breadCostume < 14:
                    breadCostume = 7
            elif movingRight and movingLeft:
                if 18 < breadCostume < 21:
                    breadCostume = 14
                elif 25 < breadCostume < 28:
                    breadCostume = 21
        self.diagonal = False
        self.hold = False

    def attack(self):
        global breadCostume
        global attacking
        breadCostume += 1
        if self.attackAnimation < 4:
            self.attackAnimation += 1
        else:
            attacking = False
            breadCostume -= 5


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def bump(self):
        global hitWall
        global breadCostume
        if (bread.y + 62 > self.y > bread.y + 52 and bread.x - 38 < self.x < bread.x + 78) and \
                (not movingRight and not movingLeft or movingRight and movingLeft) and movingDown:
            bread.y = self.y - 62
            hitWall = True
            if 4 < breadCostume < 7:
                breadCostume = 0
            elif 11 < breadCostume < 14:
                breadCostume = 7
            elif 18 < breadCostume < 21:
                breadCostume = 14
            elif 25 < breadCostume < 28:
                breadCostume = 21
        else:
            hitWall = False
            if bread.y + 62 > self.y > bread.y + 56 and bread.x - 38 < self.x < bread.x + 78 and movingLeft and not \
                    movingRight and movingDown:
                bread.y = self.y - 62
                bread.x -= speed - (speed * (math.sqrt(2) / 2))
            elif bread.y + 62 > self.y > bread.y + 56 and bread.x - 38 < self.x < bread.x + 78 and movingRight and not \
                    movingLeft and movingDown:
                bread.y = self.y - 62
                bread.x += speed - (speed * (math.sqrt(2) / 2))
            elif bread.y + 85 > self.y > bread.y + 55 and bread.x - 12 < self.x < bread.x + 60 and movingLeft and not \
                    movingRight and not movingDown and not movingUp:
                bread.y = self.y - 85
                bread.x -= speed - (speed * (math.sqrt(2) / 2))
            elif bread.y + 69 > self.y > bread.y + 39 and bread.x - 12 < self.x < bread.x + 60 and movingRight and not \
                    movingLeft and not movingDown and not movingUp:
                bread.y = self.y - 69
                bread.x += speed - (speed * (math.sqrt(2) / 2))
        if (bread.y - 16 < self.y < bread.y - 6 and bread.x - 38 < self.x < bread.x + 78) and \
                (not movingRight and not movingLeft or movingRight and movingLeft) and movingUp:
            bread.y = self.y + 16
            hitWall = True
            if 4 < breadCostume < 7:
                breadCostume = 0
            elif 11 < breadCostume < 14:
                breadCostume = 7
            elif 18 < breadCostume < 21:
                breadCostume = 14
            elif 25 < breadCostume < 28:
                breadCostume = 21
        else:
            hitWall = False
            if bread.y - 16 < self.y < bread.y - 6 and bread.x - 38 < self.x < bread.x + 78 and movingLeft and not \
                    movingRight and movingUp:
                bread.y = self.y + 16
                bread.x -= speed - (speed * (math.sqrt(2) / 2))
            elif bread.y - 16 < self.y < bread.y - 6 and bread.x - 38 < self.x < bread.x + 78 and movingRight and not \
                    movingLeft and movingUp:
                bread.y = self.y + 16
                bread.x += speed - (speed * (math.sqrt(2) / 2))
            elif bread.y - 29 < self.y < bread.y + 1 and bread.x - 12 < self.x < bread.x + 50 and movingLeft and not \
                    movingRight and not movingDown and not movingUp:
                bread.y = self.y + 29
                bread.x -= speed - (speed * (math.sqrt(2) / 2))
            elif bread.y - 45 < self.y < bread.y - 15 and bread.x - 12 < self.x < bread.x + 50 and movingRight and not \
                    movingLeft and not movingDown and not movingUp:
                bread.y = self.y + 45
                bread.x += speed - (speed * (math.sqrt(2) / 2))
        if (bread.x + 60 > self.x > bread.x + 54 and bread.y + 67 > self.y > bread.y - 44) and \
                (not movingUp and not movingDown or movingUp and movingDown) and movingRight:
            bread.x = self.x - 60
            hitWall = True
            if 4 < breadCostume < 7:
                breadCostume = 0
            elif 11 < breadCostume < 14:
                breadCostume = 7
            elif 18 < breadCostume < 21:
                breadCostume = 14
            elif 25 < breadCostume < 28:
                breadCostume = 21
        else:
            hitWall = False
            if bread.x + 82 > self.x > bread.x + 48 and bread.y + 59 > self.y > bread.y - 16 and movingUp and not \
                    movingDown and movingRight:
                bread.x = self.x - 82
                bread.y -= speed - (speed * (math.sqrt(2) / 2))
            elif bread.x + 82 > self.x > bread.x + 48 and bread.y + 59 > self.y > bread.y - 16 and movingDown and not \
                    movingUp and movingRight:
                bread.x = self.x - 82
                bread.y += speed - (speed * (math.sqrt(2) / 2))
            elif bread.x + 82 > self.x > bread.x + 48 and bread.y + 59 > self.y > bread.y - 16 and movingUp and not \
                    movingDown and not movingRight:
                bread.x = self.x - 82
            elif bread.x + 82 > self.x > bread.x + 48 and bread.y + 59 > self.y > bread.y - 16 and movingDown and not \
                    movingUp and not movingRight:
                bread.x = self.x - 82
        if (bread.x - 22 < self.x < bread.x - 16 and bread.y + 83 > self.y > bread.y - 29) and \
                (not movingUp and not movingDown or movingUp and movingDown) and movingLeft:
            bread.x = self.x + 22
            hitWall = True
            if 4 < breadCostume < 7:
                breadCostume = 0
            elif 11 < breadCostume < 14:
                breadCostume = 7
            elif 18 < breadCostume < 21:
                breadCostume = 14
            elif 25 < breadCostume < 28:
                breadCostume = 21
        else:
            hitWall = False
            if bread.x - 42 < self.x < bread.x - 8 and bread.y + 59 > self.y > bread.y - 16 and movingUp and not \
                    movingDown and movingLeft:
                bread.x = self.x + 42
                bread.y -= speed - (speed * (math.sqrt(2) / 2))
            elif bread.x - 42 < self.x < bread.x - 8 and bread.y + 59 > self.y > bread.y - 16 and movingDown and not \
                    movingUp and movingLeft:
                bread.x = self.x + 42
                bread.y += speed - (speed * (math.sqrt(2) / 2))
            elif bread.x - 42 < self.x < bread.x - 8 and bread.y + 59 > self.y > bread.y - 16 and movingUp and not \
                    movingDown and not movingLeft:
                bread.x = self.x + 42
            elif bread.x - 42 < self.x < bread.x - 8 and bread.y + 59 > self.y > bread.y - 16 and movingDown and not \
                    movingUp and not movingLeft:
                bread.x = self.x + 42


class Floor:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class DoorHorizontal:
    def __init__(self, x, y):
        global i
        self.x = x
        self.y = y
        self.roomUp = False
        self.roomDown = False
        self.roomRight = False
        self.roomLeft = False
        self.newRoomAnimation = 0
        self.remove = []
        for i in range(len(walls)):
            if walls[i].x + 40 == self.x or walls[i].x == self.x:
                if walls[i].y + 40 == self.y or walls[i].y == self.y:
                    self.remove.append(walls[i])
        for i in range(len(self.remove)):
            for x in range(len(walls) - 4):
                if self.remove[i] == walls[x]:
                    walls.remove(walls[x])

    def open(self):
        global i
        global roomMove
        if not self.roomDown and ((self.x - 40 < bread.x + 40 < self.x + 40 and self.y < bread.y + 24 < self.y + 6) or
                                  self.roomUp):
            self.roomUp = True
            roomMove = True
            if self.newRoomAnimation < 10:
                bread.y += 58
                for i in range(len(walls)):
                    walls[i].y += 64
                for i in range(len(floors)):
                    floors[i].y += 64
                for i in range(len(horizontalDoors)):
                    horizontalDoors[i].y += 64
                for i in range(len(verticalDoors)):
                    verticalDoors[i].y += 64
                for i in range(len(locks)):
                    locks[i].y += 64
                for i in range(len(keys)):
                    keys[i].y += 64
                for i in range(len(tutorialTextBoxes)):
                    tutorialTextBoxes[i].y += 64
                for i in range(len(tutorialArrows)):
                    tutorialArrows[i].y += 64
                for i in range(len(goblins)):
                    goblins[i].y += 64
                for i in range(len(spiders)):
                    spiders[i].y += 64
                self.newRoomAnimation += 1
            else:
                roomMove = False
                self.roomUp = False
        elif not self.roomUp and ((self.x - 40 < bread.x + 40 < self.x + 40 and self.y - 6 < bread.y + 62 < self.y) or
                                  self.roomDown):
            self.roomDown = True
            roomMove = True
            if self.newRoomAnimation < 10:
                bread.y -= 58
                for i in range(len(walls)):
                    walls[i].y -= 64
                for i in range(len(floors)):
                    floors[i].y -= 64
                for i in range(len(horizontalDoors)):
                    horizontalDoors[i].y -= 64
                for i in range(len(verticalDoors)):
                    verticalDoors[i].y -= 64
                for i in range(len(locks)):
                    locks[i].y -= 64
                for i in range(len(keys)):
                    keys[i].y -= 64
                for i in range(len(tutorialTextBoxes)):
                    tutorialTextBoxes[i].y -= 64
                for i in range(len(tutorialArrows)):
                    tutorialArrows[i].y -= 64
                for i in range(len(goblins)):
                    goblins[i].y -= 64
                for i in range(len(spiders)):
                    spiders[i].y -= 64
                self.newRoomAnimation += 1
            else:
                roomMove = False
                self.roomDown = False
        else:
            self.newRoomAnimation = 0


class DoorVertical:
    def __init__(self, x, y):
        global i
        self.x = x
        self.y = y
        self.roomUp = False
        self.roomDown = False
        self.roomRight = False
        self.roomLeft = False
        self.newRoomAnimationV = 0
        self.remove = []
        for i in range(len(walls)):
            if walls[i].x + 40 == self.x or walls[i].x == self.x:
                if walls[i].y + 40 == self.y or walls[i].y == self.y:
                    self.remove.append(walls[i])
        for i in range(len(self.remove)):
            for x in range(len(walls) - 4):
                if self.remove[i] == walls[x]:
                    walls.remove(walls[x])

    def open(self):
        global i
        global roomMove
        if not self.roomLeft and ((self.y - 40 < bread.y + 40 < self.y + 40 and self.x - 6 < bread.x + 60 < self.x) or
                                  self.roomRight):
            self.roomRight = True
            roomMove = True
            if self.newRoomAnimationV < 10:
                bread.x -= 58
                for i in range(len(walls)):
                    walls[i].x -= 64
                for i in range(len(floors)):
                    floors[i].x -= 64
                for i in range(len(horizontalDoors)):
                    horizontalDoors[i].x -= 64
                for i in range(len(verticalDoors)):
                    verticalDoors[i].x -= 64
                for i in range(len(locks)):
                    locks[i].x -= 64
                for i in range(len(keys)):
                    keys[i].x -= 64
                for i in range(len(tutorialTextBoxes)):
                    tutorialTextBoxes[i].x -= 64
                for i in range(len(tutorialArrows)):
                    tutorialArrows[i].x -= 64
                for i in range(len(goblins)):
                    goblins[i].x -= 64
                for i in range(len(spiders)):
                    spiders[i].x -= 64
                self.newRoomAnimationV += 1
            else:
                roomMove = False
                self.roomRight = False
        elif not self.roomRight and ((self.y - 40 < bread.y + 40 < self.y + 40 and self.x < bread.x + 18 < self.x + 6)
                                     or self.roomLeft):
            self.roomLeft = True
            roomMove = True
            if self.newRoomAnimationV < 10:
                bread.x += 58
                for i in range(len(walls)):
                    walls[i].x += 64
                for i in range(len(floors)):
                    floors[i].x += 64
                for i in range(len(horizontalDoors)):
                    horizontalDoors[i].x += 64
                for i in range(len(verticalDoors)):
                    verticalDoors[i].x += 64
                for i in range(len(locks)):
                    locks[i].x += 64
                for i in range(len(keys)):
                    keys[i].x += 64
                for i in range(len(tutorialTextBoxes)):
                    tutorialTextBoxes[i].x += 64
                for i in range(len(tutorialArrows)):
                    tutorialArrows[i].x += 64
                for i in range(len(goblins)):
                    goblins[i].x += 64
                for i in range(len(spiders)):
                    spiders[i].x += 64
                self.newRoomAnimationV += 1
            else:
                roomMove = False
                self.roomLeft = False
        else:
            self.newRoomAnimationV = 0


class LockTop:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

    def unlock(self):
        global greyKeyInventory
        global goldKeyInventory
        if self.x - 10 < bread.x < self.x + 10 and self.y + 16 == bread.y:
            if self.colour == 'grey':
                if greyKeyInventory > 0:
                    greyKeyInventory -= 1
                    locks.remove(self)
            elif self.colour == 'red':
                if redKeyInventory > 0:
                    locks.remove(self)
            else:
                if goldKeyInventory > 0:
                    goldKeyInventory -= 1
                    locks.remove(self)

    def bump(self):
        global hitWall
        global breadCostume
        if (bread.y - 16 < self.y < bread.y - 10 and bread.x - 78 < self.x < bread.x + 78) and \
                (not movingRight and not movingLeft or movingRight and movingLeft) and movingUp:
            bread.y = self.y + 16
            hitWall = True
            if 4 < breadCostume < 7:
                breadCostume = 0
            elif 11 < breadCostume < 14:
                breadCostume = 7
            elif 18 < breadCostume < 21:
                breadCostume = 14
            elif 25 < breadCostume < 28:
                breadCostume = 21
        else:
            hitWall = False
            if bread.y - 16 < self.y < bread.y - 10 and bread.x - 78 < self.x < bread.x + 78 and movingLeft and not \
                    movingRight and movingUp:
                bread.y = self.y + 16
                bread.x -= speed - (speed * (math.sqrt(2) / 2))
            elif bread.y - 16 < self.y < bread.y - 10 and bread.x - 78 < self.x < bread.x + 78 and movingRight and not \
                    movingLeft and movingUp:
                bread.y = self.y + 16
                bread.x += speed - (speed * (math.sqrt(2) / 2))
            elif bread.y - 29 < self.y < bread.y + 1 and bread.x - 78 < self.x < bread.x + 78 and movingLeft and not \
                    movingRight and not movingDown and not movingUp:
                bread.y = self.y + 29
                bread.x -= speed - (speed * (math.sqrt(2) / 2))
            elif bread.y - 45 < self.y < bread.y - 15 and bread.x - 78 < self.x < bread.x + 78 and movingRight and not \
                    movingLeft and not movingDown and not movingUp:
                bread.y = self.y + 45
                bread.x += speed - (speed * (math.sqrt(2) / 2))


class LockBottom:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

    def unlock(self):
        global greyKeyInventory
        global goldKeyInventory
        if self.x + 30 < bread.x + 40 < self.x + 50 and self.y - 62 == bread.y:
            if self.colour == 'grey':
                if greyKeyInventory > 0:
                    greyKeyInventory -= 1
                    locks.remove(self)
            elif self.colour == 'red':
                if redKeyInventory > 0:
                    locks.remove(self)
            else:
                if goldKeyInventory > 0:
                    goldKeyInventory -= 1
                    locks.remove(self)

    def bump(self):
        global hitWall
        global breadCostume
        if (bread.y + 62 > self.y > bread.y + 56 and bread.x - 78 < self.x < bread.x + 78) and \
                (not movingRight and not movingLeft or movingRight and movingLeft) and movingDown:
            bread.y = self.y - 62
            hitWall = True
            if 4 < breadCostume < 7:
                breadCostume = 0
            elif 11 < breadCostume < 14:
                breadCostume = 7
            elif 18 < breadCostume < 21:
                breadCostume = 14
            elif 25 < breadCostume < 28:
                breadCostume = 21
        else:
            hitWall = False
            if bread.y + 62 > self.y > bread.y + 56 and bread.x - 78 < self.x < bread.x + 78 and movingLeft and not \
                    movingRight and movingDown:
                bread.y = self.y - 62
                bread.x -= speed - (speed * (math.sqrt(2) / 2))
            elif bread.y + 62 > self.y > bread.y + 56 and bread.x - 78 < self.x < bread.x + 78 and movingRight and not \
                    movingLeft and movingDown:
                bread.y = self.y - 62
                bread.x += speed - (speed * (math.sqrt(2) / 2))
            elif bread.y + 85 > self.y > bread.y + 55 and bread.x - 78 < self.x < bread.x + 78 and movingLeft and not \
                    movingRight and not movingDown and not movingUp:
                bread.y = self.y - 85
                bread.x -= speed - (speed * (math.sqrt(2) / 2))
            elif bread.y + 69 > self.y > bread.y + 39 and bread.x - 78 < self.x < bread.x + 78 and movingRight and not \
                    movingLeft and not movingDown and not movingUp:
                bread.y = self.y - 69
                bread.x += speed - (speed * (math.sqrt(2) / 2))


class LockRight:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

    def unlock(self):
        global greyKeyInventory
        global goldKeyInventory
        if self.y + 30 < bread.y + 40 < self.y + 50 and self.x - 60 == bread.x:
            if self.colour == 'grey':
                if greyKeyInventory > 0:
                    greyKeyInventory -= 1
                    locks.remove(self)
            elif self.colour == 'red':
                if redKeyInventory > 0:
                    locks.remove(self)
            else:
                if goldKeyInventory > 0:
                    goldKeyInventory -= 1
                    locks.remove(self)

    def bump(self):
        global hitWall
        global breadCostume
        if (bread.x + 60 > self.x > bread.x + 54 and bread.y + 67 > self.y > bread.y - 84) and \
                (not movingUp and not movingDown or movingUp and movingDown) and movingRight:
            bread.x = self.x - 60
            hitWall = True
            if 4 < breadCostume < 7:
                breadCostume = 0
            elif 11 < breadCostume < 14:
                breadCostume = 7
            elif 18 < breadCostume < 21:
                breadCostume = 14
            elif 25 < breadCostume < 28:
                breadCostume = 21
        else:
            hitWall = False
            if bread.x + 82 > self.x > bread.x + 48 and bread.y + 59 > self.y > bread.y - 56 and movingUp and not \
                    movingDown:
                bread.x = self.x - 82
                bread.y -= speed - (speed * (math.sqrt(2) / 2))
            elif bread.x + 82 > self.x > bread.x + 48 and bread.y + 59 > self.y > bread.y - 56 and movingDown and not \
                    movingUp:
                bread.x = self.x - 82
                bread.y += speed - (speed * (math.sqrt(2) / 2))


class LockLeft:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

    def unlock(self):
        global greyKeyInventory
        global goldKeyInventory
        if self.y + 30 < bread.y + 40 < self.y + 50 and self.x + 22 == bread.x:
            if self.colour == 'grey':
                if greyKeyInventory > 0:
                    greyKeyInventory -= 1
                    locks.remove(self)
            elif self.colour == 'red':
                if redKeyInventory > 0:
                    locks.remove(self)
            else:
                if goldKeyInventory > 0:
                    goldKeyInventory -= 1
                    locks.remove(self)

    def bump(self):
        global hitWall
        global breadCostume
        if (bread.x - 22 < self.x < bread.x - 16 and bread.y + 83 > self.y > bread.y - 69) and \
                (not movingUp and not movingDown or movingUp and movingDown) and movingLeft:
            bread.x = self.x + 22
            hitWall = True
            if 4 < breadCostume < 7:
                breadCostume = 0
            elif 11 < breadCostume < 14:
                breadCostume = 7
            elif 18 < breadCostume < 21:
                breadCostume = 14
            elif 25 < breadCostume < 28:
                breadCostume = 21
        else:
            hitWall = False
            if bread.x - 42 < self.x < bread.x - 16 and bread.y + 59 > self.y > bread.y - 56 and movingUp and not \
                    movingDown:
                bread.x = self.x + 42
                bread.y -= speed - (speed * (math.sqrt(2) / 2))
            elif bread.x - 42 < self.x < bread.x - 16 and bread.y + 59 > self.y > bread.y - 56 and movingDown and not \
                    movingUp:
                bread.x = self.x + 42
                bread.y += speed - (speed * (math.sqrt(2) / 2))


class Key:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
        self.hidden = False

    def hide(self):
        global i
        self.hidden = False
        for i in range(len(goblins)):
            if 0 < goblins[i].x < 560:
                self.hidden = True

    def collect(self):
        global greyKeyInventory
        global goldKeyInventory
        global redKeyInventory
        if -1 < breadCostume < 14:
            if self.x - 77 < bread.x < self.x + 37 and self.y - 47 < bread.y < self.y + 5:
                keys.remove(self)
                if self.colour == 'grey':
                    greyKeyInventory += 1
                elif self.colour == 'gold':
                    goldKeyInventory += 1
                else:
                    redKeyInventory += 1
        elif 13 < breadCostume < 21:
            if self.x - 59 < bread.x < self.x + 11 and self.y - 58 < bread.y < self.y + 34:
                keys.remove(self)
                if self.colour == 'grey':
                    greyKeyInventory += 1
                elif self.colour == 'gold':
                    goldKeyInventory += 1
                else:
                    redKeyInventory += 1
        else:
            if self.x - 49 < bread.x < self.x + 21 and self.y - 74 < bread.y < self.y + 18:
                keys.remove(self)
                if self.colour == 'grey':
                    greyKeyInventory += 1
                elif self.colour == 'gold':
                    goldKeyInventory += 1
                else:
                    redKeyInventory += 1


class TutorialTextBox:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text


class TutorialArrow:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.prime = False
        self.branch = False
        global placerX
        global placerY
        global floorX
        global floorY
        global bossRoom
        placerX = x
        placerY = y
        global i
        global j
        for i in range(0, 256):
            floorX = 40 * (i % 16) + placerX
            floorY = 40 * (int(i / 16)) + placerY
            floors.append(Floor(floorX, floorY))
        walls.append(Wall(placerX, placerY))
        for i in range(15):
            placerX += 40
            walls.append(Wall(placerX, placerY))
        for i in range(15):
            placerY += 40
            walls.append(Wall(placerX, placerY))
        for i in range(15):
            placerX -= 40
            walls.append(Wall(placerX, placerY))
        for i in range(14):
            placerY -= 40
            walls.append(Wall(placerX, placerY))
        if not inTutorial:
            if bossRoom:
                prob = 10
                bossRoom = False
            else:
                prob = random.randint(1, 10)
            if prob == 1:
                placerX += 160
                placerY += 120
                walls.append(Wall(placerX, placerY))
                placerX += 40
                walls.append(Wall(placerX, placerY))
                placerX += 200
                walls.append(Wall(placerX, placerY))
                placerX += 40
                walls.append(Wall(placerX, placerY))
                placerY += 40
                walls.append(Wall(placerX, placerY))
                placerY += 200
                walls.append(Wall(placerX, placerY))
                placerY += 40
                walls.append(Wall(placerX, placerY))
                placerX -= 40
                walls.append(Wall(placerX, placerY))
                placerX -= 200
                walls.append(Wall(placerX, placerY))
                placerX -= 40
                walls.append(Wall(placerX, placerY))
                placerY -= 40
                walls.append(Wall(placerX, placerY))
                placerY -= 200
                walls.append(Wall(placerX, placerY))
            elif prob == 2:
                placerX += 160
                placerY += 120
                walls.append(Wall(placerX, placerY))
                placerX += 280
                walls.append(Wall(placerX, placerY))
                placerY += 280
                walls.append(Wall(placerX, placerY))
                placerX -= 280
                walls.append(Wall(placerX, placerY))
            elif prob == 3:
                prob = (1, 2)
                if prob == 1:
                    placerX += 160
                    placerY += 120
                    for i in range(8):
                        walls.append(Wall(placerX, placerY))
                        placerX += 40
                    placerX -= 320
                    placerY += 280
                    for i in range(8):
                        walls.append(Wall(placerX, placerY))
                        placerX += 40
                elif prob == 2:
                    placerX += 160
                    placerY += 120
                    for i in range(8):
                        walls.append(Wall(placerX, placerY))
                        placerY += 40
                    placerY -= 320
                    placerX += 280
                    for i in range(8):
                        walls.append(Wall(placerX, placerY))
                        placerY += 40
            elif prob == 4:
                prob = random.randint(1, 4)
                if prob == 1:
                    placerX += 200
                    placerY += 160
                    walls.append(Wall(placerX, placerY))
                    for i in range(5):
                        placerY += 40
                        walls.append(Wall(placerX, placerY))
                    for i in range(5):
                        placerX += 40
                        walls.append(Wall(placerX, placerY))
                    for i in range(5):
                        placerY -= 40
                        walls.append(Wall(placerX, placerY))
                elif prob == 2:
                    placerX += 200
                    placerY += 160
                    walls.append(Wall(placerX, placerY))
                    for i in range(5):
                        placerX += 40
                        walls.append(Wall(placerX, placerY))
                    for i in range(5):
                        placerY += 40
                        walls.append(Wall(placerX, placerY))
                    for i in range(5):
                        placerX -= 40
                        walls.append(Wall(placerX, placerY))
                elif prob == 3:
                    placerX += 400
                    placerY += 360
                    walls.append(Wall(placerX, placerY))
                    for i in range(5):
                        placerY -= 40
                        walls.append(Wall(placerX, placerY))
                    for i in range(5):
                        placerX -= 40
                        walls.append(Wall(placerX, placerY))
                    for i in range(5):
                        placerY += 40
                        walls.append(Wall(placerX, placerY))
                elif prob == 4:
                    placerX += 400
                    placerY += 360
                    walls.append(Wall(placerX, placerY))
                    for i in range(5):
                        placerX -= 40
                        walls.append(Wall(placerX, placerY))
                    for i in range(5):
                        placerY -= 40
                        walls.append(Wall(placerX, placerY))
                    for i in range(5):
                        placerX += 40
                        walls.append(Wall(placerX, placerY))
            elif prob == 5:
                for i in range(5):
                    placerX += 40
                    walls.append(Wall(placerX, placerY))
                placerX += 160
                for i in range(5):
                    placerX += 40
                    walls.append(Wall(placerX, placerY))
                for i in range(4):
                    placerY += 40
                    walls.append(Wall(placerX, placerY))
                placerY += 160
                for i in range(5):
                    placerY += 40
                    walls.append(Wall(placerX, placerY))
                for i in range(4):
                    placerX -= 40
                    walls.append(Wall(placerX, placerY))
                placerX -= 160
                for i in range(5):
                    placerX -= 40
                    walls.append(Wall(placerX, placerY))
                for i in range(4):
                    placerY -= 40
                    walls.append(Wall(placerX, placerY))
                placerY -= 160
                for i in range(4):
                    placerY -= 40
                    walls.append(Wall(placerX, placerY))
                for i in range(3):
                    placerX += 40
                    walls.append(Wall(placerX, placerY))
                placerX += 240
                for i in range(3):
                    placerX += 40
                    walls.append(Wall(placerX, placerY))
                for i in range(2):
                    placerY += 40
                    walls.append(Wall(placerX, placerY))
                placerY += 240
                for i in range(3):
                    placerY += 40
                    walls.append(Wall(placerX, placerY))
                for i in range(2):
                    placerX -= 40
                    walls.append(Wall(placerX, placerY))
                placerX -= 240
                for i in range(3):
                    placerX -= 40
                    walls.append(Wall(placerX, placerY))
                for i in range(2):
                    placerY -= 40
                    walls.append(Wall(placerX, placerY))
                placerY -= 240
                for i in range(2):
                    placerY -= 40
                    walls.append(Wall(placerX, placerY))
                placerX += 40
                walls.append(Wall(placerX, placerY))
                placerX += 360
                walls.append(Wall(placerX, placerY))
                placerY += 360
                walls.append(Wall(placerX, placerY))
                placerX -= 360
                walls.append(Wall(placerX, placerY))
            elif prob == 6:
                prob = random.randint(1, 4)
                if prob == 1:
                    placerX += 160
                    placerY += 120
                    walls.append(Wall(placerX, placerY))
                    placerX += 40
                    walls.append(Wall(placerX, placerY))
                    placerX += 240
                    for i in range(8):
                        walls.append(Wall(placerX, placerY))
                        placerY += 40
                    placerY -= 40
                    for i in range(7):
                        placerX -= 40
                        walls.append(Wall(placerX, placerY))
                    placerY -= 240
                    walls.append(Wall(placerX, placerY))
                elif prob == 2:
                    placerX += 440
                    placerY += 120
                    walls.append(Wall(placerX, placerY))
                    placerY += 40
                    walls.append(Wall(placerX, placerY))
                    placerY += 240
                    for i in range(8):
                        walls.append(Wall(placerX, placerY))
                        placerX -= 40
                    placerX += 40
                    for i in range(7):
                        placerY -= 40
                        walls.append(Wall(placerX, placerY))
                    placerX += 240
                    walls.append(Wall(placerX, placerY))
                elif prob == 3:
                    placerX += 440
                    placerY += 400
                    walls.append(Wall(placerX, placerY))
                    placerX -= 40
                    walls.append(Wall(placerX, placerY))
                    placerX -= 240
                    for i in range(8):
                        walls.append(Wall(placerX, placerY))
                        placerY -= 40
                    placerY += 40
                    for i in range(7):
                        placerX += 40
                        walls.append(Wall(placerX, placerY))
                    placerY += 240
                    walls.append(Wall(placerX, placerY))
                elif prob == 4:
                    placerX += 160
                    placerY += 400
                    walls.append(Wall(placerX, placerY))
                    placerY -= 40
                    walls.append(Wall(placerX, placerY))
                    placerY -= 240
                    for i in range(8):
                        walls.append(Wall(placerX, placerY))
                        placerX += 40
                    placerX -= 40
                    for i in range(7):
                        placerY += 40
                        walls.append(Wall(placerX, placerY))
                    placerX -= 240
                    walls.append(Wall(placerX, placerY))
            elif prob == 7:
                prob = random.randint(1, 4)
                if prob == 1:
                    placerX += 40
                    for i in range(3):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 240
                        placerY += 40
                    for i in range(2):
                        for j in range(11):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 440
                        placerY += 40
                    placerX += 120
                    placerY += 160
                    for i in range(2):
                        for j in range(11):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 440
                        placerY += 40
                    placerX += 200
                    for i in range(3):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 240
                        placerY += 40
                elif prob == 2:
                    placerX += 40
                    for i in range(3):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerY += 40
                        placerY -= 240
                        placerX += 40
                    for i in range(2):
                        for j in range(11):
                            walls.append(Wall(placerX, placerY))
                            placerY += 40
                        placerY -= 440
                        placerX += 40
                    placerY += 120
                    placerX += 160
                    for i in range(2):
                        for j in range(11):
                            walls.append(Wall(placerX, placerY))
                            placerY += 40
                        placerY -= 440
                        placerX += 40
                    placerY += 200
                    for i in range(3):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerY += 40
                        placerY -= 240
                        placerX += 40
                elif prob == 3:
                    placerX += 560
                    for i in range(3):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 240
                        placerY += 40
                    for i in range(2):
                        for j in range(11):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 440
                        placerY += 40
                    placerY += 160
                    placerX -= 120
                    for i in range(2):
                        for j in range(11):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 440
                        placerY += 40
                    placerX -= 200
                    for i in range(3):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 240
                        placerY += 40
                elif prob == 4:
                    placerX += 560
                    for i in range(3):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerY += 40
                        placerY -= 240
                        placerX -= 40
                    for i in range(2):
                        for j in range(11):
                            walls.append(Wall(placerX, placerY))
                            placerY += 40
                        placerY -= 440
                        placerX -= 40
                    placerX -= 160
                    placerY += 120
                    for i in range(2):
                        for j in range(11):
                            walls.append(Wall(placerX, placerY))
                            placerY += 40
                        placerY -= 440
                        placerX -= 40
                    placerY += 200
                    for i in range(3):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerY += 40
                        placerY -= 240
                        placerX -= 40
            elif prob == 8:
                prob = random.randint(1, 8)
                if prob == 1:
                    placerX += 40
                    for i in range(5):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 240
                        placerY += 40
                    for i in range(5):
                        walls.append(Wall(placerX, placerY))
                        placerX += 40
                    placerX -= 40
                    placerY += 40
                    for i in range(4):
                        walls.append(Wall(placerX, placerY))
                        placerY += 40
                    placerY -= 40
                    placerX += 40
                    for i in range(5):
                        walls.append(Wall(placerX, placerY))
                        placerX += 40
                    placerX -= 160
                    placerY -= 200
                    for i in range(4):
                        walls.append(Wall(placerX, placerY))
                        placerX += 40
                elif prob == 2:
                    placerX += 560
                    for i in range(5):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 240
                        placerY += 40
                    for i in range(5):
                        walls.append(Wall(placerX, placerY))
                        placerX -= 40
                    placerX += 40
                    placerY += 40
                    for i in range(4):
                        walls.append(Wall(placerX, placerY))
                        placerY += 40
                    placerY -= 40
                    placerX -= 40
                    for i in range(5):
                        walls.append(Wall(placerX, placerY))
                        placerX -= 40
                    placerX += 160
                    placerY -= 200
                    for i in range(4):
                        walls.append(Wall(placerX, placerY))
                        placerX -= 40
                if prob == 3:
                    placerX += 40
                    for i in range(5):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 240
                        placerY += 40
                    for i in range(5):
                        walls.append(Wall(placerX, placerY))
                        placerX += 40
                    placerX -= 40
                    placerY += 40
                    for i in range(4):
                        walls.append(Wall(placerX, placerY))
                        placerY += 40
                    placerY -= 240
                    placerX += 80
                    for i in range(4):
                        walls.append(Wall(placerX, placerY))
                        placerX += 40
                    placerX -= 40
                    placerY += 40
                    for i in range(5):
                        walls.append(Wall(placerX, placerY))
                        placerY += 40
                elif prob == 4:
                    placerX += 560
                    for i in range(5):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 240
                        placerY += 40
                    for i in range(5):
                        walls.append(Wall(placerX, placerY))
                        placerX -= 40
                    placerX += 40
                    placerY += 40
                    for i in range(4):
                        walls.append(Wall(placerX, placerY))
                        placerY += 40
                    placerY -= 240
                    placerX -= 80
                    for i in range(4):
                        walls.append(Wall(placerX, placerY))
                        placerX -= 40
                    placerX += 40
                    placerY += 40
                    for i in range(5):
                        walls.append(Wall(placerX, placerY))
                        placerY += 40
                if prob == 5:
                    placerX += 40
                    placerY += 520
                    for i in range(5):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 240
                        placerY -= 40
                    for i in range(5):
                        walls.append(Wall(placerX, placerY))
                        placerX += 40
                    placerX -= 40
                    placerY -= 40
                    for i in range(4):
                        walls.append(Wall(placerX, placerY))
                        placerY -= 40
                    placerY += 240
                    placerX += 80
                    for i in range(4):
                        walls.append(Wall(placerX, placerY))
                        placerX += 40
                    placerX -= 40
                    placerY -= 40
                    for i in range(5):
                        walls.append(Wall(placerX, placerY))
                        placerY -= 40
                elif prob == 6:
                    placerX += 560
                    placerY += 520
                    for i in range(5):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 240
                        placerY -= 40
                    for i in range(5):
                        walls.append(Wall(placerX, placerY))
                        placerX -= 40
                    placerX += 40
                    placerY -= 40
                    for i in range(4):
                        walls.append(Wall(placerX, placerY))
                        placerY -= 40
                    placerY += 240
                    placerX -= 80
                    for i in range(4):
                        walls.append(Wall(placerX, placerY))
                        placerX -= 40
                    placerX += 40
                    placerY -= 40
                    for i in range(5):
                        walls.append(Wall(placerX, placerY))
                        placerY -= 40
                if prob == 7:
                    placerX += 40
                    placerY += 520
                    for i in range(5):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 240
                        placerY -= 40
                    for i in range(5):
                        walls.append(Wall(placerX, placerY))
                        placerX += 40
                    placerX -= 40
                    placerY -= 40
                    for i in range(4):
                        walls.append(Wall(placerX, placerY))
                        placerY -= 40
                    placerY += 40
                    placerX += 40
                    for i in range(5):
                        walls.append(Wall(placerX, placerY))
                        placerX += 40
                    placerX -= 160
                    placerY += 200
                    for i in range(4):
                        walls.append(Wall(placerX, placerY))
                        placerX += 40
                elif prob == 8:
                    placerX += 560
                    placerY += 520
                    for i in range(5):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 240
                        placerY -= 40
                    for i in range(5):
                        walls.append(Wall(placerX, placerY))
                        placerX -= 40
                    placerX += 40
                    placerY -= 40
                    for i in range(4):
                        walls.append(Wall(placerX, placerY))
                        placerY -= 40
                    placerY += 40
                    placerX -= 40
                    for i in range(5):
                        walls.append(Wall(placerX, placerY))
                        placerX -= 40
                    placerX += 160
                    placerY += 200
                    for i in range(4):
                        walls.append(Wall(placerX, placerY))
                        placerX -= 40
            elif prob == 9:
                prob = random.randint(1, 8)
                if prob == 1:
                    placerX += 40
                    for i in range(5):
                        for j in range(5 - i):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 40 * (5 - i)
                        placerY += 40
                    placerY -= 200
                    placerX += 320
                    for i in range(6):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 240
                        placerY += 40
                    for i in range(2):
                        for j in range(2):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 80
                        placerY += 40
                    placerX -= 160
                    for i in range(2):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 240
                        placerY += 40
                elif prob == 2:
                    placerX += 560
                    for i in range(5):
                        for j in range(5 - i):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 40 * (5 - i)
                        placerY += 40
                    placerY -= 200
                    placerX -= 320
                    for i in range(6):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 240
                        placerY += 40
                    for i in range(2):
                        for j in range(2):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 80
                        placerY += 40
                    placerX += 160
                    for i in range(2):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 240
                        placerY += 40
                if prob == 3:
                    placerX += 40
                    for i in range(5):
                        for j in range(5 - i):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 40 * (5 - i)
                        placerY += 40
                    placerY += 120
                    for i in range(6):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 240
                        placerY += 40
                    placerX += 240
                    placerY -= 200
                    for i in range(2):
                        for j in range(2):
                            walls.append(Wall(placerX, placerY))
                            placerY -= 40
                        placerY += 80
                        placerX += 40
                    for i in range(2):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerY -= 40
                        placerY += 240
                        placerX += 40
                elif prob == 4:
                    placerX += 560
                    for i in range(5):
                        for j in range(5 - i):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 40 * (5 - i)
                        placerY += 40
                    placerY += 120
                    for i in range(6):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 240
                        placerY += 40
                    placerX -= 240
                    placerY -= 200
                    for i in range(2):
                        for j in range(2):
                            walls.append(Wall(placerX, placerY))
                            placerY -= 40
                        placerY += 80
                        placerX -= 40
                    for i in range(2):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerY -= 40
                        placerY += 240
                        placerX -= 40
                if prob == 5:
                    placerX += 40
                    placerY += 520
                    for i in range(5):
                        for j in range(5 - i):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 40 * (5 - i)
                        placerY -= 40
                    placerY += 200
                    placerX += 320
                    for i in range(6):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 240
                        placerY -= 40
                    for i in range(2):
                        for j in range(2):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 80
                        placerY -= 40
                    placerX -= 160
                    for i in range(2):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 240
                        placerY -= 40
                elif prob == 6:
                    placerX += 560
                    placerY += 520
                    for i in range(5):
                        for j in range(5 - i):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 40 * (5 - i)
                        placerY -= 40
                    placerY += 200
                    placerX -= 320
                    for i in range(6):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 240
                        placerY -= 40
                    for i in range(2):
                        for j in range(2):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 80
                        placerY -= 40
                    placerX += 160
                    for i in range(2):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 240
                        placerY -= 40
                if prob == 7:
                    placerX += 40
                    placerY += 520
                    for i in range(5):
                        for j in range(5 - i):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 40 * (5 - i)
                        placerY -= 40
                    placerY -= 120
                    for i in range(6):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX += 40
                        placerX -= 240
                        placerY -= 40
                    placerX += 240
                    placerY += 240
                    for i in range(2):
                        for j in range(2):
                            walls.append(Wall(placerX, placerY))
                            placerY -= 40
                        placerY += 80
                        placerX += 40
                    placerY += 160
                    for i in range(2):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerY -= 40
                        placerY += 240
                        placerX += 40
                if prob == 8:
                    placerX += 560
                    placerY += 520
                    for i in range(5):
                        for j in range(5 - i):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 40 * (5 - i)
                        placerY -= 40
                    placerY -= 120
                    for i in range(6):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerX -= 40
                        placerX += 240
                        placerY -= 40
                    placerX -= 240
                    placerY += 240
                    for i in range(2):
                        for j in range(2):
                            walls.append(Wall(placerX, placerY))
                            placerY -= 40
                        placerY += 80
                        placerX -= 40
                    placerY += 160
                    for i in range(2):
                        for j in range(6):
                            walls.append(Wall(placerX, placerY))
                            placerY -= 40
                        placerY += 240
                        placerX -= 40


class Goblin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walkAnimation = 0
        self.direction = random.randint(0, 0)
        self.prob = 0
        self.distance = 40
        self.angle = 0
        self.knock = 0
        self.wait = random.randint(1, 100)
        self.ticker = 0
        self.goblinCostume = 0
        self.HT = 14
        self.HB = 12
        self.HRL = 2
        self.VRL = 20
        self.VTB = 2

    def move(self):
        global j
        if self.ticker == self.wait:
            self.direction = random.randint(0, 3)
            self.ticker = 0
            self.wait = random.randint(1, 100)
        else:
            self.ticker += 1
        for j in range(len(walls)):
            if self.x + 80 > walls[j].x > self.x + 60 and self.y - 40 < walls[j].y < self.y + 80:
                self.direction = 1
        for j in range(len(walls)):
            if self.x - 40 < walls[j].x < self.x - 20 and self.y - 40 < walls[j].y < self.y + 80:
                self.direction = 0
        for j in range(len(walls)):
            if self.y + 80 > walls[j].y > self.y + 60 and self.x - 40 < walls[j].x < self.x + 80:
                self.direction = 2
        for j in range(len(walls)):
            if self.y - 40 < walls[j].y < self.y - 20 and self.x - 40 < walls[j].x < self.x + 80:
                self.direction = 3
        for j in range(len(locks)):
            if self.x + 80 > locks[j].x > self.x + 60 and self.y - 80 < locks[j].y < self.y + 80:
                self.direction = 1
        for j in range(len(locks)):
            if self.x - 40 < locks[j].x < self.x - 20 and self.y - 80 < locks[j].y < self.y + 80:
                self.direction = 0
        for j in range(len(locks)):
            if self.y + 80 > locks[j].y > self.y + 60 and self.x - 80 < locks[j].x < self.x + 80:
                self.direction = 2
        for j in range(len(locks)):
            if self.y - 40 < locks[j].y < self.y - 20 and self.x - 80 < locks[j].x < self.x + 80:
                self.direction = 3
        if self.direction == 0:
            self.x += speed
            if self.walkAnimation < 2:
                self.walkAnimation += 1
            else:
                self.walkAnimation = 0
                if self.goblinCostume == 5:
                    self.goblinCostume = 4
                else:
                    self.goblinCostume = 5
        if self.direction == 1:
            self.x -= speed
            if self.walkAnimation < 2:
                self.walkAnimation += 1
            else:
                self.walkAnimation = 0
                if self.goblinCostume == 7:
                    self.goblinCostume = 6
                else:
                    self.goblinCostume = 7
        if self.direction == 2:
            self.y -= speed
            if self.walkAnimation < 2:
                self.walkAnimation += 1
            else:
                self.walkAnimation = 0
                if self.goblinCostume == 3:
                    self.goblinCostume = 2
                else:
                    self.goblinCostume = 3
        if self.direction == 3:
            self.y += speed
            if self.walkAnimation < 2:
                self.walkAnimation += 1
            else:
                self.walkAnimation = 0
                if self.goblinCostume == 1:
                    self.goblinCostume = 0
                else:
                    self.goblinCostume = 1

    def die(self):
        global i
        if 0 < breadCostume < 5 and self.goblinCostume < 8:
            if bread.x - 80 < self.x < bread.x + 80 and bread.y - 40 < self.y < bread.y + 80:
                self.goblinCostume = 8
        if 7 < breadCostume < 12 and self.goblinCostume < 8:
            if bread.x - 80 < self.x < bread.x + 80 and bread.y - 80 < self.y < bread.y + 40:
                self.goblinCostume = 8
        if 14 < breadCostume < 19 and self.goblinCostume < 8:
            if bread.x - 40 < self.x < bread.x + 80 and bread.y - 80 < self.y < bread.y + 80:
                self.goblinCostume = 8
        if 21 < breadCostume < 26 and self.goblinCostume < 8:
            if bread.x - 80 < self.x < bread.x + 40 and bread.y - 80 < self.y < bread.y + 80:
                self.goblinCostume = 8
        if 7 < self.goblinCostume < 16:
            self.goblinCostume += 1
            self.x -= 10
            self.y -= 20
        if self.goblinCostume > 15:
            goblins.remove(self)

    def bump(self):
        global j
        if self.knock == 1:
            self.knock = 0
        else:
            self.knock = 1
        self.angle = math.atan((bread.y - self.y) / (bread.x - self.x))
        if bread.x - self.x < 0:
            self.angle += math.pi
        bread.y += self.distance * math.sin(self.angle)
        bread.x += self.distance * math.cos(self.angle)
        if -1 < breadCostume < 14:
            for j in range(len(walls)):
                while bread.x - 42 < walls[j].x < bread.x + 82 and bread.y - 16 < walls[j].y < bread.y + 62:
                    bread.y -= self.distance * math.sin(self.angle)
                    bread.x -= self.distance * math.cos(self.angle)
        elif 13 < breadCostume < 21:
            for j in range(len(walls)):
                while bread.x - 12 < walls[j].x < bread.x + 60 and bread.y - 31 < walls[j].y < bread.y + 83:
                    bread.y -= self.distance * math.sin(self.angle)
                    bread.x -= self.distance * math.cos(self.angle)
        elif 20 < breadCostume < 28:
            for j in range(len(walls)):
                while bread.x - 22 < walls[j].x < bread.x + 50 and bread.y - 29 < walls[j].y < bread.y + 85:
                    bread.y -= self.distance * math.sin(self.angle)
                    bread.x -= self.distance * math.cos(self.angle)

    def attack(self):
        if self.knock == 1:
            self.bump()
        if 4 < breadCostume < 7 or breadCostume == 0 or 11 < breadCostume < 14 or breadCostume == 7:
            if self.goblinCostume < 4:
                if bread.x - 60 < self.x < bread.x + 60 and bread.y - 44 < self.y < bread.y + 38:
                    self.bump()
                    bread.hp -= 1
            elif self.goblinCostume < 8:
                if bread.x - 42 < self.x < bread.x + 42 and bread.y - 54 < self.y < bread.y + 50:
                    self.bump()
                    bread.hp -= 1
        if 18 < breadCostume < 21 or breadCostume == 14 or 25 < breadCostume < 28 or breadCostume == 21:
            if self.goblinCostume < 4:
                if bread.x - 46 < self.x < bread.x + 44 and bread.y - 57 < self.y < bread.y + 55:
                    self.bump()
                    bread.hp -= 1
            elif self.goblinCostume < 8:
                if bread.x - 28 < self.x < bread.x + 26 and bread.y - 67 < self.y < bread.y + 67:
                    self.bump()
                    bread.hp -= 1


class Spider:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.costume = 0
        self.idleAnim = 0
        self.jumpCountdown = 0
        self.destinationX = 0
        self.destinationY = 0
        self.yVel = 0
        self.jumpFrames = 0
        self.initHeight = 0
        self.jumpTime = 0
        self.c = 0
        self.angle = 0
        self.distance = 40
        self.knock = 0
        self.bumpAngle = 0
        self.T = 3
        self.B = 1

    def move(self):
        if self.jumpCountdown > 5 and self.costume < 2:
            self.costume = 2
            self.destinationX = bread.x + 20
            self.destinationY = bread.y + 20
            self.yVel = (-1.05*(math.sqrt((self.destinationY - self.y)**2 + (self.destinationX - self.x)**2)))/20
            self.jumpFrames = 1
            self.initHeight = self.y
            self.jumpCountdown = 0
            self.jumpTime = int(-2*self.yVel/1.05)
            self.angle = math.atan((self.destinationY - self.y)/(self.destinationX - self.x))
            if self.destinationX - self.x < 0:
                self.angle += math.pi

        elif self.costume < 2:
            if self.idleAnim < 6:
                self.idleAnim += 1
            else:
                if self.costume == 0:
                    self.costume = 1
                else:
                    self.costume = 0
                self.idleAnim = 0
                self.jumpCountdown += 1
        if self.costume == 2:
            self.x += 10*math.cos(self.angle)
            self.y = self.initHeight + self.yVel*self.jumpFrames + 0.5*1.05*(self.jumpFrames**2) + self.jumpFrames*10 *\
                math.sin(self.angle)
            self.jumpFrames += 1
            if self.jumpFrames > self.jumpTime:
                self.costume = 0

    def bump(self):
        global j
        if self.knock == 1:
            self.knock = 0
        else:
            self.knock = 1
        self.bumpAngle = math.atan((bread.y - self.y) / (bread.x - self.x))
        if bread.x - self.x < 0:
            self.bumpAngle += math.pi
        bread.y += self.distance * math.sin(self.bumpAngle)
        bread.x += self.distance * math.cos(self.bumpAngle)
        if -1 < breadCostume < 14:
            for j in range(len(walls)):
                while bread.x - 42 < walls[j].x < bread.x + 82 and bread.y - 16 < walls[j].y < bread.y + 62:
                    bread.y -= self.distance * math.sin(self.bumpAngle)
                    bread.x -= self.distance * math.cos(self.bumpAngle)
        elif 13 < breadCostume < 21:
            for j in range(len(walls)):
                while bread.x - 12 < walls[j].x < bread.x + 60 and bread.y - 31 < walls[j].y < bread.y + 83:
                    bread.y -= self.distance * math.sin(self.bumpAngle)
                    bread.x -= self.distance * math.cos(self.bumpAngle)
        elif 20 < breadCostume < 28:
            for j in range(len(walls)):
                while bread.x - 22 < walls[j].x < bread.x + 50 and bread.y - 29 < walls[j].y < bread.y + 85:
                    bread.y -= self.distance * math.sin(self.bumpAngle)
                    bread.x -= self.distance * math.cos(self.bumpAngle)

    def attack(self):
        if self.knock == 1:
            self.bump()
        if 4 < breadCostume < 7 or breadCostume == 0 or 11 < breadCostume < 14 or breadCostume == 7:
            if self.costume < 2:
                if bread.x - 22 < self.x < bread.x + 62 and bread.y - 15 < self.y < bread.y + 49:
                    self.bump()
                    bread.hp -= 1
        if 18 < breadCostume < 21 or breadCostume == 14 or 25 < breadCostume < 28 or breadCostume == 21:
            if self.costume < 2:
                if bread.x - 8 < self.x < bread.x + 46 and bread.y - 28 < self.y < bread.y + 66:
                    self.bump()
                    bread.hp -= 1

    def die(self):
        global i
        if 0 < breadCostume < 5 and self.costume < 3:
            if bread.x - 40 < self.x < bread.x + 80 and bread.y < self.y < bread.y + 80:
                self.costume = 3
        if 7 < breadCostume < 12 and self.costume < 8:
            if bread.x - 40 < self.x < bread.x + 80 and bread.y - 40 < self.y < bread.y + 40:
                self.costume = 3
        if 14 < breadCostume < 19 and self.costume < 8:
            if bread.x < self.x < bread.x + 80 and bread.y - 40 < self.y < bread.y + 80:
                self.costume = 3
        if 21 < breadCostume < 26 and self.costume < 8:
            if bread.x - 40 < self.x < bread.x + 40 and bread.y - 40 < self.y < bread.y + 80:
                self.costume = 3
        if 2 < self.costume < 11:
            self.costume += 1
            self.x -= 10
            self.y -= 20
        if self.costume > 10:
            spiders.remove(self)


class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.costume = 0
        self.ticker = 0
        self.k = 10
        self.c = 1000
        self.fx = 0
        self.fy = 0
        self.r1 = 0
        self.r2 = 0
        self.r3 = 0
        self.r4 = 0
        self.vx = 0
        self.vy = 0
        self.d = 0
        self.countdown = 0

    def move(self):
        if self.countdown < 200:
            self.countdown += 1
            if self.ticker < 3:
                self.ticker += 1
            elif self.costume < 3:
                self.costume += 1
                self.ticker = 0
            elif self.costume == 3:
                self.costume = 0
                self.ticker = 0
            self.r1 = math.sqrt(pow((self.x - 560), 2) + pow(self.y, 2))
            self.r2 = math.sqrt(pow(self.x, 2)+pow(self.y, 2))
            self.r3 = math.sqrt(pow((self.y - 560), 2) + pow(self.x, 2))
            self.r4 = math.sqrt(pow((self.y - 560), 2) + pow((self.x - 560), 2))
            self.fx = self.k*(1/self.r1 - 1/self.r2)
            self.fy = (-self.k/self.y)*((self.x-560)/self.r1 - self.x/self.r2)
            self.fx += (-self.k/self.x)*((self.y-560)/self.r3 - self.y/self.r2)
            self.fy += self.k * (1 / self.r3 - 1 / self.r2)
            self.fx += self.k * (1 / self.r4 - 1 / self.r3)
            self.fy += (-self.k / (self.y - 560)) * ((self.x - 560) / self.r4 - self.x / self.r3)
            self.fx += (-self.k / (self.x-560)) * ((self.y - 560) / self.r4 - self.y / self.r1)
            self.fy += self.k * (1 / self.r4 - 1 / self.r1)
            self.d = math.sqrt(pow((self.x - bread.x), 2) + pow((self.y - bread.y), 2))
            self.fx += self.c*(self.x - bread.x)/pow(self.d, 3)
            self.fy += self.c*(self.y - bread.y)/pow(self.d, 3)
            self.vx += self.fx
            self.vy += self.fy
            if self.vx > 7:
                self.vx = 7
            elif self.vx < -7:
                self.vx = -7
            if self.vy > 7:
                self.vy = 7
            elif self.vy < -7:
                self.vy = -7
            self.x += self.vx
            self.y += self.vy
        else:
            self.attack()

    def attack(self):
        self.ticker = 0
        if self.ticker < 3:
            self.ticker += 1
        elif self.ticker < 6:
            self.costume = 5
        else:
            energyBalls.append(EnergyBall(45))
            self.ticker = 0
            self.countdown = 0


class EnergyBall:
    def __init__(self, init_angle):
        self.x = 0
        self.y = 0
        self.angle = init_angle
        self.speed = 5

    def move(self):
        self.x += self.speed*math.cos(self.angle)
        self.y += self.speed*math.sin(self.angle)


bread = Bread()
walls = []
floors = []
horizontalDoors = []
verticalDoors = []
locks = []
keys = []
tutorialTextBoxes = []
tutorialArrows = []
rooms = []
goblins = []
spiders = []
ghosts = []
energyBalls = []


def generate():
    global bossRoom
    global placerX
    global placerY
    global i
    global j
    global locksLeft
    global layerOffset
    global dungeonX
    global dungeonY
    global checker
    global redKeyPlaced
    global greyDoorCount
    global greyKeyCount
    global isRedDoor
    redKeyPlaced = False
    isRedDoor = False
    rooms.append(Room(0, 0))
    graphCode.clear()
    graphCode.append(random.randint(1, 3))
    layerOffset = 0
    for i in range(graphCode[0]):
        locksLeft = random.randint(4 - graphCode[0], 6 - graphCode[0])
        if graphCode[0] == 1:
            prob = (random.randint(0, 3))
        elif graphCode[0] == 2:
            prob = (random.randint(4, 7))
        else:
            prob = (random.randint(8, 11))
        if prob == 0:
            graphCode.append(0)
        elif 0 < prob < 4:
            graphCode.append(1)
        elif prob == 4 and i == 0:
            graphCode.append(0)
        elif 8 < prob < 12 and i == 0:
            graphCode.append(0)
        elif prob == 8 and i == 1:
            graphCode.append(0)
        else:
            graphCode.append(random.randint(0, 1))
        if locksLeft > 3:
            graphCode.append(random.randint(1, 3) - graphCode[1 + layerOffset])
        elif locksLeft > 1:
            graphCode.append(random.randint(1, 2) - graphCode[1 + layerOffset])
        elif locksLeft > 0:
            graphCode.append(1 - graphCode[1 + layerOffset])
        locksLeft -= graphCode[1 + layerOffset] + graphCode[2 + layerOffset]
        if locksLeft > 0:
            if not ((prob == 4 and i == 0) or (8 < prob < 12 and i == 0) or (prob == 8 and i == 1)):
                if graphCode[2 + layerOffset] < locksLeft:
                    for x in range(random.randint(1 - graphCode[1 + layerOffset], graphCode[2 + layerOffset])):
                        graphCode.append(1)
                        graphCode.append(0)
                        locksLeft -= 1
                else:
                    for x in range(random.randint(1 - graphCode[1 + layerOffset], locksLeft)):
                        graphCode.append(1)
                        graphCode.append(0)
                        locksLeft -= 1
        if locksLeft > 0:
            loop = True
            while loop:
                graphCode.append(0)
                graphCode.append(random.randint(1, locksLeft))
                locksLeft -= graphCode[len(graphCode) - 1]
                if locksLeft == 0:
                    loop = False
        layerOffset = len(graphCode)
        graphCode.append(6)
    print(graphCode)
    dungeonX = 0
    dungeonY = 0
    layerOffset = 0
    rooms[0].branch = True
    for k in range(graphCode[0]):
        if k > 0:
            for i in range(len(rooms)):
                rooms[i].branch = False
                if rooms[i].prime:
                    dungeonX = rooms[i].x
                    dungeonY = rooms[i].y
                    rooms[i].prime = False
            snake('normal')
            rooms[len(rooms) - 1].branch = True
        for i in range(random.randint(0, 1)):
            snake('normal')
            rooms[len(rooms) - 1].branch = True
        if graphCode[1 + layerOffset] > 0:
            prob = random.randint(0, 1)
            if prob == 0:
                snake('normal')
                rooms[len(rooms) - 1].branch = True
            snake('red')
        for i in range(graphCode[2 + layerOffset]):
            prob = random.randint(0, 1)
            if prob == 0:
                snake('normal')
                if graphCode[1 + layerOffset] == 0 and i == 0:
                    rooms[len(rooms) - 1].branch = True
            snake('grey')
        rooms[len(rooms) - 1].prime = True
        checker = 0
        if graphCode[3 + layerOffset] == 6:
            layerOffset = 3 + layerOffset
        else:
            loop = True
            while loop:
                prob = random.randint(0, len(rooms) - 1)
                if rooms[prob].branch:
                    dungeonX = rooms[prob].x
                    dungeonY = rooms[prob].y
                    for j in range(random.randint(0, 1)):
                        snake('normal')
                        rooms[len(rooms) - 1].branch = True
                    if graphCode[3 + checker + layerOffset] > 0:
                        prob = random.randint(0, 1)
                        if prob == 0:
                            snake('normal')
                            rooms[len(rooms) - 1].branch = True
                        snake('red')
                    for j in range(graphCode[4 + checker + layerOffset]):
                        prob = random.randint(0, 1)
                        if prob == 0:
                            snake('normal')
                            if graphCode[3 + checker + layerOffset] == 0 and j == 0:
                                rooms[len(rooms) - 1].branch = True
                        snake('grey')
                    if graphCode[3 + checker + layerOffset] > 0:
                        keys.append(Key(dungeonX + 300, dungeonY + 300, 'grey'))
                    elif graphCode[1 + layerOffset] > 0 and not redKeyPlaced:
                        keys.append(Key(dungeonX + 300, dungeonY + 300, 'red'))
                        redKeyPlaced = True
                    else:
                        keys.append(Key(dungeonX + 300, dungeonY + 300, 'grey'))
                    if graphCode[5 + checker + layerOffset] == 6:
                        loop = False
                        layerOffset = 5 + checker + layerOffset
                    checker += 2
        greyDoorCount = 0
        greyKeyCount = 0
        for i in range(len(locks)):
            if locks[i].colour == 'grey':
                greyDoorCount += 1
        for i in range(len(keys)):
            if keys[i].colour == 'grey':
                greyKeyCount += 1
        for i in range(greyDoorCount - greyKeyCount):
            loop = True
            while loop:
                prob = random.randint(0, len(rooms) - 1)
                if rooms[prob].branch:
                    dungeonX = rooms[prob].x
                    dungeonY = rooms[prob].y
                    prob = random.randint(0, 1)
                    if prob == 0:
                        snake('normal')
                        rooms[len(rooms) - 1].branch = True
                    snake('normal')
                    rooms[len(rooms) - 1].branch = True
                    keys.append(Key(dungeonX + 300, dungeonY + 300, 'grey'))
                    loop = False
        for i in range(len(locks)):
            if locks[i].colour == 'red':
                isRedDoor = True
        if not redKeyPlaced and isRedDoor:
            loop = True
            while loop:
                prob = random.randint(0, len(rooms) - 1)
                if rooms[prob].branch:
                    dungeonX = rooms[prob].x
                    dungeonY = rooms[prob].y
                    prob = random.randint(0, 1)
                    if prob == 0:
                        snake('normal')
                        rooms[len(rooms) - 1].branch = True
                    snake('normal')
                    rooms[len(rooms) - 1].branch = True
                    keys.append(Key(dungeonX + 300, dungeonY + 300, 'red'))
                    redKeyPlaced = True
                    loop = False
    for i in range(len(rooms)):
        if rooms[i].prime:
            keys.append(Key(rooms[i].x + 300, rooms[i].y + 300, 'gold'))
    loop = True
    while loop:
        prob = random.randint(0, len(rooms) - 1)
        if rooms[prob].branch:
            dungeonX = rooms[prob].x
            dungeonY = rooms[prob].y
            prob = random.randint(0, 1)
            if prob == 0:
                snake('normal')
            bossRoom = True
            snake('gold')
            loop = False


def snake(colour):
    global dungeonX
    global dungeonY
    global wrongWay
    global i
    global blockedRoutes
    blockedRoutes = 0
    for i in range(len(rooms)):
        if dungeonX == rooms[i].x + 640 and dungeonY == rooms[i].y:
            blockedRoutes += 1
    for i in range(len(rooms)):
        if dungeonX == rooms[i].x - 640 and dungeonY == rooms[i].y:
            blockedRoutes += 1
    for i in range(len(rooms)):
        if dungeonX == rooms[i].x and dungeonY == rooms[i].y + 640:
            blockedRoutes += 1
    for i in range(len(rooms)):
        if dungeonX == rooms[i].x and dungeonY == rooms[i].y - 640:
            blockedRoutes += 1
    if blockedRoutes > 3:
        print("EXIT-FAILURE")
        walls.clear()
        floors.clear()
        horizontalDoors.clear()
        verticalDoors.clear()
        locks.clear()
        keys.clear()
        rooms.clear()
        dungeonX = 1/0
    loop = True
    while loop:
        wrongWay = False
        prob = random.randint(0, 3)
        if prob == 0:
            dungeonX += 640
            for i in range(len(rooms)):
                if dungeonX == rooms[i].x and dungeonY == rooms[i].y:
                    dungeonX -= 640
                    wrongWay = True
                    break
            if not wrongWay:
                rooms.append(Room(dungeonX, dungeonY))
                verticalDoors.append(DoorVertical(dungeonX, dungeonY + 320))
                if colour == 'grey':
                    locks.append(LockRight(dungeonX - 40, dungeonY + 280, 'grey'))
                elif colour == 'red':
                    locks.append(LockRight(dungeonX - 40, dungeonY + 280, 'red'))
                elif colour == 'gold':
                    locks.append(LockRight(dungeonX - 40, dungeonY + 280, 'gold'))
                loop = False
        elif prob == 1:
            dungeonX -= 640
            for i in range(len(rooms)):
                if dungeonX == rooms[i].x and dungeonY == rooms[i].y:
                    dungeonX += 640
                    wrongWay = True
                    break
            if not wrongWay:
                rooms.append(Room(dungeonX, dungeonY))
                verticalDoors.append(DoorVertical(dungeonX + 640, dungeonY + 320))
                if colour == 'grey':
                    locks.append(LockLeft(dungeonX + 640, dungeonY + 280, 'grey'))
                elif colour == 'red':
                    locks.append(LockLeft(dungeonX + 640, dungeonY + 280, 'red'))
                elif colour == 'gold':
                    locks.append(LockLeft(dungeonX + 640, dungeonY + 280, 'gold'))
                loop = False
        elif prob == 2:
            dungeonY += 640
            for i in range(len(rooms)):
                if dungeonX == rooms[i].x and dungeonY == rooms[i].y:
                    dungeonY -= 640
                    wrongWay = True
                    break
            if not wrongWay:
                rooms.append(Room(dungeonX, dungeonY))
                horizontalDoors.append(DoorHorizontal(dungeonX + 320, dungeonY))
                if colour == 'grey':
                    locks.append(LockBottom(dungeonX + 280, dungeonY - 40, 'grey'))
                elif colour == 'red':
                    locks.append(LockBottom(dungeonX + 280, dungeonY - 40, 'red'))
                elif colour == 'gold':
                    locks.append(LockBottom(dungeonX + 280, dungeonY - 40, 'gold'))
                loop = False
        else:
            dungeonY -= 640
            for i in range(len(rooms)):
                if dungeonX == rooms[i].x and dungeonY == rooms[i].y:
                    dungeonY += 640
                    wrongWay = True
                    break
            if not wrongWay:
                rooms.append(Room(dungeonX, dungeonY))
                horizontalDoors.append(DoorHorizontal(dungeonX + 320, dungeonY + 640))
                if colour == 'grey':
                    locks.append(LockTop(dungeonX + 280, dungeonY + 640, 'grey'))
                elif colour == 'red':
                    locks.append(LockTop(dungeonX + 280, dungeonY + 640, 'red'))
                elif colour == 'gold':
                    locks.append(LockTop(dungeonX + 280, dungeonY + 640, 'gold'))
                loop = False


def tutorial():
    global inTutorial
    inTutorial = True
    ghosts.append(Ghost(100, 100))
    rooms.append(Room(0, 0))
    rooms.append(Room(0, -640))
    horizontalDoors.append(DoorHorizontal(320, 0))
    locks.append(LockTop(280, 0, 'grey'))
    keys.append(Key(300, 120, 'grey'))
    tutorialTextBoxes.append(TutorialTextBox(180, 190, ['Grey keys unlock grey doors.',
                                                        'Grey keys can each be used',
                                                        'only once']))
    tutorialTextBoxes.append(TutorialTextBox(180, 360, ['Use WASD or arrow keys to',
                                                        'move']))
    tutorialTextBoxes.append(TutorialTextBox(100, 500, ['Keys in your inventory will',
                                                        'appear here']))
    tutorialArrows.append(TutorialArrow(50, 550))
    rooms.append(Room(640, -640))
    verticalDoors.append(DoorVertical(640, -320))
    locks.append(LockRight(600, -360, 'red'))
    keys.append(Key(300, -340, 'red'))
    tutorialTextBoxes.append(TutorialTextBox(180, -280, ['Red keys unlock red doors.']))
    rooms.append(Room(640, 0))
    horizontalDoors.append(DoorHorizontal(960, 0))
    locks.append(LockBottom(920, -40, 'red'))
    tutorialTextBoxes.append(TutorialTextBox(820, -340, ['Red keys do not leave your',
                                                         'inventory after use, and can',
                                                         'be used on many doors']))
    rooms.append(Room(640, 640))
    horizontalDoors.append(DoorHorizontal(960, 640))
    locks.append(LockBottom(920, 600, 'grey'))
    keys.append(Key(940, 300, 'grey'))
    goblins.append(Goblin(940, 300))
    tutorialTextBoxes.append(TutorialTextBox(820, 190, ['Press space to attack. Often',
                                                        'a room will need to be',
                                                        'cleared of enemies before a',
                                                        'key will appear']))
    rooms.append(Room(0, 640))
    verticalDoors.append(DoorVertical(640, 960))
    locks.append(LockLeft(640, 920, 'gold'))
    keys.append(Key(940, 940, 'gold'))
    tutorialTextBoxes.append(TutorialTextBox(820, 800, ['Gold keys can be used on',
                                                        'gold doors. Only one gold',
                                                        'key and door will be found',
                                                        'in the dungeon, and will',
                                                        'always lead to the chamber',
                                                        'of Moldemort']))
    tutorialTextBoxes.append(TutorialTextBox(180, 900, ['This chamber is empty, but',
                                                        'to face the real Moldemort,',
                                                        'you must begin a new game.',
                                                        'Press ESC to enter the pause',
                                                        'menu and return to the start',
                                                        'screen']))


gameLoop = True
while gameLoop:
    pygame.time.delay(33)
    screen.fill((0, 0, 0))
    mouseX, mouseY = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.MOUSEBUTTONDOWN and not fadeOut:
            if not started:
                if 340 < mouseX < 620 and 520 < mouseY < 620:
                    started = True
                    tryLoop = True
                    while tryLoop:
                        try:
                            generate()
                            tryLoop = False
                        except:
                            continue
                if 20 < mouseX < 300 and 520 < mouseY < 620:
                    started = True
                    tutorial()
            if paused:
                if 58 < mouseX < 310 and 350 < mouseY < 440:
                    paused = False
                    pauseTransparency = 0
                    if 4 < breadCostume < 7:
                        breadCostume = 0
                    elif 11 < breadCostume < 14:
                        breadCostume = 7
                    elif 18 < breadCostume < 21:
                        breadCostume = 14
                    elif 25 < breadCostume < 28:
                        breadCostume = 21
                if 330 < mouseX < 582 and 350 < mouseY < 440:
                    fadeOut = True
            if gameOver:
                if 58 < mouseX < 310 and 350 < mouseY < 440:
                    gameOver = False
                    movingRight = False
                    movingLeft = False
                    movingUp = False
                    movingDown = False
                    attacking = False
                    breadCostume = 0
                    hitWall = False
                    placerX = 0
                    placerY = 0
                    floorX = 0
                    floorY = 0
                    roomMove = False
                    greyKeyInventory = 0
                    redKeyInventory = 0
                    goldKeyInventory = 0
                    pauseTransparency = 0
                    walls.clear()
                    floors.clear()
                    horizontalDoors.clear()
                    verticalDoors.clear()
                    locks.clear()
                    keys.clear()
                    tutorialTextBoxes.clear()
                    tutorialArrows.clear()
                    rooms.clear()
                    goblins.clear()
                    spiders.clear()
                    bread.x = 280
                    bread.y = 280
                    bread.attackAnimation = 0
                    bread.walkAnimation = 0
                    bread.diagonal = False
                    bread.hold = False
                    fadeTransparency = 0
                    fadeOut = False
                    bread.hp = 5
                    if inTutorial:
                        tutorial()
                    else:
                        tryLoop = True
                        while tryLoop:
                            try:
                                generate()
                                tryLoop = False
                            except:
                                continue
                if 330 < mouseX < 582 and 350 < mouseY < 440:
                    fadeOut = True
        if event.type == pygame.KEYDOWN and started:
            if event.key == pygame.K_SPACE and not attacking and not roomMove:
                attacking = True
                if movingUp and not movingDown:
                    breadCostume = 7
                elif movingDown and not movingUp:
                    breadCostume = 0
                elif movingRight and not movingLeft:
                    breadCostume = 14
                elif movingLeft and not movingRight:
                    breadCostume = 21
                bread.attackAnimation = 0
                break
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                movingRight = True
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                movingLeft = True
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                movingUp = True
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                movingDown = True
            elif event.key == pygame.K_ESCAPE:
                paused = True
        if event.type == pygame.KEYUP and started:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                movingRight = False
                if not movingLeft and not attacking and not paused and not gameOver:
                    breadCostume = 14
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                movingLeft = False
                if not movingRight and not attacking and not paused and not gameOver:
                    breadCostume = 21
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                movingUp = False
                if not movingDown and not attacking and not paused and not gameOver:
                    breadCostume = 7
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                movingDown = False
                if not movingUp and not attacking and not paused and not gameOver:
                    breadCostume = 0
    if not attacking and not roomMove and not paused and not gameOver:
        bread.move()
    elif attacking and not roomMove and not paused and not gameOver:
        bread.attack()
    if not roomMove and not paused and not gameOver:
        for i in range(len(goblins)):
            if goblins[i].goblinCostume < 8 and 0 <= goblins[i].x <= 640 and 0 <= goblins[i].y <= 640:
                goblins[i].move()
                goblins[i].attack()
            goblins[i].die()
            if len(goblins) == i + 1:
                break
        for i in range(len(spiders)):
            if spiders[i].costume < 3 and ((0 <= spiders[i].x <= 640 and 0 <= spiders[i].y <= 640) or spiders[i].costume
                                           == 2):
                spiders[i].move()
                spiders[i].attack()
            spiders[i].die()
            if len(spiders) == i + 1:
                break
        for i in range(len(ghosts)):
            if ghosts[i].costume < 6 and (0 <= ghosts[i].x <= 640 and 0 <= ghosts[i].y <= 640):
                ghosts[i].move()
            if len(ghosts) == i + 1:
                break
    for i in range(len(walls)):
        walls[i].bump()
    for i in range(len(horizontalDoors)):
        horizontalDoors[i].open()
    for i in range(len(verticalDoors)):
        verticalDoors[i].open()
    for i in range(len(locks)):
        locks[i].bump()
        locks[i].unlock()
        if len(locks) == i + 1:
            break
    for i in range(len(keys)):
        keys[i].hide()
    for i in range(len(keys)):
        if not keys[i].hidden:
            keys[i].collect()
        if len(keys) == i + 1:
            break
    if fadeOut:
        if fadeTransparency < 350:
            fadeTransparency += 7.5
        else:
            started = False
            paused = False
            gameOver = False
            movingRight = False
            movingLeft = False
            movingUp = False
            movingDown = False
            attacking = False
            breadCostume = 0
            hitWall = False
            placerX = 0
            placerY = 0
            floorX = 0
            floorY = 0
            roomMove = False
            greyKeyInventory = 0
            redKeyInventory = 0
            goldKeyInventory = 0
            pauseTransparency = 0
            walls.clear()
            floors.clear()
            horizontalDoors.clear()
            verticalDoors.clear()
            locks.clear()
            keys.clear()
            tutorialTextBoxes.clear()
            tutorialArrows.clear()
            rooms.clear()
            goblins.clear()
            spiders.clear()
            bread.x = 280
            bread.y = 280
            bread.attackAnimation = 0
            bread.walkAnimation = 0
            bread.diagonal = False
            bread.hold = False
            fadeTransparency = 0
            fadeOut = False
            inTutorial = False
            bread.hp = 5
    if not started:
        screen.fill((100, 100, 100))
        screen.blit(breadArtImg, (320, 0))
        for i in range(len(startScreenText)):
            screen.blit(font.render(startScreenText[i], True, (0, 0, 0)), (20, 30*i + 30))
        if 340 < mouseX < 620 and 520 < mouseY < 620:
            screen.blit(startButtonHoverImg, (340, 520))
        else:
            screen.blit(startButtonImg, (340, 520))
        if 20 < mouseX < 300 and 520 < mouseY < 620:
            screen.blit(tutorialButtonHoverImg, (20, 520))
        else:
            screen.blit(tutorialButtonImg, (20, 520))
    if started:
        for i in range(len(floors)):
            screen.blit(floorTileImg, (floors[i].x, floors[i].y))
        for i in range(len(walls)):
            screen.blit(brickBlockImg, (walls[i].x, walls[i].y))
        for i in range(len(tutorialTextBoxes)):
            pygame.draw.rect(screen, (100, 100, 100), (tutorialTextBoxes[i].x - 10, tutorialTextBoxes[i].y - 10, 300,
                                                       (20 * len(tutorialTextBoxes[i].text)) + 20))
            for j in range(len(tutorialTextBoxes[i].text)):
                screen.blit(font.render(tutorialTextBoxes[i].text[j], True, (0, 0, 0)), (tutorialTextBoxes[i].x, 20*j +
                                                                                         tutorialTextBoxes[i].y))
        for i in range(len(tutorialArrows)):
            screen.blit(arrowImg, (tutorialArrows[i].x, tutorialArrows[i].y))
        if -1 < breadCostume < 14:
            screen.blit(breadImgs[breadCostume], (bread.x, bread.y))
        elif 13 < breadCostume < 21:
            screen.blit(breadImgs[breadCostume], (bread.x, bread.y - 7))
        else:
            screen.blit(breadImgs[breadCostume], (bread.x, bread.y + 7))
        for i in range(len(locks)):
            if locks[i].colour == 'grey':
                if type(locks[i]) == LockTop:
                    screen.blit(greyDoorImg, (locks[i].x, locks[i].y))
                elif type(locks[i]) == LockRight:
                    screen.blit(pygame.transform.rotate(greyDoorImg, -90), (locks[i].x, locks[i].y))
                elif type(locks[i]) == LockLeft:
                    screen.blit(pygame.transform.rotate(greyDoorImg, 90), (locks[i].x, locks[i].y))
                else:
                    screen.blit(pygame.transform.rotate(greyDoorImg, 180), (locks[i].x, locks[i].y))
            if locks[i].colour == 'red':
                if type(locks[i]) == LockTop:
                    screen.blit(redDoorImg, (locks[i].x, locks[i].y))
                elif type(locks[i]) == LockRight:
                    screen.blit(pygame.transform.rotate(redDoorImg, -90), (locks[i].x, locks[i].y))
                elif type(locks[i]) == LockLeft:
                    screen.blit(pygame.transform.rotate(redDoorImg, 90), (locks[i].x, locks[i].y))
                else:
                    screen.blit(pygame.transform.rotate(redDoorImg, 180), (locks[i].x, locks[i].y))
            if locks[i].colour == 'gold':
                if type(locks[i]) == LockTop:
                    screen.blit(goldDoorImg, (locks[i].x, locks[i].y))
                elif type(locks[i]) == LockRight:
                    screen.blit(pygame.transform.rotate(goldDoorImg, -90), (locks[i].x, locks[i].y))
                elif type(locks[i]) == LockLeft:
                    screen.blit(pygame.transform.rotate(goldDoorImg, 90), (locks[i].x, locks[i].y))
                else:
                    screen.blit(pygame.transform.rotate(goldDoorImg, 180), (locks[i].x, locks[i].y))
        for i in range(len(keys)):
            if keys[i].colour == 'grey' and not keys[i].hidden:
                screen.blit(greyKeyImg, (keys[i].x, keys[i].y))
            if keys[i].colour == 'red' and not keys[i].hidden:
                screen.blit(redKeyImg, (keys[i].x, keys[i].y))
            if keys[i].colour == 'gold' and not keys[i].hidden:
                screen.blit(goldKeyImg, (keys[i].x, keys[i].y))
        for i in range(greyKeyInventory):
            screen.blit(greyKeyImg, (40 * i, 600))
        for i in range(redKeyInventory):
            screen.blit(redKeyImg, ((greyKeyInventory * 40) + (i * 40), 600))
        for i in range(goldKeyInventory):
            screen.blit(goldKeyImg, ((greyKeyInventory * 40) + (redKeyInventory * 40) + (i * 40), 600))
        for i in range(len(goblins)):
            screen.blit(goblinImgs[goblins[i].goblinCostume], (goblins[i].x, goblins[i].y))
        for i in range(len(spiders)):
            screen.blit(spiderImgs[spiders[i].costume], (spiders[i].x, spiders[i].y))
        for i in range(len(ghosts)):
            screen.blit(ghostImgs[ghosts[i].costume], (ghosts[i].x, ghosts[i].y))
        for i in range(bread.hp):
            screen.blit(heartImg, (600 - (i * 40), 600))
        if bread.hp < 1:
            gameOver = True
            breadCostume = 28
    if paused:
        if pauseTransparency < 255:
            pauseTransparency = pauseTransparency + 25.5
        pauseScreenImg.set_alpha(pauseTransparency)
        startScreenButtonImg.set_alpha(pauseTransparency)
        continueButtonImg.set_alpha(pauseTransparency)
        startScreenButtonHoverImg.set_alpha(pauseTransparency)
        continueButtonHoverImg.set_alpha(pauseTransparency)
        screen.blit(pauseScreenImg, (20, 160))
        screen.blit(bigFont.render('Paused', True, (0, 0, 0)), (225, 180))
        if 58 < mouseX < 310 and 350 < mouseY < 440 and not fadeOut:
            screen.blit(continueButtonHoverImg, (58, 350))
        else:
            screen.blit(continueButtonImg, (58, 350))
        if 330 < mouseX < 582 and 350 < mouseY < 440 and not fadeOut:
            screen.blit(startScreenButtonHoverImg, (330, 350))
        else:
            screen.blit(startScreenButtonImg, (330, 350))
    if gameOver:
        if pauseTransparency < 255:
            pauseTransparency = pauseTransparency + 25.5
        pauseScreenImg.set_alpha(pauseTransparency)
        startScreenButtonImg.set_alpha(pauseTransparency)
        continueButtonImg.set_alpha(pauseTransparency)
        startScreenButtonHoverImg.set_alpha(pauseTransparency)
        continueButtonHoverImg.set_alpha(pauseTransparency)
        screen.blit(pauseScreenImg, (20, 160))
        screen.blit(bigFont.render('Game Over', True, (150, 0, 0)), (175, 180))
        screen.blit(deadBreadImg, (280, 240))
        if 58 < mouseX < 310 and 350 < mouseY < 440 and not fadeOut:
            screen.blit(continueButtonHoverImg, (58, 350))
        else:
            screen.blit(continueButtonImg, (58, 350))
        if 330 < mouseX < 582 and 350 < mouseY < 440 and not fadeOut:
            screen.blit(startScreenButtonHoverImg, (330, 350))
        else:
            screen.blit(startScreenButtonImg, (330, 350))
    fadeOutScreenImg.set_alpha(fadeTransparency)
    screen.blit(fadeOutScreenImg, (0, 0))
    pygame.display.update()
pygame.quit()
