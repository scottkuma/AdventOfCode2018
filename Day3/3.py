import re
import numpy as np


class Claim:
    def __init__(self,num,x,y,w,h):
        self.num = int(num)
        self.x = int(x)
        self.y = int(y)
        self.w = int(w)
        self.h = int(h)
        self.overlaps = False

claims = []

max_x = 0
max_y = 0

with open("3-input.txt") as f:
    for line in f:
        g = re.search(r"(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line)
        num,x,y,w,h = g.groups()
        #print(x,y,w,h)
        if int(x) + int(w) > max_x:
            max_x = int(x) + int(w)
        if int(y) + int(h) > max_y:
            max_y = int(y) + int(h)
        claims.append(Claim(num,x,y,w,h))

#print(max_x,max_y)

cloth = np.zeros((max_y, max_x))

for c in claims:
    for x in range(c.x,c.x + c.w):
        for y in range(c.y,c.y+c.h):
            cloth[y][x] += 1

print len(cloth[np.where(cloth > 1)])

for c in claims:
    for x in range(c.x,c.x + c.w):
        for y in range(c.y,c.y+c.h):
            if cloth[y][x] > 1:
                c.overlaps = True
    if not c.overlaps:
        print("Non-Overlapping Claim: #{}".format(c.num))
