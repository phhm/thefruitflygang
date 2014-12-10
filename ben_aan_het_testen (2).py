Melanogaster = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
l = [[13,14,15,16], [3,4]]
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
		print a,b
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


print update(l,Melanogaster)



