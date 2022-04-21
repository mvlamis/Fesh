from turtle import back
import pygame
import time

pygame.init()
pygame.font.init()

global debug
debug = False

display_width = 960
display_height = 544
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('lil dude man')

global xPos
global yPos

black = (0,0,0)
white = (255,255,255)
xPos = (-401)
yPos = (-401)
speed = 1

font = pygame.font.Font('freesansbold.ttf', 32)

playerSize = 32

counter = 0

clock = pygame.time.Clock()
hasStarted = False
playerImg = pygame.image.load('char/Walk/Down/images/Char_walk_down_01.png')
playerImg = pygame.transform.scale(playerImg, (playerSize,playerSize))

downImages = ['char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_04.png','char/Walk/Down/images/Char_walk_down_04.png','char/Walk/Down/images/Char_walk_down_04.png','char/Walk/Down/images/Char_walk_down_04.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_06.png','char/Walk/Down/images/Char_walk_down_06.png','char/Walk/Down/images/Char_walk_down_06.png','char/Walk/Down/images/Char_walk_down_06.png','char/Walk/Down/images/Char_walk_down_06.png']
leftImages = ['char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_04.png','char/Walk/Left/images/Char_walk_left_04.png','char/Walk/Left/images/Char_walk_left_04.png','char/Walk/Left/images/Char_walk_left_04.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_06.png','char/Walk/Left/images/Char_walk_left_06.png','char/Walk/Left/images/Char_walk_left_06.png','char/Walk/Left/images/Char_walk_left_06.png','char/Walk/Left/images/Char_walk_left_06.png']
rightImages = ['char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_04.png','char/Walk/Right/images/Char_walk_right_04.png','char/Walk/Right/images/Char_walk_right_04.png','char/Walk/Right/images/Char_walk_right_04.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_06.png','char/Walk/Right/images/Char_walk_right_06.png','char/Walk/Right/images/Char_walk_right_06.png','char/Walk/Right/images/Char_walk_right_06.png','char/Walk/Right/images/Char_walk_right_06.png']
upImages = ['char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_06.png','char/Walk/Up/images/Char_walk_up_06.png','char/Walk/Up/images/Char_walk_up_06.png','char/Walk/Up/images/Char_walk_up_06.png','char/Walk/Up/images/Char_walk_up_06.png']

cloud1 = pygame.image.load('images/cloud1.png')
cloud2 = pygame.image.load('images/cloud2.png')
cloud1 = pygame.transform.scale(cloud1, (37 * 15,21 * 15)).convert()
cloud2 = pygame.transform.scale(cloud2, (37 * 15,21 * 15)).convert()
cloud1_x = -600
cloud2_x = 1200

menuBg = pygame.image.load('images/menubg.png')
menuBg = menuBg.convert()

startButton = pygame.image.load('images/slay.png')
optionsButton = pygame.image.load('images/options.png')
optionsButton = pygame.transform.scale(optionsButton, (100,50))
global options 
options = False

gameMap = pygame.image.load('images/map.png')
gameMap = pygame.transform.scale(gameMap, (display_width * 2, display_height * 2))
gameMap.set_alpha(0)
mapAlpha = 0

global debugColor
debugColor = white


backText = font.render('Back', True, white)
quitText = font.render('Quit', True, white)

def rightCollide(x,y1,y2):
    global xPos
    global yPos
    if xPos == x:
        if yPos <= y1 and yPos >= y2:
            xPos = xPos - speed
            
def leftCollide(x,y1,y2):
    global xPos
    global yPos
    if xPos == x:
        if yPos <= y1 and yPos >= y2:
            xPos = xPos + speed

def topCollide(y,x1,x2):
    global xPos
    global yPos
    if yPos == y:
        if xPos <= x1 and xPos >= x2:
            yPos = yPos + speed

def bottomCollide(y,x1,x2):
    global xPos
    global yPos
    if yPos == y:
        if xPos <= x1 and xPos >= x2:
            yPos = yPos - speed


