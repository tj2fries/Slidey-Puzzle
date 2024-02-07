import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1344, 672))
TopLeftCornerImg = pygame.image.load('Top Left Corner.png')
TopLeftMiddleImg = pygame.image.load('Top Left Middle.png')
TopRightMiddleImg = pygame.image.load('Top Right Middle.png')
TopRightCornerImg = pygame.image.load('Top Right Corner.png')
UpperLeftSideImg = pygame.image.load('Upper Left Side.png')
CenterTopLeftImg = pygame.image.load('Center Top Left.png')
CenterTopRightImg = pygame.image.load('Center Top Right.png')
UpperRightSideImg = pygame.image.load('Upper Right Side.png')
LowerLeftSideImg = pygame.image.load('Lower Left Side.png')
CenterBottomLeftImg = pygame.image.load('Center Bottom Left.png')
CenterBottomRightImg = pygame.image.load('Center Bottom Right.png')
LowerRightSideImg = pygame.image.load('Lower Right Side.png')
BottomLeftCornerImg = pygame.image.load('Bottom Left Corner.png')
BottomLeftMiddleImg = pygame.image.load('Bottom Left Middle.png')
BottomRightMiddleImg = pygame.image.load('Bottom Right Middle.png')
BottomRightCornerImg = pygame.image.load('Bottom Right Corner.png')
FullMetroidImg = pygame.image.load('pixil-frame-0.png')
FullMetroidImg = pygame.transform.scale(FullMetroidImg, (500, 500))
TitleScreenImg = pygame.image.load('Title Screen.png')
TitleScreenImg = pygame.transform.scale(TitleScreenImg, (1344, 672))
Background = pygame.image.load('Background.png')
StartButtonImg = pygame.image.load('Start Button.png')
StartButtonHoverImg = pygame.image.load('Start Button(Hover).png')
RestartButtonImg = pygame.image.load('Restart Button.png')
RestartButtonImg = pygame.transform.scale(RestartButtonImg, (224, 100))
RestartButtonHoverImg = pygame.image.load('Restart Button(Hover).png')
RestartButtonHoverImg = pygame.transform.scale(RestartButtonHoverImg, (224, 100))
ContinueButtonImg = pygame.image.load('Continue Button.png')
ContinueButtonImg = pygame.transform.scale(ContinueButtonImg, (224, 100))
ContinueButtonHoverImg = pygame.image.load('Continue Button(Hover).png')
ContinueButtonHoverImg = pygame.transform.scale(ContinueButtonHoverImg, (224, 100))
VolumeSliderImg = pygame.image.load('Volume Slider.png')
VolumeSliderImg = pygame.transform.scale(VolumeSliderImg, (420, 75))
VolumeKnobImg = pygame.image.load('Volume Knob.png')
WinScreen = pygame.image.load('Win Screen.png')
PauseMenu = pygame.image.load('Pause Menu.png')
font = pygame.font.Font('freesansbold.ttf', 32)
timer = font.render('0:00', True, (255, 0, 0))
finalTime = font.render('0:00', True, (255, 0, 0))
pygame.display.set_caption('Metroid Puzzle')
pygame.display.set_icon(FullMetroidImg)
pygame.mixer.music.set_volume(.0)
tileimgs = [TopLeftCornerImg, TopLeftMiddleImg, TopRightMiddleImg, UpperLeftSideImg, CenterTopLeftImg,
            CenterTopRightImg, UpperRightSideImg, LowerLeftSideImg, CenterBottomLeftImg, CenterBottomRightImg,
            LowerRightSideImg, BottomLeftCornerImg, BottomLeftMiddleImg, BottomRightMiddleImg, BottomRightCornerImg]
moving = 0
win = 0
paused = 0
seconds = 0
dececonds = 0
minutes = 0
transparency = 0
screenTransparency = 0
pauseTransparency = 0
started = 0
startTime = 0
pauseTime = 0
volAdjust = 0
music = pygame.mixer.music.load('Super_Metroid_Music_-_Title_Theme_(getmp3.pro).mp3')
pygame.mixer.music.play(-1)
playlist = ['Super Metroid Music - Crateria Main theme.mp3', 'Super Metroid Music - Brinstar (Underground Depths).mp3',
            'Super Metroid Music - Brinstar (The Jungle Floor).mp3',
            'Super Metroid Music - Norfair (Ridley\'s Lair).mp3', 'Vs. Ridley [Super Metroid].mp3']
