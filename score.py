from OpenGL.GL import *
from OpenGL.GLU import *

class Score:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def zero(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glColor4f(0, 0, 0, 1)
        glBegin(GL_LINE_STRIP)
        glVertex2f(self.x - 20, self.y + 40)
        glVertex2f(self.x + 20, self.y + 40)
        glVertex2f(self.x + 20, self.y - 40)
        glVertex2f(self.x - 20, self.y - 40)
        glVertex2f(self.x - 20, self.y + 40)
        glEnd()

    def one(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glColor4f(0, 0, 0, 1)
        glBegin(GL_LINE_STRIP)
        glVertex2f(self.x, self.y + 40)
        glVertex2f(self.x, self.y - 40)
        glEnd()
    
    def two(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glColor4f(0, 0, 0, 1)
        glBegin(GL_LINE_STRIP)
        glVertex2f(self.x - 20, self.y + 40)
        glVertex2f(self.x + 20, self.y + 40)
        glVertex2f(self.x + 20, self.y)
        glVertex2f(self.x - 20, self.y)
        glVertex2f(self.x - 20, self.y - 40)
        glVertex2f(self.x + 20, self.y - 40)
        glEnd()

    def three(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glColor4f(0, 0, 0, 1)
        glBegin(GL_LINE_STRIP)
        glVertex2f(self.x - 20, self.y + 40)
        glVertex2f(self.x + 20, self.y + 40)
        glVertex2f(self.x + 20, self.y)
        glVertex2f(self.x - 20, self.y)
        glVertex2f(self.x + 20, self.y)
        glVertex2f(self.x + 20, self.y - 40)
        glVertex2f(self.x - 20, self.y - 40)
        glEnd()

    def four(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glColor4f(0, 0, 0, 1)
        glBegin(GL_LINE_STRIP)
        glVertex2f(self.x - 20, self.y + 40)
        # glVertex2f(self.x + 20, self.y)
        glVertex2f(self.x - 20, self.y)
        glVertex2f(self.x + 20, self.y)
        glVertex2f(self.x + 20, self.y + 40)
        glVertex2f(self.x + 20, self.y - 40)
        glEnd()
    
    def five(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glColor4f(0, 0, 0, 1)
        glBegin(GL_LINE_STRIP)
        glVertex2f(self.x + 20, self.y + 40)
        glVertex2f(self.x - 20, self.y + 40)
        glVertex2f(self.x - 20, self.y)
        glVertex2f(self.x + 20, self.y)
        # glVertex2f(self.x + 20, self.y)
        glVertex2f(self.x + 20, self.y - 40)
        glVertex2f(self.x - 20, self.y - 40)
        glEnd()
    
    def six(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glColor4f(0, 0, 0, 1)
        glBegin(GL_LINE_STRIP)
        glVertex2f(self.x + 20, self.y + 40)
        glVertex2f(self.x - 20, self.y + 40)
        glVertex2f(self.x - 20, self.y)
        glVertex2f(self.x + 20, self.y)
        glVertex2f(self.x + 20, self.y - 40)
        glVertex2f(self.x - 20, self.y - 40)
        glVertex2f(self.x - 20, self.y)
        glEnd()

    def seven(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glColor4f(0, 0, 0, 1)
        glBegin(GL_LINE_STRIP)
        glVertex2f(self.x - 20, self.y + 40)
        glVertex2f(self.x + 20, self.y + 40)
        glVertex2f(self.x, self.y -40)
        glEnd()
    
    def eight(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glColor4f(0, 0, 0, 1)
        glBegin(GL_LINE_STRIP)
        glVertex2f(self.x + 20, self.y)
        glVertex2f(self.x + 20, self.y + 40)
        glVertex2f(self.x - 20, self.y + 40)
        glVertex2f(self.x - 20, self.y)
        glVertex2f(self.x + 20, self.y)
        glVertex2f(self.x + 20, self.y - 40)
        glVertex2f(self.x - 20, self.y - 40)
        glVertex2f(self.x - 20, self.y)
        glEnd()

    def nine(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glColor4f(0, 0, 0, 1)
        glBegin(GL_LINE_STRIP)
        glVertex2f(self.x - 20, self.y)
        glVertex2f(self.x - 20, self.y + 40)
        glVertex2f(self.x + 20, self.y + 40)
        glVertex2f(self.x + 20, self.y)
        glVertex2f(self.x - 20, self.y)
        glVertex2f(self.x + 20, self.y)
        glVertex2f(self.x + 20, self.y - 40)
        glEnd()

    
