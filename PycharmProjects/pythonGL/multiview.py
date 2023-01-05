## multiview.py
## Nate Robins, 1997
## shows how to use multiple viewports
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from sys import *

global win

# some object oriented stuff
class struct : pass
GBL = struct() # globals
GBL.torus_list = 0
GBL.spin_x = 0.0
GBL.spin_y = 0.0
GBL.width, GBL.height = 0, 0
GBL.old_x, GBL.old_y = 0, 0

def text(s) :
    # the next statement should be on one line!
    map(glutBitmapCharacter, (GLUT_BITMAP_HELVETICA_18,) * len(s), map(ord, s))

def lists() :
    gold_Ka = (0.24725, 0.1995, 0.0745, 1.0)
    gold_Kd = (0.75164, 0.60648, 0.22648, 1.0)
    gold_Ks = (0.628281, 0.555802, 0.366065, 1.0)
    gold_Ke = 41.2
    silver_Ka = (0.05, 0.05, 0.05, 1.0)
    silver_Kd = (0.4, 0.4, 0.4, 1.0)
    silver_Ks = (0.7, 0.7, 0.7, 1.0)
    silver_Ke = 12.0
    GBL.torus_list = glGenLists(1)
    glNewList(GBL.torus_list, GL_COMPILE)
    glMaterialfv(GL_FRONT, GL_AMBIENT, gold_Ka)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, gold_Kd)
    glMaterialfv(GL_FRONT, GL_SPECULAR, gold_Ks)
    glMaterialf(GL_FRONT, GL_SHININESS, gold_Ke)
    glMaterialfv(GL_BACK, GL_AMBIENT, silver_Ka)
    glMaterialfv(GL_BACK, GL_DIFFUSE, silver_Kd)
    glMaterialfv(GL_BACK, GL_SPECULAR, silver_Ks)
    glMaterialf(GL_BACK, GL_SHININESS, silver_Ke)
    # glutWireTorus(0.3, 0.5, 16, 32)
    glutWireTeapot(0.5)
    glEndList()

def init() :
    light_pos = (1.0, 1.0, 1.0, 0.0)
    glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glDisable(GL_CULL_FACE)

def reshape(width, height) :
    glClearColor(0.0, 0.0, 0.0, 0.0)

def projection(width, height, perspective) :
    ratio = float(width) / height
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if (perspective):
        gluPerspective(60, ratio, 1, 256)
    else:
        glOrtho(-ratio, ratio, -ratio, ratio, 1, 256)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

def bottom_left() :
    glViewport(0, 0, int(GBL.width), int(GBL.height))
    glScissor(0, 0, int(GBL.width), int(GBL.height))

def bottom_right() :
    glViewport(int(GBL.width), 0, int(GBL.width), int(GBL.height))
    glScissor(int(GBL.width), 0, int(GBL.width), int(GBL.height))

def top_left() :
    glViewport(0, int(GBL.height), int(GBL.width), int(GBL.height))
    glScissor(0, int(GBL.height), int(GBL.width), int(GBL.height))

def top_right() :
    glViewport(int(GBL.width), int(GBL.height), int(GBL.width), int(GBL.height))
    glScissor(int(GBL.width), int(GBL.height), int(GBL.width), int(GBL.height))

def front() :
    projection(GBL.width, GBL.height, 0)
    glRotatef(GBL.spin_y, 1.0, 0.0, 0.0)
    glRotatef(GBL.spin_x, 0.0, 1.0, 0.0)

def back() :
    projection(GBL.width, GBL.height, 0)
    glRotatef(180.0, 0.0, 1.0, 0.0)
    glRotatef(GBL.spin_y, 1.0, 0.0, 0.0)
    glRotatef(GBL.spin_x, 0.0, 1.0, 0.0)

def right() :
    projection(GBL.width, GBL.height, 0)
    glRotatef(90.0, 0.0, 1.0, 0.0)
    glRotatef(GBL.spin_y, 1.0, 0.0, 0.0)
    glRotatef(GBL.spin_x, 0.0, 1.0, 0.0)

def left() :
    projection(GBL.width, GBL.height, 0)
    glRotatef(-90.0, 0.0, 1.0, 0.0)
    glRotatef(GBL.spin_y, 1.0, 0.0, 0.0)
    glRotatef(GBL.spin_x, 0.0, 1.0, 0.0)

def top() :
    projection(GBL.width, GBL.height, 0)
    glRotatef(90.0, 1.0, 0.0, 0.0)
    glRotatef(GBL.spin_y, 1.0, 0.0, 0.0)
    glRotatef(GBL.spin_x, 0.0, 1.0, 0.0)

def bottom() :
    projection(GBL.width, GBL.height, 0)
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    glRotatef(GBL.spin_y, 1.0, 0.0, 0.0)
    glRotatef(GBL.spin_x, 0.0, 1.0, 0.0)

def perspective() :
    projection(GBL.width, GBL.height, 1)
    glRotatef(30.0, 0.0, 1.0, 0.0)
    glRotatef(20.0, 1.0, 0.0, 0.0)
    glRotatef(GBL.spin_y, 1.0, 0.0, 0.0)
    glRotatef(GBL.spin_x, 0.0, 1.0, 0.0)

def display() :

    GBL.width = glutGet(GLUT_WINDOW_WIDTH)
    GBL.height = glutGet(GLUT_WINDOW_HEIGHT)
    glViewport(0, 0, GBL.width, GBL.height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, GBL.width, 0, GBL.height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glDisable(GL_LIGHTING)
    glColor3ub(255, 255, 255)

    glBegin(GL_LINES)
    glVertex2i(int(GBL.width / 2), 0)
    glVertex2i(int(GBL.width / 2), GBL.height)
    glVertex2i(0, int(GBL.height / 2))
    glVertex2i(GBL.width, int(GBL.height / 2))
    glEnd()

    glRasterPos2i(5, 5)
    text(b"Front")
    glRasterPos2i(int(GBL.width / 2) + 5, 5)
    text(b"Right")
    glRasterPos2i(5, int(GBL.height / 2) + 5)
    text(b"Top")
    glRasterPos2i(int(GBL.width / 2) + 5, int(GBL.height / 2) + 5)
    text(b"Perspective")
    glEnable(GL_LIGHTING)
    GBL.width = (GBL.width + 1) / 2
    GBL.height = (GBL.height + 1) / 2
    glEnable(GL_SCISSOR_TEST)
    bottom_left()
    front()
    glCallList(GBL.torus_list)
    bottom_right()
    right()
    glCallList(GBL.torus_list)
    top_left()
    top()
    glCallList(GBL.torus_list)
    top_right()
    perspective()
    glCallList(GBL.torus_list)
    glDisable(GL_SCISSOR_TEST)
    glutSwapBuffers()

def keyboard(key, x, y) :
    global win

    if key == b'0x1b' or key == b'q' :
        glutDestroyWindow(win)
    glutPostRedisplay()

def mouse(button, state, x, y) :
    GBL.old_x = x
    GBL.old_y = y
    glutPostRedisplay()

def motion(x, y) :
    GBL.spin_x = x - GBL.old_x
    GBL.spin_y = y - GBL.old_y
    glutPostRedisplay()

def main() :
    global win
    glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(512, 512)
    glutInit()
    win = glutCreateWindow(b"Multiple Viewports")
    glutKeyboardFunc(keyboard)
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutMotionFunc(motion)
    glutMouseFunc(mouse)
    init()
    lists()
    glutMainLoop()

main()


