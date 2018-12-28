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
# for part 1 of today's problem, set size = 3
size = 20

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
