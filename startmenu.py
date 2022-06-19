from OpenGL.GL import *
from OpenGL.GLU import *

def hor_line(x1, y1, x2):
    glColor4f(0, 0, 0, 1)
    glBegin(GL_LINE_STRIP)
    # glPointSize(100)
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glEnd()


def vert_line(x1, y1, y2):
    glColor4f(0, 0, 0, 1)
    # glPointSize(100)
    glBegin(GL_LINE_STRIP)
    # glPointSize(100)
    glVertex2f(x1, y1)
    glVertex2f(x1, y2)
    glEnd()


def start_menu():
    # glClear(1.0,1.0,1.0,1.0)
    glColor4f(0.7, 0.7, 0.9, 1)
    glBegin(GL_POLYGON)
    glVertex2f(1300, 1400)
    glVertex2f(2400, 1400)
    glVertex2f(2400, 1800)
    glVertex2f(1300, 1800)
    glEnd()
    hor_line(1360, 1780, 1550)
    vert_line(1360, 1780, 1480)  # The 4 lines represent E
    hor_line(1360, 1480, 1550)
    hor_line(1360, 1620, 1550)

    vert_line(1580, 1780, 1480)
    hor_line(1580, 1780, 1700)
    vert_line(1700, 1780, 1480)  # The 5 lines represent N
    hor_line(1700, 1480, 1820)
    vert_line(1820, 1780, 1480)

    hor_line(1850, 1780, 2100)
    vert_line(2100, 1780, 1480)  # The 4 lines represent D
    hor_line(1850, 1480, 2100)
    vert_line(1870, 1780, 1480)

    glBegin(GL_POLYGON)
    glColor4f(0.7, 0.7, 0.9, 1)
    glVertex2f(1300, 1900)
    glVertex2f(2400, 1900)
    glVertex2f(2400, 2300)
    glVertex2f(1300, 2300)
    glEnd()

    hor_line(1360, 2280, 1540)
    vert_line(1360, 2280, 2130)  # The 5 lines represent 'S'
    hor_line(1360, 2130, 1540)
    vert_line(1540, 2130, 1950)
    hor_line(1540, 1950, 1360)

    hor_line(1570, 2280, 1750)  # The 2 lines represent 'T'
    vert_line(1660, 2280, 1950)

    vert_line(1780, 2280, 1950)
    hor_line(1780, 2280, 1960)  # The 4 lines represent 'A'
    hor_line(1780, 2130, 1960)
    vert_line(1960, 2280, 1950)

    vert_line(1990, 2280, 1950)
    hor_line(1990, 2280, 2140)
    vert_line(2140, 2280, 2130)  # The 5 lines represent 'R'
    hor_line(1990, 2130, 2170)
    vert_line(2170, 2130, 1950)

    hor_line(2170, 2280, 2350)
    vert_line(2260, 2280, 1950)  # The 2 lines represent 'T'
