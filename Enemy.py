import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from helicopter import Helicopter
from cmath import cos, sin

class Enemy:
    def __init__(self,x_pos,y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
    def pos(self):
        return (self.x_pos,self.y_pos)
    def draw(self):
        # glClear(GL_COLOR_BUFFER_BIT)
        # glEnable(GL_BLEND)
        # glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
        glColor4f(0.0, 0.0, 0.0, 1.0)
        # glEnable(GL_BLEND)
        glPointSize(10)
        glBegin(GL_POLYGON)
        glVertex2f(80 + self.x_pos, -100 + self.y_pos)
        glVertex2f(80 + self.x_pos, 100 + self.y_pos)
        glVertex2f(-80 + self.x_pos, 100 + self.y_pos)
        glVertex2f(-80 + self.x_pos, -100 + self.y_pos)
        glEnd()
    def draw_bullet(self,x_start, y_start):
        arr = np.linspace(0,360, 1000)
        count = 0
        glBegin(GL_POLYGON)
        glColor4f(1.0,0.5,0,1.0)
        rad = 15
        teta = arr[count]
        while teta < 360:
            x = rad * cos(teta)
            y = rad * sin(teta)
            x = x.real
            y = y.real
            glVertex2d(x + x_start ,y + y_start)
            count+=1
            teta = arr[count]
        glEnd()

    




            

        
        
        