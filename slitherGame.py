import pygame, sys
import time
import random

pygame.init()
white = (255, 255, 255)
black = (100, 0, 0)
red = (255, 0, 0)
window_width = 800
window_height = 600
gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("slither")
clock = pygame.time.Clock()
FPS = 5
blockSize = 20
noPixel = 0


def myQuit():
    pygame.quit()
    sys.exit(0)


font = pygame.font.SysFont(None, 25, bold=True)


def drawGrid():
    sizeGrid = window_width


def snake(blockSize, snakelist):
    for size in snakelist:
        pygame.draw.rect(gameDisplay, black, [size[0] + 5, size[1], blockSize, blockSize],5)


def message(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [int(window_width / 2), int(window_height / 2)])


def gameLoop():
    gameExit = False
    gameOver = False
    lead_X = window_width / 2
    lead_Y = window_height / 2

    change_X = 0
    change_Y = 0
    snakelist = []
    snakeLength = 1
    randomAppleX = round(random.randrange(0, window_width - blockSize) / 10.0) * 10.0
    randomAppleY = round(random.randrange(0, window_height - blockSize) / 10.0) * 10.0
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message("Game over! Press c to play and q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    myQuit()
                    
                leftArrow = event.key == pygame.K_LEFT
                rightArrow = event.key == pygame.K_RIGHT
                upArrow = event.key == pygame.K_UP
                downArrow = event.key == pygame.K_DOWN
                if leftArrow:
                    change_X = -blockSize
                    change_Y = noPixel
                elif rightArrow:
                    change_X = +blockSize
                    change_Y = noPixel
                elif upArrow:
                    change_X = noPixel
                    change_Y = -blockSize
                elif downArrow:
                    change_X = noPixel
                    change_Y = blockSize

            if lead_X >= window_width or lead_X < 0 or lead_Y >=window_height or lead_Y < 0:
                gameOver = True

        lead_X += change_X
        lead_Y += change_Y
        gameDisplay.fill(white)

        AppleThickness = 20

        print([int(randomAppleX), int(randomAppleY), AppleThickness, AppleThickness])
        pygame.draw.rect(gameDisplay, red, [randomAppleX, randomAppleY, AppleThickness, AppleThickness])

        allspriteslist = []
        allspriteslist.append(lead_X)
        allspriteslist.append(lead_Y)
        snakelist.append(allspriteslist)

        if len(snakelist) > snakeLength:
            del snakelist[0]

        for eachSegment in snakelist[:-1]:
            if eachSegment == allspriteslist:
                gameOver = True

        snake(blockSize, snakelist)

        pygame.display.update()

        if lead_X >= randomAppleX and lead_X <= randomAppleX + AppleThickness:
            if lead_Y >= randomAppleY and lead_Y <= randomAppleY + AppleThickness:
                randomAppleX = round(random.randrange(0, window_width - blockSize) / 10.0) * 10.0
                randomAppleY = round(random.randrange(0, window_height - blockSize) / 10.0) * 10.0
                snakeLength += 1

        clock.tick(FPS)

    pygame.quit()
    quit()


gameLoop()
