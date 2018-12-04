import re
import numpy as np

class GuardRecord:
    def __init__(self):
        self.sleep_record = np.zeros(60)
        self.fell_asleep_at = None

    def mins_asleep(self):
        return np.sum(self.sleep_record)

observations = []
with open("4-input.txt") as f:
    for line in f:
        observations.append(line.strip())

observations.sort()

get_guard = re.compile("Guard #(\d+)")
get_minute = re.compile("\d+:(\d+)")

guards = {}
current_guard = None
for obs in observations:
    if "Guard #" in obs:
        #New Guard
        current_guard = get_guard.search(obs).group(1)
        if current_guard not in guards:
            guards[current_guard] = GuardRecord()

    if "falls asleep" in obs:
        min = int(get_minute.search(obs).group(1))
        guards[current_guard].fell_asleep_at = min

    if "wakes up" in obs:
        min = int(get_minute.search(obs).group(1))
        for m in range(guards[current_guard].fell_asleep_at,min):
            guards[current_guard].sleep_record[m] += 1

guard_most_asleep = None
most_mins_asleep = 0

print("Strategy 1:")
for g,r in guards.iteritems():
    if r.mins_asleep() > most_mins_asleep:
        guard_most_asleep = g
        most_mins_asleep = r.mins_asleep()

g = int(guard_most_asleep)
m = np.argmax(guards[guard_most_asleep].sleep_record)

print("Guard Most Asleep: {}".format(g))
print("Min Most Asleep At: {}".format(m))
print("Checksum: {}\n\n".format(g * m))

print("Strategy 2:")
mins = np.zeros(60)
gs = np.zeros(60)
for g,r in guards.iteritems():
    for mm in range(0,60):
        if r.sleep_record[mm] > mins[mm]:
            mins[mm] = r.sleep_record[mm]
            gs[mm] = g

min_most = int(np.argmax(mins))
guard_max_mins = int(gs[min_most])
checksum2 = min_most * guard_max_mins

print("Min with most sleeping: {}".format(min_most))
print("Guard most sleeping then: {}".format(guard_max_mins))
print("Checksum: {}".format(checksum2))
