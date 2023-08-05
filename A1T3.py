from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_lines(x1,y1,x2,y2):
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()


def iterate():
    glViewport(0, 0, 900, 400)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 900, 0.0, 400, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # call the draw methods here
    #1
    glColor3f(1.0, 0.0, 0.0)
    draw_lines(100, 300, 100, 100)

    #8
    glColor3f(0.0, 0.0, 1.0)
    draw_lines(150, 300, 250, 300)
    draw_lines(150, 200, 250, 200)
    draw_lines(150, 100, 250, 100)

    draw_lines(150, 300, 150, 100)
    draw_lines(250, 300, 250, 100)

    #3
    glColor3f(0.0, 1.0, 0.0)
    draw_lines(300, 300, 350, 300)
    draw_lines(300, 200, 350, 200)
    draw_lines(300, 100, 350, 100)

    draw_lines(350, 300, 350, 100)

    #0
    glColor3f(0.0, 1.0, 1.0)
    draw_lines(400, 300, 450, 300)
    draw_lines(400, 100, 450, 100)

    draw_lines(400, 300, 400, 100)
    draw_lines(450, 300, 450, 100)

    #1
    glColor3f(1.0, 0.0, 0.0)
    draw_lines(500, 300, 500, 100)

    #2
    glColor3f(1.0, 0.0, 1.0)
    draw_lines(550, 300, 600, 300)
    draw_lines(550, 200, 600, 200)
    draw_lines(550, 100, 600, 100)

    draw_lines(600, 300, 600, 200)
    draw_lines(550, 200, 550, 100)

    #6
    glColor3f(1.0, 1.0, 0.0)
    draw_lines(650, 300, 700, 300)
    draw_lines(650, 200, 700, 200)
    draw_lines(650, 100, 700, 100)

    draw_lines(650, 300, 650, 100)
    draw_lines(700, 200, 700, 100)

    #5
    glColor3f(1.0, 1.0, 1.0)
    draw_lines(750, 300, 800, 300)
    draw_lines(750, 200, 800, 200)
    draw_lines(750, 100, 800, 100)

    draw_lines(750, 300, 750, 200)
    draw_lines(800, 200, 800, 100)




    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(900, 400) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task3: StudentID")
glutDisplayFunc(showScreen)

glutMainLoop()
