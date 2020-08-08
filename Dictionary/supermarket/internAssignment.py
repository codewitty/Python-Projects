# -----------------------------------------------------------
# Demonstrates how to sort input into given categories using
# python.
#
# Joshua Gomes
# -----------------------------------------------------------
import string

# List of states for comparison to input
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
nation = "US"

'''
This function accepts the input from the user and formats it according
to the required parameters to provide the output
'''
def getOutput(expr):
    # Strip punctuation from the input
    expr = expr.translate(str.maketrans('', '', string.punctuation))
    # Split the input string and add the words to a list
    out = expr.split()
    # Create an empty list to add brand names in key value pairs
    cobrid = [] 
    # Create a frame in the required output format. 
    frame = {"brands":[], "state":"", "country":"", "ph no":""}
    num = 1         # number for the key-value pairs of brands

    # Loop through each word in the input and assign values to correct
    # keys of the output dictionary
    for word in out:
        if word in states:
            frame["state"] = word
        elif word == nation:
            frame["country"] = word
        elif word.isdigit():
            frame["ph no"] = word
        else:
            cobrid.append({str(num) : word.lower()})
            num += 1
    frame["brands"] = cobrid

    return frame        # return formatted output

'''
This function creates a dictionary in case of multiple user inputs
The function maps the input as the key and the output as the value
'''
def createTable(table, key, value):
    table[key] = value

    return table
    

def main():
    newTable = {}
    # While loop to facilitate multiple user input
    while True:
        exp = input("Please enter input: ")
        out = getOutput(exp)
        # Print formatted output for a single input
        print(f'Output is: {getOutput(exp)}')
        createTable(newTable, exp, out)
        # Ask user for additional input
        check = input(f'Would you like to enter another input? \nEnter Y if Yes or N if no.\n').upper()
        if  check != "Y":
            break

    # Display table of output in the form of a dictionary
    print(f'**********Tabulated Output***********\n{newTable}')

if __name__ == '__main__':
    main()
