Melanogaster = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
length = len(Melanogaster)

def Swap(sequence,(i,j)):
		if i < j:
		    return sequence[:i] + [element for element in reversed(sequence[i:j + 1])] + sequence[j + 1:]
		else:
		    return sequence[:j] + [element for element in reversed(sequence[j:i + 1])] + sequence[i + 1:]

def PossibleChildren(Melanogaster):

	swap_list = []
	for i in range(length):
		for j in range(i + 1, length + 1):
			swap_list.append((i,j))
	return swap_list

def breakpoint_search(List):
	'''
	Function to determine Breakpoint positions.
	Breakpoints are returned in a list containing each Breakpoint.
	'''
	# Creating borders to check for Breakpoints before the first, and behind the last element.
	start = min(List) - 1
	end = max(List) + 1

	# copy the List, appending start and end
	List_breakpoint_check = List[:]
	List_breakpoint_check.append(end)
	List_breakpoint_check.insert(0,start)

	# Creates an empty list of Breakpoints, This is used to append the breakpoints found in the Genome.
	# Checker is the value of the previous List element, starting at the first element of our List: start.
	# Count is used to keep track of the index value inside our List while looping.
	Breakpoints = []
	checker = start
	count = 0

	# For-loop used to check if an element is consecutive with the previous value (either +1 or -1).
	# Previous value is determined by checker and updated using "count".
	for e in List_breakpoint_check[1:]:

		# if element is consecutive with the previous value, skip to next value
		if e == checker + 1 or e == checker -1:
			count += 1
			checker = List_breakpoint_check[count]
		# if value is non-consecutive with the previous value, append it to Breakpoints
		else:
			Breakpoints.append(List_breakpoint_check.index(e))
			count += 1
			checker = List_breakpoint_check[count]

	return Breakpoints

children_swaps = PossibleChildren(Melanogaster)

dictionary = {}
counter = 0
for swap in children_swaps:
	child = Swap(Melanogaster, swap)
	BPs = len(breakpoint_search(child))

	if BPs in dictionary:
		dictionary[BPs].append(child)
	else:
		dictionary[BPs] = [child]

while True:
	if min(dictionary) == 0:
		print len(dictionary[0])
		break
	print min(dictionary), max(dictionary), "start"
	dictionary2 = {}
	number = 0

	for key in dictionary:
		for value in dictionary[key]:
			for swap in children_swaps:
				child = Swap(value, swap)

				BPs = len(breakpoint_search(value))

				if BPs in dictionary2:
					if BPs <= min(dictionary2) + number:
						dictionary2[BPs].append(child)
				else:
					dictionary2[BPs] = [child]

	for key in dictionary2:
		for value in dictionary2[key]:
			BPs = len(breakpoint_search(value))
			if BPs in dictionary:
				dictionary[BPs].append(value)
			else:
				dictionary[BPs] = [child]


	minimum = min(dictionary)
	maximum = max(dictionary)
	

	for key in range(minimum+number+1, maximum +1):
		dictionary.pop(key, None)


