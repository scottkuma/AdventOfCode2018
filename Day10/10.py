import re
import time

class Point:
    def __init__(self,posx,posy,velx,vely):
        self.posx = posx
        self.posy = posy
        self.velx = velx
        self.vely = vely

    def __repr__(self):
        return "[@({},{}) v({},{})]".format(posx,posy,velx,vely)

    def posAtT(self,t):
        return Point(self.posx + self.velx * t,
                     self.posy + self.vely * t,
                     self.velx,
                     self.vely
        )


def getLargestDisplacement(arr):
    largestd = 0
    for p in arr:
        largestd = abs(p.posx) if abs(p.posx) > largestd else largestd
        largestd = abs(p.posy) if abs(p.posy) > largestd else largestd
    return largestd


def makeStarField(arr):
    ld = getLargestDisplacement(arr)
    fieldSize = ld * 2 + 1
    print fieldSize
    field = [['.' for col in range(fieldSize)] for row in range(fieldSize)]
    for point in arr:
        field[point.posy + ld][point.posx + ld] = '#'
    return field

def printStarField(arr):
    for line in arr:
        print ''.join(line)

with open("10-input.txt") as f:

    largestd = 0

    points = []
    lines = []

    for line in f:
        #print(line)
        s = re.search('position=<([- 0-9]+),([- 0-9]+)> velocity=<([- 0-9]+),([- 0-9]+)>',line)
        posx = int(s.group(1))
        posy = int(s.group(2))
        velx = int(s.group(3))
        vely = int(s.group(4))

        lines.append([posx,posy,velx,vely])
        points.append(Point(posx,posy,velx,vely))


    t = 10558

    print "\n\nAfter T = {} seconds\n".format(t)
    arr = [p.posAtT(t) for p in points]
    board = makeStarField(arr)
    printStarField(board)
    time.sleep(1)

    t += 1
    for p in points:
        p.tick()
