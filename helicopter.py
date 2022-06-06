from cmath import cos, sin
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math



class Helicopter:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 1.0, 1.0)
        glEnable(GL_BLEND)
        glPointSize(10)
        glBegin(GL_POLYGON)
        rad = 160
        teta = 0.0
        while teta < 361:
            x = rad * cos(teta)
            y = rad * sin(teta)
            x = x.real
            y = y.real
            glVertex2d(x + self.x,
                       y + self.y)
            teta = teta + 1
        glColor4f(0.0, 0.0, 0.0, 0.0)

        glEnd()
        glBegin(GL_LINE_LOOP)
        glVertex2f(-600 + self.x, -60 +self.y)
        glVertex2f(-600 + self.x, 20+self.y)
        glVertex2f(-190 + self.x, 25+self.y)
        glVertex2f(-200+ self.x, -5 +self.y)
        glVertex2f(-190 + self.x, -70+self.y)
        glEnd()
        glFlush()
