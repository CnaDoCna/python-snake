import pygame
import random

snake_size = 10
screen_size = 200
food_size = 10
green = (0, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
snake_speed = 10
rosnij = False
collected_food = 0
direction = ""
Game = True

snake_moves = []
food_position = [random.randint(10, screen_size-10), random.randint(10, screen_size-10)]
snake_body = [[screen_size/2, screen_size/2]]

pygame.init()
gameDisplay = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption('Game - Snake')
font1 = pygame.font.SysFont('Arial', 15)
font2 = pygame.font.SysFont('theblueoasisnormalny', 30)
clock = pygame.time.Clock()


def scoresDisplay():
    score_text = font1.render("Foods: " + str(collected_food), True, white)
    gameDisplay.blit(score_text,
        (screen_size/2 - score_text.get_width()/2, screen_size/10))


def drawEverything():
    for i in range (-1, len(snake_body)-1):
        (pygame.draw.rect(gameDisplay, green, (snake_body[i][0], snake_body[i][1], snake_size, snake_size)))
    head = pygame.draw.rect(gameDisplay, green, (snake_body[0][0], snake_body[0][1], snake_size, snake_size))
    food = pygame.draw.rect(gameDisplay, red, (food_position[0], food_position[1], food_size, food_size))
    wall1 = pygame.draw.line(gameDisplay, white, [0,screen_size], [0,0], 5)
    wall2 = pygame.draw.line(gameDisplay, white, [0,0], [screen_size,0], 5)
    wall3 = pygame.draw.line(gameDisplay, white, [screen_size-2,0], [screen_size-2,screen_size-2], 5)
    wall4 = pygame.draw.line(gameDisplay, white, [0,screen_size-2], [screen_size-2,screen_size-2], 5)

    return head, food, wall1, wall2, wall3, wall4



while True:
    gameDisplay.fill(black)
    scoresDisplay()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

            if event.key == pygame.K_UP:
                direction = "up"

            if event.key == pygame.K_DOWN:
                direction = "down"

            if event.key == pygame.K_LEFT:
                direction = "left"

            if event.key == pygame.K_RIGHT:
                direction = "right"

    if Game:
        #zapisywanie ruchów głowy i przepisywanie do ciała
        snake_moves.append([snake_body[0][0], snake_body[0][1]])
        if len(snake_moves) > len(snake_body):
            snake_moves.remove(snake_moves[0])
        if not rosnij:
            for i in range (len(snake_body)-1, 0, -1):
                snake_body[i][0] = snake_moves[i][0]
                snake_body[i][1] = snake_moves[i][1]

        # programowanie ruchu
        if direction == "up":
            if rosnij:
                snake_body[0][1] -= snake_size
                snake_body[-1][1] -= snake_size #nowa czesc
                rosnij = False
            else:
                snake_body[0][1] -= snake_speed
        elif direction == "down":
            if rosnij:
                snake_body[0][1] += snake_size
                snake_body[-1][1] += snake_size #nowa czesc
                rosnij = False
            else:
                snake_body[0][1] += snake_speed
        elif direction == "left":
            if rosnij:
                snake_body[0][0] -= snake_size
                snake_body[-1][0] -= snake_size #nowa czesc
                rosnij = False
            else:
                snake_body[0][0] -= snake_speed
        elif direction == "right":
            if rosnij:
                snake_body[0][0] += snake_size
                snake_body[-1][0] += snake_size #nowa czesc
                rosnij = False
            else:
                snake_body[0][0] += snake_speed


    #rysowanie
        head, food, wall1, wall2, wall3, wall4 = drawEverything()


    # kolizja z okienkiem
        if head.colliderect(wall1) or head.colliderect(wall2) or head.colliderect(wall3) or head.colliderect(wall4):
            Game = False

    #kolizja z jedzeniem
        if head.colliderect(food):
            food_position = [random.randint(10, screen_size-10), random.randint(10, screen_size-10)]
            snake_body.append([snake_moves[-1][0], snake_moves[-1][1]])
            rosnij = True
            collected_food +=1

    #kolizaja z samym soba
        for i in range (len(snake_body)-2, 0, -1):
            if snake_body[0] == snake_body[i]:
                Game = False

        pygame.display.update()
        clock.tick(10)

    else:
        gameDisplay.fill(red)
        scoresDisplay()
        drawEverything()
        gameover_text = font2.render("Game Over", True, white)
        gameDisplay.blit(gameover_text,
            (screen_size/2 - gameover_text.get_width()/2, screen_size/2))

        pygame.display.update()
        clock.tick(10)
