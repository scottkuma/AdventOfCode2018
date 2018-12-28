rules = {}

with open("12-input.txt") as f:
    state = f.readline().split(':')[1].strip()
    f.readline()
    for line in f:
        rule,result = line.strip().split(' => ')
        if result == "#":
            rules[rule] = "#"
front_insert = 5
state = '.' * front_insert + state
state += '.'*5

oldsum = 0

for x in range(1050):
    newstate = ''
    for c in range(len(state)):
        comp = ''

        if c == 0:
            comp = '..' + state[:3]
        elif c == 1:
            comp = '.' + state[:4]
        else:
            comp = state[c-2:c+3]
            while len(comp)< 5:
                comp += '.'
        #print comp + " => " + rules[comp]
        if comp in rules:
            newstate = newstate + '#'
        else:
            newstate = newstate + '.'

    if '#' in newstate[-3:]:
        newstate = newstate + '.'

    sum = 0
    for p in range(len(newstate)):
        if newstate[p] == '#':
            sum += p - front_insert
#        print (p-2), newstate[p], sum

#    print "{:2}: {} {}".format(x+1,newstate,sum)
    state = newstate
    print x+1, sum, '-',oldsum, '=', sum-oldsum
    oldsum = sum

desiredval = 50000000000
diff = 69

sumat102 = 9306

val = sumat102 + (desiredval - 102) * diff
print val
