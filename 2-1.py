checksum2 = 0
checksum3 = 0

with open("2-input.txt") as f:
	for line in f:
		has2 = False
		has3 = False
		
		for c in line.strip():
			num = line.strip().count(c)
			#print "{} --> {}".format(c,num)
			if num == 2:
				has2 = True
			elif num == 3:
				has3 = True
			print has2
			print has3
				
		if has2:
			checksum2 += 1
		if has3:
			checksum3 += 1
			
checksum = checksum2 * checksum3

print checksum
	