class VolumeKnob:
    def __init__(self):
        self.x = 1200
        self.y = 616
class tile:
    def __init__(self):
        if i < 3:
            self.x = 168*(i%4)
        else:
            self.x = 168*((i+1)%4)
        self.y = 168*(int((i+1)/4))
        self.movingr = 0
        self.movingl = 0
        self.movingu = 0
        self.movingd = 0
    def moveRight(self):
        self.blocked = 0
        for i in range(len(tiles)):
            if self.x + 168 == tiles[i].x and self.y == tiles[i].y:
                self.blocked = 1
            if self.x == 504:
                self.blocked = 1
    def moveLeft(self):
        self.blocked = 0
        for i in range(len(tiles)):
            if self.x - 168 == tiles[i].x and self.y == tiles[i].y:
                self.blocked = 1
            if self.x == 0:
                self.blocked = 1
    def moveUp(self):
        self.blocked = 0
        for i in range(len(tiles)):
            if self.y - 168 == tiles[i].y and self.x == tiles[i].x:
                self.blocked = 1
            if self.y == 0:
                self.blocked = 1
    def moveDown(self):
        self.blocked = 0
        for i in range(len(tiles)):
            if self.y + 168 == tiles[i].y and self.x == tiles[i].x:
                self.blocked = 1
            if self.y == 504:
                self.blocked = 1
def shiftRight():
    for x in range(len(tiles)):
        tiles[x].moveRight()
    for x in range(len(tiles)):
        if tiles[x].blocked == 0:
            tiles[x].x = tiles[x].x + 168
def shiftLeft():
    for x in range(len(tiles)):
        tiles[x].moveLeft()
    for x in range(len(tiles)):
        if tiles[x].blocked == 0:
            tiles[x].x = tiles[x].x - 168
def shiftUp():
    for x in range(len(tiles)):
        tiles[x].moveUp()
    for x in range(len(tiles)):
        if tiles[x].blocked == 0:
            tiles[x].y = tiles[x].y - 168
def shiftDown():
    for x in range(len(tiles)):
        tiles[x].moveDown()
    for x in range(len(tiles)):
        if tiles[x].blocked == 0:
            tiles[x].y = tiles[x].y + 168
def randomize():
    for i in range(1000):
        direction = random.randint(1, 4)
        if direction == 1:
            shiftRight()
        elif direction == 2:
            shiftLeft()
        elif direction == 3:
            shiftUp()
        elif direction == 4:
            shiftDown()
    loop = True
    while loop:
        cornerEmpty = 15
        direction = random.randint(1, 4)
        if direction == 1:
            shiftRight()
        elif direction == 2:
            shiftLeft()
        elif direction == 3:
            shiftUp()
        elif direction == 4:
            shiftDown()
        for i in range(len(tiles)):
            if tiles[i].x == 504 and tiles[i].y == 0:
                loop = True
            else:
                cornerEmpty = cornerEmpty - 1
        if cornerEmpty == 0:
            loop = False
tiles = []
for i in range(15):
    tiles.append(tile())
