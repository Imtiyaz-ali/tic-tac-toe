import pygame
from variables import *
import numpy as np
from loguru import logger as log
import time

# 
pygame.init()
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(gameName)


matrix = np.zeros((3,3))
log.debug(matrix)
def drawLines():
    for i in range(4):
        lineWidth = 1
        pygame.draw.line(win,lineColors,((WIDTH//3)*i,0),((WIDTH//3)*i,HEIGHT),lineWidth)
        pygame.draw.line(win,lineColors,(0,(HEIGHT//3)*i),(WIDTH,HEIGHT//3*i),lineWidth)


def getUserAction(px,py,player):
    xpos = int(px//(WIDTH/3))
    ypos = int(py//(HEIGHT/3))
    if matrix[ypos][xpos]==0:
        matrix[ypos][xpos] = player
        print(matrix)
        check = check_win(player)
        if check is True:
            return player,False,check
        if player ==1:
            player = 2
        else:
            player = 1
        return player,False,check
    else:
        return player,True,False



def draw_circle(x,y):
    pygame.draw.circle(win,red,(((WIDTH//3)*x+extra_space),((HEIGHT//3)*y+extra_space)),circle_radius,2)

def draw_x(x,y):
    pygame.draw.line(win,green,(((WIDTH//3)*x+extra_space_line_2),((HEIGHT//3)*y+extra_space_line_2)),(((WIDTH//3)*x+extra_space_line),((HEIGHT//3)*y+extra_space_line)),line_width)
    pygame.draw.line(win,green,(((WIDTH//3)*x+extra_space_line),((HEIGHT//3)*y+extra_space_line_2)),(((WIDTH//3)*x+extra_space_line_2),((HEIGHT//3)*y+extra_space_line)),line_width)


def drawPlayers():
    for i in range(3):
        for j in range(3):
            if matrix[i][j]==1:
                draw_circle(j,i)
            if matrix[i][j]==2:
                draw_x(j,i)

def check_win(player):
    # vertical
    for i in range(3):
        if matrix[i][0] == player and matrix[i][1] == player and matrix[i][2] ==player:
            pygame.draw.line(win,red,(30,(((WIDTH/3)/2))),(WIDTH-30,(WIDTH/3)-(WIDTH/3)/2),3)

            pygame.display.update()
            return True
        
    # horizontal
    for i in range(3):
        if matrix[0][i] == player and matrix[1][i] == player and matrix[2][i] == player:
            return True

    # diagonal
    if  matrix[0][0] == player and matrix[1][1] ==  player and matrix[2][2]:
        return True
    if  matrix[0][2] == player and matrix[1][1] ==  player and matrix[2][0]:
        return True

    return False



def showText(user,color,xp,yp):
    l = len(user)
    pygame.draw.rect(win,green,(xp-5,yp-5,l*12,30))
    font = pygame.font.Font(None,30)
    string = font.render(user,True,color)
    win.blit(string,(xp,yp))

def show_info(string,size,color):
    l = len(string)
    pygame.draw.rect(win,white,(0,(HEIGHT/2)-30,WIDTH,60))
    pygame.draw.rect(win,red,(0,(HEIGHT/2)-20,WIDTH,40))
    font = pygame.font.Font(None,size)
    ss = font.render(string,True,color)
    win.blit(ss,((WIDTH/2)-l*6,(HEIGHT/2)-10))

def draw_mark(x,y):
    pygame.draw.line(win,red,)

occupied_space = False
win_game = False
while gameRunning:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            gameRunning = False
            # pygame.quit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            data = pygame.mouse.get_pos()
            data1 = getUserAction(data[0],data[1],currunt_player)
            currunt_player = data1[0]
            occupied_space = data1[1]
            win_game = data1[2]




    win.fill(backGround)
    drawLines()
    drawPlayers()
    showText(f"P1 = {player1}",white,30,30)
    showText(f"P2 = {player2}",white,WIDTH-100,30)
    if occupied_space is True:
        show_info("Already Taken",30,white)
        pygame.display.flip()
        time.sleep(1.5)
        occupied_space =False
    
    if win_game:
        if currunt_player == 1:
            player1 +=1
        else:
            player2+=1
        show_info(f"PLAYER: {currunt_player} WINS!!!!!!",30,white)
        pygame.display.flip()
        time.sleep(2)
        matrix = np.zeros((3,3))
        win_game = False



    pygame.display.update()
