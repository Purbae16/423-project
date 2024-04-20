from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Line:
    def drawPoint(self, x, y):
        glPointSize(1.5)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()
        glFlush()

    def findZone(self, x0, y0, x1, y1):
        dx = x1 - x0
        dy = y1 - y0
        if abs(dx) >= abs(dy):
            if dx >= 0:
                if dy >= 0:
                    return 0
                else:
                    return 7
            elif dx <= 0:
                if dy >= 0:
                    return 3
                else:
                    return 4
        else:
            if dy >= 0:
                if dx >= 0:
                    return 1
                else:
                    return 6
            elif dy <= 0 :
                if dx >= 0:
                    return 2
                else:
                    return 5

    def convertToZone0(self, x, y, zone):
        if zone == 0:
            return x, y
        elif zone == 1:
            return y, x
        elif zone == 2:
            return -y, x
        elif zone == 3:
            return -x, y
        elif zone == 4:
            return -x, -y
        elif zone == 5:
            return -y, -x
        elif zone == 6:
            return y, -x
        elif zone == 7:
            return x, -y
        
    def plotPoint(self, x, y, zone):
        if zone == 0:
            Line.drawPoint(self, x, y)
        elif zone == 1:
            Line.drawPoint(self, y, x)
        elif zone == 2:
            Line.drawPoint(self, y, -x)
        elif zone == 3:
            Line.drawPoint(self, -x, y)
        elif zone == 4:
            Line.drawPoint(self, -x, -y)
        elif zone == 5:
            Line.drawPoint(self, -y, -x)
        elif zone == 6:
            Line.drawPoint(self, -y, x)
        elif zone == 7:
            Line.drawPoint(self, x, -y)

    def drawLine(self, x0, y0, x1, y1):
        zone = Line.findZone(self, x0, y0, x1, y1)
        x0, y0 = Line.convertToZone0(self, x0, y0, zone)
        x1, y1 = Line.convertToZone0(self, x1, y1, zone)

        dx = x1 - x0
        dy = y1 - y0
        d = 2 * dy - dx
        deltaE = 2 * dy
        deltaNE = 2 * (dy - dx)
        x = x0
        y = y0
        Line.plotPoint(self, x, y, zone)

        while x < x1:
            if d <= 0:
                d += deltaE
                x += 1
            else:
                d += deltaNE
                x += 1
                y += 1
            Line.plotPoint(self, x, y, zone)