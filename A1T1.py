from OpenGL.GL import *
from OpenGL.GLUT import *
import random
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_POINTS) #GL_POINTS is a built-in method. it can be line or anything else
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    for i in range(100):
        x= random.randint(0, 500)
        y= random.randint(0, 500)
        draw_points(x, y)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task1: 50 random pixels")
glutDisplayFunc(showScreen)

glutMainLoop()
