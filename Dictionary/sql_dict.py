import json
import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

#data = json.load(open("data.json"))

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

# Query the database
query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if results:
	for result in results:
		print(f'{result[0]}')
else:
	print(f'{getMeaning(word)}')