randomize()
volumeKnob = VolumeKnob()
loop = True
while loop:
    pygame.time.delay(10)
    correctTiles = 0
    mouseX, mouseY = pygame.mouse.get_pos()
    if started == 0:
        pygame.mixer.music.set_volume((volumeKnob.x-1100)/200)
    else:
        pygame.mixer.music.set_volume((volumeKnob.x-638)/200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN and win == 0 and moving == 0 and started == 1:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                for x in range(len(tiles)):
                    tiles[x].moveRight()
                for x in range(len(tiles)):
                    if tiles[x].blocked == 0:
                        tiles[x].movingr = 1
                        moving = 1
                break
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                for x in range(len(tiles)):
                    tiles[x].moveLeft()
                for x in range(len(tiles)):
                    if tiles[x].blocked == 0:
                        tiles[x].movingl = 1
                        moving = 1
                break
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                for x in range(len(tiles)):
                    tiles[x].moveUp()
                for x in range(len(tiles)):
                    if tiles[x].blocked == 0:
                        tiles[x].movingu = 1
                        moving = 1
                break
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                for x in range(len(tiles)):
                    tiles[x].moveDown()
                for x in range(len(tiles)):
                    if tiles[x].blocked == 0:
                        tiles[x].movingd = 1
                        moving = 1
                break
            elif event.key == pygame.K_ESCAPE and started == 1 and win == 0:
                paused = 1
                pauseTime = pygame.time.get_ticks()
                break
        if event.type == pygame.MOUSEBUTTONDOWN:
            if started == 0:
                if volumeKnob.x < mouseX < volumeKnob.x + 37 and volumeKnob.y < mouseY < volumeKnob.y + 37:
                    volAdjust = 1
                if 504 < mouseX < 840 and 475 < mouseY < 625:
                    started = 1
                    volumeKnob.x = volumeKnob.x - 462
                    volumeKnob.y = 279
                    startTime = pygame.time.get_ticks()
                    music = pygame.mixer.music.load(playlist[random.randint(0,4)])
                    pygame.mixer.music.play(-1)
            elif win == 1 and pygame.time.get_ticks() - startTime > 2000:
                if 560 < mouseX < 784 and 360 < mouseY < 460:
                    startTime = pygame.time.get_ticks()
                    moving = 0
                    win = 0
                    seconds = 0
                    dececonds = 0
                    minutes = 0
                    transparency = 0
                    screenTransparency = 0
                    randomize()
                    music = pygame.mixer.music.load(playlist[random.randint(0, 4)])
                    pygame.mixer.music.play(-1)
            elif paused == 1:
                if volumeKnob.x < mouseX < volumeKnob.x + 37 and volumeKnob.y < mouseY < volumeKnob.y + 37:
                    volAdjust = 1
                if 392 < mouseX < 616 and 360 < mouseY < 460:
                    startTime = pygame.time.get_ticks()
                    moving = 0
                    win = 0
                    seconds = 0
                    dececonds = 0
                    minutes = 0
                    transparency = 0
                    screenTransparency = 0
                    paused = 0
                    randomize()
                    music = pygame.mixer.music.load(playlist[random.randint(0, 4)])
                    pygame.mixer.music.play(-1)
                if 728 < mouseX < 952 and 360 < mouseY < 460:
                    paused = 0
                    startTime = startTime + (pygame.time.get_ticks() - pauseTime)
        if event.type == pygame.MOUSEBUTTONUP:
            volAdjust = 0
    if 0 < moving < 5:
        for i in range(len(tiles)):
            if tiles[i].movingr == 1:
                tiles[i].x = tiles[i].x + 42
                moving = moving + 1
            elif tiles[i].movingl == 1:
                tiles[i].x = tiles[i].x - 42
                moving = moving + 1
            elif tiles[i].movingu == 1:
                tiles[i].y = tiles[i].y - 42
                moving = moving + 1
            elif tiles[i].movingd == 1:
                tiles[i].y = tiles[i].y + 42
                moving = moving + 1
    else:
        moving = 0
        for i in range(len(tiles)):
            tiles[i].movingr = 0
            tiles[i].movingl = 0
            tiles[i].movingu = 0
            tiles[i].movingd = 0
    for i in range(len(tiles)):
        if i < 3:
            if tiles[i].x == 168 * (i % 4) and tiles[i].y == 168 * (int((i+1) / 4)):
                correctTiles = correctTiles + 1
        else:
            if tiles[i].x == 168 * ((i+1) % 4) and tiles[i].y == 168 * (int((i+1) / 4)):
                correctTiles = correctTiles + 1
    if volAdjust == 1 and started == 0:
        if 1118 < mouseX < 1318:
            volumeKnob.x = mouseX - 18
        elif mouseX <= 1118:
            volumeKnob.x = 1100
        else:
            volumeKnob.x = 1300
    if volAdjust == 1 and paused == 1:
        if 656 < mouseX < 856:
            volumeKnob.x = mouseX - 18
        elif mouseX <= 656:
            volumeKnob.x = 638
        else:
            volumeKnob.x = 838
    screen.fill((0, 0, 0))
    if started == 0:
        screen.blit(TitleScreenImg, (0, 0))
        screen.blit(VolumeSliderImg, (924, 597))
        screen.blit(VolumeKnobImg, (volumeKnob.x, volumeKnob.y))
        if 504 < mouseX < 840 and 475 < mouseY < 625:
            screen.blit(StartButtonHoverImg, (504, 475))
        else:
            screen.blit(StartButtonImg, (504, 475))
    elif win == 0 and paused == 0:
        screen.blit(Background, (0, 0))
        for i in range(len(tiles)):
            screen.blit(tileimgs[i], (tiles[i].x, tiles[i].y))
        if correctTiles == 15:
            win = 1
            startTime = pygame.time.get_ticks()
            finalTime = font.render('Your time was ' + str(minutes) + ':' + str(dececonds) + str(seconds), True,
                                    (255, 0, 0))
        screen.blit(FullMetroidImg, (758, 86))
        if pygame.time.get_ticks() - startTime > 999:
            seconds = seconds + 1
            startTime = pygame.time.get_ticks()
        if seconds > 9:
            dececonds = dececonds + 1
            seconds = 0
        if dececonds > 5:
            minutes = minutes + 1
            dececonds = 0
        timer = font.render(str(minutes) + ':' + str(dececonds) + str(seconds), True, (255, 0, 0))
        screen.blit(timer, (975, 25))
    elif win == 0 and paused == 1:
        screen.blit(Background, (0, 0))
        for i in range(len(tiles)):
            screen.blit(tileimgs[i], (tiles[i].x, tiles[i].y))
        if pauseTransparency < 255:
            pauseTransparency = pauseTransparency + 10.2
        PauseMenu.set_alpha(pauseTransparency)
        RestartButtonImg.set_alpha(pauseTransparency)
        RestartButtonHoverImg.set_alpha(pauseTransparency)
        ContinueButtonImg.set_alpha(pauseTransparency)
        ContinueButtonHoverImg.set_alpha(pauseTransparency)
        VolumeSliderImg.set_alpha(pauseTransparency)
        VolumeKnobImg.set_alpha(pauseTransparency)
        screen.blit(FullMetroidImg, (758, 86))
        screen.blit(timer, (975, 25))
        screen.blit(PauseMenu, (336, 168))
        screen.blit(VolumeSliderImg, (462, 260))
        screen.blit(VolumeKnobImg, (volumeKnob.x, volumeKnob.y))
        if 392 < mouseX < 616 and 360 < mouseY < 460:
            screen.blit(RestartButtonHoverImg, (392, 360))
        else:
            screen.blit(RestartButtonImg, (392, 360))
        if 728 < mouseX < 952 and 360 < mouseY < 460:
            screen.blit(ContinueButtonHoverImg, (728, 360))
        else:
            screen.blit(ContinueButtonImg, (728, 360))
    else:
        screen.blit(Background, (0, 0))
        for i in range(len(tiles)):
            screen.blit(tileimgs[i], (tiles[i].x, tiles[i].y))
        if pygame.time.get_ticks() - startTime > 250 and transparency < 255:
            transparency = transparency + 5.1
        if pygame.time.get_ticks() - startTime > 1500 and screenTransparency < 255:
            screenTransparency = screenTransparency + 5.1
        TopRightCornerImg.set_alpha(transparency)
        WinScreen.set_alpha(screenTransparency)
        RestartButtonImg.set_alpha(screenTransparency)
        RestartButtonHoverImg.set_alpha(screenTransparency)
        finalTime.set_alpha(screenTransparency)
        screen.blit(TopRightCornerImg, (504, 0))
        screen.blit(FullMetroidImg, (758, 86))
        screen.blit(timer, (975, 25))
        screen.blit(WinScreen, (336, 168))
        if 560 < mouseX < 784 and 360 < mouseY < 460:
            screen.blit(RestartButtonHoverImg, (560, 360))
        else:
            screen.blit(RestartButtonImg, (560, 360))
        screen.blit(finalTime, (530, 290))
    pygame.display.update()
pygame.quit()
