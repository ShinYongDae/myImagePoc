# PyPolar.py
# Plotting Polar Equations

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys

# Set the width and height of the window with global variables
# Set the axis range globally using global variable axrng
global width
global height
global axrng
global win


# Initial values
width = 400
height = 400
axrng = 7.0

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)

# GLUT Display Function
def plotpolar():
    glClear(GL_COLOR_BUFFER_BIT)
    # Plot axis lines for reference
    glColor3f(0.0, 0.0, 0.0)

    glBegin(GL_LINES)
    glVertex2f(-axrng, 0)
    glVertex2f(axrng, 0)
    glVertex2f(0, axrng)
    glVertex2f(0, -axrng)
    glEnd()

    # Plot polar equation for a Limacon
    glPointSize(2.0)
    glBegin(GL_POINTS)
    for theta in arange(0.0, 6.28, 0.001):
        r = 4 * cos(theta) + 2
        x = r * cos(theta)
        y = r * sin(theta)
        #glBegin(GL_POINTS)
        glVertex2f(x, y)
        #glEnd()
        #glFlush()
    glEnd()
    glFlush() # glutSwapBuffers()

# This is new... this is a reshape function so that the
# aspect ratio of the graphics window will be preserved
# and anything we draw will look in proper proportion
def reshape(w, h):
    # To insure we don't have a zero window height
    if h == 0:
        h = 1

    # Fill the entire graphics window!
    glViewport(0, 0, w, h)

    # Set the projection matrix... our "view"
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Set the aspect ratio of the plot so that it
    # Always looks "OK" and never distorted.

    if w <= h:
        gluOrtho2D(-axrng, axrng, -axrng * h / w, axrng * h / w)
    else:
        gluOrtho2D(-axrng * w / h, axrng * w / h, -axrng, axrng)

    # Set the matrix for the object we are drawing
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def keyboard(key, x, y):
    global win
    # Allows us to quit by pressing 'Esc' or 'q'
    if key == b'\x1b': # ESC(27), Enter(13), Special(224)[ArrowDown(80), ArrowUp(72)]
        glutDestroyWindow(win)
        #sys.exit()
    if key == b'q':
        glutDestroyWindow(win)
        #sys.exit()
    '''
    if key == chr(27): # 'Esc'
        sys.exit()
    if key == "q":
        sys.exit()
    '''

def main():
    global width
    global height
    global win
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE) # GLUT_DOUBLE
    glutInitWindowPosition(10, 10)
    glutInitWindowSize(width, height)
    win = glutCreateWindow(b"Polar Equations")
    glutReshapeFunc(reshape)
    glutDisplayFunc(plotpolar)
    glutKeyboardFunc(keyboard)
    #glutIdleFunc(RenderScene)
    #glutSpecialFunc(ProcessSpecialKeys)

    init()
    glutMainLoop()

main()
# End Program
