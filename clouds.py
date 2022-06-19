from cmath import cos, sin
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Clouds:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def drawCloud(self):
        # glClear(GL_COLOR_BUFFER_BIT)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
        glPointSize(10)
        glBegin(GL_POLYGON)
        glColor4f(1.0, 1.0, 1.0, 0.05)
        rad = 300
        teta = 0.0
        while teta < 360:
            x = rad * cos(teta)
            y = rad * sin(teta)
            x = x.real
            y = y.real
            glVertex2d(x + self.x, y + self.y)
            teta = teta + 1
        glEnd()
        glBegin(GL_POLYGON)
        glColor4f(1.0, 1.0, 1.0, 0.05)
        rad = 230
        teta = 0.0
        while teta < 360:
            x = rad * cos(teta)
            y = rad * sin(teta)
            x = x.real
            y = y.real
            glVertex2d(x + self.x - 300, y + self.y)
            teta = teta + 1
        glEnd()
        glBegin(GL_POLYGON)
        glColor4f(1.0, 1.0, 1.0, 0.05)
        rad = 200
        teta = 0.0
        while teta < 360:
            x = rad * cos(teta)
            y = rad * sin(teta)
            x = x.real
            y = y.real
            glVertex2d(x + self.x + 300, y + self.y)
            teta = teta + 1
        glEnd()
