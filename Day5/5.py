import string

with open("5-input.txt") as f:
    s = f.readline().strip()

def fullyReact(polymer):
    p = 1
    while True:
        start_len = len(polymer)
        for a in string.ascii_uppercase:
            c = a + a.lower()
            r = a.lower() + a
            polymer = polymer.replace(c,'').replace(r,'')
        if len(polymer) == start_len:
            return polymer

def improve_polymer(polymer):
    r = None
    l = 999999
    
    for a in string.ascii_uppercase:
        test_polymer = polymer.replace(a,'').replace(a.lower(),'')
        test_len = len(fullyReact(test_polymer))
        if test_len < l:
            r = a
            l = test_len
    return (r,l)

print ("Reacting base polymer returns a polymer of length {}\n\n".format(len(fullyReact(s))))

r,l = improve_polymer(s)

print("Removing {} and fully reacting returns an optimized polymer of length {}".format(r,l))
