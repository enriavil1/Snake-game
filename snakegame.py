import pygame
import time
import random


pygame.init()

clock= pygame.time.Clock()

blue=(0,0,255)
red=(255,0,0)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

dis_width = 800
dis_height= 600
snake_block= 10

directions= ["up", "down", "right", "left", "tl", "tr", "bl", "br"]


font_style = pygame.font.SysFont("bahnschrift", 30) 
score_font = pygame.font.SysFont("comicsansms", 35)

def score(score):
    mesg = font_style.render("Your score: " + str(score), True, black)
    display.blit(mesg,[0,0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [dis_width/4, dis_height/2])

def food_spawn(dis_width,dis_height):
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    while foodx >= dis_width or foodx < 0:
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    
    while foody >= dis_height or foody < 0:
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    return foodx,foody


def snake(snake_block, snake_size):
    for x in snake_size:
        pygame.draw.rect(display,black, [x[0],x[1], snake_block,snake_block])

display = pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()
pygame.display.set_caption("Snake game")

def game_loop(starting):
    game_over = False
    if starting == True:
        game_close = None
    else:
        game_close = False

    x1 = dis_width/2
    y1= dis_height/2

    changeX = 0
    changeY = 0

    snake_lst= []
    snake_size= 1

    direction = None

    foodx, foody= food_spawn(dis_width,dis_height)

    while not game_over:

        while game_close == True:
            display.fill(black)
            message("You lost! Press 'Enter' to play again or 'Q' to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

                if event.type ==  pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop(False)
                    if event.key == pygame.K_q:
                        game_close = False
                        game_over = True
        
    
        while game_close == None:
            display.fill(black)
            message("Press 'Enter' to play or 'Q' to quit", white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

                if event.type ==  pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_close = False
                    if event.key == pygame.K_q:
                        game_close = False
                        game_over = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            if event.type == pygame.KEYDOWN:
                if snake_size > 1:
                    if event.key == pygame.K_w and direction != directions[1]:
                        direction = directions[0]
                        changeY = -snake_block
                        changeX= 0
                    
                    if event.key == pygame.K_s and direction != directions[0]:
                        direction = directions[1]
                        changeY = snake_block
                        changeX= 0
                    
                    if event.key == pygame.K_d and direction != directions[3]:
                        direction = directions[2]
                        changeX = snake_block
                        changeY =0

                    if event.key == pygame.K_a and direction != directions[2]:
                        direction = directions[3]
                        changeX = -snake_block
                        changeY =0

                else:
                    if event.key == pygame.K_w:
                        direction = directions[0]
                        changeY = -snake_block
                        changeX= 0
                    
                    if event.key == pygame.K_s:
                        direction = directions[1]
                        changeY = snake_block
                        changeX= 0
                    
                    if event.key == pygame.K_d:
                        direction = directions[2]
                        changeX = snake_block
                        changeY =0

                    if event.key == pygame.K_a:
                        direction = directions[3]
                        changeX = -snake_block
                        changeY =0
                    

                        

        if x1 >= dis_width or x1 < 0:
            game_close = True
        
        if y1 >= dis_height or y1 < 0:
            game_close = True


        x1 += changeX
        y1 += changeY

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_lst.append(snake_head)

        if len(snake_lst)  > snake_size:
            snake_lst.pop(0)
        

        for i in snake_lst[:-1]:
            if i == snake_head:
                game_close = True

        if x1 == foodx and y1 == foody:
            foodx, foody= food_spawn(dis_width,dis_height)
            snake_size+=1
        

        display.fill(white)
        snake(snake_block,snake_lst)
        pygame.draw.rect(display, green, [foodx,foody, snake_block,snake_block])
        score(snake_size-1)
        pygame.display.update()
        clock.tick(1000)
    pygame.quit()
    quit()

game_loop(starting=True)
