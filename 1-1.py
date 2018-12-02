frequency = 0
with open("1-input.txt") as f:
	for i in f:
		print(i)
		frequency += int(i)
		print("Frequency = {}".format(frequency))
		
