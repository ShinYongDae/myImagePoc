# Midpt.py... Stan Blank
# An exploration into geometry
# January 2005
# import important GL stuff
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
# Might need some math stuff
from math import *
from random import *
import sys
#define some globals
global vv
global aff
global wd
global ht
global MouseX
global MouseY
global flag
global count
global n
global win

# for zooming in and out
global zoom
zoom = 0.0

# Vertices
n = 500

# define the vertex point array
vv = []

#define the affine identity matrix
aff = (1.0,0.0,0.0,0.0,
        0.0,1.0,0.0,0.0,
        0.0,0.0,1.0,0.0,
        0.0,0.0,0.0,1.0)

#initial window and mouse settings
wd = 1000
ht = 1000
MouseX = wd/2
MouseY = ht/2

def calcit():
        # DO need these... first global assignment
        global vv
        global count
        global flag
        global n
        flag = -1
        count = 0
        # Assign n random vertices within
        # a -2 to 2 box on in all 3 axes
        while count < n:
                x = 4 * random() - 2
                y = 4 * random() - 2
                z = 4 * random() - 2
                # Store the x,y,z coordinates in the array
                vv = vv + [[x, y, z]]
                # Keep track of how many vertices there are
                count = count + 1

#The usual display routine
def display():
        # don't need these IF already assigned
        # values as globals... weird
        # global vv
        # global count
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        glTranslatef(0.0, 0.0, zoom)
        # Prep for the rotations
        glMultMatrixf(aff)
        # try glTranslatef here and see what happens
        # glTranslatef(0.0,0.0, zoom)
        glLineWidth(2.0)
        # Draw the 3D polygon from the stored values
        glBegin(GL_LINE_STRIP)
        for n in range(0, count):
                # glColor3f(random(),random(),random())
                glVertex3fv(vv[n])
        glVertex3fv(vv[0])
        glEnd()
        glPopMatrix()
        glFlush()
        glutSwapBuffers()

def midpt():
        # global count
        # global vv
        # Calculate the midpoint of each segment
        # An store this new vertex back in the
        # Original array... this was not easy
        # To figure out!
        x0 = vv[0][0]
        y0 = vv[0][1]
        z0 = vv[0][2]
        for n in range(0, count - 1):
                # the next two lines belong on ONE line
                vv[n] = [((vv[n][0] + vv[n + 1][0]) / 2), ((vv[n][1] + vv[n+1][1])/2),((vv[n][2] + vv[n+1][2])/2)]
        # the next two lines belong on ONE line
        vv[count - 1] = [((vv[count - 1][0] + x0) / 2), ((vv[count - 1][1]+y0)/2),((vv[count-1][2]+z0)/2)]
        glutPostRedisplay()

#keyboard stuff
def keyboard(key, x, y):
        global flag, win
        if key == b'\x1b' or key == b'q':
                glutDestroyWindow(win)
        # This starts and stops the animation
        if key == "a":
                flag = -1 * flag
                midpt()
        glutPostRedisplay()

# if we change the screen dimensions
# Everything still looks normal
def reshape(width, height):
        global wd
        global ht
        global zoom
        glClearColor(0.0, 0.0, 0.0, 0.0)
        if height == 0:
                height = 1
        wd = width
        ht = height
        glViewport(0, 0, wd, ht)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # Since we are rotating and moving about
        # A perspective view is much nicer!
        gluPerspective(45., 1., .1, 400.)
        # Look this up to see what it means!
        gluLookAt(0, 0, 5.0,
                  0, 0, 0,
                  0, 1, 0)
        # if wd<=ht:
        # glOrtho(-2.0,2.0,-2.0*ht/wd,2.0*ht/wd,-2.0,2.0)
        # else:
        # glOrtho(-2.0*wd/ht,2.0*wd/ht,-2.0,2.0,-2.0,2.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

#does nothing at this point
def motion(x,y):
        # print x,y
        return 0

def chaptrack():
        global MouseX
        global MouseY
        global wd
        global ht
        global aff
        dx = (MouseX - (wd / 2)) / 164
        dy = (MouseY - (ht / 2)) / 164
        glMatrixMode(GL_TEXTURE)
        glPushMatrix()
        glLoadIdentity()
        glRotatef(dx, 0, 1.0, 0.0)
        glRotatef(dy, 1.0, 0.0, 0.0)
        glMultMatrixf(aff)
        # this line is different from the C
        # version. Python handles it a bit
        # differently... was a pain to figure out!
        aff = glGetFloatv(GL_TEXTURE_MATRIX)
        glPopMatrix()

def idle():
        chaptrack()
        glutPostRedisplay()
        # Whether or not to keep on calculating
        if flag == 1:
                midpt()

def mousemotion(x,y):
        global MouseX
        global MouseY
        MouseX = x
        MouseY = y

def arrowkeys(key, x, y):
        global zoom
        # Zoom in and out
        if key == GLUT_KEY_UP:
                zoom = zoom + .1
        if key == GLUT_KEY_DOWN:
                zoom = zoom - .1
        # Reset back to the original distance
        if key == GLUT_KEY_HOME:
                zoom = 5.0
        glutPostRedisplay()

#Traditional main subroutine
def main() :
        global wd
        global ht
        global win

        glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE)
        glutInitWindowPosition(50, 50)
        glutInitWindowSize(wd, ht)
        glutInit(sys.argv)
        win = glutCreateWindow(b"Mid-Point Exploration")
        glutKeyboardFunc(keyboard)
        glutReshapeFunc(reshape)
        glutDisplayFunc(display)
        glutMotionFunc(motion)
        glutSpecialFunc(arrowkeys)
        ##glutMouseFunc(mouse)
        glutIdleFunc(idle)
        glutPassiveMotionFunc(mousemotion)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # glOrtho(-2.0,2.0,-2.0,2.0,-2.0,2.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        # Could add additional function calls
        calcit()
        ##lists()
        glutMainLoop()

main()

