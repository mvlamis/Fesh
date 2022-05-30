# Fesh by Michael Vlamis 2022
#
#       /`·.¸
#      /¸...¸`:·
#  ¸.·´  ¸   `·.¸.·´)
# : © ):´;      ¸  {
#  `·.¸ `·  ¸.·´\`·¸)
#      `\\´´\¸.·´
                     
                     
import pygame
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

global debug
debug = False # set to true to see debug info

sound = True
music = True

display_width = 960 # collisions depend on game resolution, do not change
display_height = 544
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('lil dude man')
canMove = True
fishingHUD = False
canFish = False
fishingLineY = 200

global xPos
global yPos

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
xPos = (-401)
yPos = (-401)
mousex, mousey = pygame.mouse.get_pos()
speed = 1

font = pygame.font.Font('inter.ttf', 32, bold = True)
dialoguefont = pygame.font.Font('inter.ttf', 24)
dialoguetext = ''
choicetext = ''
notiftext = ''
selectedChoice = 0
choiceMode = None
global showingChoice
showingChoice = False
isbuying = False

global inv
inv = ['','','','',''] # inventory
money = 0
if 'mega fishing rod' not in inv:
    fish = ['miss', 'carp'] # list of fish
else:
    fish = ['miss', 'carp', 'squid', 'tuna']

playerSize = 32
npcImg = pygame.image.load('images/npc.png')
npcImg = pygame.transform.scale(npcImg, (playerSize,playerSize))
npcRect = pygame.Rect(xPos + 420,yPos + 200,npcImg.get_width(),npcImg.get_height())
counter = 0

#sounds init
menuMusic = pygame.mixer.music.load('sounds/menu.mp3')
startSound = pygame.mixer.Sound('sounds/start.wav')
opendialogueSound = pygame.mixer.Sound('sounds/opendialogue.wav')
closedialogueSound = pygame.mixer.Sound('sounds/closedialogue.wav')
purchaseSound = pygame.mixer.Sound('sounds/purchase.wav')

charlesImg = pygame.image.load('images/charles.png')
charlesImg = pygame.transform.scale(charlesImg, (playerSize,playerSize))
shoppingChoice = None
buyingChoice = None

clock = pygame.time.Clock()
hasStarted = False
playerImg = pygame.image.load('char/Walk/Down/images/Char_walk_down_01.png')
playerImg = pygame.transform.scale(playerImg, (playerSize,playerSize))
playerRect = pygame.Rect(display_width/2, display_height/2, playerSize, playerSize)
location = "outside"

# walking images - while key pressed, cycle through images
downImages = ['char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_04.png','char/Walk/Down/images/Char_walk_down_04.png','char/Walk/Down/images/Char_walk_down_04.png','char/Walk/Down/images/Char_walk_down_04.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_06.png','char/Walk/Down/images/Char_walk_down_06.png','char/Walk/Down/images/Char_walk_down_06.png','char/Walk/Down/images/Char_walk_down_06.png','char/Walk/Down/images/Char_walk_down_06.png']
leftImages = ['char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_04.png','char/Walk/Left/images/Char_walk_left_04.png','char/Walk/Left/images/Char_walk_left_04.png','char/Walk/Left/images/Char_walk_left_04.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_06.png','char/Walk/Left/images/Char_walk_left_06.png','char/Walk/Left/images/Char_walk_left_06.png','char/Walk/Left/images/Char_walk_left_06.png','char/Walk/Left/images/Char_walk_left_06.png']
rightImages = ['char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_04.png','char/Walk/Right/images/Char_walk_right_04.png','char/Walk/Right/images/Char_walk_right_04.png','char/Walk/Right/images/Char_walk_right_04.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_06.png','char/Walk/Right/images/Char_walk_right_06.png','char/Walk/Right/images/Char_walk_right_06.png','char/Walk/Right/images/Char_walk_right_06.png','char/Walk/Right/images/Char_walk_right_06.png']
upImages = ['char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_06.png','char/Walk/Up/images/Char_walk_up_06.png','char/Walk/Up/images/Char_walk_up_06.png','char/Walk/Up/images/Char_walk_up_06.png','char/Walk/Up/images/Char_walk_up_06.png']

