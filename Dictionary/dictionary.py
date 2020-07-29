import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def getMeaning(w):
	w = w.lower()
	if w in data.keys():
		return data[w]
	elif len(get_close_matches(w, data.keys())) > 0:
		check = input(f'Did you mean {get_close_matches(w.lower(), data.keys())[0]}? \nEnter Y if Yes or N if no.\n')
		if check == "Y" or "y":
			return data[get_close_matches(w.lower(), data.keys())[0]]
		else:
			print (f'No matching word found.')
	else:
		print(f'No matching word found in dictionary.')

word = input("Enter word: ")

print (f'{getMeaning(word)}')

