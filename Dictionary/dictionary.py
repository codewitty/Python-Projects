import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def getMeaning(w):
	wl = w.lower()
	wu = w.upper()
	if w in data.keys():
		return data[w]
	if wu in data.keys():
		return data[wu]
	if w.title() in data.keys():
		return data[w.title()]
	elif wl in data.keys():
		return data[wl]
	elif len(get_close_matches(wl, data.keys())) > 0:
		check = input(f'Did you mean {get_close_matches(wl, data.keys())[0]}? \nEnter Y if Yes or N if no.\n').upper()
		if check == "Y":
			return data[get_close_matches(wl, data.keys())[0]]
		else:
			return (f'No matching word found.')
	else:
		return (f'No matching word found in dictionary.')

word = input("Enter word: ")

output = getMeaning(word)

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)