# object images
scaleImg = pygame.image.load('images/fishingscale.png')
rodImg = pygame.image.load('images/fishingrod.png')
carpImg = pygame.image.load('images/carp.png')
moneyImg = pygame.image.load('images/moneybag.png')

# loading screen clouds
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
musicColor = green
soundColor = green

backText = font.render('Back', True, white)
quitText = font.render('Quit', True, white)
musicText = font.render('Music', True, musicColor)
soundText = font.render('Sound', True, soundColor)

def drawCollisionLine(x1,y1,x2,y2): # draws a line to show where the player is colliding with
    pygame.draw.line(gameDisplay, white, (xPos + x1, yPos + y1), (xPos + x2,yPos + y2), 2)

def addToInventory(item):
    global inv
    if '' in inv:
        for i in range(len(inv)):
            if inv[i] == '':
                inv[i] = item
                return
    else:
        notif('Your inventory is full!')
        pygame.time.set_timer(pygame.USEREVENT, 3000)

def touchingWater(): # checks if player is touching water
    global canFish
    print('touching water')
    canFish = True
    pygame.time.set_timer(pygame.USEREVENT, 3000)


def dialogue(text): 
    dialogueText = dialoguefont.render(str(text), True, white)
    gameDisplay.blit(dialoguebox, (0,0))
    gameDisplay.blit(dialogueText, (100,400))
    # pygame.mixer.Sound.play(opendialogueSound)
    
def choice(choice1, choice2, choice3=None, choice4=None): # choice hud
    global showingChoice
    global selectedChoice
    showingChoice == True
    choice1Text = font.render(str(choice1), True, white)
    choice1Rect = choice1Text.get_rect()
    choice1Rect.topleft = (650,400) # set the top left corner of the rectangle to coords of text
    choice2Text = font.render(str(choice2), True, white)
    choice2Rect = choice2Text.get_rect()
    choice2Rect.topleft = (650,450)

    #only render the choices if they are not none
    if choice3 != None:
        choice3Text = font.render(str(choice3), True, white)
        choice3Rect = choice3Text.get_rect()
        choice3Rect.topleft = (850,400)
        gameDisplay.blit(choice3Text, (850,400))
    if choice4 != None:
        choice4Text = font.render(str(choice4), True, white)
        choice4Rect = choice4Text.get_rect()
        choice4Rect.topleft = (850,450)
        gameDisplay.blit(choice4Text, (850,450))
    gameDisplay.blit(choice1Text, (650,400))
    gameDisplay.blit(choice2Text, (650,450))

    # draw rects behind the text to detect mouse clicks
    pygame.draw.rect(gameDisplay, white, choice1Rect, 1, 5)
    pygame.draw.rect(gameDisplay, white, choice2Rect, 1, 5)
    if choice3 != None:
        pygame.draw.rect(gameDisplay, white, choice3Rect, 1, 5)
    if choice4 != None:
        pygame.draw.rect(gameDisplay, white, choice4Rect, 1, 5)

    # click handler
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            if choice1Rect.collidepoint(pygame.mouse.get_pos()):
                return choice1
            elif choice2Rect.collidepoint(pygame.mouse.get_pos()):
                return choice2
            elif choice3 != None:
                if choice3Rect.collidepoint(pygame.mouse.get_pos()):
                    return choice3
            elif choice4 != None:
                if choice4Rect.collidepoint(pygame.mouse.get_pos()):
                    return choice4

def shopping():
    global inv
    global dialoguetext
    global choicetext
    global choiceMode
    global selectedChoice
    if inv[0] == '':
        dialoguetext = 'You got nothing on ya, who do you think you are? Scram!'
    else:
        dialoguetext = 'Wanna buy some\'n or sell some\'n?'
        choiceMode = 'shopping'

