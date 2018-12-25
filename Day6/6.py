import csv
import numpy as np

def manhattan_distance(p,q):
    if len(p) != len(q):
        print("Make sure # dimensions in points is the same!")
        return None

    s = 0
    for i in xrange(len(p)):

        s += abs(p[i] - q[i])

    return s


points = []
with open("6-test-input.txt") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        points.append([int(val) for val in row])

max_x = 0
max_y = 0

for p in points:
    if p[0] > max_x:
        max_x = p[0]
    if p[1] > max_y:
        max_y = p[1]

owner_grid = np.zeros((max_x,max_y),dtype=np.int8)
dist_grid = np.zeros((max_x, max_y),dtype=np.int8)


for x in xrange(max_x):
    for y in xrange(max_y):
        max_d = 0
        for p in xrange(len(points)):
            #print p, points[p],"-->",x,y," <> ", [x,y]
            md = manhattan_distance(points[p],[x,y])
            print points[p],[x,y],md
            if md > max_d:
                #print x,y,p
                owner_grid[x][y] = p
                max_d = md
            if md == dist_grid[x][y]:
                owner_grid[x][y]= -1


print owner_grid
