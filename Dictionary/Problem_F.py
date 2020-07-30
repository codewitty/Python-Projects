# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# Unit F take-home assignment

def invoice(unitPrice, quantity, shipping = 10, handling = 5):
	print (f'Cost (unitPrice x quantity) = {unitPrice * quantity}')
	print (f'Shipping = {shipping}')
	print (f'Handling = {handling}') 
	print (f'Total = {(unitPrice * quantity) + shipping + handling}\n')

def printGroupMembers(groupName, *members):
	print(f'Members of {groupName}')
	for name in members:
		print (f'{name}')

def buildBell(rows):
    l1 = [[1]]
    for i in range(1, rows):
        l2 = []
        l2.append(l1[i-1][len(l1)-1])
        for j in range(0, i):
            l2.append(l1[i-1][j] + l2[j])   
        l1.append(l2)
    return l1

def printBell(lst):
	for i in range(len(lst)):
		for j in range(0, i+1):
			print (f'{lst[i][j]:>5}', end = '') 
		print (f'\n')
		

#print('\n'.join(' '.join(map(str,sl)) for sl in lst))


def main():
	invoice(unitPrice = 20, quantity = 4, shipping = 8)
	invoice(unitPrice = 15, quantity = 3, handling = 15)

	printGroupMembers("Group A", "Li", "Audry", "Jia")
	groupB = ["Group B", "Sasha", "Migel", "Tanya", "Hiroto"]
	printGroupMembers(groupB[0], groupB[1], groupB[2], groupB[3], groupB[4])
	print (f'\nBuild a Bell Triangle Output with 8 Rows:\n')

	printBell(buildBell(8))

if __name__ == '__main__':
    main()

'''
Execution results:

Cost (unitPrice x quantity) = 80
Shipping = 8
Handling = 5
Total = 93

Cost (unitPrice x quantity) = 45
Shipping = 10
Handling = 15
Total = 70

Members of Group A
Li
Audry
Jia
Members of Group B
Sasha
Migel
Tanya
Hiroto

Build a Bell Triangle Output with 8 Rows:

    1

    1    2

    2    3    5

    5    7   10   15

   15   20   27   37   52

   52   67   87  114  151  203

  203  255  322  409  523  674  877

  877 1080 1335 1657 2066 2589 3263 4140

'''
