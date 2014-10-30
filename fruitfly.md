thefruitflygang
===============

# attempt 1: Fruitfly

# create list melanogaster

melanogaster = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
print melanogaster

def swap(melanogaster):
    swaps = 0
    # while list is unsorted, execute.
    while (sorted(melanogaster) != melanogaster):
        location = 0

        # check if values corresond to absolute values
        for i in range(0, 25):
             
            if melanogaster[i] != i + 1:
               location = melanogaster.index(i+1)
               temlist = []
               reversetemlist = []

               for j in range(i, location + 1):
                   temlist.append(melanogaster[j])

               for l in reversed(temlist):
                   reversetemlist.append(l)

               indexx = 0
               for k in range (len(temlist)):
                    melanogaster[i+k] = reversetemlist[indexx]
                    indexx += 1
               swaps += 1

                    
    print melanogaster
    print "swaps = ", swaps
swap(melanogaster)
