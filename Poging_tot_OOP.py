
Melanogaster = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
Goal = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)


Genome = tuple(Melanogaster)

import math
from Queue import PriorityQueue


class Sequence(object):
	'''
	'''
	def __init__(self, sequence, parent=None, start=0, goal=0):
		self.children = []
		self.parent = parent
		self.sequence = sequence
		self.dist = 0
		self.max = max(sequence)
		self.min = min(sequence)
		self.length = len(sequence)


		if parent:
			self.path = parent.path[:]
			self.path.append(sequence)
			self.start = parent.start
			self.goal = parent.goal
			self.depth = parent.depth + 1
		else:
			self.path = [sequence]
			self.start = start
			self.goal = goal
			self.depth = 0

		def GetDist(self):
			pass
		def PossibleChildren(self):
			pass
		def Breakpoint_search(self):
			pass
		def Swap(self):
			pass
		def Strips(self):
			pass
		def Strips_pos_or_neg(self):
			pass
		def unique(self):
			pass

class state_sequence(Sequence):
	def __init__(self, sequence, parent, start = 0, goal = 0):
		super(state_sequence, self).__init__(sequence, parent, start, goal)
		self.breakpoints, self.BPs = self.breakpoint_search()
		self.dist = self.GetDist()
		self.strips = self.Strips()
		self.neg_strips, self.pos_strips = self.Strips_pos_or_neg()
		self.Possiblechildren = self.PossibleChildren()

	def GetDist(self):
		if self.sequence == self.goal:
			return 0
		return math.ceil(self.BPs/2 + self.depth)

	def Swap(self,(i,j)):
		if i < j:
		    return self.sequence[:i] + tuple([element for element in reversed(self.sequence[i:j + 1])]) + self.sequence[j + 1:]
		else:
		    return self.sequence[:j] + tuple([element for element in reversed(self.sequence[j:i + 1])]) + self.sequence[i + 1:]

	def breakpoint_search(self):
		'''
		Function to determine Breakpoint positions.
		Breakpoints are returned in a list containing each Breakpoint.
		'''

		# Creating borders to check for Breakpoints before the first, and behind the last element.
		start = self.min - 1
		end = self.max + 1

		# copy the List, appending start and end
		List_breakpoint_check = list(self.sequence[:])
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

		return Breakpoints,len(Breakpoints)

	def Strips(self):
		'''
		Checks the list of Breakpoints and returns all the strips inside the Melanogaster sequence:
		returns the strips in a list
		'''
		# evaluates each value in the breakpoint_list with its previous value:
		# If breakpoints list is: [1,2,5], this will return [1,3] because 2-1=1 and 5-2=3
		compare_with_previous = [j-i for i, j in zip(self.breakpoints[:-1], self.breakpoints[1:])]

		strips = []
		index = 0

		# for each element in compare_with_previous list
		for e in compare_with_previous:
			# if a strip is found (a strip is a number sequence of 2 and longer)
			if e >= 2:
				# search index of strip in Melanogaster
				# append the strip to Strip_list
				strip = self.sequence[index:index+e]
				strips.append(strip)
				index += e # increase index with strip length
			else:
				index +=1 # increase index by one to skip to next number
		return strips

	def Strips_pos_or_neg(self):
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
		for e in self.strips:
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

	def PossibleChildren(self):
		numb_inside_strips = set()
		for e in self.strips:
			for i in e[1:-1]:
				numb_inside_strips.add(self.sequence.index(i))
		

		swap_list = []
		for i in range(self.length):
			for j in range(i + 1, self.length + 1):

				if i not in numb_inside_strips and j not in numb_inside_strips:
					swap_list.append((i,j))
		return swap_list

	def unique(self, list_of_states):
		if self.sequence in list_of_states:
			if self.depth <= list_of_states[self.sequence]:
				list_of_states[self.sequence] = self.depth
				return True, list_of_states
			else:
				return False, list_of_states

		list_of_states[self.sequence] = self.depth
		return True, list_of_states



def Greedy(genome, Goal):
    """
    """

    Object = state_sequence(genome, None, genome, Goal)
    list_of_states = {}


    while True:
    	parent = Object
    	print Object.sequence, Object.depth

        perfect_children = []
        regular_children = []
        imperfect_children = []

        for i in parent.Possiblechildren:
        	child = parent.Swap(i)
        	child_object = state_sequence(child, parent)

        	unique, list_of_states = child_object.unique(list_of_states)
        	if unique:
        		# if child_object.sequence == child_object.goal:
        		# 	print "yess"
        		# 	break

        		if child_object.BPs == parent.BPs - 2:
        			perfect_children.append(child_object)
        		if child_object.BPs == parent.BPs - 1:
        			regular_children.append(child_object)
        		if child_object.BPs == parent.BPs:
        			imperfect_children.append(child_object)

    	while True:

    		if len(perfect_children) >= 1:
    			for i in perfect_children:
    				if len(i.neg_strips) > 0:
    					Object = i
    					break
    			Object = perfect_children[0]
    			break

			if len(perfect_children) == 0 and len(regular_children) >= 1:
				for i in regular_children:
					if len(i.neg_strips) > 0:
						Object = i
						break
				Object = regular_children[0]
				break

			if len(perfect_children) == 0 and len(regular_children) ==0:
				for i in imperfect_children:
					if len(i.neg_strips) > 0:
						Object = i
						break
				Object = imperfect_children[0]
				break


#############################################################################################################
# Greedy algorithm does not work
# Objects are pretty messy, but belows examples show what you can do with a "state_sequence" object

b = Sequence((23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9))
a = state_sequence((23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9),b)
print a.sequence, "sequence"
print a.parent.sequence, "parent sequence"
print a.breakpoints, "breakpoints list"
print a.BPs, "number of breakpoints"
print a.strips, "strips"
print a.pos_strips, "positive strips"
print "possible swap-borders in this state", a.Possiblechildren

# DEMO 
parent = a
possible_swaps = parent.Possiblechildren
for swap in possible_swaps:
	child = parent.Swap(swap)
	child_object = state_sequence(child, parent)
	if child_object.BPs == parent.BPs -2:
		print child_object.sequence

