def getPowerLevel(x,y,serial):
    rackID = (x) + 10
    powerLevel = rackID * (y)
    powerLevel += serial
    powerLevel *= rackID
    pstr = str(powerLevel)
    if len(pstr) < 3:
        powerLevel = 0
    else:
        powerLevel = int(pstr[-3])
    powerLevel -= 5
    return powerLevel

def getSquarePowerLevel(x,y,size,serial):
    sum = 0
    for a in range(size):
        for b in range(size):
            pl = getPowerLevel(x+b,y+a,serial)
            sum += pl
    return sum

serial = 9221

maxSqVal = -9999999
maxSize = 0
maxSqCoord = (-1,-1)


# for part 1 of today's problem, set size = 3

print("-"*20 + "PART 1" + "-"*20)

size = 3
s = size

for x in xrange(299 - (s - 1)):
    #print s,x
    for y in xrange(299 - (s - 1)):
        #print s,x,y
        pl = getSquarePowerLevel(x+1,y+1,s,serial)
        if pl > maxSqVal:
            maxSqVal = pl
            maxSize = s
            maxSqCoord = (x+1, y+1)
            print(maxSqCoord,maxSize,maxSqVal)

print("\n\n\n" + "-"*20 + "PART 2" + "-"*20)

size = 20 # num of computations goes up GREATLY, so let's start low & see what happens

maxSqVal = -9999999
maxSize = 0
maxSqCoord = (-1,-1)

for s in xrange(size,0,-1):
    print s
    for x in xrange(299 - (s - 1)):
        #print s,x
        for y in xrange(299 - (s - 1)):
            #print s,x,y
            pl = getSquarePowerLevel(x+1,y+1,s,serial)
            if pl > maxSqVal:
                maxSqVal = pl
                maxSize = s
                maxSqCoord = (x+1, y+1)
                print(maxSqCoord,maxSize,maxSqVal)

            #print (s,(x+1,y+1),pl)
