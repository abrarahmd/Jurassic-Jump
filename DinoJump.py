from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

dinosaur_jump = 0
goingUP = False
goingDOWN = False

def dinosaur():
    glColor3f(0, 0, 0)
    #head
    midpoint(90, 200 + dinosaur_jump, 105, 200 + dinosaur_jump)
    midpoint(90, 200 + dinosaur_jump, 90, 195 + dinosaur_jump)
    midpoint(85, 195 + dinosaur_jump, 90, 195 + dinosaur_jump)
    midpoint(85, 195 + dinosaur_jump, 85, 190 + dinosaur_jump)
    midpoint(80, 190 + dinosaur_jump, 85, 190 + dinosaur_jump)
    midpoint(80, 190 + dinosaur_jump, 80, 110 + dinosaur_jump)
    midpoint(105, 200 + dinosaur_jump, 105, 195 + dinosaur_jump)
    midpoint(105, 195 + dinosaur_jump, 112, 195 + dinosaur_jump)
    midpoint(112, 195 + dinosaur_jump, 112, 190 + dinosaur_jump)
    midpoint(112, 190 + dinosaur_jump, 117, 190 + dinosaur_jump)
    midpoint(117, 190 + dinosaur_jump, 117, 185 + dinosaur_jump)
    midpoint(117, 185 + dinosaur_jump, 125, 185 + dinosaur_jump)
    midpoint(125, 185 + dinosaur_jump, 125, 180 + dinosaur_jump)
    midpoint(125, 180 + dinosaur_jump, 130, 180 + dinosaur_jump)
    midpoint(130, 180 + dinosaur_jump, 130, 160 + dinosaur_jump)
    midpoint(125, 160 + dinosaur_jump, 130, 160 + dinosaur_jump)
    midpoint(125, 160 + dinosaur_jump, 125, 155 + dinosaur_jump)
    midpoint(105, 155 + dinosaur_jump, 125, 155 + dinosaur_jump)
    #eye
    midpoint(95, 185 + dinosaur_jump, 102, 185 + dinosaur_jump)
    midpoint(102, 185 + dinosaur_jump, 102, 178 + dinosaur_jump)
    midpoint(95, 178 + dinosaur_jump, 102, 178 + dinosaur_jump)
    midpoint(95, 185 + dinosaur_jump, 95, 178 + dinosaur_jump)
    #body
    midpoint(105, 155 + dinosaur_jump, 105, 115 + dinosaur_jump)
    midpoint(105, 115 + dinosaur_jump, 110, 115 + dinosaur_jump)
    midpoint(110, 115 + dinosaur_jump, 110, 110 + dinosaur_jump)
    midpoint(110, 110 + dinosaur_jump, 115, 110 + dinosaur_jump)
    midpoint(115, 110 + dinosaur_jump, 115, 70 + dinosaur_jump)
    midpoint(110, 70 + dinosaur_jump, 115, 70 + dinosaur_jump)
    midpoint(110, 70 + dinosaur_jump, 110, 65 + dinosaur_jump)
    midpoint(102, 65 + dinosaur_jump, 110, 65 + dinosaur_jump)
    midpoint(102, 65 + dinosaur_jump, 102, 60 + dinosaur_jump)
    midpoint(47, 60 + dinosaur_jump, 90, 60 + dinosaur_jump)
    midpoint(50, 110 + dinosaur_jump, 80, 110 + dinosaur_jump)
    midpoint(50, 110 + dinosaur_jump, 50, 105 + dinosaur_jump)
    midpoint(45, 105 + dinosaur_jump, 50, 105 + dinosaur_jump)
    midpoint(45, 105 + dinosaur_jump, 45, 100 + dinosaur_jump)
    midpoint(40, 100 + dinosaur_jump, 45, 100 + dinosaur_jump)
    midpoint(40, 100 + dinosaur_jump, 40, 95 + dinosaur_jump)
    midpoint(35, 95 + dinosaur_jump, 40, 95 + dinosaur_jump)
    midpoint(35, 95 + dinosaur_jump, 35, 90 + dinosaur_jump)
    #tail
    midpoint(15, 90 + dinosaur_jump, 35, 90 + dinosaur_jump)
    midpoint(15, 90 + dinosaur_jump, 15, 85 + dinosaur_jump)
    midpoint(15, 85 + dinosaur_jump, 20, 85 + dinosaur_jump)
    midpoint(20, 85 + dinosaur_jump, 20, 80 + dinosaur_jump)
    midpoint(20, 80 + dinosaur_jump, 25, 80 + dinosaur_jump)
    midpoint(25, 80 + dinosaur_jump, 25, 75 + dinosaur_jump)
    midpoint(25, 75 + dinosaur_jump, 35, 75 + dinosaur_jump)
    midpoint(35, 75 + dinosaur_jump, 35, 60 + dinosaur_jump)
    midpoint(47, 60 + dinosaur_jump, 50, 60 + dinosaur_jump)
    #leg front 1
    midpoint(110, 65 + dinosaur_jump, 110, 55 + dinosaur_jump)
    midpoint(110, 55 + dinosaur_jump, 120, 55 + dinosaur_jump)
    midpoint(120, 55 + dinosaur_jump, 120, 45 + dinosaur_jump)
    midpoint(102, 45 + dinosaur_jump, 120, 45 + dinosaur_jump)
    midpoint(102, 60 + dinosaur_jump, 102, 45 + dinosaur_jump)
    #leg front 2 (big one)
    midpoint(102, 60 + dinosaur_jump, 102, 45 + dinosaur_jump)
    midpoint(102, 45 + dinosaur_jump, 110, 45 + dinosaur_jump)
    midpoint(110, 45 + dinosaur_jump, 110, 35 + dinosaur_jump)
    midpoint(90, 35 + dinosaur_jump, 110, 35 + dinosaur_jump)
    midpoint(90, 60 + dinosaur_jump, 90, 35 + dinosaur_jump)
    #leg back 1 (big one)
    midpoint(35, 60 + dinosaur_jump, 35, 35 + dinosaur_jump)
    midpoint(35, 35 + dinosaur_jump, 55, 35 + dinosaur_jump)
    midpoint(55, 45 + dinosaur_jump, 55, 35 + dinosaur_jump)
    midpoint(47, 45 + dinosaur_jump, 55, 45 + dinosaur_jump)
    midpoint(47, 60 + dinosaur_jump, 47, 45 + dinosaur_jump)
    #leg back 2
    midpoint(47, 60 + dinosaur_jump, 47, 45 + dinosaur_jump)
    midpoint(47, 45 + dinosaur_jump, 65, 45 + dinosaur_jump)
    midpoint(65, 55 + dinosaur_jump, 65, 45 + dinosaur_jump)
    midpoint(55, 55 + dinosaur_jump, 65, 55 + dinosaur_jump)
    midpoint(55, 55 + dinosaur_jump, 65, 55 + dinosaur_jump)
    midpoint(55, 60 + dinosaur_jump, 55, 55 + dinosaur_jump)

