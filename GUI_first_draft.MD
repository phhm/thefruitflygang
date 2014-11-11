# GUI testfile for Drosophila exercise
# Author: Riaan Zoetmulder



import time
import random

# Import Tkinter library
from Tkinter import *



#reinit the list
def initlist(melanogaster, reversetemlist):
    
    w.after(0, w.delete("rectangles", "swaptangle", "text"))
   

    for i in range(0,len(melanogaster)): # 10 here can be substituted by the number of numbers.
        color = "#"
        hexadecimal = str(hex(int((15* melanogaster[i])/len(melanogaster))))
        hexadecimal_edited = (3 * hexadecimal[2:])
    
        color = color+hexadecimal_edited

        w.create_rectangle(100 + i * 1000/len(melanogaster), 300, 200 + i*1000/len(melanogaster), 400,fill = color , tags = "rectangles")
        w.create_text(120 + i *1000/len(melanogaster), 350, fill = "red", text = melanogaster[i], tags = "text")
    swapscounter = "swaps =",  swaps
    var.set(swapscounter)


def initchecker(reversetemlist, melanogaster, location, front):
    if front is True:
        location = location - len(reversetemlist) + 1 

    for j in range (0, len(reversetemlist)):
        color = "#"
        hexadecimal = str(hex(int((15* reversetemlist[j])/len(melanogaster))))
        hexadecimal_edited = (3*  hexadecimal[2:] )
        color = color+hexadecimal_edited
        w.create_rectangle(100 +(location*1000/len(melanogaster))  + j * 1000/len(melanogaster), 400, 200 +(location*1000/len(melanogaster))+ j*1000/len(melanogaster), 500 ,fill = color , tags = "rectangles", outline= "green", width = 5)
    
    master.update_idletasks()
    time.sleep(.2)
    
    
    
def action():
    # remove button
    b.pack_forget()
    b2.pack_forget()

    # activate swap
    swap(melanogaster)

def action2():
    # remove button
    b2.pack_forget()
    b.pack_forget()

    # activate mergesort
    mergesort(melanogaster)
    
def calc_absolute(melanogaster):
    sorted_melanogaster = sorted(melanogaster)
    absolute_number = []
    for k in range(0, len(melanogaster)):
        absolute_number.append[k] = sorted_melanogaster
        w.create_text(120 + k *1000/len(melanogaster), 250, fill = "blue", text = melanogaster[i], tags = "text")

def swap(melanogaster):
    global swaps
    swaps = 0
    sorted_melanogaster = sorted(melanogaster)
    # while list is unsorted, execute.
    while sorted_melanogaster != melanogaster:
        
        location = 0
        front = True

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
                initchecker(reversetemlist, melanogaster, location, front)
                
                
                indexx = 0
                for l in range (len(temlist)):
                    melanogaster[i+l] = reversetemlist[indexx]
                    indexx += 1
                swaps += 1
                initlist(melanogaster, reversetemlist)
            
            
            

                
        print melanogaster
        print "swaps = ", swaps
        initlist(melanogaster, reversetemlist)

def mergesort(melanogaster):
    global swaps
    global front
    
    swaps = 0
    sorted_melanogaster = sorted(melanogaster)
    
    # while list is unsorted, execute.
    while sorted_melanogaster != melanogaster:

        print melanogaster
                       
        # if swaps is divisible by 2, swap from beginning
        for i in range(0, len(melanogaster)):
            
            # check if melanogaster is unsorted from the beginning          
            if melanogaster[i] != i + 1 and (swaps % 2 == 0 or swaps == 0):
                front = True 
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
                initchecker(reversetemlist, melanogaster, location, front)

                # replace values in melanogaster with reversed sequence
                indexx = 0
                for l in range (len(temlist)):
                    melanogaster[i+l] = reversetemlist[indexx]
                    indexx += 1

                swaps += 1
                print melanogaster
                initlist(melanogaster, stemlist)
                break
        
        for m in range(len(melanogaster), 0, -1):
            # check if melanogaster is unsorted at the end
            
            if melanogaster[m - 1] != m and swaps % 2 != 0:
                front = False
                
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
                initchecker(reversetemlist, melanogaster, location, front)
                

                # replace values in melanogaster with reversed sequence
                indexx = 0
                for l in range (len(temlist)):
                    melanogaster[location + l] = reversetemlist[indexx]
                    indexx += 1
                print melanogaster
                swaps += 1
                initlist(melanogaster, temlist)
                break
    print "swaps = ", swaps
        
               

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
b = Button(master, text="Brute force", command=action)
b.pack()
b2 = Button(master, text= "Merge sort", command = action2)
b2.pack()


mainloop()


