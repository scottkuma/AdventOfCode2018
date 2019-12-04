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
        if self.location + num >= l:
            self.location = (self.location + num) - l
            while self.location >= l:
                self.location -= l
        else:
            self.location = self.location + num

def add_to_recipes(elf1, elf2, recipes):
    e1val = recipes[elf1.location]
    e2val = recipes[elf2.location]

    return str(int(e1val) + int(e2val))

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

target_string = "580741"
target_string_len = len(target_string)
compare_string = "37"

e1 = Elf(0)
e2 = Elf(1)

num = 0
while True:
    num += 1
    if num % 100000 == 0:
        print("Searched thru {}".format(num))
        #sys.exit()
    suff = add_to_recipes(e1,e2,recipes)
    suff_len = len(suff)
    recipes = recipes + suff
    compare_string = compare_string + suff

    #print(target_string + " : " + compare_string)

    if target_string in compare_string:
        print "found @ {}".format(recipes.find(target_string))
        break

    if len(compare_string) > target_string_len:
        compare_string = compare_string[-1 * target_string_len:]

    e1.move(int(recipes[e1.get_loc()]) + 1, recipes)
    e2.move(int(recipes[e2.get_loc()]) + 1, recipes)
