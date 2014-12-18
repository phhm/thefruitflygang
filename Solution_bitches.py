Melanogaster = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]

sorted_Melanogaster = sorted(Melanogaster)

class Sequence(object):
	def __init__(self, sequence, parent=None):
		self.parent = parent
		self.sequence = sequence
		self.max = max(sequence)
		self.min = min(sequence)
		self.length = len(sequence)
		self.goal = sorted_Melanogaster
		self.breakpoints, self.BPs = self.Breakpoints()
		self.strips = self.Strips()
		self.PossibleChildren = self.PossibleSwaps()

		if parent:
			self.path = parent.path[:]
			self.path.append(sequence)
			self.depth = parent.depth + 1
		else:
			self.path = [sequence]
			self.depth = 0


	def Swap(self,(i,j)):
		if i < j:
		    return self.sequence[:i] + [element for element in reversed(self.sequence[i:j + 1])] + self.sequence[j + 1:]
		else:
		    return self.sequence[:j] + [element for element in reversed(self.sequence[j:i + 1])] + self.sequence[i + 1:]

	def Breakpoints(self):
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

		return Breakpoints, len(Breakpoints)

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

	def PossibleSwaps(self):
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

def Beamsearch(Melanogaster):
	start = Sequence(Melanogaster)

	dictionary = {}
	dictionary2 = {}
	

	for swap in start.PossibleChildren:
		child = start.Swap(swap)
		child = Sequence(child, start)

		if child.BPs in dictionary:
			dictionary[child.BPs].append(child)
		else:
			dictionary[child.BPs] = [child] 
	
	while True:
		number = 0
		minimum = min(dictionary)
		maximum = max(dictionary)
		if minimum == 0:
			break

		print minimum,maximum

		for key in dictionary:
			answer_list = []
			for value in dictionary[key]:
				parent = value
				for swap in parent.PossibleChildren:
					child = parent.Swap(swap)
					child = Sequence(child,parent)

					if child.BPs in dictionary2:
						if child.BPs <= min(dictionary2) + number:
							if child.path not in answer_list:
								dictionary2[child.BPs].append(child)
								answer_list.append(child.path)
					else:
						dictionary2[child.BPs] = [child]
				

		for key in dictionary2:
			for value in dictionary2[key]:
				BPs = value.BPs
				if BPs in dictionary:
					dictionary[BPs].append(value)
				else:
					dictionary[BPs] = [value]	

		minimum = min(dictionary)
		maximum = max(dictionary)

		for key in range(minimum+number+1, maximum +1):
			dictionary.pop(key, None)

	# x = 1
	# length = len(dictionary[0])
	# for i in range(0,length):
	# 	print "Path:", x, ":", dictionary[0][i].path
	# 	x += 1


	a= dictionary[0][0]

	history = []
	while a != None:
	    history.append(a)
	    a = a.parent

	history = history[::-1]

	for e in history:
		print e.sequence, "depth: ",e.depth
	

Beamsearch(Melanogaster)
