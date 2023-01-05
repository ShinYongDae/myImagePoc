# PyBarnsleyFern.py
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import *
from numpy import *
import sys

# Globals for window width and height
global width
global height
global win

# Initial values of width and height
width = 600
height = 600
def init():
    # White background
    glClearColor(1.0, 1.0, 1.0, 0.0)
    # Green Plot… it IS a Fern
    glColor3f(0.3, 0.6, 0.2)
    # Set the projection matrix... our "view"
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Set the plot window range
    gluOrtho2D(-3.0, 3.0, 0.0, 10.5)
    # Set the matrix for the object we are drawing
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def plotfunc():
    # Choose an initial point... any point
    # You can randomize this if you wish
    x = -1.5
    y = 0.75
    glClear(GL_COLOR_BUFFER_BIT)
    # Plot 100000 points. This number is very large.
    # Feel free to experiment with smaller values.
    for n in range(0, 100000):
        # n allows us to reject the first few points
        # to give the attractor a chance to do its “thing”
        # Choose a random value between 0 and 1 and
        # then select a set of parameters based on this value.
        v = random.random()

        if v >= 0 and v <= 0.8000:
            a = 0
            b = 1.6
            c = -2.5 * pi / 180
            d = -2.5 * pi / 180
            e = 0.85
            f = 0.85
            # glColor3f(1.0, 0.0, 0.0)
        elif v > 0.8000 and v <= 0.8050:
            a = 0
            b = 0
            c = 0 * pi / 180
            d = 0 * pi / 180
            e = 0
            f = 0.16
            # glColor3f(0.0, 1.0, 0.0)
        elif v > 0.8050 and v <= 0.9025:
            a = 0
            b = 1.6
            c = 49 * pi / 180
            d = 49 * pi / 180
            e = 0.3
            f = 0.34
            # glColor3f(0.0, 0.0, 1.0)
        elif v > 0.9025 and v <= 1.0:
            a = 0
            b = 0.44
            c = 120 * pi / 180
            d = -50 * pi / 180
            e = 0.3
            f = 0.37
            # glColor3f(1.0, 0.0, 1.0)

        # Save the old values of x and y so we can iterate
        # those values according to the chosen parameters
        # and rules.
        xx = x
        yy = y
        # Apply the parameters to the rule equations
        x = e * xx * cos(c) - f * yy * sin(d) + a
        y = e * xx * sin(c) + f * yy * cos(d) + b
        # Start plotting after the 10th point
        if n > 10:
            glBegin(GL_POINTS)
            glVertex2f(x, y)
            glEnd()
            glFlush()

def keyboard(key, x, y):
    global win

    # Allows us to quit by pressing 'Esc' or 'q'
    if key == b'\x1b': #chr(27):
        glutDestroyWindow(win)
        #sys.exit()
    if key == b"q":
        glutDestroyWindow(win)
        #sys.exit()

def main():
    global width
    global height
    global win

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(width, height)
    win = glutCreateWindow(b"The Chaos Game... Fern!")
    glutDisplayFunc(plotfunc)
    glutKeyboardFunc(keyboard)
    init()
    glutMainLoop()

main()
#End of Program