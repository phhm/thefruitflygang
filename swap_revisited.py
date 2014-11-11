# Swap function revisited using reversed

List = [4, 5, 6, 8, 2, 3, 1, 7]

left_border = 6
right_border = 3
i = List.index(left_border)
j = List.index(right_border)

templist = []

for number in reversed(List[i:j+1]):
	templist.append(number)

print List[:i] + templist + List[j+1:]

