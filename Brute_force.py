Melanogaster = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]

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


def Consecutive_genes_check(breakpoints_list):
	'''
	Checks the list of Breakpoints and returns the largest consecutive genes set:
	returns the index of the first element of this consecutive gene sets + the length
	'''
	# Searches for the biggest difference in values in the Breakpoints List
	# It evaluates each value in the list with its previous value:
	# If breakpoints list is: [1,2,5], this will return [1,3] because 2-1=1 and 5-2=3
	new_list = [j-i for i, j in zip(breakpoints_list[:-1], breakpoints_list[1:])]
	# By choosing the largest number in new_list, the biggest consecutive gene set is found
	# The same could be done for the smalles set of consecutive genes
	longest_consecutive_list_length = max(new_list)

	# Finding the index of the biggest number in new_list
	# adding 1 gives the index in Melanogaster of the start of the longest gene-set
	longest_start = new_list.index(longest_consecutive_list_length) + 1 
	return longest_start, longest_consecutive_list_length


def brute_force(Melanogaster):
	'''
	brute_force method: Chooses random swap-borders, swaps Melanogster, if breakpoints are 
	less in the new list of Melanogaster: returns new list. Hashes every state, checks for 
	repetetive steps.
	'''

	import random

	List_of_states = []
	minimum = min(Melanogaster)
	maximum = max(Melanogaster)

	while True: 
		a = random.randrange(minimum, maximum)
		b = random.randrange(minimum, maximum)

		if Melanogaster.index(a)<Melanogaster.index(b):
			New_melanogaster = Swap(Melanogaster, a, b)
		else:
			New_melanogaster = Swap(Melanogaster, b, a)

		i = breakpoint_search(New_melanogaster)
		j = breakpoint_search(Melanogaster) 



		if len(i) < len(j):
			String_hash = ''.join(str(x) for x in New_melanogaster)
			List_of_states.append(String_hash)
			if len(List_of_states)!=len(set(List_of_states)):
				Melanogaster = New_melanogaster
				return Melanogaster


# # THIS CHOOSES 1 RANDOM SWAP, AFTER WHICH THE LIST IS REDUCED BY 1 BREAKPOINT
# print "Before 1 random swap"
# print Melanogaster
# print "this is the amount of breakpoints at this step", len(breakpoint_search(Melanogaster))
# Melanogaster = brute_force(Melanogaster)
# print "After 1 random swap:"
# print Melanogaster
# print "this is the amount of breakpoints at this step", len(breakpoint_search(Melanogaster))


# #THIS IS A BRUTE FORCE METHOD: COMMENT THE FOLLOWING LINES OUT TO RUN IT
count = 0

while Melanogaster != sorted(Melanogaster):
	Melanogaster = brute_force(Melanogaster)
	print Melanogaster
	count += 1
	if count >= 30:
		break



