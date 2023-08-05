from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def findZone(x0, y0, x1, y1):
    dy = y1-y0
    dx = x1-x0
    if abs(dx) > abs(dy):   #for zone 0, 3, 4, 7
        if dx > 0 and dy > 0:
            return 0
        elif dx < 0 and dy > 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        else:
            return 7

    else:                   #for zone 1, 2, 5, 6
        if dx > 0 and dy > 0:
            return 1
        elif dx < 0 and dy > 0:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        else:
            return 6


def ZoneZeroConversion(zone, x, y):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y

def zero_to_original_zone(zone, x, y):
    if zone == 0:
        return x, y
    if zone == 1:
        return y, x
    if zone == 2:
        return -y, -x
    if zone == 3:
        return -x, y
    if zone == 4:
        return -x, -y
    if zone == 5:
        return -y, -x
    if zone == 6:
        return y, -x
    if zone == 7:
        return x, -y

def MidPointLine(zone, x0, y0, x1, y1):
    dy = y1-y0
    dx = x1-x0
    d_init = 2*dy - dx
    e = 2*dy
    ne = 2*(dy-dx)

    x = x0
    y = y0

    while x <= x1:
        a, b = zero_to_original_zone(zone, x, y)  # Converting the points to the original zone and then drawing it
        draw_points(a, b)

        if d_init <= 0:
            x += 1
            d_init += e

        else:
            x += 1
            y += 1
            d_init += ne

def eight_way_symmetry(x0, y0, x1, y1):
    zone = findZone(x0, y0, x1, y1)
    z0_x0, z0_y0 = ZoneZeroConversion(zone, x0, y0)
    z0_x1, z0_y1 = ZoneZeroConversion(zone, x1, y1)
    MidPointLine(zone, z0_x0, z0_y0, z0_x1, z0_y1)

def six():
    eight_way_symmetry(100, 400, 200, 400)
    eight_way_symmetry(100, 400, 100, 100)
    eight_way_symmetry(100, 100, 200, 100)
    eight_way_symmetry(100, 250, 200, 250)
    eight_way_symmetry(200, 250, 200, 100)


def five():
    eight_way_symmetry(300, 400, 400, 400)
    eight_way_symmetry(300, 400, 300, 250)
    eight_way_symmetry(300, 250, 400, 250)
    eight_way_symmetry(400, 250, 400, 100)
    eight_way_symmetry(300, 100, 400, 100)

def draw_points(x, y):
    glPointSize(5)
    glBegin(GL_POINTS)
    # Think of this as a co-ordinate. At the given x and y position the pixel will be drawn.
    glVertex2f(x, y)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    # (Red, Green, Blue)
    glColor3f(1.0, 1.0, 1.0)

    six()
    five()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)

# Size of the window.
# Manipulating this value will let us change the size of the output widow where the pixel is shown.
glutInitWindowSize(500, 600)

glutInitWindowPosition(0, 0)

# window name
wind = glutCreateWindow(b"MidpointLineDrawingAlgorithm:18301265")

glutDisplayFunc(showScreen)

glutMainLoop()
