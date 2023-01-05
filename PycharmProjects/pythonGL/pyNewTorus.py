# pyNewTorus.py
# Credit to George K. Francis for the excellent original program
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import sys
#import psyco
#psyco.full()

# define some new trig functions here for
# later use in the program. This is NEAT STUFF!
def C(u): return cos(u*0.01745)
def S(u): return sin(u*0.01745)
global wd
global ht
global mouseX
global mouseY
global aff
global nrange
global win

nrange = 2.0
aff = [1.0, 0.0, 0.0, 0.0,
        0.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 1.0]

def drawvert(th,ta):
    # parametric sphere equations
    n0 = C(th) * C(ta)
    n1 = S(th) * C(ta)
    n2 = S(ta)
    # new color scheme!
    glColor3f(S(th), C(ta), S(th * ta))
    # torus!
    glVertex3f(C(th) + .5 * n0, S(th) + .5 * n1, .5 * n2)
    # sphere
    # glVertex3f(n0, n1, n2)

def drawtor():
    for th in range(0, 348, 15):
        glBegin(GL_TRIANGLE_STRIP)
        for ta in range(0, 348, 15):
            drawvert(th, ta);
            drawvert(th + 8, ta)
        glEnd()

#assign initial window and mouse settings
wd = 600
ht = 600
mouseX = wd/2
mouseY = ht/2
brake = 128.0

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glMultMatrixf(aff)
    drawtor()
    glutSwapBuffers()

#typical keyboard callback
def keyboard(key, x, y):
    global win

    if key == b'\x1b' or key == b'q':
        glutDestroyWindow(win)
    glutPostRedisplay()

#adjust to resizing of the window
def reshape(width, height):
    global wd
    global ht

    glClearColor(0.0, 0.0, 0.0, 0.0)
    if height == 0:
        height = 1
    wd = width
    ht = height
    glViewport(0, 0, wd, ht)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if wd <= ht:
        glOrtho(-nrange, nrange, -nrange * ht / wd, nrange * ht / wd, -nrange,nrange)
    else:
        glOrtho(-nrange * wd / ht, nrange * wd / ht, -nrange, nrange, -nrange,nrange)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

#Note that we must declare the globals again
def chaptrack():
    global mouseX
    global mouseY
    global wd
    global ht
    global aff
    dx = (mouseX - wd / 2) / brake
    dy = (mouseY - ht / 2) / brake
    glMatrixMode(GL_TEXTURE)
    glPushMatrix()
    glLoadIdentity()
    glRotatef(dx, 0, 1.0, 0.0)
    glRotatef(dy, 1.0, 0.0, 0.0)
    glMultMatrixf(aff)
    aff = glGetFloatv(GL_TEXTURE_MATRIX)
    glPopMatrix()

#traditional idle
def idle():
    chaptrack()
    glutPostRedisplay()

#ditto traditional mousemotion
def mousemotion(x,y):
    global mouseX
    global mouseY
    mouseX = x
    mouseY = y

def init():
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

#Traditional main subroutine
def main() :
    global wd
    global ht
    global win

    glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(wd, ht)
    glutInit()
    win = glutCreateWindow(b"illiTorus")
    glutKeyboardFunc(keyboard)
    glutDisplayFunc(display)
    glutIdleFunc(idle)
    glutReshapeFunc(reshape)
    glutPassiveMotionFunc(mousemotion)
    init()
    glutMainLoop()

main()