def cactus():
    glColor3f(0, 0, 0)

    midpoint(500, 37, 525, 37)
    midpoint(500, 80, 500, 37)
    midpoint(500,200,500,95)
    midpoint(525, 200, 525, 110)
    midpoint(525,90,525,37)
    midpoint(500,200,505,200)
    midpoint(520,200,525,200)
    midpoint(505,205,505,200)
    midpoint(505,205,520,205)
    midpoint(520,205,520,200)

    midpoint(475,80,500,80)
    midpoint(475,85,475,80)
    midpoint(470,85,475,85)
    midpoint(470,85,470,90)
    midpoint(465,90,470,90)
    midpoint(470,90,470,85)
    midpoint(465,150, 465,90)
    midpoint(465,150,470,150)
    midpoint(470,155,470,150)
    midpoint(470,155,475,155)
    midpoint(475,155,475,150)
    midpoint(475,150,480,150)
    midpoint(480,150,480,95)
    midpoint(480,95,500,95)

    midpoint(525,90,560,90)
    midpoint(525,110,554,110)
    midpoint(560,97,560,90)
    midpoint(560,97,567,97)
    midpoint(567,104,567,97)
    midpoint(567,104,574,104)
    midpoint(574,165,574,104)
    midpoint(567,165,574,165)
    midpoint(567,170,567,165)
    midpoint(561,170,567,170)
    midpoint(561,170,561,165)
    midpoint(554,165,561,165)
    midpoint(554,165,554,110)


