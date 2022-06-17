import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import helicopter
import Enemy
import numpy as np
import time



# def init():
#     pygame.init()
#     display = (500, 500)
#     pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
#     glClearColor(0.7, 0.9, 1.0, 1.0)
#     gluOrtho2D(0, 2000.0, 0, 2000.0)
#     glClear(GL_COLOR_BUFFER_BIT)
# def background():
#     glClear(GL_COLOR_BUFFER_BIT)
#     glColor3f(1.0, 1.0, 1.0)
#     glPointSize(1)
#     glBegin(GL_POINT)
#     glEnd()
# def enemy():
#     pass
def hor_line(x1,y1,x2):
    glColor4f(0,0,0,1)
    glBegin(GL_LINE_STRIP)
    # glPointSize(100)
    glVertex2f(x1,y1)
    glVertex2f(x2,y1)
    glEnd()
def vert_line(x1,y1,y2):
    glColor4f(0,0,0,1)
    glPointSize(100)
    glBegin(GL_LINE_STRIP)
    # glPointSize(100)
    glVertex2f(x1,y1)
    glVertex2f(x1,y2)
    glEnd()

def start_menu():
    # glClear(1.0,1.0,1.0,1.0)
    glColor4f(0.7,0.7,0.9,1)
    glBegin(GL_POLYGON)
    glVertex2f(1300,1400)
    glVertex2f(2400,1400)
    glVertex2f(2400,1800)
    glVertex2f(1300,1800)
    glEnd()
    hor_line(1360,1780,1550)
    vert_line(1360,1780,1480) #The 4 lines represent E
    hor_line(1360,1480,1550)
    hor_line(1360,1620,1550)

    vert_line(1580,1780,1480)
    hor_line(1580,1780,1700)
    vert_line(1700,1780,1480) #The 5 lines represent N
    hor_line(1700,1480,1820)
    vert_line(1820,1780,1480)

    hor_line(1850,1780,2100)
    vert_line(2100,1780,1480) # The 4 lines represent D
    hor_line(1850,1480,2100)
    vert_line(1870,1780,1480)


    glBegin(GL_POLYGON)
    glColor4f(0.7,0.7,0.9,1)
    glVertex2f(1300,1900)
    glVertex2f(2400,1900)
    glVertex2f(2400,2300)
    glVertex2f(1300,2300)
    glEnd()

    hor_line(1360,2280,1540)
    vert_line(1360,2280,2130) #The 5 lines represent 'S'
    hor_line(1360,2130,1540)
    vert_line(1540,2130,1950)
    hor_line(1540,1950,1360)

    hor_line(1570,2280,1750)  #The 2 lines represent 'T'
    vert_line(1660,2280,1950)

    vert_line(1780,2280,1950)
    hor_line(1780,2280,1960) # The 4 lines represent 'A'
    hor_line(1780,2130,1960)
    vert_line(1960,2280,1950)

    vert_line(1990,2280,1950)
    hor_line(1990,2280,2140)
    vert_line(2140,2280,2130) #The 5 lines represent 'R'
    hor_line(1990,2130,2170)
    vert_line(2170,2130,1950)

    hor_line(2170,2280,2350)
    vert_line(2260,2280,1950) #The 2 lines represent 'T'



