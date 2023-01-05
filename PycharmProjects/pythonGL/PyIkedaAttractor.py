# PyIkedaAttractor.py
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import *
from numpy import *
import sys

global width
global height
global win

# Initial values of width and height
width = 600
height = 600

def init():
    # White background
    glClearColor(1.0, 1.0, 1.0, 0.0)

    # Ugly Purple Plot
    glColor3f(0.45, 0.3, 0.5)

    # Set the projection matrix... our "view"
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Set the plot window range
    #gluOrtho2D(-0.75, 2.0, -2.25, 1.25)
    #gluOrtho2D(-20.0, 20.0, -20.0, 20.0)
    #gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    gluOrtho2D(-8.0, 10.0, -8.0, 10.0)

    # Set the matrix for the object we are drawing
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def plotikeda():
    # Choose an initial point... any point
    x = 0.5
    y = 0.5

    glClear(GL_COLOR_BUFFER_BIT)
    for n in range(0, 100000):
        temp = 0.4 - 7.7 / (1 + x * x + y * y)
        xx = 1 + 0.9 * (x * cos(temp) - y * sin(temp))
        y = 0.9 * (x * sin(temp) + y * cos(temp))
        x = xx
        # glColor3f(cos(x), sin(y), tan(x))
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()
        glFlush()

def plotmira():
    glClear(GL_COLOR_BUFFER_BIT)
    # Initial values for parameters
    # This attractor is very sensitive
    # To the values for x, y, a, and b
    x = 12
    y = 0
    a = 0.301
    b = 0.9998
    c = 2 - 2*a
    w = a*x + c*x*x/(1+x*x)
    # Plot a significant number of points
    for n in arange(0,100000):
        z = x
        x = b*y + w
        u = x*x
        w = a*x + c*u/(1 + u)
        y = w - z
        # Don't plot anything until we've hit the attractor
        if n > 100:
            # How does this color statement work?
            glColor3f(sqrt(x*x + y*y)/15, 0.0, 0.0)
            glBegin(GL_POINTS)
            glVertex2f(x,y)
            glEnd()
            glFlush()
# End function

def plot3Body():
    a = 1.16
    glClear(GL_COLOR_BUFFER_BIT)
    for x in arange(0,1.0, 0.05):
        for y in arange(0,1.0, 0.05):
            for i in arange(1,1000):
                xx = x*cos(a) - (y-x*x)*sin(a)
                y = x*sin(a) + (y-x*x)*cos(a)
                x = xx
                if x > 1.0 or x < -1.0 or y > 1.0 or y < -1.0:
                    break
                glColor3f(cos(i),sin(i),tan(i))
                glBegin(GL_POINTS)
                glVertex2f(x,y)
                glEnd()
                glFlush()
# End Function

def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    # Initial values for parameters
    # This attractor is very sensitive
    # To the values for x, y, a, and b
    x = -0.1
    y = 0
    # Plot a significant number of points
    for n in arange(0,50000):
        xx = 1 - y + abs(x)
        y = x
        x = xx
        # Don't plot until we've hit the attractor
        if n > 100:
            # How does this color statement work?
            glColor3f(sqrt(x*x+y*y)/15, 0.0, 0.0)
            glBegin(GL_POINTS)
            glVertex2f(x,y)
            glEnd()
            glFlush()

def keyboard(key, x, y):
    global win

    # Allows us to quit by pressing 'Esc' or 'q'
    if key == b'\x1b': #chr(27):
        glutDestroyWindow(win)
    if key == b"q":
        glutDestroyWindow(win)

def main():
    global win
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(width, height)
    win = glutCreateWindow(b"The Ikeda Attractor")
    #glutDisplayFunc(plotikeda)
    #glutDisplayFunc(plotmira)
    #glutDisplayFunc(plot3Body)
    glutDisplayFunc(plotfunc)
    glutKeyboardFunc(keyboard)
    init()
    glutMainLoop()

main()
# End Program



