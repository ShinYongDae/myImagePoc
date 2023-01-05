# PyFunc.py
# Plotting functions
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    #gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
    #gluOrtho2D(-3.0, 3.0, -3.0, 3.0)
    gluOrtho2D(-2.0, 2.0, -2.0, 2.0)

"""
def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(3.0)

    glBegin(GL_LINES)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)
    glEnd()

    glBegin(GL_POINTS)
    '''
    for x in arange(-5.0, 5.0, 0.1):
        #y = x*x
        #y = 2 * x ** 3 - 3 * x ** 2 + x - 5
        #y = x**2 - 2
        #y = x**3 - 3*x - 1
        #y = x**4 - 5*x**3 + x**2 - 3*x - 1
        #y = sin(x)
        #y = sin(3*x)
        #y = sin(x / 3)
        y = cos(x)

        #glBegin(GL_POINTS)
        glVertex2f(x, y)
        #glEnd()

        #glFlush()
    '''

    '''
    for x in arange(-5.0, 5.0, 0.01):
        y = x * x
        a = x + 1
        #glBegin(GL_POINTS)
        glVertex2f(x, y)
        glVertex2f(x, a)
        #glEnd()
    '''
    r = 1.0
    for x in arange(-1.0, 1.0, 0.01):
        y = sqrt(r ** 2 - x ** 2)
        #glBegin(GL_POINTS)
        glVertex2f(x, y)
        # do we need another glVertex2f statement here?
        y = -sqrt(r ** 2 - x ** 2)
        glVertex2f(x, y)
        #glEnd()

    glEnd()

    glFlush()
"""

"""
def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)

    glPointSize(1.0)
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_POINTS)
    for x in arange(-5.0, 5.0, 0.01):
        y = x*x
        y2 = x+1
        #glColor3f(0.0, 0.0, 0.0)

        #glBegin(GL_POINTS)
        glVertex2f(x,y)
        glVertex2f(x, y2)
        #glEnd()

        for a in arange(-5.0, 5.0, 0.01):
            #if a < x*x and x > 0 and a > 0:
            if a > x * x and a < x + 1 and x > 0 and a > 0:
                #glColor3f(0.50,0.50,0.50)

                #glBegin(GL_POINTS)
                glVertex2f(x,a)
                #glEnd()

    glEnd()

    glColor3f(0.0, 0.0, 0.0)

    glBegin(GL_LINES)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)
    glEnd()

    glFlush()
    # End of plotfunc block
"""
"""
def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(1.0)
    # Plot the coordinate axes
    glBegin(GL_LINES)
    glVertex2f(-2.0, 0.0)
    glVertex2f(2.0, 0.0)
    glVertex2f(0.0, 2.0)
    glVertex2f(0.0, -2.0)
    glEnd()

    a = 0.5
    b = 0.5
    c = 0.25
    d = 0.0

    glBegin(GL_POINTS)
    # Plot the parametric equations
    #for t in arange(0.0,6.28, 0.001):
    for t in arange(-6.28, 6.28, 0.001):
        #x = sin(t)
        #y = cos(t)
        #x = (c * t + d) * sin(t)
        #y = sin(a * t + b)
        x = sin(t)
        y = sin(a * t + b) + c * sin(d * t + e)
        #glBegin(GL_POINTS)
        glVertex2f(x, y)
        #glEnd()
        #glFlush()
    glEnd()

    glFlush()
    # End plotfunc()
"""
def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(1.0)

    b = 2.25
    c = 5.0

    for a in arange(0.1, 2.0, 0.1):
        #for t in arange(-200.0, 200.0, 0.005):
        for t in arange(-4.4, 4.4, 0.01):
            #x = 0.3*a*(t*t - 3)
            #y = 0.1*a*t*(t*t - 3)
            #x = sin(0.99 * t) - 0.7 * cos(3.01 * t)
            #y = cos(1.01 * t) + 0.1 * sin(15.03 * t)
            #x = a * cos(t) ** 3
            #y = a * sin(t) ** 3
            #x = a * (2.0 * cos(t) - cos(2.0 * t))
            #y = a * (2.0 * sin(t) - sin(2.0 * t))
            #x = (a + b) * cos(t) - b * cos((a / b + 1.0) * t)
            #y = (a + b) * sin(t) - b * sin((a / b + 1.0) * t)
            #x = (a + b) * cos(t) - c * cos((a / b + 1.0) * t)
            #y = (a + b) * sin(t) - c * sin((a / b + 1.0) * t)
            #x = (a - b) * cos(t) + b * cos((a / b - 1.0) * t)
            #y = (a - b) * sin(t) - b * sin((a / b - 1.0) * t)
            #x = (a - b) * cos(t) + c * cos((a / b - 1.0) * t)
            #y = (a - b) * sin(t) - c * sin((a / b - 1.0) * t)
            #x = a * (cos(t) + t * sin(t))
            #y = a * (sin(t) - t * cos(t))
            x = a * t
            y = a / (1.0 + t ** 2)

            glBegin(GL_POINTS)
            glVertex2f(x, y)
            glEnd()
            glFlush()

    # End plotfunc()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,50)
    glutInitWindowSize(400,400)
    glutCreateWindow(b"Function Plotter")
    glutDisplayFunc(plotfunc)
    init()
    glutMainLoop()

main()

# End of program