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


breakpoints_list = breakpoint_search(Melanogaster)




def Strips(breakpoints_list):
	'''
	Checks the list of Breakpoints and returns all the strips inside the Melanogaster sequence:
	returns the strips in a list
	'''
	# evaluates each value in the breakpoint_list with its previous value:
	# If breakpoints list is: [1,2,5], this will return [1,3] because 2-1=1 and 5-2=3
	compare_with_previous = [j-i for i, j in zip(breakpoints_list[:-1], breakpoints_list[1:])]


	strips = []
	index = 0

	# for each element in compare_with_previous list
	for e in compare_with_previous:
		# if a strip is found (a strip is a number sequence of 2 and longer)
		if e >= 2:
			# search index of strip in Melanogaster
			# append the strip to Strip_list
			strip = Melanogaster[index:index+e]
			strips.append(strip)
			index += e # increase index with strip length
		else:
			index +=1 # increase index by one to skip to next number
	return strips

a = Strips(breakpoints_list)

print a