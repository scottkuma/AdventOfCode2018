import re

class Task:
    def __init__(self, name, prereq=None):
        self.available = True
        self.prereqs = []
        self.name = name
        self.timeToFinish = 60 + (ord(self.name) - 64)
        if prereq:
            self.setPrereq(prereq)

    def __repr__(self):
        return("Task {} Avx={} Prereqs={} TTF={}".format(self.name,
                                                         self.available,
                                                         self.prereqs,
                                                         self.timeToFinish))

    def setPrereq(self,prereq):
        if prereq not in self.prereqs:
            self.available = False
            self.prereqs.append(prereq)

    def tick(self):
        self.timeToFinish -= 1
        if self.timeToFinish > 0:
            return False
        else:
            return True



def removePrereqs(prereq,tasks):
    ##print tasks
    for k,t in tasks.iteritems():
        if prereq in t.prereqs:
            t.prereqs.remove(prereq)
        if len(t.prereqs) == 0:
            t.available = True

tasks = {}

with open("7-input.txt") as f:
    for line in f:
        s = re.search('[Ss]tep (.) must be finished before step (.)',line)
        prereq = s.group(1)
        step = s.group(2)

        if prereq not in tasks.keys():
            tasks[prereq] = Task(prereq)

        if step not in tasks.keys():
            tasks[step] = Task(step, prereq)
        elif prereq not in tasks[step].prereqs:
            tasks[step].setPrereq(prereq)


order = ''
seconds = 0
elves = [False,False,False,False,False]
available_tasks = {}

while len(tasks) > 0 or elves != [False,False,False,False,False]:

    for t in sorted(tasks.keys()):
        if tasks[t].available and t not in available_tasks.keys():
            available_tasks[t] = tasks[t]


    at_keys = sorted(available_tasks.keys())
    available_elves = []

    # assign tasks to elves
    for ei in range(len(elves)):
        if not elves[ei]:
            if len(available_tasks) > 0:
                taskToAssign = at_keys.pop(0)
                elves[ei] = available_tasks.pop(taskToAssign)
                tasks.pop(taskToAssign)


    for te in range(len(elves)):
        if elves[te]:
            if elves[te].tick(): # it's done!
                order += elves[te].name
                removePrereqs(elves[te].name,tasks)
                elves[te] = False

    seconds += 1


print "It took {} seconds".format(seconds)
print "Order: {}".format(order)