def notif(text):
    notifText = dialoguefont.render(str(text), True, white)
    gameDisplay.blit(notifText, (650,320))

collisionLines = []

def rightCollide(x,y1,y2, action=None):
    global xPos
    global yPos
    if xPos == x:
        if yPos <= y1 and yPos >= y2:
            xPos = xPos - speed
            if action != None:
                action()

    collisionLines.append(x)
    collisionLines.append(y1)
    collisionLines.append(y2)

    drawCollisionLine(x,y1,x,y2)
            
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

def enterShop():
    global xPos
    global yPos
    global mapImg
    global location
    location = 'shop'
    mapImg = 'images/shop.png'
    print('Entering shop')
    xPos = 336
    yPos = -8

def enterOutside():
    global xPos
    global yPos
    global mapImg
    global location
    if location == 'house':
        mapImg = 'images/map.png'
        print('Entering outside')
        xPos = 304
        yPos = -170
        location = 'outside'

    if location == 'shop':
        mapImg = 'images/map.png'
        print('Entering outside')
        xPos = -274
        yPos = -397
        location = 'outside'

if music:
    pygame.mixer.music.load('sounds/menu.mp3')
    pygame.mixer.music.play(-1)
# menu screen loop
while not hasStarted:
    debugText = font.render('Debug mode', True, debugColor)
    musicText = font.render('Music', True, musicColor)
    soundText = font.render('Sound', True, soundColor)
    
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONUP:
            print(mouse[0], mouse[1])
            # options button
            if mouse[0] > 440 and mouse[0] < 520 and mouse[1] > 300 and mouse[1] < 370:
                options = True
                print("options")
            
            # debug button
            if options == True and mouse[0] > 150 and mouse[0] < 350 and mouse[1] > 150 and mouse[1] < 190:
                debug = not debug
            
            # back button
            if options == True and mouse[0] > 150 and mouse[0] < 230 and mouse[1] > 450 and mouse[1] < 480:
                options = False

            # quit button
            if options == True and mouse[0] > 700 and mouse[0] < 800 and mouse[1] > 450 and mouse[1] < 480:
                hasStarted = False

            # sound button
            if options == True and mouse[0] > 150 and mouse[0] < 230 and mouse[1] > 250 and mouse[1] < 290:
                sound = not sound
                if sound:
                    print('sound on')
                else:
                    print('sound off')

            # music button
            if options == True and mouse[0] > 150 and mouse[0] < 230 and mouse[1] > 200 and mouse[1] < 240:
                music = not music
                if music:
                    pygame.mixer.music.load('sounds/menu.mp3')
                    pygame.mixer.music.play(-1)
                else:
                    pygame.mixer.music.stop()

            # start button
            if mouse[0] > display_width/2 - startButton.get_width()/2 and mouse[1] > display_height/2 - startButton.get_height()/2 and mouse[0] < display_width/2 + startButton.get_width()/2 and mouse[1] < display_height/2 + startButton.get_height()/2:
                if sound:
                    pygame.mixer.Sound.play(startSound)
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

    if options == True: # options menu
        gameDisplay.blit(menuBg, (0,0))
        gameDisplay.blit(debugText, (150,150))
        gameDisplay.blit(backText, (150,450))
        gameDisplay.blit(musicText, (150,200))
        gameDisplay.blit(soundText, (150,250))
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                # debug button
                if options == True and mouse[0] > 150 and mouse[0] < 350 and mouse[1] > 150 and mouse[1] < 190:
                    debug = not debug
                
                # back button
                if options == True and mouse[0] > 150 and mouse[0] < 230 and mouse[1] > 450 and mouse[1] < 480:
                    options = False

                    
        if debug:
            debugColor = green
        else:
            debugColor = white
        if sound:
            soundColor = green
        else:
            soundColor = white
        if music:
            musicColor = green
        else:
            musicColor = white
    else:
        if hasStarted == False:
            gameDisplay.blit(startButton, (display_width/2 - startButton.get_width()/2, display_height/2 - startButton.get_height()/2))
            gameDisplay.blit(optionsButton, (430,330))
    pygame.display.update()
    clock.tick(60)
    pygame.event.pump()

