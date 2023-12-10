from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

start_time = 0
listfortimeprint = []
gameOver = False
dinosaur_jump = 0
goingUP = False
goingDOWN = False
movingCactus1 = 0
cactus_1 = 2000
cactus = 3000
cactus1 = 5000
speed = 1
seconds = 0
bird_x = 1500
bird_y = 4500
bird_speed = 15

def dinosaur():
    glColor3f(0.4, 0.0, 0.5)
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
    midpointCircle(2, 98, 181 + dinosaur_jump) #Midpoint Circle Algorithm Part
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

def cacTus():
    glColor3f(0.0, 0.2, 0.0)
    #cactus1
    midpoint(500 + cactus_1 - movingCactus1, 37, 525 + cactus_1 - movingCactus1, 37)
    midpoint(500 + cactus_1 - movingCactus1, 80, 500 + cactus_1 - movingCactus1, 37)
    midpoint(500 + cactus_1 - movingCactus1,200,500 + cactus_1 - movingCactus1,95)
    midpoint(525 + cactus_1 - movingCactus1, 200, 525 + cactus_1 - movingCactus1, 110)
    midpoint(525 + cactus_1 - movingCactus1,90,525 + cactus_1 - movingCactus1,37)
    midpoint(500 + cactus_1 - movingCactus1,200,505 + cactus_1 - movingCactus1,200)
    midpoint(520 + cactus_1 - movingCactus1,200,525 + cactus_1 - movingCactus1,200)
    midpoint(505 + cactus_1 - movingCactus1,205,505 + cactus_1 - movingCactus1,200)
    midpoint(505 + cactus_1 - movingCactus1,205,520 + cactus_1 - movingCactus1,205)
    midpoint(520 + cactus_1 - movingCactus1,205,520 + cactus_1 - movingCactus1,200)
    midpoint(475 + cactus_1 - movingCactus1,80,500 + cactus_1 - movingCactus1,80)
    midpoint(475 + cactus_1 - movingCactus1,85,475 + cactus_1 - movingCactus1,80)
    midpoint(470 + cactus_1 - movingCactus1,85,475 + cactus_1 - movingCactus1,85)
    midpoint(470 + cactus_1 - movingCactus1,85,470 + cactus_1 - movingCactus1,90)
    midpoint(465 + cactus_1 - movingCactus1,90,470 + cactus_1 - movingCactus1,90)
    midpoint(470 + cactus_1 - movingCactus1,90,470 + cactus_1 - movingCactus1,85)
    midpoint(465 + cactus_1 - movingCactus1,150, 465 + cactus_1 - movingCactus1,90)
    midpoint(465 + cactus_1 - movingCactus1,150,470 + cactus_1 - movingCactus1,150)
    midpoint(470 + cactus_1 - movingCactus1,155,470 + cactus_1 - movingCactus1,150)
    midpoint(470 + cactus_1 - movingCactus1,155,475 + cactus_1 - movingCactus1,155)
    midpoint(475 + cactus_1 - movingCactus1,155,475 + cactus_1 - movingCactus1,150)
    midpoint(475 + cactus_1 - movingCactus1,150,480 + cactus_1 - movingCactus1,150)
    midpoint(480 + cactus_1 - movingCactus1,150,480 + cactus_1 - movingCactus1,95)
    midpoint(480 + cactus_1 - movingCactus1,95,500 + cactus_1 - movingCactus1,95)
    midpoint(525 + cactus_1 - movingCactus1,90,560 + cactus_1 - movingCactus1,90)
    midpoint(525 + cactus_1 - movingCactus1,110,554 + cactus_1 - movingCactus1,110)
    midpoint(560 + cactus_1 - movingCactus1,97,560 + cactus_1 - movingCactus1,90)
    midpoint(560 + cactus_1 - movingCactus1,97,567 + cactus_1 - movingCactus1,97)
    midpoint(567 + cactus_1 - movingCactus1,104,567 + cactus_1 - movingCactus1,97)
    midpoint(567 + cactus_1 - movingCactus1,104,574 + cactus_1 - movingCactus1,104)
    midpoint(574 + cactus_1 - movingCactus1,165,574 + cactus_1 - movingCactus1,104)
    midpoint(567 + cactus_1 - movingCactus1,165,574 + cactus_1 - movingCactus1,165)
    midpoint(567 + cactus_1 - movingCactus1,170,567 + cactus_1 - movingCactus1,165)
    midpoint(561 + cactus_1 - movingCactus1,170,567 + cactus_1 - movingCactus1,170)
    midpoint(561 + cactus_1 - movingCactus1,170,561 + cactus_1 - movingCactus1,165)
    midpoint(554 + cactus_1 - movingCactus1,165,561 + cactus_1 - movingCactus1,165)
    midpoint(554 + cactus_1 - movingCactus1,165,554 + cactus_1 - movingCactus1,110)
    #cactus2
    midpoint(500 +cactus-movingCactus1, 37, 525 +cactus-movingCactus1, 37)
    midpoint(500 +cactus-movingCactus1, 80, 500 +cactus-movingCactus1, 37)
    midpoint(500 +cactus-movingCactus1,200,500 +cactus-movingCactus1,95)
    midpoint(525 +cactus-movingCactus1, 200, 525 +cactus-movingCactus1, 110)
    midpoint(525 +cactus-movingCactus1,90,525 +cactus-movingCactus1,37)
    midpoint(500 +cactus-movingCactus1,200,505 +cactus-movingCactus1,200)
    midpoint(520 +cactus-movingCactus1,200,525 +cactus-movingCactus1,200)
    midpoint(505 +cactus-movingCactus1,205,505 +cactus-movingCactus1,200)
    midpoint(505 +cactus-movingCactus1,205,520 +cactus-movingCactus1,205)
    midpoint(520 +cactus-movingCactus1,205,520 +cactus-movingCactus1,200)
    midpoint(475 +cactus-movingCactus1,80,500 +cactus-movingCactus1,80)
    midpoint(475 +cactus-movingCactus1,85,475 +cactus-movingCactus1,80)
    midpoint(470 +cactus-movingCactus1,85,475 +cactus-movingCactus1,85)
    midpoint(470 +cactus-movingCactus1,85,470 +cactus-movingCactus1,90)
    midpoint(465 +cactus-movingCactus1,90,470 +cactus-movingCactus1,90)
    midpoint(470 +cactus-movingCactus1,90,470 +cactus-movingCactus1,85)
    midpoint(465 +cactus-movingCactus1,150, 465 +cactus-movingCactus1,90)
    midpoint(465 +cactus-movingCactus1,150,470 +cactus-movingCactus1,150)
    midpoint(470 +cactus-movingCactus1,155,470 +cactus-movingCactus1,150)
    midpoint(470 +cactus-movingCactus1,155,475 +cactus-movingCactus1,155)
    midpoint(475 +cactus-movingCactus1,155,475 +cactus-movingCactus1,150)
    midpoint(475 +cactus-movingCactus1,150,480 +cactus-movingCactus1,150)
    midpoint(480 +cactus-movingCactus1,150,480 +cactus-movingCactus1,95)
    midpoint(480 +cactus-movingCactus1,95,500 +cactus-movingCactus1,95)
    midpoint(525 +cactus-movingCactus1,90,560 +cactus-movingCactus1,90)
    midpoint(525 +cactus-movingCactus1,110,554 +cactus-movingCactus1,110)
    midpoint(560 +cactus-movingCactus1,97,560 +cactus-movingCactus1,90)
    midpoint(560 +cactus-movingCactus1,97,567 +cactus-movingCactus1,97)
    midpoint(567 +cactus-movingCactus1,104,567 +cactus-movingCactus1,97)
    midpoint(567 +cactus-movingCactus1,104,574 +cactus-movingCactus1,104)
    midpoint(574 +cactus-movingCactus1,165,574 +cactus-movingCactus1,104)
    midpoint(567 +cactus-movingCactus1,165,574 +cactus-movingCactus1,165)
    midpoint(567 +cactus-movingCactus1,170,567 +cactus-movingCactus1,165)
    midpoint(561 +cactus-movingCactus1,170,567 +cactus-movingCactus1,170)
    midpoint(561 +cactus-movingCactus1,170,561 +cactus-movingCactus1,165)
    midpoint(554 +cactus-movingCactus1,165,561 +cactus-movingCactus1,165)
    midpoint(554 +cactus-movingCactus1,165,554 +cactus-movingCactus1,110)
    #cactus_3
    midpoint(500 +cactus1 - movingCactus1, 37, 525 +cactus1 - movingCactus1, 37)
    midpoint(500 +cactus1 - movingCactus1, 80, 500 +cactus1 - movingCactus1, 37)
    midpoint(500 +cactus1 - movingCactus1,200,500 +cactus1 - movingCactus1,95)
    midpoint(525 +cactus1 - movingCactus1, 200, 525 +cactus1 - movingCactus1, 110)
    midpoint(525 +cactus1 - movingCactus1,90,525 +cactus1 - movingCactus1,37)
    midpoint(500 +cactus1 - movingCactus1,200,505 +cactus1 - movingCactus1,200)
    midpoint(520 +cactus1 - movingCactus1,200,525 +cactus1 - movingCactus1,200)
    midpoint(505 +cactus1 - movingCactus1,205,505 +cactus1 - movingCactus1,200)
    midpoint(505 +cactus1 - movingCactus1,205,520 +cactus1 - movingCactus1,205)
    midpoint(520 +cactus1 - movingCactus1,205,520 +cactus1 - movingCactus1,200)
    midpoint(475 +cactus1 - movingCactus1,80,500 +cactus1 - movingCactus1,80)
    midpoint(475 +cactus1 - movingCactus1,85,475 +cactus1 - movingCactus1,80)
    midpoint(470 +cactus1 - movingCactus1,85,475 +cactus1 - movingCactus1,85)
    midpoint(470 +cactus1 - movingCactus1,85,470 +cactus1 - movingCactus1,90)
    midpoint(465 +cactus1 - movingCactus1,90,470 +cactus1 - movingCactus1,90)
    midpoint(470 +cactus1 - movingCactus1,90,470 +cactus1 - movingCactus1,85)
    midpoint(465 +cactus1 - movingCactus1,150, 465 +cactus1 - movingCactus1,90)
    midpoint(465 +cactus1 - movingCactus1,150,470 +cactus1 - movingCactus1,150)
    midpoint(470 +cactus1 - movingCactus1,155,470 +cactus1 - movingCactus1,150)
    midpoint(470 +cactus1 - movingCactus1,155,475 +cactus1 - movingCactus1,155)
    midpoint(475 +cactus1 - movingCactus1,155,475 +cactus1 - movingCactus1,150)
    midpoint(475 +cactus1 - movingCactus1,150,480 +cactus1 - movingCactus1,150)
    midpoint(480 +cactus1 - movingCactus1,150,480 +cactus1 - movingCactus1,95)
    midpoint(480 +cactus1 - movingCactus1,95,500 +cactus1 - movingCactus1,95)
    midpoint(525 +cactus1 - movingCactus1,90,560 +cactus1 - movingCactus1,90)
    midpoint(525 +cactus1 - movingCactus1,110,554 +cactus1 - movingCactus1,110)
    midpoint(560 +cactus1 - movingCactus1,97,560 +cactus1 - movingCactus1,90)
    midpoint(560 +cactus1 - movingCactus1,97,567 +cactus1 - movingCactus1,97)
    midpoint(567 +cactus1 - movingCactus1,104,567 +cactus1 - movingCactus1,97)
    midpoint(567 +cactus1 - movingCactus1,104,574 +cactus1 - movingCactus1,104)
    midpoint(574 +cactus1 - movingCactus1,165,574 +cactus1 - movingCactus1,104)
    midpoint(567 +cactus1 - movingCactus1,165,574 +cactus1 - movingCactus1,165)
    midpoint(567 +cactus1 - movingCactus1,170,567 +cactus1 - movingCactus1,165)
    midpoint(561 +cactus1 - movingCactus1,170,567 +cactus1 - movingCactus1,170)
    midpoint(561 +cactus1 - movingCactus1,170,561 +cactus1 - movingCactus1,165)
    midpoint(554 +cactus1 - movingCactus1,165,561 +cactus1 - movingCactus1,165)
    midpoint(554 +cactus1 - movingCactus1,165,554 +cactus1 - movingCactus1,110)
       
