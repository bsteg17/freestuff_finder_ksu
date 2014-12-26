import re

displayed_words = ""

#def display_free_items(description):
	
def find_free_food(description):
	deslist = []
	freelist = []
	for word in description.split(" "):
		deslist.append(word)
	for index, word in enumerate(deslist):
		if (word == "free"):
			if (deslist[index - 1] == "feel"):
				if (deslist[index + 1] == "to"):
					pass
				else:
					displayed_words = deslist[index - 1], word, deslist[index + 1]
					freelist.append(displayed_words)
			else:
				freelist.append(word+" "+deslist[index + 1])
	if len(freelist) > 0:
		return True, freelist
	else:
		return False, freelist