# game loop
while hasStarted:
    print(inv)
    print(choiceMode)
    print(shoppingChoice)
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

        if event.type == pygame.USEREVENT:
            notiftext = ''
            canFish = False

    keys = pygame.key.get_pressed()  #checking pressed keys
    if canMove:
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            yPos += speed
            counter = (counter + 1) % len(upImages)
            playerImg = pygame.image.load(upImages[counter])
            playerImg = pygame.transform.scale(playerImg, (playerSize,playerSize))
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            yPos -= speed
            counter = (counter + 1) % len(downImages)
            playerImg = pygame.image.load(downImages[counter])
            playerImg = pygame.transform.scale(playerImg, (playerSize,playerSize))
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            xPos += speed
            counter = (counter + 1) % len(leftImages)
            playerImg = pygame.image.load(leftImages[counter])
            playerImg = pygame.transform.scale(playerImg, (playerSize,playerSize))
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            xPos -= speed
            counter = (counter + 1) % len(rightImages)
            playerImg = pygame.image.load(rightImages[counter])
            playerImg = pygame.transform.scale(playerImg, (playerSize,playerSize))
    if keys[pygame.K_SPACE]: 
        if dialoguetext != '' and sound:
            pygame.mixer.Sound.play(closedialogueSound)
        dialoguetext = ''
        canMove = True
        if choiceMode != None:
            choiceMode = None
            shoppingChoice = None
        if 'fishing rod' in inv and canFish == True and fishingHUD == False:
            fishingHUD = True
            canMove = False
            print('fishing')
    if keys[pygame.K_f] and fishingHUD == True:
        caughtFish = random.choice(fish)
        if '' in inv:
            if caughtFish == 'miss':
                notiftext = 'You missed!'
            else:
                addToInventory(caughtFish)
                notiftext = 'You caught a ' + caughtFish + '!'
        else:
            notiftext = 'Your inventory is full!'
        fishingHUD = False
        canMove = True

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
        bottomCollide(-385,-230,-316, enterShop)

        # house border
        rightCollide(195,87,-160)
        leftCollide(420,87,-160)
        topCollide(87,420,195)
        bottomCollide(-160,420,195, enterHouse)


        # water border
        leftCollide(-103,20,-150, touchingWater)
        bottomCollide(-150,-103,-1000, touchingWater)
        leftCollide(-974,-626,-1000, touchingWater)
        leftCollide(-879,-441,-627, touchingWater)
        leftCollide(-845,-224,-441, touchingWater)
        leftCollide(-806,-150,-224, touchingWater)
        bottomCollide(-224,-806,-1000, touchingWater)
        bottomCollide(-441,-845,-1000, touchingWater)
        bottomCollide(-627,-879,-1000, touchingWater)
        topCollide(20,-103,-1000, touchingWater)
        leftCollide(-131,115,20, touchingWater)
        leftCollide(-164,365,111, touchingWater)
        topCollide(112,-130,-1000, touchingWater)

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
        leftCollide(187,-144,-204)
        rightCollide(227,-144,-204)
        bottomCollide(-207,227,187, enterOutside)

        # npc collision
        if playerRect.colliderect(npcRect) and 'fishing rod' not in inv:
            dialoguetext = 'Take this, it\'s for you.'
            if keys[pygame.K_SPACE]:
                notiftext = 'You got a fishing rod!'
                pygame.time.set_timer(pygame.USEREVENT, 3000)
                addToInventory('fishing rod')
                dialoguetext = '' 
                
    if location == 'shop': # SHOP COLLISIONS
        bottomCollide(-16, 449,220, enterOutside)
        leftCollide(220, 122, -16)
        rightCollide(449, 122, -16)
        bottomCollide(122, 449, 122, shopping)


    if options == True: # options menu
        clock.tick(60)
        gameDisplay.blit(menuBg, (0,0))
        gameDisplay.blit(debugText, (150,150))
        gameDisplay.blit(backText, (150,450))
        gameDisplay.blit(quitText, (700,450))
        gameDisplay.blit(musicText, (150,300))
        gameDisplay.blit(soundText, (150,350))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
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
            debugColor = green
        else:
            debugColor = white
        if sound:
            soundColor = green
        else:
            soundColor = white
        if music:
            musicColor = green
        else:
            musicColor = white
    else:
        gameDisplay.fill(black)
        gameDisplay.blit(gameMap, (xPos,yPos))
        gameDisplay.blit(playerImg, (display_width / 2, display_height / 2))

        if location == 'house':
            gameDisplay.blit(npcImg, (xPos + 420,yPos + 200))
            npcRect = pygame.Rect(xPos + 420,yPos + 200,npcImg.get_width(),npcImg.get_height())

        if location == 'shop':
            gameDisplay.blit(charlesImg, (xPos + 210,yPos + 100))
    if debug == True:
        gameDisplay.blit(text, (0, 0))
        pygame.draw.rect(gameDisplay, white, playerRect, 2)
        pygame.draw.rect(gameDisplay, white, npcRect, 2)
        
    if dialoguetext != '': # render dialogue box
        dialogue(dialoguetext)
        

    if notiftext != '': # render notification box
        notif(notiftext)

    if fishingHUD == True: # render fishing HUD
        if fishingLineY == 200:
            goingUp = False
        if fishingLineY >= scaleImg.get_height()+200:
            goingUp = True
        if goingUp == True:
            fishingLineY -= 3
        else:
            fishingLineY += 3
        gameDisplay.blit(scaleImg, (750,200))
        pygame.draw.rect(gameDisplay, black , (750,200,scaleImg.get_width(),scaleImg.get_height()), 2)
        pygame.draw.rect(gameDisplay, black, (750, fishingLineY, scaleImg.get_width(), 5))

    if inv[0] != '': # first slot at x = 0
        pygame.draw.rect(gameDisplay, white, (0,512,32,32), 0)
        if inv[0] == 'fishing rod':
            gameDisplay.blit(rodImg, (0,512))
        if inv[0] == 'carp':
            gameDisplay.blit(carpImg, (0,512))

    if inv[1] != '': # second slot at x = 32
        pygame.draw.rect(gameDisplay, white, (32,512,32,32), 0)
        if inv[1] == 'fishing rod':
            gameDisplay.blit(rodImg, (32,512))
        if inv[1] == 'carp':
            gameDisplay.blit(carpImg, (32,512))

    if inv[2] != '': # third slot at x = 64
        pygame.draw.rect(gameDisplay, white, (64,512,32,32), 0)
        if inv[2] == 'fishing rod':
            gameDisplay.blit(rodImg, (64,512))
        if inv[2] == 'carp':
            gameDisplay.blit(carpImg, (64,512))
    
    if inv[3] != '': # fourth slot at x = 96
        pygame.draw.rect(gameDisplay, white, (96,512,32,32), 0)
        if inv[3] == 'fishing rod':
            gameDisplay.blit(rodImg, (96,512))
        if inv[3] == 'carp':
            gameDisplay.blit(carpImg, (96,512))

    if inv[4] != '': # fifth slot at x = 128
        pygame.draw.rect(gameDisplay, white, (128,512,32,32), 0)
        if inv[4] == 'fishing rod':
            gameDisplay.blit(rodImg, (128,512))
        if inv[4] == 'carp':
            gameDisplay.blit(carpImg, (128,512))


    # Render choices
    if choiceMode == 'shopping': # charles shopping menu
        canMove = False
        shoppingChoice = choice("Buy", "Sell Fish", "Sell Items", "Leave")

    if shoppingChoice == "Sell Fish": # sell fish menu
        if "carp" in inv:
            for i in range(len(inv)):
                if inv[i] == 'carp':
                    inv[i] = ''
                    money += 10
                    pygame.time.set_timer(pygame.USEREVENT, 3000)
                    dialoguetext = 'Thank ye for the fish!'
                    choiceMode = None
                    canMove = True        
        else:
            dialoguetext = 'You got no fish to sell!'
            choiceMode = None
            shoppingChoice = None
            canMove = True

    if shoppingChoice == "Sell Items": # sell items menu
        if 'fishing rod' in inv and 'running shoes' not in inv:
            dialoguetext = 'You got no items to sell!'
            choiceMode = None
            shoppingChoice = None
            
        if 'fishing rod' in inv and 'running shoes' in inv:
            dialoguetext = 'Thanks for them running shoes!'
            inv.remove('running shoes')
            money += 30
            choiceMode = None
            shoppingChoice = None

        if 'mega fishing rod' in inv and 'running shoes' not in inv:
            dialoguetext = 'Thanks for that mega fishing rod!'
            inv.remove('mega fishing rod')
            choiceMode = None
            shoppingChoice = None

        if 'mega fishing rod' in inv and 'running shoes' in inv:
            dialoguetext = 'Thanks for thems thingies!'
            inv.remove('running shoes')
            inv.remove('mega fishing rod')
            money += 10
            choiceMode = None
            shoppingChoice = None

    if shoppingChoice == "Buy": # buy menu
        dialoguetext = 'Whachu want?'
        choiceMode = None
        shoppingChoice = None
        isbuying = True

    if shoppingChoice == "Leave":
        choiceMode = None
        shoppingChoice = None
        canMove = True
        dialoguetext = ''
        

    if isbuying:
        buyingChoice = choice("Mega Fishing Rod (150)", "Running Shoes (50)")

    if buyingChoice == "Mega Fishing Rod (150)":
        if money < 150:
            dialoguetext = 'You don\'t have enough money!'
            choiceMode = None
            shoppingChoice = None
            isbuying = False
            buyingChoice = None
        else:
            money = money - 150
            if inv[0] == 'fishing rod':
                inv[0] = ('mega fishing rod')
                money -= 150
                dialoguetext = 'Pleasure doing business!'
                if sound:
                    pygame.mixer.Sound.play(purchaseSound)
                buyingChoice = None
                choiceMode = None
                isbuying = False
            else:
                dialoguetext = 'You got no room for that!'
                choiceMode = None

                buyingChoice = None
                isbuying = False

    if buyingChoice == "Running Shoes (50)":
        if money < 50:
            dialoguetext = 'You don\'t have enough money!'
            choiceMode = None
            shoppingChoice = None
            isbuying = False
            buyingChoice = None
        else:
            if '' in inv:
                addToInventory('running shoes')
                money -= 50
                dialoguetext = 'Pleasure doing business!'
                if sound:
                    pygame.mixer.Sound.play(purchaseSound)
                buyingChoice = None
                choiceMode = None
                isbuying = False
            else:
                dialoguetext = 'You got no room for that!'
                choiceMode = None

                buyingChoice = None
                isbuying = False


    if len(choicetext) > 0:
        if len(choicetext) == 2:
            choice(choicetext[0], choicetext[1])
        if len(choicetext) == 3:
            choice(choicetext[0], choicetext[1], choicetext[2])
        if len(choicetext) == 4:
            choice(choicetext[0], choicetext[1], choicetext[2], choicetext[3])

    # render money
    moneyText = font.render("$" + str(money), True, white)
    moneyTextRect = moneyText.get_rect()
    gameDisplay.blit(moneyText, (960 - moneyTextRect.width, 544 - moneyTextRect.height))
    gameDisplay.blit(moneyImg, (960 - moneyTextRect.width - moneyImg.get_width(), 544 - moneyTextRect.height))

        
    pygame.display.update()
    clock.tick(60)
    # pygame.event.pump()

pygame.quit()
quit()