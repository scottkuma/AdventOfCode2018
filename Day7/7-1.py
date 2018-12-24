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
            #print("New Prereq added!")



def removePrereqs(prereq,tasks):
    ##print tasks
    for k,t in tasks.iteritems():
        #print("  Checking task {}'s prereqs".format(k))
        ##print(t)
        if prereq in t.prereqs:
            #print("  Removing prereq {} from {}!".format(prereq, k))
            t.prereqs.remove(prereq)
        if len(t.prereqs) == 0:
            #print("  Task {} now available!".format(k))
            t.available = True

tasks = {}

with open("7-input.txt") as f:
    for line in f:
        #print(line)
        s = re.search('[Ss]tep (.) must be finished before step (.)',line)
        prereq = s.group(1)
        step = s.group(2)

        #print tasks.keys()

        if prereq not in tasks.keys():
            #print("Creating new task {}".format(prereq))
            tasks[prereq] = Task(prereq)

        if step not in tasks.keys():
            #print("Creating new task {} with prereq {}.".format(step,prereq))
            tasks[step] = Task(step, prereq)
        elif prereq not in tasks[step].prereqs:
            #print("Adding prereq {} to task {}".format(prereq, step))
            tasks[step].setPrereq(prereq)


for t in sorted(tasks.keys()):
    print(tasks[t])

order = ''
while len(tasks) > 0:
    #print("Starting New Cycle\n\n")
    avx = []
    for t in sorted(tasks.keys()):
        if tasks[t].available:
            avx.append(t)
        #print avx

    taskToPerform = ''
    if len(avx) == 0:
        #print("Error: No tasks available!")
        exit(1)
    elif len(avx) == 1:
        taskToPerform = avx[0]
    else:
        taskToPerform = sorted(avx)[0]

    #print("Performing task {}".format(taskToPerform))
    order += taskToPerform
    tasks.pop(taskToPerform)
    removePrereqs(taskToPerform,tasks)

print order
