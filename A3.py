from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def draw_circle(r, x0, y0):
    midpointLine(r, x0, y0)                #outer circle

    midpointLine(r/2, x0+r/2, y0)          #1
    midpointLine(r/2, x0-r/2, y0)          #5
    midpointLine(r/2, x0, y0+r/2)          #3
    midpointLine(r/2, x0, y0-r/2)          #7

    diagonal = math.sin(math.radians(45)) * r/2

    midpointLine(r/2, x0+diagonal, y0+diagonal) #2
    midpointLine(r/2, x0+diagonal, y0-diagonal) #8
    midpointLine(r/2, x0-diagonal, y0+diagonal) #4
    midpointLine(r/2, x0-diagonal, y0-diagonal) #6

def midpointLine(r, x0, y0):
    d = 1-r
    x = 0
    y = r
    circlePoints(x, y, x0, y0)

    while x<y:
        #Choose East
        if d<0:
            d = d+ 2*x +3
            x += 1
        #Choose South East
        else:
            d = d+ 2*x -2*y + 5
            x += 1
            y = y-1

        circlePoints(x, y, x0, y0)

def circlePoints(x, y, x0, y0):
    draw_points(x + x0, y + y0)
    draw_points(y + x0, x + y0)
    draw_points(y + x0, -x + y0)
    draw_points(x + x0, -y + y0)
    draw_points(-x + x0, -y + y0)
    draw_points(-y + x0, -x + y0)
    draw_points(-y + x0, x + y0)
    draw_points(-x + x0, y + y0)

def draw_points(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)

    glEnd()


def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # (Red, Green, Blue)
    glColor3f(1.0, 1.0, 1.0)

    #calling the draw circle method (radius,x0,y0)
    draw_circle(400, 500, 500)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000) #window_size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"MidPointCircle")

glutDisplayFunc(showScreen)
glutMainLoop()