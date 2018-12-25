import re
import time

class marble:
    def __init__(self, value, cw = None, acw = None):
        self.value = value
        if not cw:
            self.cw = self
        else:
            self.cw = cw
        if not acw:
            self.acw = self
        else:
            self.acw = acw

    def __repr__(self):
        return "{}".format(self.value,self.cw.value, self.acw.value)


def play(numplayers,last):

    print("\n\n" + '-' * 50)
    print("New Game! {} players, {} marbles\n".format(numplayers,last) + '-' * 50)
    players = {}
    for p in range(numplayers):
        players[p+1] = 0

    cp = 0
    currMarble = None

    for i in xrange(last + 1):
        cp = (cp % numplayers) + 1
        if currMarble == None:
            currMarble = marble(0)

        elif i % 23 == 0:
            players[cp] += i
            #print("Player {} pockets marble {}".format(
            #cp,
            #i
            #))
            r = currMarble
            #get marble to remove
            for x in range(7):
                r = r.acw

            players[cp] += r.value
            #print("Player {} also pockets marble {}!".format(
            #cp,r.value
            #))
            currMarble = r.cw

            currMarble.acw = r.acw
            r.acw.cw = currMarble

        else:
            # get the insert point (this will be the acw)
            ip = currMarble.cw

            # make the new marble
            nm = marble(i,ip.cw, ip)

            # set links to new marble
            nm.cw.acw = nm
            nm.acw.cw = nm

            #print("Player {} inserted new marble {} between {} and {}".format(
            #    cp,
            #    i,
            #    nm.acw,
            #    nm.cw
            #))

            #change current marble
            currMarble = nm

    maxScore = 0
    for k,v in players.iteritems():
        if v > maxScore:
            maxScore = v

    print "Max Score = {}".format(maxScore)



with open("9-input.txt") as f:
    for line in f:
        #print(line)
        s = re.search('([0-9]+) players; last marble is worth ([0-9]+) points',line)
        players = int(s.group(1))
        last = int(s.group(2))

        t1 = time.time()
        score = play(players,last)
        t2 = time.time()
        print "Seconds elapsed: {}".format(t2-t1)


        print "\n\n"

        t1 = time.time()
        score100 = play(players,last * 100)
        t2 = time.time()
        print "Seconds elapsed: {}".format(t2-t1)
