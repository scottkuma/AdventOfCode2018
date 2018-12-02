frequency = 0
anomalylist = []
frequencyset = {0}
dupeflag = False

with open("1-input.txt") as f:
	for i in f:
		anomalylist.append(i)

cycle = 0		
while dupeflag == False:
	cycle += 1
	print("Cycle {}:".format(cycle))
	for i in anomalylist:
		frequency += int(i)
		if frequency in frequencyset:
			print("DUPE FREQUENCY = {}\nCYCLE = {}".format(frequency,cycle))
			exit(0)
		else:
			frequencyset.add(frequency)
