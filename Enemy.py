import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

class Enemy:
    def __init__(self,x_pos,y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def draw(self):
        # glClear(GL_COLOR_BUFFER_BIT)
        # glEnable(GL_BLEND)
        # glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
        glColor4f(0.9, 0.8, 0.9, 1.0)
        # glEnable(GL_BLEND)
        glPointSize(10)
        glBegin(GL_POLYGON)
        glVertex2f(80 + self.x_pos, 270 + self.y_pos)
        glVertex2f(80 + self.x_pos, 140 + self.y_pos)
        glVertex2f(200 + self.x_pos, 140 + self.y_pos)
        glVertex2f(200 + self.x_pos, 270 + self.y_pos)
        glEnd()
        
        
        