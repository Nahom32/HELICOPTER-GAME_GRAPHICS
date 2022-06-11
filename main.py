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
 
def main():
    boolval = True
    enemylist = []
    # init()
    x = [1200, 700]
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
        if boolval:
            glClear(GL_COLOR_BUFFER_BIT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            p = pygame.key.get_pressed()

            pygame.draw.rect(wn,(255,255,255),(20,20, 100,200),)
            # Gravity for the heli
            if x[1] > 200:
                x[1] = x[1] - 2
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
            draw = helicopter.Helicopter(x[0],x[1], counter, deg) # Calls the helicopter class
            deg += 7 # provide the degree of rotation
            draw.draw()
            # The while loop below displays the enemies stored in ENEMYLIST list traversing through the whole list
            # Once an enemy is generated it the position along the x will be decreased by the JUMP variable in order to change the position
            index = 0
            while index < len(enemylist):
                enemy = Enemy.Enemy(enemylist[index][0], enemylist[index][1])
                enemy.draw()
                # The if statement below checks if there is a collision between the heli and the enemies
                # If the condition is satisfied it will change the BOOLVAL to false in which case the game play screen will not be displayed
                if(x[1] - 180 < enemylist[index][1] < x[1] + 180 and x[0] - 400 < enemylist[index][0]-10 <= x[0]+220):
                    boolval = False
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
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            glClear(GL_COLOR_BUFFER_BIT)
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