def bird():
    global bird_x, bird_y
    glColor3f(0.5, 0.5, 0.0)
    #bird1
    midpoint(179 + bird_x, 176, 185 + bird_x, 179)
    midpoint(185 + bird_x, 179, 197 + bird_x, 184)
    midpoint(197 + bird_x, 184, 201 + bird_x, 173)
    midpoint(201 + bird_x, 173, 207 + bird_x, 169)
    midpoint(207 + bird_x, 169, 210 + bird_x, 166)
    midpoint(210 + bird_x, 166, 213 + bird_x, 158)
    midpoint(213 + bird_x, 158, 218 + bird_x, 159)
    midpoint(218 + bird_x, 159, 214 + bird_x, 166)
    midpoint(214 + bird_x, 166, 230 + bird_x, 187)
    midpoint(230 + bird_x, 187, 256 + bird_x, 200)
    midpoint(256 + bird_x, 200, 235 + bird_x, 201)
    midpoint(235 + bird_x, 201, 224 + bird_x, 199)
    midpoint(224 + bird_x, 199, 216 + bird_x, 193)
    midpoint(216 + bird_x, 193, 212 + bird_x, 200)
    midpoint(212 + bird_x, 200, 205 + bird_x, 205)
    midpoint(205 + bird_x, 205, 191 + bird_x, 207)
    midpoint(191 + bird_x, 207, 197 + bird_x, 200)
    midpoint(197 + bird_x, 200, 200 + bird_x, 193)
    midpoint(200 + bird_x, 193, 185 + bird_x, 184)
    midpoint(185 + bird_x, 184, 180 + bird_x, 180)
    midpoint(180 + bird_x, 180, 179 + bird_x, 176)
    midpoint(216 + bird_x, 193, 205 + bird_x, 180)
    midpoint(205 + bird_x, 180, 204 + bird_x, 191)
    midpoint(204 + bird_x, 191, 207 + bird_x, 195)
    midpoint(207 + bird_x, 195, 200 + bird_x, 193)
    midpoint(197 + bird_x, 186, 179 + bird_x, 176)
    #Bird2
    midpoint(179 + bird_y, 176, 185 + bird_y, 179)
    midpoint(185 + bird_y, 179, 197 + bird_y, 184)
    midpoint(197 + bird_y, 184, 201 + bird_y, 173)
    midpoint(201 + bird_y, 173, 207 + bird_y, 169)
    midpoint(207 + bird_y, 169, 210 + bird_y, 166)
    midpoint(210 + bird_y, 166, 213 + bird_y, 158)
    midpoint(213 + bird_y, 158, 218 + bird_y, 159)
    midpoint(218 + bird_y, 159, 214 + bird_y, 166)
    midpoint(214 + bird_y, 166, 230 + bird_y, 187)
    midpoint(230 + bird_y, 187, 256 + bird_y, 200)
    midpoint(256 + bird_y, 200, 235 + bird_y, 201)
    midpoint(235 + bird_y, 201, 224 + bird_y, 199)
    midpoint(224 + bird_y, 199, 216 + bird_y, 193)
    midpoint(216 + bird_y, 193, 212 + bird_y, 200)
    midpoint(212 + bird_y, 200, 205 + bird_y, 205)
    midpoint(205 + bird_y, 205, 191 + bird_y, 207)
    midpoint(191 + bird_y, 207, 197 + bird_y, 200)
    midpoint(197 + bird_y, 200, 200 + bird_y, 193)
    midpoint(200 + bird_y, 193, 185 + bird_y, 184)
    midpoint(185 + bird_y, 184, 180 + bird_y, 180)
    midpoint(180 + bird_y, 180, 179 + bird_y, 176)
    midpoint(216 + bird_y, 193, 205 + bird_y, 180)
    midpoint(205 + bird_y, 180, 204 + bird_y, 191)
    midpoint(204 + bird_y, 191, 207 + bird_y, 195)
    midpoint(207 + bird_y, 195, 200 + bird_y, 193)
    midpoint(197 + bird_y, 186, 179 + bird_y, 176)

