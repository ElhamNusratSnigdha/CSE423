from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_POINTS) #GL_POINTS is a built-in method. it can be line or anything else
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def draw_lines(x1,y1,x2,y2):
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()

def draw_triangles(x1,y1,x2,y2,x3,y3):
    glLineWidth(5)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
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
    # call the draw methods here
    #roof
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    draw_triangles(250, 600, 750, 600, 500, 900)

    #house
    glColor3f(1.0, 0.0, 0.0)
    draw_lines(250,600,750,600)
    draw_lines(250, 600, 250, 100)
    draw_lines(750, 600, 750, 100)
    draw_lines(250, 100, 750, 100)

    #windows
    glColor3f(1.0, 0.0, 1.0)
    draw_lines(300, 500, 400, 500)
    draw_lines(300, 500, 300, 400)
    draw_lines(300, 400, 400,400)
    draw_lines(400, 400, 400, 500)

    draw_lines(600, 500, 600, 400)
    draw_lines(600, 400, 700, 400)
    draw_lines(700, 400, 700, 500)
    draw_lines(600, 500, 700, 500)

    #door
    glColor3f(0.0, 1.0, 1.0)
    draw_lines(450, 300, 550, 300)
    draw_lines(450, 300, 450, 100)
    draw_lines(550, 300, 550, 100)

    draw_points(520, 200)


    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task2: House Building")
glutDisplayFunc(showScreen)

glutMainLoop()
