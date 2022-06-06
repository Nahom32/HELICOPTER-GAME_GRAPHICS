from cmath import cos, sin
from ctypes.wintypes import RGB
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np



class Helicopter:
    def __init__(self,x,y, wn) -> None:
        self.wn = wn
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.circle(self.wn,(0,0,0), (self.x,self.y), 50)