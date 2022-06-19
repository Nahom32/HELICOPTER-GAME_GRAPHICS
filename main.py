# import imp
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import helicopter
import Enemy
# import numpy as np
# import time
from startmenu import *
import random
from clouds import Clouds
from score import *
import os


def main():
    pygame.init()
    # os.getcwd()
    # helisound = pygame.mixer.Sound("helisound.ogg")
    # pygame.mixer.music.load('jazz.wav')
    boolval = "menu"
    enemylist = []
    booletlist = []
    wait = 0
    special = 0
    score = 0
    cloudcounter = 0
    cloudlist = []
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
    glClear(GL_COLOR_BUFFER_BIT)
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
                        booletlist.append([x[0] + 220, x[1] - 95])
            p = pygame.key.get_pressed()

            # pygame.draw.rect(wn,(255,255,255),(20,20, 100,200),)
            # Gravity for the heli
            if x[1] > 200:
                x[1] = x[1] - 10
            # movement up for the heli
            if p[K_w] or p[K_UP]:
                x[1] = x[1] + 25
            # movement down for the heli
            if p[K_s] or p[K_DOWN]:
                if x[1] > 200:
                    x[1] = x[1] -15
            # movement down for the heli
            if p[K_a] or p[K_LEFT]:
                if x[0] > 650:
                    x[0] = x[0] - 15
            # movement right for the heli
            if p[K_d] or p[K_RIGHT]:
                x[0] = x[0] + 15
           


            # background()
            # print(x)

            intx = 3800
            counter += 10
            newscore = score
            curscore = str(newscore)
            int(score)
            # numdraw = Score(3900, inty)
            for sc in curscore:
                numdraw = Score(intx, 3800)
                if sc == "1":
                    numdraw.one()
                elif sc == "2":
                    numdraw.two()
                elif sc == "3":
                    numdraw.three()
                elif sc == "4":
                    numdraw.four()
                elif sc == "5":
                    numdraw.five()
                elif sc == "6":
                    numdraw.six()
                elif sc == "7":
                    numdraw.seven() 
                elif sc == "8":
                    numdraw.eight()
                elif sc == "9":
                    numdraw.nine()
                elif sc == "0":
                    numdraw.zero()
                intx += 60

            cloudcounter += 1
            if cloudcounter == 1:
                cloudpos = random.randint(2500,3800)
                cloudlist.append([4500, cloudpos])
            if cloudcounter == 500:
                cloudcounter = 0
            cldcounter = 0
            while cldcounter < len(cloudlist):
                if cloudlist[cldcounter][1] < -500:
                    cloudlist.pop(cldcounter)
                cldcounter += 1
            cldcounter = 0
            # print("some")
            while cldcounter < len(cloudlist):
                cld = Clouds(cloudlist[cldcounter][0], cloudlist[cldcounter][1])
                cld.drawCloud()
                cloudlist[cldcounter] = [
                    cloudlist[cldcounter][0]-5, cloudlist[cldcounter][1]]
                cldcounter += 1
            draw = helicopter.Helicopter(x[0],x[1], counter, deg, score = score) # Calls the helicopter class
            deg += 17 # provide the degree of rotation
            draw.draw()
            # helisound.play(-1)
            # start_menu()
            index = 0
            while index < len(booletlist):
                draw.draw_bullet(booletlist[index][0], booletlist[index][1])
                booletlist[index] = [booletlist[index][0] + 40, booletlist[index][1]]
                if (booletlist[index][0] > 4000):
                    booletlist.pop(index)
                index += 1
            index = 0
            while index < len(booletlist):
                if booletlist[index][1] > 4000:
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
                        score += 1
                        if(len(booletlist) == 0):
                            break
                    else:
                        booletindex += 1
                index += 1
            # print(score)
            # The below if statement appends position of enemies in to ENEMYLIST list
            # Also increases the defficulty of the game by increasing the speed by which enmies are grnerated
            # When the game begins enemies are generated once in 700 screen renders in time this will decrease up to 150(SCREENS variable)
            # Every time the condition is satisfied the movement of the enemy blocks is increased by 0.2 coordinates(JUMP variable)
            if(counter == screens):
                enemylist.append([4000,x[1]])
                if special == 1000:
                    num = random.randint(100,3950)
                    special = 0
                    if num != x[1]:
                        enemylist.append([4000, num])
                if screens > 150:
                    screens -= 15
                counter = 0
                jump += 9
            special += 10
            if special == 1000:
                num = random.randint(100, 3950)
                special = 0
                if num != x[1]:
                    enemylist.append([4000, num])
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
            # cloud = Clouds(3000,3000)
            # cloud.drawCloud()
            cloudcounter += 1
            if cloudcounter == 1:
                cloudpos = random.randint(2500, 3800)
                cloudlist.append([4500, cloudpos])
            if cloudcounter == 300:
                cloudcounter = 0
            cldcounter = 0
            while cldcounter < len(cloudlist):
                if cloudlist[cldcounter][1] < -500:
                    cloudlist.pop(cldcounter)
                cldcounter += 1
            cldcounter = 0
            # print("some")
            while cldcounter < len(cloudlist):
                cld = Clouds(cloudlist[cldcounter][0],
                             cloudlist[cldcounter][1])
                cld.drawCloud()
                cloudlist[cldcounter] = [
                    cloudlist[cldcounter][0]-5, cloudlist[cldcounter][1]]
                cldcounter += 1
            draw = helicopter.Helicopter(x[0], x[1], counter, deg)
            deg += 7  # provide the degree of rotation
            draw.draw()
            start_menu()
            score = 0
        elif boolval == "quit":
            pygame.quit()
            quit()
            pass
        elif boolval == "gameover":
            glClear(GL_COLOR_BUFFER_BIT)
            if wait >= 500:
                print(score)
                boolval = "menu"
                enemylist = []
                booletlist = []
                wait = 0
                # init()
                x = [1000, 1000]
                counter = 0
                deg = 0.0
                jump = 10
                screens = 700
            wait += 9
        glFlush()
        pygame.display.flip()
        pygame.time.wait(10)
        

main()