Melanogaster = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]

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

Where_are_the_breakpoints = breakpoint_search(Melanogaster)
print "this is where are breakpoints are located: ", Where_are_the_breakpoints
print "This is how many breakpoints we have now: " + str(len(Where_are_the_breakpoints))
print Where_are_the_breakpoints

