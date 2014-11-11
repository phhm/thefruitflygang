# GUI testfile for Drosophila exercise
# Author: Riaan Zoetmulder



import time
import random

# Import Tkinter library
from Tkinter import *



#reinit the list
def initlist(melanogaster, temlist):
    
    w.after(0, w.delete("rectangles", "text", "swaptangle"))
 
    for i in range(0,len(melanogaster)): 
        color = "#"
        hexadecimal = str(hex(int((15* melanogaster[i])/len(melanogaster))))
        hexadecimal_edited = (3 * hexadecimal[2:])
    
        color = color+hexadecimal_edited

        w.create_rectangle(100 + i * 1000/len(melanogaster), 300, 200 + i*1000/len(melanogaster), 400,fill = color , tags = "rectangles")
        w.create_text(120 + i *1000/len(melanogaster), 350, fill = "red", text = melanogaster[i], tags = "text")
##        print melanogaster, "MELANO"
##        print temlist, "This is temlist"
##        print melanogaster[temlist[0]], "This is melanogaster temlist 0"

    print temlist
    print len(temlist)
    print melanogaster.index(temlist[0]), "MindexTemlist0"
    w.create_rectangle((100 + (1000/len(melanogaster)* (melanogaster.index(temlist[0]) - 1))), 300, 100 + (1000/len(melanogaster) * len(temlist)), 400, outline = "blue", tags = "swaptangle", width = 5)  
    swapscounter = "swaps =",  swaps
    var.set(swapscounter)
    master.update_idletasks()
    time.sleep(0.5)


def action():
    # remove button
    b.pack_forget()

    # activate swap
    swap(melanogaster)
    
    

def swap(melanogaster):
    global swaps
    global temlist
    swaps = 0
    sorted_melanogaster = sorted(melanogaster)
    # while list is unsorted, execute.
    while sorted_melanogaster != melanogaster:
        
        location = 0

        # check if values corresond to absolute values
        for i in range(0, len(melanogaster)):
            
            
            if melanogaster[i] != i + 1:
                print melanogaster
                location = melanogaster.index(i+1)
                temlist = []
                reversetemlist = []

                for j in range(i, location + 1):
                    temlist.append(melanogaster[j])
                for k in reversed(temlist):
                    reversetemlist.append(k)

                indexx = 0
                for l in range (len(temlist)):
                    melanogaster[i+l] = reversetemlist[indexx]
                    indexx += 1
                swaps += 1
            initlist(melanogaster, temlist)
            

                
        print melanogaster
        print "swaps = ", swaps
        initlist(melanogaster)
        
               

   


# define list
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
    #melanogaster = [22, 14, 2, 3, 21, 12, 20, 23, 13, 10, 1, 5, 16, 25, 17, 4, 18, 8, 19, 15, 24, 9, 7, 6, 11]

# make canvas pretty
master = Tk()
master.title("Drosophila DNA splicing machine")
w = Canvas(master, width=1200, height=600, background= "white")
w.pack()

# counter
var = StringVar()
var.set('0')
l= Label(master, textvariable = var)
l.pack()

# update canvas
w.update()

# functional button
b = Button(master, text="Start", command=action)
b.pack()


mainloop()
