import pygame


pygame.init()


display_width = 350
display_height = 200

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('lil dude man')

speed = 1

black = (0,0,0)
white = (255,255,255)
x =  (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
y_change = 0
clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('lildude.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.45)
y = (display_height * 0.8)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -speed
            elif event.key == pygame.K_RIGHT:
                x_change = speed
            elif event.key == pygame.K_UP:
                y_change = -speed
            elif event.key == pygame.K_DOWN:
                y_change = speed
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0


    x += x_change
    y += y_change
     
    gameDisplay.fill(white)
    car(x,y)

        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()