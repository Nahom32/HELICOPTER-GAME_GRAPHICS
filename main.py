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

 
def main():
    # init()
    x = [1200, 700]
    counter = 0
    deg = 0.0
    pygame.init()
    display = (800, 900)
    wn = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.7, 0.9, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 4000.0, 0, 4000.0)
    # glClear(GL_COLOR_BUFFER_BIT)
    while True:
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
        print(x)
        counter += 1
        draw = helicopter.Helicopter(x[0],x[1], counter, deg)
        enemy = Enemy.Enemy(800,800)
        deg += 7
        draw.draw()
        
        enemy.draw()
        glFlush()
        # pygame.display.update()
        pygame.display.flip()
        pygame.time.wait(1)
        
    

main()