# menu screen
while not hasStarted:
    debugText = font.render('Debug mode', True, debugColor)
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(mouse[0], mouse[1])
            # options button
            if mouse[0] > 440 and mouse[0] < 520 and mouse[1] > 300 and mouse[1] < 370:
                options = True
                print("options")

            # start button
            if mouse[0] > display_width/2 - startButton.get_width()/2 and mouse[1] > display_height/2 - startButton.get_height()/2 and mouse[0] < display_width/2 + startButton.get_width()/2 and mouse[1] < display_height/2 + startButton.get_height()/2:
                while mapAlpha < 255:
                    gameDisplay.blit(menuBg, (0,0))
                    cloud1_x += 7
                    cloud2_x -= 7
                    gameDisplay.blit(cloud1, (cloud1_x, 0))
                    gameDisplay.blit(cloud2, (cloud2_x, 21 * 15))
                    gameMap.set_alpha(mapAlpha)
                    mapAlpha += 1
                    gameDisplay.blit(gameMap, (xPos, yPos))
                    cloud1.set_alpha(255)
                    cloud2.set_alpha(255)
                    pygame.display.update()

                
                print("start")
                hasStarted = True


    gameDisplay.fill(white)
    gameDisplay.blit(menuBg, (0,0))
    gameDisplay.blit(gameMap, (xPos,yPos))

    if options == True:
        gameDisplay.blit(menuBg, (0,0))
        gameDisplay.blit(debugText, (150,150))
        gameDisplay.blit(backText, (150,450))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # debug button
                if options == True and mouse[0] > 150 and mouse[0] < 350 and mouse[1] > 150 and mouse[1] < 190:
                    debug = not debug
                
                # back button
                if options == True and mouse[0] > 150 and mouse[0] < 230 and mouse[1] > 450 and mouse[1] < 480:
                    options = False
                    
        if debug:
            debugColor = (0,255,0)
        else:
            debugColor = white
    else:
        if hasStarted == False:
            gameDisplay.blit(startButton, (display_width/2 - startButton.get_width()/2, display_height/2 - startButton.get_height()/2))
            gameDisplay.blit(optionsButton, (430,330))
    pygame.display.update()
    clock.tick(60)
    pygame.event.pump()

# game loop
while hasStarted:
    text = font.render("Position: " + str(xPos) + ", " + str(yPos) + " | Speed: " + str(speed) + " | FPS: ", True, white)
    debugText = font.render('Debug mode', True, debugColor)
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hasStarted = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                options = not options

    keys = pygame.key.get_pressed()  #checking pressed keys

    if keys[pygame.K_UP]:
        yPos += speed
        counter = (counter + 1) % len(upImages)
        playerImg = pygame.image.load(upImages[counter])
        playerImg = pygame.transform.scale(playerImg, (playerSize,playerSize))
    if keys[pygame.K_DOWN]:
        yPos -= speed
        counter = (counter + 1) % len(downImages)
        playerImg = pygame.image.load(downImages[counter])
        playerImg = pygame.transform.scale(playerImg, (playerSize,playerSize))
    if keys[pygame.K_LEFT]:
        xPos += speed
        counter = (counter + 1) % len(leftImages)
        playerImg = pygame.image.load(leftImages[counter])
        playerImg = pygame.transform.scale(playerImg, (playerSize,playerSize))
    if keys[pygame.K_RIGHT]:
        xPos -= speed
        counter = (counter + 1) % len(rightImages)
        playerImg = pygame.image.load(rightImages[counter])
        playerImg = pygame.transform.scale(playerImg, (playerSize,playerSize))
    
    # debug mode
    if debug == True:
        text = font.render("Position: " + str(xPos) + ", " + str(yPos) + " | Speed: " + str(speed) + " | FPS: " + str(int(clock.get_fps())), True, white)
        if keys[pygame.K_RIGHTBRACKET]:
            speed += 1
        if keys[pygame.K_LEFTBRACKET]:
            speed -= 1
        if keys[pygame.K_BACKSLASH]:
            speed = 1


    # left border
    if xPos > 500:
        xPos = xPos - speed

    # right border
    if xPos < -1425:
        xPos = xPos + speed

    # top border
    if yPos > 300:
        yPos = yPos - speed

    # bottom border
    if yPos < -785:
        yPos = yPos + speed


    # tent border
    rightCollide(-316,-318,-385)
    leftCollide(-230,-318,-385)
    topCollide(-318,-230,-316)
    bottomCollide(-385,-230,-316)



    # house right border
    if xPos == 195 and yPos < 87 and yPos > -160:
        xPos = xPos - speed

    # house left border
    if xPos == 420 and yPos < 87 and yPos > -160:
        xPos = xPos + speed

    # house top border
    if yPos == 87 and xPos < 420 and xPos > 195:
        yPos = yPos + speed

    # house bottom border
    if yPos == -160 and xPos < 420 and xPos > 195:
        yPos = yPos - speed

    if options == True:
        clock.tick(60)
        gameDisplay.blit(menuBg, (0,0))
        gameDisplay.blit(debugText, (150,150))
        gameDisplay.blit(backText, (150,450))
        gameDisplay.blit(quitText, (700,450))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # debug button
                if options == True and mouse[0] > 150 and mouse[0] < 350 and mouse[1] > 150 and mouse[1] < 190:
                    debug = not debug
                
                # back button
                if options == True and mouse[0] > 150 and mouse[0] < 230 and mouse[1] > 450 and mouse[1] < 480:
                    options = False

                # quit button
                if options == True and mouse[0] > 700 and mouse[0] < 800 and mouse[1] > 450 and mouse[1] < 480:
                    hasStarted = False
    
        if debug:
            debugColor = (0,255,0)
        else:
            debugColor = white
    else:
        gameDisplay.fill(black)
        gameDisplay.blit(gameMap, (xPos,yPos))
        gameDisplay.blit(playerImg, (display_width / 2, display_height / 2))
    if debug == True:
        gameDisplay.blit(text, (0, 0))
        

    pygame.display.update()
    clock.tick(60)
    pygame.event.pump()

pygame.quit()
quit()