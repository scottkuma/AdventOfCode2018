def getCommonLetters(word1, word2):
	letters = ""
	for p in range(len(word1)):
		if word1[p] == word2[p]:
			letters += word1[p]
	return letters
	

with open("2-input.txt") as f:
	content = f.readlines()
	
box_list = [x.strip() for x in content]
box_list.sort()

prev_box = ""
for box in box_list:
	if prev_box == "":
		prev_box = box
	else:
		cl = getCommonLetters(box,prev_box)
		if  len(box) - len(cl) == 1:
			print( getCommonLetters(box, prev_box) )
			exit()
		else:
			prev_box = box
			
		
