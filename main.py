import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import helicopter
import numpy as np


x = [400, 400]

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
    pygame.init()
    display = (800, 800)
    wn = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.7, 0.9, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 4000.0, 0, 4000.0)
    glClear(GL_COLOR_BUFFER_BIT)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        p = pygame.key.get_pressed()

        pygame.draw.rect(wn,(255,255,255),(20,20, 100,200),)
        if p[K_w] or p[K_UP]:
            # print("up")
            x[1] = x[1] + 2
        if p[K_s] or p[K_DOWN]:
            x[1] = x[1] -2
        if p[K_a] or p[K_LEFT]:
            x[0] = x[0] - 2
        if p[K_d] or p[K_RIGHT]:
            x[0] = x[0] + 2
        # background()
        print(x)
        draw = helicopter.Helicopter(x[0],x[1])
        draw.draw()
        # pygame.display.update()
        pygame.display.flip()
        pygame.time.wait(1)

main()