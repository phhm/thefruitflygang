import math
from Queue import PriorityQueue



Melanogaster = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
sorted_Melanogaster = sorted(Melanogaster)
unsorted_Melanogaster = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]

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

def Strips(breakpoints_list, List):
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
			strip = List[index:index+e]
			strips.append(strip)
			index += e # increase index with strip length
		else:
			index +=1 # increase index by one to skip to next number
	return strips

def Strips_pos_or_neg(strip_list):
	'''
	Strips are defined as number-sequences having either a positive or negative relationship.
	A positive strip is characterized by an increasing number sequence (from left to right).
	A negative strip is characterized by a decreasing number sequence (from left to right).
	Checks if strips are Positive or Negative.
	'''
	first_number = 0

	decreasing_strip = []
	increasing_strip = []

	# loops over all strips in strip_list
	for e in strip_list:
		# for each strip
		for i in e:
			# define first number in each strip as the checker
			if first_number == 0:
				first_number = i
			# if the second number in the strip is smaller then the first value
			# append strip to decreasing striplist
			elif i < first_number:
				decreasing_strip.append(e)
				first_number = 0
				break
			# if the second number in the strip is bigger then the first value
			# append strip to increasing striplist
			elif i > first_number:
				increasing_strip.append(e)
				first_number = 0
				break
	return decreasing_strip, increasing_strip

def possible_swap_Lists(Melanogaster):
	'''
	brute_force method: Chooses random swap-borders, swaps Melanogster, if breakpoints are 
	less in the new list of Melanogaster: returns new list. Hashes every state, checks for 
	repetetive steps.
	'''

	Ideal_swap_list = []
	Swap1_list = []
	return_state = 0
	while True: 
		a = 1
		b = 2

		if Melanogaster.index(a)<Melanogaster.index(b):
			New_melanogaster = Swap(Melanogaster, a, b)
		else:
			New_melanogaster = Swap(Melanogaster, b, a)

		i = breakpoint_search(New_melanogaster)
		j = breakpoint_search(Melanogaster) 

		n = Strips(i)
		m = Strips_pos_or_neg(n)

		while True:
			if len(i) == len(j) -2:
				Ideal_swap_list.append([a,b])
				if b < 25: 
					b += 1
				elif b == 25:
					if a < 25:
						a += 1
						b = 1
					elif a == 25:
						break
			else:
				if b < 25: 
					b += 1
				elif b == 25:
					if a < 25:
						a += 1
						b = 1
					elif a == 25:
						a = 1
						b = 2
						break

			if Melanogaster.index(a)<Melanogaster.index(b):
				New_melanogaster = Swap(Melanogaster, a, b)
			else:
				New_melanogaster = Swap(Melanogaster, b, a)

			i = breakpoint_search(New_melanogaster)
			j = breakpoint_search(Melanogaster) 

		while True:
			if len(i) == len(j) - 1:
				Swap1_list.append([a,b])
				if b < 25: 
					b += 1
				elif b == 25:
					if a < 25:
						a += 1
						b = 1
					elif a == 25:
						break
			else:
				if b < 25: 
					b += 1
				elif b == 25:
					if a < 25:
						a += 1
						b = 1
					elif a == 25:
						return_state = 1
						break

			if Melanogaster.index(a)<Melanogaster.index(b):
				New_melanogaster = Swap(Melanogaster, a, b)
			else:
				New_melanogaster = Swap(Melanogaster, b, a)

			i = breakpoint_search(New_melanogaster)
			j = breakpoint_search(Melanogaster) 
		if return_state == 1:
			break

	Ideal_swap_list_checked_for_doubles = []
	for e in Ideal_swap_list:
		combination = sorted(e)
		if combination not in Ideal_swap_list_checked_for_doubles:
			Ideal_swap_list_checked_for_doubles.append(combination)

	Swap1_list_checked_for_doubles = []
	for e in Swap1_list:
		combination = sorted(e)
		if combination not in Swap1_list_checked_for_doubles:
			Swap1_list_checked_for_doubles.append(combination)


	return Ideal_swap_list_checked_for_doubles, Swap1_list_checked_for_doubles

dictionary = {}
def Hash(Melanogaster,layer):
	hashed = tuple(Melanogaster)
	dictionary[hashed] = layer

def unique(Melanogaster, layer):
	if Melanogaster in dictionary:
		if layer <= dictionary[Melanogaster]:
			dictionary[Melanogaster] = layer
			return True
		else:
			return False

	dictionary[Melanogaster] = layer
	return True

def DefineHash(Melanogaster, layer):
	if layer == 1:
		hashed1.add(tuple(Melanogaster))

def Distance(Melanogaster):
	a = breakpoint_search(Melanogaster)
	Distance = math.ceil(len(a)/2)
	return Distance

