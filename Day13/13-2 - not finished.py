infile = "prod_track.txt"

class Cart:
    def turn_right(self):
        dirs = {"^":">", ">":"v", "v":"<", "<":"^"}
        self.facing = dirs[self.facing]

    def turn_left(self):
        dirs = {"^":"<", ">":"^", "v":">", "<":"v"}
        self.facing = dirs[self.facing]

    def hit_intersection(self):
        if self.last_turn == None or self.last_turn == "R":
            self.last_turn = "L"
            self.turn_left()
        elif self.last_turn == "L":
            self.last_turn = "S"
        elif self.last_turn == "S":
            self.last_turn = "R"
            self.turn_right()
        else:
            print("Uh oh!")

    def get_curr_pos(self):
        return self.track[self.posy][self.posx]

    def hit_curve(self,curve):
        if curve == "\\":
            if self.facing in "^v":
                self.turn_left()
            elif self.facing in "<>":
                self.turn_right()
        if curve == "/":
            if self.facing in "^v":
                self.turn_right()
            elif self.facing in "<>":
                self.turn_left()

    def step(self):
        if self.facing == "<":
            self.posx -= 1
        elif self.facing == ">":
            self.posx += 1
        elif self.facing == "v":
            self.posy += 1
        elif self.facing == "^":
            self.posy -= 1
        if self.get_curr_pos() == "+":
            self.hit_intersection()

        if self.get_curr_pos() in "/\\":
            self.hit_curve(self.get_curr_pos())



    def __init__(self,facing,posx,posy,track):
        self.facing = facing
        self.posx = posx
        self.posy = posy
        self.track = track
        self.last_turn=None

    def __repr__(self):
        return(self.facing + " @ ({},{}) on {}".format(self.posx, self.posy, self.get_curr_pos()))

    def __str__(self):
        return(self.facing + " @ ({},{}) on {}".format(self.posx, self.posy, self.get_curr_pos()))

def get_track_pos(posy,posx,pos_char,carts):
    out_char = pos_char
    found_car = False
    for cart in carts:
        if cart.posy == posy and cart.posx == posx:
            if found_car:
                out_char = "X"
            else:
                out_char = cart.facing
                found_car = True
    return out_char

def get_clean_track(track):
    clean_track = []
    for r in track:
        r = r.replace("<", "-")
        r = r.replace(">", "-")
        r = r.replace("^", "|")
        r = r.replace("v", "|")
        clean_track.append(r)
    return(clean_track)


def drawboard(track,cars):
    for r in range(len(track)):
        row = ""
        for c in range(len(track[r])):
            if track[r][c] in "-|+/\\":
                row += get_track_pos(r,c,track[r][c],cars)
            else:
                row += " "
        print(row)

def get_cars(track):
    cars = []

    for r in range(len(track)):
        for c in range(len(track[r])):
            if track[r][c] in "<>^v":
                cars.append(Cart(track[r][c],c,r,get_clean_track(track)))
                print(cars[-1])

    return cars

def is_crash(cars):
    positions = []
    crash = False
    crashPositions = []
    for car in cars:
        if (car.posx, car.posy) in positions:
            crash = True
            crashPositions.append((car.posx, car.posy))
        else:
            positions.append((car.posx, car.posy))
    print(crashPositions)
    return crashPositions


track = open(infile).readlines()
track = [l.strip('\n') for l in track] #remove trailing linefeeds

cars = get_cars(track)
track = get_clean_track(track)

crash = False
num_steps = 0
while len(cars) > 1:
    num_steps += 1
    #print("Step #{}".format(num_steps))
    for c in cars:
        c.step()
    crash = is_crash(cars)

    if len(crash) > 0:
        for c in crash:
            print("CRASH @ ({}, {})!!!!!!!!!!!!!!!!!".format([0], [1]))
            print(cars)
            cars_to_remove = []
            for idx in range(0,len(cars)):
                if (cars[idx].posx, cars[idx].posy) == (c[0], c[1]):
                    print("removing car @ idx {}: {}, {}".format(idx,c[0], c[1]))
                    cars_to_remove.append(idx)
            if len(cars_to_remove) > 0:
                for i in reversed(cars_to_remove):
                    del cars[i]
                print(len(cars))

print ("Steps = {}".format(num_steps))
print ("Last Car Position:")
print(cars)
