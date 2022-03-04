from turtle import window_width
import pygame
import time

pygame.init()

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


downImages = ['char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_01.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_02.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_03.png','char/Walk/Down/images/Char_walk_down_04.png','char/Walk/Down/images/Char_walk_down_04.png','char/Walk/Down/images/Char_walk_down_04.png','char/Walk/Down/images/Char_walk_down_04.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_05.png','char/Walk/Down/images/Char_walk_down_06.png','char/Walk/Down/images/Char_walk_down_06.png','char/Walk/Down/images/Char_walk_down_06.png','char/Walk/Down/images/Char_walk_down_06.png','char/Walk/Down/images/Char_walk_down_06.png']
leftImages = ['char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_01.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_02.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_03.png','char/Walk/Left/images/Char_walk_left_04.png','char/Walk/Left/images/Char_walk_left_04.png','char/Walk/Left/images/Char_walk_left_04.png','char/Walk/Left/images/Char_walk_left_04.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_05.png','char/Walk/Left/images/Char_walk_left_06.png','char/Walk/Left/images/Char_walk_left_06.png','char/Walk/Left/images/Char_walk_left_06.png','char/Walk/Left/images/Char_walk_left_06.png','char/Walk/Left/images/Char_walk_left_06.png']
rightImages = ['char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_01.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_02.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_03.png','char/Walk/Right/images/Char_walk_right_04.png','char/Walk/Right/images/Char_walk_right_04.png','char/Walk/Right/images/Char_walk_right_04.png','char/Walk/Right/images/Char_walk_right_04.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_05.png','char/Walk/Right/images/Char_walk_right_06.png','char/Walk/Right/images/Char_walk_right_06.png','char/Walk/Right/images/Char_walk_right_06.png','char/Walk/Right/images/Char_walk_right_06.png','char/Walk/Right/images/Char_walk_right_06.png']
upImages = ['char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_01.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_02.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_03.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_04.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_06.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_06.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_06.png','char/Walk/Up/images/Char_walk_up_05.png','char/Walk/Up/images/Char_walk_up_06.png','char/Walk/Up/images/Char_walk_up_06.png','char/Walk/Up/images/Char_walk_up_06.png']

gameMap = pygame.image.load('map.png')
gameMap = pygame.transform.scale(gameMap, (display_width * 2, display_height * 2))

mapRect = gameMap.get_rect()

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
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

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         x_change = speed
        #     elif event.key == pygame.K_RIGHT:
        #         x_change = -speed
        #     elif event.key == pygame.K_UP:
        #         y_change = speed
        #     elif event.key == pygame.K_DOWN:
        #         y_change = -speed
        #         counter = (counter + 1) % len(downImages)
        #         playerImg = pygame.image.load(downImages[counter])


     
    gameDisplay.fill(black)
    gameDisplay.blit(gameMap, (xPos,yPos))
    gameDisplay.blit(playerImg, (display_width / 2, display_height / 2))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()