from pickle import GLOBAL
from turtle import color
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import helicopter
import numpy as np

# def init():
    
# def background():
#     glClear(GL_COLOR_BUFFER_BIT)
#     glColor3f(1.0, 1.0, 1.0)
#     glPointSize(1)
#     glBegin(GL_POINT)
#     glEnd()


def main():
    pygame.init()
    display = (500, 500)
    wn = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.7, 0.9, 1.0, 1.0)
    gluOrtho2D(-1000.0, 1000.0, -1000.0, 1000.0)
    glClear(GL_COLOR_BUFFER_BIT)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # background()
        wn = pygame.display.set_mode((500, 500), DOUBLEBUF | OPENGL)
        draw = helicopter.Helicopter(-110, -500, wn)
        draw.draw()
        pygame.display.flip()
        pygame.time.wait(1)

main()