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

# to proof that is actually works:
List = [[1,2], [3,4,5,6], [9,8,7], [12,11,10], [13,14]]
a,b = Strips_pos_or_neg(List)
print a
print b