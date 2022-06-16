from cmath import cos, sin
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
# import math



class Helicopter:
    def __init__(self,x,y, counter, deg) -> None:
        self.deg = deg
        self.counter = counter
        self.x = x
        self.y = y
    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)

        # glColor4f(1.0, 1.0, 1.0, 1.0)
        # glEnable(GL_BLEND)
        glPointSize(10)


        # The legs of the helicopter are drawn below this
        glBegin(GL_POLYGON)
        glColor4f(0.6, 0.2, 0.4, 1.0)
        glVertex2f(-80 + self.x, -120 + self.y)
        glVertex2f(-80 + self.x, -200 + self.y)
        glVertex2f(-120 + self.x, -200 + self.y)
        glVertex2f(-100 + self.x, -120 + self.y)
        glEnd()
        glBegin(GL_POLYGON)
        glColor4f(0.6, 0.2, 0.4, 1.0)
        glVertex2f(-120 + self.x, -200 + self.y)
        glVertex2f(120 + self.x, -200 + self.y)
        glVertex2f(120 + self.x, -180 + self.y)
        glVertex2f(-120 + self.x, -180 + self.y)
        glEnd()
        glBegin(GL_POLYGON)
        glColor4f(0.6, 0.2, 0.4, 1.0)
        glVertex2f(80 + self.x, -120 + self.y)
        glVertex2f(80 + self.x, -200 + self.y)
        glVertex2f(120 + self.x, -200 + self.y)
        glVertex2f(100 + self.x, -120 + self.y)
        glEnd()
        # Drawing of the legs is finished at this point

        # The back of the helicopter is drawn here below
        glBegin(GL_POLYGON)
        glColor4f(0.0, 0.0, 0.0, 1.0)
        glVertex2f(-100 + self.x, 50 + self.y)
        glVertex2f(-100 + self.x, -50 + self.y)
        glVertex2f(-600 + self.x, 10 + self.y)
        glVertex2f(-600 + self.x, 50 + self.y)
        glEnd()

        # Trying to Build a WINDOW for the heli
        glBegin(GL_POLYGON)
        glColor4f(0.1,0.1,0.1,0.01)
        rad = 110
        teta = 0.0
        while teta < 360:
            x = rad * cos(teta)
            y = rad * sin(teta)
            x = x.real
            y = y.real
            glVertex2d(x + self.x + 100, y + self.y + 20)
            teta = teta + 1
        glEnd()

        # The middle part of the heli
        glBegin(GL_POLYGON)
        glColor4f(0.0, 0.5, 0.9, 1.0)
        rad = 160
        teta = 0.0
        while teta < 360:
            x = rad * cos(teta)
            y = rad * sin(teta)
            x = x.real
            y = y.real
            glVertex2d(x + self.x,y + self.y)
            teta = teta + 1
        glEnd()

        # The thing to cary the rototor
        glBegin(GL_POLYGON)
        glColor4f(0.0, 0.0, 0.0, 1.0)
        glVertex2f(self.x + 20,self.y + 155)
        glVertex2f(self.x - 20,self.y + 155)
        glVertex2f(self.x - 20,self.y + 200)
        glVertex2f(self.x + 20,self.y + 200)
        glEnd()
        

        # helicopter TOP-rotor drawing
        glBegin(GL_POLYGON)
        glColor4f(0.0, 0.0, 0.0, 8.0)
        radian = self.deg * np.pi / 180.0
        mat = np.array([
            [np.cos(radian), 0],
            [0, 1],
        ])
        glVertex2f(self.x + (400 * mat[0][0] + 220 * mat[0][1]),self.y +
                    (400* mat[1][0] + 220 *mat[1][1]))
        glVertex2f(self.x + 410 * mat[0][0] + 190 * mat[0][1],self.y +
                   410 * mat[1][0] + 190 * mat[1][1])
        glVertex2f(self.x -400 * mat[0][0] + 180 * mat[0]
                   [1],self.y -400 * mat[1][0] + 180 * mat[1][1])
        glVertex(self.x -410 * mat[0][0] + 150 * mat[0][1],self.y -
                 410 * mat[1][0] + 150 * mat[1][1])
        glEnd()




        # The rotor for the back of the helicopter is drawn here
        glBegin(GL_POLYGON)
        glColor4f(0.0, 0.0, 0.0, 0.7)
        radian = (self.deg) * np.pi / 180.0
        mat = np.array([
            [np.cos(radian), -np.sin(radian)],
            [np.sin(radian), np.cos(radian)],
        ])
        vertexes = [[-20,150],[20,150],[-20,-150],[20,-150]]
        for vertex in vertexes:
            glVertex2f(-570 + self.x + vertex[1] * mat[0][0] + vertex[0]*mat[0]
                       [1],27 + self.y + vertex[1] * mat[1][0] + vertex[0]*mat[1][1])
        glEnd()
        glBegin(GL_POLYGON)
        glColor4f(0.0, 0.0, 0.0, 0.7)
        radian = (self.deg) * np.pi / 180.0
        mat = np.array([
            [np.cos(radian), -np.sin(radian)],
            [np.sin(radian), np.cos(radian)],
        ])
        vertexes = [[-20, 150], [20, 150], [-20, -150], [20, -150]]
        for vertex in vertexes:
            glVertex2f(-570 + self.x + vertex[0] * mat[0][0] + vertex[1]*mat[0]
                       [1], 27 + self.y + vertex[0] * mat[1][0] + vertex[1]*mat[1][1])
        glEnd()
    def get_pos(self):
        #This helps the enemy to get the position of the helicopter
        return (self.x,self.y)
    def draw_bullet(self,x_start, y_start):
        arr = np.linspace(0,360, 200)
        count = 0
        glBegin(GL_POLYGON)
        glColor4f(1.0,0.5,0,1.0)
        rad = 20
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
    # def shoot(self):
    #     bullet_list = []
    #     bullet_list.append(self.get_pos())
        #This is where the shooting structure is done
        

        
