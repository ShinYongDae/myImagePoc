'''
# Super-3 Numbers
import string
i = input("Please enter the upper bound: ")
print(type(i))

for n in range(int(i)):
    x = 3*n**3
    #if string.find(str(x), "333") != -1:
    print (n, x)
# End of program3
'''

"""
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
    # background color (red, green, blue, alpha)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    #glClearColor(0.0, 0.0, 0.0, 1.0)

    # gluOrtho2D(x-left, x-right, y-bottom, y-top)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    #gluOrtho2D(-10.0, 10.0, -10.0, 10.0)

'''
def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    #glPointSize(2.0)
    glLineWidth(2.0)
    #glBegin(GL_POINTS)
    #glBegin(GL_LINES)
    #glBegin(GL_LINE_STRIP)
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.0, 0.0)
    glVertex2f(1.0, 1.0)
    glVertex2f(0.0, 1.0)
    #glVertex2f(-1.0, 1.0)
    #glVertex2f(-1.0,-1.0)
    glEnd()
    glFlush()
'''

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    # First draw x and y axes
    # Using black as a color
    glColor3f(0.0, 0.0, 0.0)

    glBegin(GL_LINES)
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0,0.0)
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, 1.0)
    glEnd()

    # Store an ordered pair in variables
    #x = 0.5
    #y = 0.5
    x = 0.25
    y = 0.75

    # Plot points in bright red
    glColor3f(1.0, 0.0, 0.0)
    # Increase the point size
    glPointSize(3.0)

    glBegin(GL_POINTS)
    # Plot the point
    glVertex2f(x, y)
    # Plot the mirror image or reflection of the point
    # in the x axis. Note the sign change!
    #glVertex2f(x, -y)
    glVertex2f(y, x)
    glEnd()

    glFlush()
    # End of plotFunc()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    #glutWireTeapot(0.5)
    #glutWireTeapot(-0.5)
    #glutWireTeapot(0.75)
    #glutWireTeapot(-0.75)
    #glutWireSphere(0.75, 25, 25)
    #glutWireSphere(0.5, 10, 10)
    #glutWireSphere(0.5, 5, 10)
    #glutWireCube(-1.0)
    #glutWireCube(0.5)
    #glutWireTetrahedron()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"My First OGL Program")
    #glutDisplayFunc(draw)
    glutDisplayFunc(plotpoints)

    init()
    glutMainLoop()

main()

# End of Program
"""


'''
def sqr(x):
    n = x*x
    return n

print (sqr(5))
'''

