# GUI testfile for Drosophila exercise
# Author: Riaan Zoetmulder

# import library

import time
from Tkinter import *



#reinit the list
def initlist(melanogaster):
    
    w.after(0, w.delete("rectangles"))

    for i in range(0,25): # 10 here can be substituted by the number of numbers.
        color = "#"
        hexadecimal = str(hex(int((15* melanogaster[i])/25)))
        hexadecimal_edited = (3 * hexadecimal[2:])
    
        color = color+hexadecimal_edited

        w.create_rectangle(100 + i * 1000/25, 300, 200 + i*1000/25, 400,fill = color , tags = "rectangles")
    w.update()
    swapscounter = "swaps =",  swaps
    var.set(swapscounter)
    master.update_idletasks()
    time.sleep(.5)
    
def action():
    b.pack_forget()
    swap(melanogaster)
    
    

def swap(melanogaster):
    global swaps
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
            initlist(melanogaster)
            

                
        print melanogaster
        print "swaps = ", swaps
        initlist(melanogaster)
        
               

   


# define list
melanogaster = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]

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

# non-functional button
b = Button(master, text="Start", command=action)
b.pack()


mainloop()



