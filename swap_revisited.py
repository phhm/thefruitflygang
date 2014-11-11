# Swap function revisited using reversed

# Somewhere in the program, a list and swap-borders are given
# For this example the following variables are used:
List = [4, 5, 6, 8, 2, 3, 1, 7]
left_border = 6
right_border = 3



def Swap(List, left_border, right_border):
	'''
	Swaps a sequence of List elements between the
	left_border and right_border
	'''

	i = List.index(left_border)
	j = List.index(right_border)

	templist = []

	for number in reversed(List[i:j+1]):
		templist.append(number)

	return List[:i] + templist + List[j+1:]


# Uses the example variables and prints output
na_swap = Swap(List, left_border, right_border)
print na_swap
