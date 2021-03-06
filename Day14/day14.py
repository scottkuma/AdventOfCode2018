import sys

class Elf:
    def __init__(self, location):
        self.location = location

    def __str__(self):
        return "Elf on location {}".format(self.location)

    def __repr__(self):
        return self.__str__()

    def get_loc(self):
        return int(self.location)

    def move(self,num,recipes):
        l = len(recipes)
        #print("Recipes Length: {}".format(l))
        if self.location + num >= l:
            self.location = (self.location + num) - l
            while self.location >= l:
                self.location -= l
        else:
            self.location = self.location + num
        #print("New Location: {}".format(self.location))
        #print("Value: {}".format(recipes[self.location]))

def add_recipes(elf1, elf2, recipes):
    e1val = recipes[elf1.location]
    e2val = recipes[elf2.location]

    return recipes + str(int(e1val) + int(e2val))

def print_recipes(recipes,elf1,elf2):

    outstr = ""
    rating = ""
    for a in range(len(recipes)):

        rating = recipes[a]
        if a == elf1.get_loc():
            rating = "({})".format(rating)
        if a == elf2.get_loc():
            rating = "[{}]".format(rating)
        if len(rating) == 1:
            outstr += " " + rating + " "
        else:
            outstr += rating

    return(outstr)

recipes = "37"

num_recipes_to_check = 10
initial_length = len(recipes)
check_after = 580741

target_start = check_after

e1 = Elf(0)
e2 = Elf(1)

while True:

#    print(print_recipes(recipes,e1,e2))

    recipes = add_recipes(e1,e2,recipes)
    e1.move(int(recipes[e1.get_loc()]) + 1, recipes)
    e2.move(int(recipes[e2.get_loc()]) + 1, recipes)

    if len(recipes) > target_start + num_recipes_to_check:
        #print(recipes)
        print(recipes[target_start:target_start + num_recipes_to_check])
        print("Done")
        sys.exit()