def bird():
    glColor3f(0, 0, 0)
    midpoint(179, 176, 185, 179)
    midpoint(185, 179, 197, 184)
    midpoint(197, 184, 201, 173)
    midpoint(201, 173, 207, 169)
    midpoint(207, 169, 210, 166)
    midpoint(210, 166, 213, 158)
    midpoint(213, 158, 218, 159)
    midpoint(218, 159, 214, 166)
    midpoint(214, 166, 230, 187)
    midpoint(230, 187, 256, 200)
    midpoint(256, 200, 235, 201)
    midpoint(235, 201, 224, 199)
    midpoint(224, 199, 216, 193)
    midpoint(216, 193, 212, 200)
    midpoint(212, 200, 205, 205)
    midpoint(205, 205, 191, 207)
    midpoint(191, 207, 197, 200)
    midpoint(197, 200, 200, 193)
    midpoint(200, 193, 185, 184)
    midpoint(185, 184, 180, 180)
    midpoint(180, 180, 179, 176)
    midpoint(216, 193, 205, 180)
    midpoint(205, 180, 204, 191)
    midpoint(204, 191, 207, 195)
    midpoint(207, 195, 200, 193)
    midpoint(197, 186, 179, 176)

def land():
    midpoint(0, 35, 10000, 35)


def keyboardListener(key, x, y):
    global dinosaur_jump, goingUP, goingDOWN
    if key==b' ':
        if goingDOWN != True:
            goingUP = True
    glutPostRedisplay()

def draw_points(x0, y0):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x0,y0)
    glEnd()

def midpoint(x0, y0, x1, y1):
    zone = findZone(x0, y0, x1, y1)
    x0, y0 = zoneConvert0(zone, x0, y0)
    x1, y1 = zoneConvert0(zone, x1, y1)
    dx = x1 - x0
    dy = y1 - y0
    dinit = 2 * dy - dx
    dne = 2 * dy - 2 * dx
    de = 2 * dy
    for i in range(x0, x1):
        a, b = convert0_Original(zone, x0, y0)
        if dinit >= 0:
            dinit = dinit + dne
            draw_points(a, b)
            x0 += 1
            y0 += 1
        else:
            dinit = dinit + de
            draw_points(a, b)
            x0 += 1

def findZone(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    if abs(dx) > abs(dy): #For Zone 0, 3, 4 & 7
        if dx > 0 and dy > 0:
            return 0
        elif dx < 0 and dy > 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        else:
            return 7
    else: #For zone 1, 2, 5 & 6
        if dx > 0 and dy > 0:
            return 1
        elif dx < 0 and dy > 0:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        else:
            return 6

def zoneConvert0(zone, x0, y0):
    if zone == 0:
        return x0, y0
    elif zone == 1:
        return y0, x0
    elif zone == 2:
        return -y0, x0
    elif zone == 3:
        return -x0, y0
    elif zone == 4:
        return -x0, -y0
    elif zone == 5:
        return -y0, -x0
    elif zone == 6:
        return -y0, x0
    elif zone == 7:
        return x0, -y0
   
def convert0_Original(zone, x0, y0):
    if zone == 0:
        return x0, y0
    if zone == 1:
        return y0, x0
    if zone == 2:
        return -y0, -x0
    if zone == 3:
        return -x0, y0
    if zone == 4:
        return -x0, -y0
    if zone == 5:
        return -y0, -x0
    if zone == 6:
        return y0, -x0
    if zone == 7:
        return x0, -y0
   
def specialKeyListener(key, left, right):
    glutPostRedisplay()
    pass
    glutPostRedisplay()

def mouseListener(button, state, x, y):
    global ballx, bally, create_new, pauseBoolean, gameOver, score
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):
            pass

def animate():
    global dinosaur_jump, goingUP, goingDOWN
    glutPostRedisplay()
    if goingUP == True and goingDOWN == False:
        dinosaur_jump += 15
        if dinosaur_jump >= 250:
            goingUP = False
            goingDOWN = True
    if goingDOWN == True and goingUP == False: 
        dinosaur_jump -= 15
        if dinosaur_jump < 0:
            goingDOWN = False
            goingUP = False
            dinosaur_jump = 0


def iterate():
    glViewport(0, 0, 800, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.9, 0.9, 0.95, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    animate()
    dinosaur()
    land()
    cactus()
    bird()

    glutSwapBuffers()
    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Jurassic Jump") #window name
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutKeyboardFunc(keyboardListener)
glutMainLoop()