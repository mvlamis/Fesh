import pygame

pygame.init()
pygame.font.init()

debug = False

display_width = 960
display_height = 544

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('lil dude man')

speed = 1

black = (0,0,0)
white = (255,255,255)
xPos = (-401)
yPos = (-401)

playerSize = 32

counter = 0

clock = pygame.time.Clock()
crashed = False
playerImg = pygame.image.load('char/Walk/Down/images/Char_walk_down_01.png')
playerImg = pygame.transform.scale(playerImg, (playerSize,playerSize))




downImages = ['char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_04.png','char/Walk/Down/images/Char_walk_down_04.png','char/Walk/Down/images/Char_walk_down_04.png','char/Walk/Down/images/Char_walk_down_04.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_06.png','char/Walk/Down/images/Char_walk_down_06.png','char/Walk/Down/images/Char_walk_down_06.png','char/Walk/Down/images/Char_walk_down_06.png','char/Walk/Down/images/Char_walk_down_06.png']
leftImages = ['char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_04.png','char/Walk/Left/images/Char_walk_left_04.png','char/Walk/Left/images/Char_walk_left_04.png','char/Walk/Left/images/Char_walk_left_04.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_06.png','char/Walk/Left/images/Char_walk_left_06.png','char/Walk/Left/images/Char_walk_left_06.png','char/Walk/Left/images/Char_walk_left_06.png','char/Walk/Left/images/Char_walk_left_06.png']
rightImages = ['char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_04.png','char/Walk/Right/images/Char_walk_right_04.png','char/Walk/Right/images/Char_walk_right_04.png','char/Walk/Right/images/Char_walk_right_04.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_06.png','char/Walk/Right/images/Char_walk_right_06.png','char/Walk/Right/images/Char_walk_right_06.png','char/Walk/Right/images/Char_walk_right_06.png','char/Walk/Right/images/Char_walk_right_06.png']
upImages = ['char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_06.png','char/Walk/Up/images/Char_walk_up_06.png','char/Walk/Up/images/Char_walk_up_06.png','char/Walk/Up/images/Char_walk_up_06.png','char/Walk/Up/images/Char_walk_up_06.png']

gameMap = pygame.image.load('map.png')
gameMap = pygame.transform.scale(gameMap, (display_width * 2, display_height * 2))

mapRect = gameMap.get_rect()

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    keys = pygame.key.get_pressed()  #checking pressed keys

    if keys[pygame.K_BACKQUOTE]:
        debug = not debug
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
        font = pygame.font.Font('freesansbold.ttf', 18)
        text = font.render("Position: " + str(xPos) + ", " + str(yPos) + " | Speed: " + str(speed), True, white)
        if keys[pygame.K_RIGHTBRACKET]:
            speed += 1
        if keys[pygame.K_LEFTBRACKET]:
            speed -= 1

    # left border
    if xPos == 500:
        xPos = xPos - speed

    # right border
    if xPos == -1425:
        xPos = xPos + speed

    # top border
    if yPos == 300:
        yPos = yPos - speed

    # bottom border
    if yPos == -785:
        yPos = yPos + speed


    # tent right border
    if xPos == -316 and yPos < -318 and yPos > -385:
        xPos = xPos - speed

    # tent left border
    if xPos == -230 and yPos < -318 and yPos > -385:
        xPos = xPos + speed

    # tent top border
    if yPos == -318 and xPos < -230 and xPos > -316:
        yPos = yPos + speed

    # tent bottom border
    if yPos == -385 and xPos < -230 and xPos > -316:
        yPos = yPos - speed


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


    gameDisplay.fill(black)
    gameDisplay.blit(gameMap, (xPos,yPos))
    gameDisplay.blit(playerImg, (display_width / 2, display_height / 2))
    if debug == True:
        gameDisplay.blit(text, (0, 0))

    pygame.display.update()
    clock.tick(60)





pygame.quit()
quit()