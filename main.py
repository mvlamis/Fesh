from turtle import back, left
import pygame
import time

pygame.init()
pygame.font.init()

global debug
debug = True

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

font = pygame.font.Font('inter.ttf', 32, bold = True)
dialoguefont = pygame.font.Font('inter.ttf', 24)
dialoguetext = ''

playerSize = 32
npcImg = pygame.image.load('images/npc.png')
npcImg = pygame.transform.scale(npcImg, (playerSize,playerSize))
npcRect = pygame.Rect(xPos + 420,yPos + 200,npcImg.get_width(),npcImg.get_height())
counter = 0

clock = pygame.time.Clock()
hasStarted = False
playerImg = pygame.image.load('char/Walk/Down/images/Char_walk_down_01.png')
playerImg = pygame.transform.scale(playerImg, (playerSize,playerSize))
playerRect = pygame.Rect(display_width/2, display_height/2, playerSize, playerSize)
location = "outside"

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

mapImg = 'images/map.png'
gameMap = pygame.image.load(mapImg)
mapRect = gameMap.get_rect()
gameMap = pygame.transform.scale(gameMap, (display_width * 2, display_height * 2))
gameMap.set_alpha(0)
mapAlpha = 0

dialoguebox = pygame.image.load('images/dialoguebox.png')

global debugColor
debugColor = white


backText = font.render('Back', True, white)
quitText = font.render('Quit', True, white)

def dialogue(text):
    dialogueText = dialoguefont.render(str(text), True, white)
    gameDisplay.blit(dialoguebox, (0,0))
    gameDisplay.blit(dialogueText, (100,400))



def rightCollide(x,y1,y2, action=None):
    global xPos
    global yPos
    if xPos == x:
        if yPos <= y1 and yPos >= y2:
            xPos = xPos - speed
            if action != None:
                action()
            
def leftCollide(x,y1,y2, action=None):
    global xPos
    global yPos
    if xPos == x:
        if yPos <= y1 and yPos >= y2:
            xPos = xPos + speed
            if action != None:
                action()

def topCollide(y,x1,x2, action=None):
    global xPos
    global yPos
    if yPos == y:
        if xPos <= x1 and xPos >= x2:
            yPos = yPos + speed
            if action != None:
                action()

def bottomCollide(y,x1,x2, action=None):
    global xPos
    global yPos
    if yPos == y:
        if xPos <= x1 and xPos >= x2:
            yPos = yPos - speed
            if action != None:
                action()

def enterHouse():
    global dialoguetext
    global xPos
    global yPos
    global mapImg
    global location
    location = 'house'
    mapImg = 'images/house.png'
    print('Entering house')
    xPos = 210
    yPos = -196

def enterOutside():
    global xPos
    global yPos
    global mapImg
    global location
    location = 'outside'
    mapImg = 'images/map.png'
    print('Entering outside')
    xPos = 304
    yPos = -170

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
    gameMap = pygame.image.load(mapImg)
    text = font.render("Position: " + str(xPos) + ", " + str(yPos) + " | Speed: " + str(speed) + " | FPS: ", True, white)
    debugText = font.render('Debug mode', True, debugColor)
    mouse = pygame.mouse.get_pos()
    gameMap = pygame.transform.scale(gameMap, (display_width * 2, display_height * 2))

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
    if keys[pygame.K_SPACE]:
        dialoguetext = ''
    
    # debug mode
    if debug == True:
        text = font.render("Position: " + str(xPos) + ", " + str(yPos) + " | Speed: " + str(speed) + " | FPS: " + str(int(clock.get_fps())), True, white)
        if keys[pygame.K_RIGHTBRACKET]:
            speed += 1
        if keys[pygame.K_LEFTBRACKET]:
            speed -= 1
        if keys[pygame.K_BACKSLASH]:
            speed = 1

    if location == 'outside': # OUTSIDE COLLISIONS

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

        # house border
        rightCollide(195,87,-160)
        leftCollide(420,87,-160)
        topCollide(87,420,195)
        bottomCollide(-160,420,195, enterHouse)


        # water border
        leftCollide(-103,20,-150)
        bottomCollide(-150,-103,-1000)
        leftCollide(-974,-626,-1000)
        leftCollide(-879,-441,-627)
        leftCollide(-845,-224,-441)
        leftCollide(-806,-150,-224)
        bottomCollide(-224,-806,-1000)
        bottomCollide(-441,-845,-1000)
        bottomCollide(-627,-879,-1000)
        topCollide(20,-103,-1000)
        leftCollide(-131,115,20)
        leftCollide(-164,365,111)
        topCollide(112,-130,-1000)

        # pond border
        leftCollide(-551,-625,-724)
        leftCollide(-585,-724,-760)
        bottomCollide(-724,-551,-585)
        bottomCollide(-760,-585,-730)
        topCollide(-625,-551,-666)
        topCollide(-654,-666,-700)

    if location == 'house': # HOUSE COLLISIONS
        bottomCollide(73,434,131)
        bottomCollide(202,131,-41)
        leftCollide(-41,202,-144)
        rightCollide(130,202,73)
        rightCollide(434,73,-144)
        topCollide(-144,434,227)
        topCollide(-144,187,-41)
        bottomCollide(-207,227,187, enterOutside)

        # npc collision
        if playerRect.colliderect(npcRect):
            dialoguetext = 'i eated soap'
            if keys[pygame.K_SPACE]:
                dialoguetext = ''

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


        if location == 'house':
            gameDisplay.blit(npcImg, (xPos + 420,yPos + 200))
            npcRect = pygame.Rect(xPos + 420,yPos + 200,npcImg.get_width(),npcImg.get_height())
            pygame.draw.rect(gameDisplay, white, npcRect, 2)
    if debug == True:
        gameDisplay.blit(text, (0, 0))
        pygame.draw.rect(gameDisplay, white, playerRect, 2)
        pygame.draw.rect(gameDisplay, white, npcRect, 2)
    if dialoguetext != '':
        dialogue(dialoguetext)
    pygame.display.update()
    clock.tick(60)
    pygame.event.pump()

pygame.quit()
quit()