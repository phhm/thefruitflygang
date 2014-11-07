# attempt 2: Fruitfly
# modification : merge type sort

# libraries
import random

# create list melanogaster

print "THIS PROGRAM CALCULATES THE NUMBER OF DNA SWAPS NECESSARY"
use_own_list = raw_input ("Would you like to use your own list of random numbers?: ")

if use_own_list == "y":
    listsize = 0
    while listsize <= 0:
        listsize = input("How large is your DNA sequence (list): " )
    
    melanogaster = [i for i in range(1, listsize + 1)]
    random.shuffle(melanogaster)


else:
    melanogaster = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]

    

def swap(melanogaster):
    swaps = 0
    sorted_melanogaster = sorted(melanogaster)
    
    # while list is unsorted, execute.
    while sorted_melanogaster != melanogaster:

        print melanogaster
                       
        # if swaps is divisible by 2, swap from beginning
        for i in range(0, len(melanogaster)):
            
            # check if melanogaster is unsorted from the beginning          
            if melanogaster[i] != i + 1 and (swaps % 2 == 0 or swaps == 0):

                # variables for location current number, temporary list storage, and reversed list
                location = melanogaster.index(i+1)
                temlist = []
                reversetemlist = []
                       
                # from point number is in wrong place, create list untill proper value found
                for j in range(i, location + 1):
                    temlist.append(melanogaster[j])
                       
                # reverse temporary list
                for k in reversed(temlist):
                    reversetemlist.append(k)

                # replace values in melanogaster with reversed sequence
                indexx = 0
                for l in range (len(temlist)):
                    melanogaster[i+l] = reversetemlist[indexx]
                    indexx += 1

                swaps += 1
                print melanogaster
                break
        
        for m in range(len(melanogaster), 0, -1):
            # check if melanogaster is unsorted at the end
            
            if melanogaster[m - 1] != m and swaps % 2 != 0:
                
                # variables for location current number, temporary list storage, and reversed list
                location = melanogaster.index(m)
                temlist = []
                reversetemlist = []
                       
                # from point number is in wrong place, create list untill proper value found
                for j in range(location, m):
                    temlist.append(melanogaster[j])
                
                # reverse temporary list
                for k in reversed(temlist):
                    reversetemlist.append(k)
                

                # replace values in melanogaster with reversed sequence
                indexx = 0
                for l in range (len(temlist)):
                    melanogaster[location + l] = reversetemlist[indexx]
                    indexx += 1
                print melanogaster
                swaps += 1
                break
        
    print "swaps = ", swaps
swap(melanogaster)