def land():
    glColor3f(0.2, 0.1, 0.0)
    midpoint(0, 35, 10000, 35)

def cross():
    glColor3f(1.0, 0.0, 0.0)
    midpoint(920, 680, 970, 650)
    midpoint(920, 650, 970, 680)

def arrowLeft():
    glColor3f(0.0, 1.0, 1.0)
    midpoint(20, 660, 70, 660)
    midpoint(20, 660, 40, 680)
    midpoint(20, 660, 40, 640)

def draw_points(x0, y0):
    glPointSize(3)
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

def circlePoints(x, y, x0, y0):
    draw_points_circle(x + x0, y + y0)
    draw_points_circle(y + x0, x + y0)
    draw_points_circle(y + x0, -x + y0)
    draw_points_circle(x + x0, -y + y0)
    draw_points_circle(-x + x0, -y + y0)
    draw_points_circle(-y + x0, -x + y0)
    draw_points_circle(-y + x0, x + y0)
    draw_points_circle(-x + x0, y + y0)

def midpointCircle(radius, x0, y0):
    d = 1 - radius 
    x = 0
    y = radius
    circlePoints(x, y, x0, y0)
    while x < y:
        if d < 0:
            d = d + 2*x + 3
            x += 1
        else:
            d = d + 2*x -2*y + 5
            x += 1
            y = y - 1
        circlePoints(x, y, x0, y0)
 