def MakePriorityQueue(Melanogaster, countah):
	queue = PriorityQueue()
	alles = All_Swaps(Melanogaster, countah)
	for each in alles:
		queue.put(each)
	return queue

def Define_swap_Position(PriorityQueue):
	first_in_line = PriorityQueue.get(True)
	a = first_in_line[1][0]
	b = first_in_line[1][1]
	return a,b

List_of_states = []

def update(negatives, Melanogaster):

	negatives_single_list = []
	for e in negatives:
		for element in e:
			negatives_single_list.append(element)

	c = len(Melanogaster)
	d = range(c+1)
	e = d[1:]

	swap_list = e[:]
	for e in negatives_single_list:
		if e in swap_list:
			swap_list.remove(e)

	acount = 0
	bcount = 0
	a = swap_list[acount]
	b = swap_list[bcount]
	swaps = []

	while True:
		if bcount < len(swap_list) -1: 
			bcount += 1
			b = swap_list[bcount]
		elif bcount >= len(swap_list) -1:
			if acount < len(swap_list) -1:
				acount += 1
				a = swap_list[acount]
				bcount = 0
				b = swap_list[bcount]
			elif acount >= len(swap_list) -1:
				break
		swaps.append([a,b])
	return swaps

def All_Swaps(Melanogaster, countah):

	All_Swaps = []

	breakpoints = breakpoint_search(Melanogaster)
	strips = Strips(breakpoints, Melanogaster)
	negatives = []
	for e in strips:
		negative = e[1:-1]
		if len(negative) >= 1:
			negatives.append(negative)

	possible_swaps = update(negatives, Melanogaster)
	
	for e in possible_swaps:
		for each in e:
			a = e[0]
			b = e[1]

		if Melanogaster.index(a)<Melanogaster.index(b):
			New_melanogaster = Swap(Melanogaster, a, b)
		else:
			New_melanogaster = Swap(Melanogaster, b, a)

		All_Swaps.append(New_melanogaster)

	values = []
	All_Swaps_single = []
	for e in All_Swaps:
		if e not in All_Swaps_single:
			if unique(tuple(e), countah):
				All_Swaps_single.append(e)

			# if tuple(e) in dictionary:
			# 	other_layer = dictionary.get(tuple(e))
			# 	if other_layer > countah:
			# 		dictionary[countah] = dictionary.pop(tuple(e))
			# 		All_Swaps_single.append(e)

	for e in All_Swaps_single:
		values.append((Distance(e) + countah, e,Distance(e), countah, Melanogaster))
	return values

def queue_get_all(q, MAX_QUEUE):
	items = []
	MAX_QUEUE = 100
	maxItemsToRetreive = 100
	for numOfItemsRetrieved in range(0, maxItemsToRetreive):
		try:
			if numOfItemsRetrieved == maxItemsToRetreive:
				break
			items.append(q.get_nowait())
		except Empty, e:
			break
	return items, MAX_QUEUE


def Main(Melanogaster):	
	MAX_QUEUE = 0
	countah = 1
	answers = 0
	found_answers = []
	all_states = {}
	first_time_countah = 1
	q = MakePriorityQueue(Melanogaster, countah)
	while answers != 10:
		
		previous = q.get(True)
		all_states[str(previous[1])] = previous[4]

		# print previous, MAX_QUEUE
		if first_time_countah == 1:
			countah = 1
			first_time_countah = 0
		else: 
			countah = previous[3] + 1

		Melanogaster = previous[1]
		all_states[str(previous[1])] = previous[4]
		a = All_Swaps(Melanogaster, countah)
		for each in a:
			q.put(each)
			MAX_QUEUE += 1
		if MAX_QUEUE >= 300:
			first_part,b = queue_get_all(q, MAX_QUEUE)
			q = PriorityQueue()
			MAX_QUEUE = b
			for each in first_part:
				q.put(each)
			first_part = []
		# print previous[3]

		no_retry = str(str(previous[1]) + str(previous[4]))

		if Melanogaster == sorted_Melanogaster and no_retry not in found_answers:
			print "Answers = ", answers
			x = 1
			one_before_present = all_states[str(previous[1])]
			print Melanogaster, " Final Result!!"
			while one_before_present:
				print one_before_present, "All states Previous", x
				one_before_present = all_states.get(str(one_before_present), None)
				x += 1
			found_answers.append(str(previous[1]) + str(previous[4]))
			countah = 1
			first_time_countah = 1
			Melanogaster = unsorted_Melanogaster
			answers += 1
			one_before_present = None 
			all_states = {}
			MAX_QUEUE =0
			q = MakePriorityQueue(Melanogaster, countah)
			print answers

Main(Melanogaster)
