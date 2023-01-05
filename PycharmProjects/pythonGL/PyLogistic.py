# PyLogistic.py
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys

# Define the width and height variables as global
global width
global height

# Initial values for width and height
width = 600
height = 600

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-8.0, 7.0, 0.0, 1.0)

def plotlogistic():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(1.0)

    # Set the initial values of x and r
    x = 0.5
    r = 2.5

    # Range over the entire interval
    for a in arange(-8.0, 7.0, 0.0001):
        # The logistic equation
        x = x * r * (1 - x)
        glColor3f(0.0, 0.0, 0.0)
        glBegin(GL_POINTS)
        glVertex2f(a, x)
        glEnd()
        glFlush()

    # Print the final value
    print(x)

def keyboard(key, x, y):
    global win
    # Allows us to quit by pressing 'Esc' or 'q'
    if key == b'\x1b': #chr(27):
        glutDestroyWindow(win)
    if key == b"q":
        glutDestroyWindow(win)

def main():
    global width
    global height
    global win

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
    glutInitWindowPosition(200,200)
    glutInitWindowSize(width,height)
    win = glutCreateWindow(b"Logistic Chaos")
    glutDisplayFunc(plotlogistic)
    glutKeyboardFunc(keyboard)
    init()
    glutMainLoop()

main()
# End Program