def draw_points_circle(x, y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
   
def mouseListener(button, state, x, y):
    global dinosaur_jump, start_time, movingCactus1, cactus_1, cactus, cactus1, speed, seconds, bird_x, bird_y, gameOver, goingUP, goingDOWN
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):
            if 736 <= x <= 774 and 15 <= y <= 40:
                glutLeaveMainLoop()
            if 15 <= x <= 60 and 10 <= y <= 40:
                print("Restarted!")
                start_time = 0
                dinosaur_jump = 0
                movingCactus1 = 0
                cactus_1 = 2000
                cactus = 3000
                cactus1 = 5000
                speed = 1
                seconds = 0
                bird_x = 1500
                bird_y = 4500
                gameOver = False
                goingUP = False
                goingDOWN = False

                

def keyboardListener(key, x, y):
    global dinosaur_jump, goingUP, goingDOWN
    if key==b' ':
        if goingDOWN != True:
            goingUP = True
    glutPostRedisplay()
                
def animate():
    global dinosaur_jump, goingUP, goingDOWN, movingCactus1, seconds, bird_x, bird_y, gameOver, start_time, listfortimeprint
    glutPostRedisplay()
    if gameOver == False:
        if goingUP == True and goingDOWN == False:
            dinosaur_jump += 30
            if dinosaur_jump >= 300:
                goingUP = False
                goingDOWN = True
        if goingDOWN == True and goingUP == False: 
            dinosaur_jump -= 10
            if dinosaur_jump < 0:
                goingDOWN = False
                goingUP = False
                dinosaur_jump = 0
        #cactusMove
        if (574 +cactus1 - movingCactus1) < 0:
            movingCactus1 = 0 
            bird_x = 1500
            bird_y = 4000
        else:
            movingCactus1 += 15
        #birdMove
        bird_x -= bird_speed
        bird_y -= bird_speed
        #clashwithCactus1
        if (35+dinosaur_jump) < 155 and 130 >= (465 + cactus_1 - movingCactus1) and 15 <= (500 + cactus_1 - movingCactus1):
            gameOver = True
        elif (35+dinosaur_jump) < 200 and 130 >= (500 + cactus_1 - movingCactus1) and 15 <= (525 + cactus_1 - movingCactus1):
            gameOver = True
        #clashwithCactus2
        elif (35+dinosaur_jump) < 155 and 130 >= (465 +cactus-movingCactus1) and 15 <= (500 +cactus-movingCactus1):
            gameOver = True
        elif (35+dinosaur_jump) < 200 and 130 >= (500 +cactus-movingCactus1) and 15 <= (525 +cactus-movingCactus1):
            gameOver = True
        #clashwithCactus3
        elif (35+dinosaur_jump) < 155 and 130 >= (465 +cactus1 - movingCactus1) and 15 <= (500 +cactus1 - movingCactus1):
            gameOver = True
        elif (35+dinosaur_jump) < 200 and 130 >= (500 +cactus1 - movingCactus1) and 15 <= (525 +cactus1 - movingCactus1):
            gameOver = True
        #clashwithBird1
        elif (35+dinosaur_jump) < 207 and 130 >= (179 + bird_x) and 55 <= (256 + bird_x):
            gameOver = True
        #clashwithBird2
        elif (35+dinosaur_jump) < 207 and 130 >= (179 + bird_y) and 55 <= (256 + bird_y):
            gameOver = True
        else: 
            pass
        start_time += 0.04
        if int(start_time) not in listfortimeprint:
            listfortimeprint.append(int(start_time))
            print(f"Score: {int(start_time)}")
            if len(listfortimeprint) > 3:
                listfortimeprint.pop(0)  
        if gameOver:
            print("Game Over!")

def iterate():
    glViewport(0, 0, 800, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 700, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.9, 0.9, 0.95, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    animate()
    cross()
    arrowLeft()
    dinosaur()
    land()
    cacTus()
    bird()
    glutSwapBuffers()
    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Jurassic Jump")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouseListener)
glutMainLoop()