def main():
    boolval = "menu"
    enemylist = []
    booletlist = []
    wait = 0
    # init()
    x = [1000, 1000]
    counter = 0
    deg = 0.0
    jump =  3
    screens = 700
    pygame.init()
    display = (800, 900)
    wn = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    if boolval:
        glClearColor(0.7, 0.9, 1.0, 1.0)
    else:
        glClearColor(0.0,0.0,0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 4000.0, 0, 4000.0)
    # glClear(GL_COLOR_BUFFER_BIT)
    while True:
        if boolval == False:
            glClearColor(0.0, 0.0, 0.0, 1.0)
        if boolval == "start":
            glClear(GL_COLOR_BUFFER_BIT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        booletlist.append(x)
            p = pygame.key.get_pressed()

            # pygame.draw.rect(wn,(255,255,255),(20,20, 100,200),)
            # Gravity for the heli
            if x[1] > 200:
                x[1] = x[1] - 1
            # movement up for the heli
            if p[K_w] or p[K_UP]:
                x[1] = x[1] + 5
            # movement down for the heli
            if p[K_s] or p[K_DOWN]:
                if x[1] > 200:
                    x[1] = x[1] -5
            # movement down for the heli
            if p[K_a] or p[K_LEFT]:
                if x[0] > 650:
                    x[0] = x[0] - 5
            # movement right for the heli
            if p[K_d] or p[K_RIGHT]:
                x[0] = x[0] + 5
           


            # background()
            # print(x)
            counter += 1
            index = 0
            draw = helicopter.Helicopter(x[0],x[1], counter, deg) # Calls the helicopter class
            deg += 7 # provide the degree of rotation
            draw.draw()
            # start_menu()
            while index < len(booletlist):
                draw.draw_bullet(booletlist[index][0], booletlist[index][1])
                booletlist[index] = [booletlist[index][0] + 20, booletlist[index][1]]
                if (booletlist[index][0] > 4000):
                    booletlist.pop(index)
                index += 1
            #  print(booletlist)
            # The while loop below displays the enemies stored in ENEMYLIST list traversing through the whole list
            # Once an enemy is generated it the position along the x will be decreased by the JUMP variable in order to change the position
            index = 0
            while index < len(enemylist):
              
                enemy = Enemy.Enemy(enemylist[index][0], enemylist[index][1])
                enemy.draw()
                # The if statement below checks if there is a collision between the heli and the enemies
                # If the condition is satisfied it will change the BOOLVAL to false in which case the game play screen will not be displayed
                if(x[1] - 180 < enemylist[index][1] < x[1] + 180 and x[0] - 400 < enemylist[index][0]-10 <= x[0]+220):
                    boolval = "gameover"
                    print("collision")
                    pass
                # The below is statement will pop values from the list which are out of the screen to manage space
                if enemylist[index][0] < -10 and index >= 1:
                    if index == 1 and enemylist[0][0] < -20:
                        enemylist.pop(0)
                    else:
                        enemylist.pop(index)
                    index -= 1
                enemylist[index] = [enemylist[index][0]-jump,enemylist[index][1]]
                booletindex = 0
                while booletindex < len(booletlist):
                    if len(enemylist) > 0 and enemylist[index][0] - 80 < booletlist[booletindex][0] - 20 < booletlist[booletindex][0] + 20 < enemylist[index][0] + 80 and enemylist[index][1] - 100 < booletlist[booletindex][1] - 20 < booletlist[booletindex][1] + 20 < enemylist[index][1] + 100:
                        enemylist.pop(index)
                        booletlist.pop(booletindex) 
                        index -= 1
                        if(len(booletlist) == 0):
                            break
                    else:
                        booletindex += 1
                index += 1
            # The below if statement appends position of enemies in to ENEMYLIST list
            # Also increases the defficulty of the game by increasing the speed by which enmies are grnerated
            # When the game begins enemies are generated once in 700 screen renders in time this will decrease up to 150(SCREENS variable)
            # Every time the condition is satisfied the movement of the enemy blocks is increased by 0.2 coordinates(JUMP variable)
            if(counter == screens):
                enemylist.append([4000,x[1]])
                if screens > 150:
                    screens -= 15
                counter = 0
                jump += 0.2
        elif boolval == "menu":
            glClear(GL_COLOR_BUFFER_BIT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                            # if  1300<pos[0]< 2400 and 1400 < pos[1] < 1800:
                        boolval = "start"
                elif event.type == MOUSEBUTTONUP:
                    print("ime here")
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    if 260 < pos[0] < 479 and 407 < pos[1] < 470:
                        boolval = "start"
                    elif 260 < pos[0] < 479 and 497 < pos[1] < 581:
                        boolval = "quit"
            # Calls the helicopter class
            draw = helicopter.Helicopter(x[0], x[1], counter, deg)
            deg += 7  # provide the degree of rotation
            draw.draw()
            start_menu()
            pass
        elif boolval == "quit":
            pygame.quit()
            quit()
            pass
        elif boolval == "gameover":
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         quit()
            glClear(GL_COLOR_BUFFER_BIT)
            if wait == 800:
                boolval = "menu"
                enemylist = []
                booletlist = []
                wait = 0
                # init()
                x = [1000, 1000]
                counter = 0
                deg = 0.0
                jump = 3
                screens = 700
            wait += 1
            # glEnable(GL_BLEND)
            # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            # draw = helicopter.Helicopter(x[0], x[1], counter, deg)
            # deg += 7
            # draw.draw()
        glFlush()
        # pygame.display.update()
        pygame.display.flip()
        pygame.time.wait(1)
        

main()