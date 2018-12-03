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
    # Find Max x and y dimensions (how big does the cloth need to be?)
    # While I'm at it, store the claims so I don't need to read the file again.
    for line in f:
        g = re.search(r"(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line)
        num,x,y,w,h = g.groups()
        if int(x) + int(w) > max_x:
            max_x = int(x) + int(w)
        if int(y) + int(h) > max_y:
            max_y = int(y) + int(h)
        claims.append(Claim(num,x,y,w,h))

# Make my cloth representation
cloth = np.zeros((max_y, max_x))

# Cycle through all claims, incrementing each sq in
# within each claim.
for c in claims:
    for x in range(c.x,c.x + c.w):
        for y in range(c.y,c.y+c.h):
            cloth[y][x] += 1

# Use numpy function magic to find how many sq in have multiple claims
print("Sq. In of overlapping cloth: {}".format(len(cloth[np.where(cloth > 1)])))

# Cycle through all claims again, looking to see if multiple claims
# exist in them.  If none, print the claim # (and keep going in case > 1)
for c in claims:
    for x in range(c.x,c.x + c.w):
        for y in range(c.y,c.y+c.h):
            if cloth[y][x] > 1:
                c.overlaps = True
    if not c.overlaps:
        print("Non-Overlapping Claim: #{}".format(c.num))
