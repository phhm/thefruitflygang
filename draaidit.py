import math
import random
import Queue
import time

Melanogaster = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]

easy = [3,4,7,6,2,5,1]


class Sequence(object):
    def __init__(self, sequence, parent=None):
        self.parent = parent
        self.sequence = sequence
        self.max = max(sequence)
        self.min = min(sequence)
        self.length = len(sequence)
        self.goal = range(self.min, self.max + 1)
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
        self.dist = self.GetDist()

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

    def unique(self, list_of_states):
        if tuple(self.sequence) in list_of_states:
            if self.depth <= list_of_states[tuple(self.sequence)]:
                list_of_states[tuple(self.sequence)] = self.depth
                return True, list_of_states
            else:
                return False, list_of_states

        list_of_states[tuple(self.sequence)] = self.depth
        return True, list_of_states

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

    def GetDist(self):
        return math.ceil(self.BPs/2) + self.depth


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
        number = 1
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

        print len(dictionary[min(dictionary)]), "first dictionary value"
        print len(dictionary[min(dictionary) + 1]), "second dictionary value"


        minimum = min(dictionary)
        maximum = max(dictionary)

        for key in range(minimum+number+1, maximum +1):
            dictionary.pop(key, None)

    # x = 1
    # length = len(dictionary[0])
    # for i in range(0,length):
    #   print "Path:", x, ":", dictionary[0][i].path
    #   x += 1


    a= dictionary[0][0]

    history = []
    while a != None:
        history.append(a)
        a = a.parent

    history = history[::-1]

    for e in history:
        print e.sequence, "depth: ",e.depth

def A_Star_restriction(Melanogaster):
    start = Sequence(Melanogaster)

    dictionary = {}
    dictionary2 = {}
    list_of_states = {}

    for swap in start.PossibleChildren:
        child = start.Swap(swap)
        child = Sequence(child, start)

        if child.dist in dictionary:
            dictionary[child.dist].append(child)
        else:
            dictionary[child.dist] = [child] 

    while True:
        goal = False
        number = 0
        minimum = min(dictionary)
        maximum = max(dictionary)

        dictionary2 = {}


        for state in dictionary[min(dictionary)]:
            if state.sequence == state.goal:
                goal = True

        if goal == True:
            break

        for key in dictionary:
            for value in dictionary[key]:
                parent = value
                for swap in parent.PossibleChildren:
                    child = parent.Swap(swap)
                    child = Sequence(child, parent)
                    if child.dist in dictionary2:
                        if child.dist <= min(dictionary2) + number:
                            dictionary2[child.dist].append(child)
                    else:
                        dictionary2[child.dist] = [child]

        for key in dictionary2:
            for value in dictionary2[key]:
                if value.dist in dictionary:
                    dictionary[value.dist].append(value)
                else:
                    dictionary[value.dist] = [value]    

        minimum = min(dictionary)
        maximum = max(dictionary)

        for key in range(int(minimum+number+1), int(maximum +1)):
            dictionary.pop(key, None)


    solution = []
    for state in dictionary[min(dictionary)]:
        if state.sequence == state.goal:
            solution.append(state)

    print len(solution)
    a = solution[0]

    history = []
    while a != None:
        history.append(a)
        a = a.parent

    history = history[::-1]

    depth_counter = 0
    for e in history:
        print e.sequence, "depth: ",depth_counter
        depth_counter += 1

def breadthFirst(genome):
    """
    Breadth first search algorithm, guaranteed to find optimal solution (minimum moves).
    """
    start = Sequence(genome)
    list_of_states = {}
    queue = Queue.Queue()
    queue.put(start)

    while True:
 
        parent = queue.get()
        for swap in parent.PossibleChildren:
            child = parent.Swap(swap)
            child = Sequence(child, parent)

            if child.sequence == child.goal:
                history = []
                while child != None:
                    history.append(child)
                    child = child.parent

                history = history[::-1]

                for element in history:
                    print element.sequence, "depth: ", element.depth
                return
            boolean, list_of_states =  child.unique(list_of_states)

            if boolean and child.BPs < parent.BPs:
                queue.put(child)

def Greedy(genome):
    start = Sequence(genome)
    parent = start
    list_of_states = {}

    while True:
        print parent.sequence
        if parent.sequence == parent.goal:
            break
        child_min2 = []
        child_min1 = []
        for swap in parent.PossibleChildren:
            child = parent.Swap(swap)
            child = Sequence(child, parent)

            if child.BPs == parent.BPs - 2:
                child_min2.append(child)

            if child.BPs == parent.BPs - 1:
                child_min1.append(child)

        if len(child_min2) != 0:
            boolean, list_of_states = child_min2[0].unique(list_of_states)
            if boolean:
                parent = child_min2[0]
        elif len(child_min2) == 0 and len(child_min1) != 0:
            boolean, list_of_states = child_min1[0].unique(list_of_states)
            if boolean:
                parent = child_min1[0]
        elif len(child_min2) ==0 and len(child_min1) == 0: 
            neg_strips, pos_strips = child.Strips_pos_or_neg()
            i = pos_strips[0][0]
            j = pos_strips[0][-1]
            i = parent.sequence.index(i)
            j = parent.sequence.index(j)
            print (i,j)
            next_parent = parent.Swap((i,j))
            boolean, list_of_states = Sequence(next_parent,parent).unique(list_of_states)
            if boolean:
                parent = Sequence(next_parent,parent)

def Beamsearch2(Melanogaster, uppervalue, number):
    start_time = time.time()
    start = Sequence(Melanogaster)
    # uppervalue = 2000
    dictionary = {}
    dictionary2 = {}
    list_of_states = {}
    

    for swap in start.PossibleChildren:
        child = start.Swap(swap)
        child = Sequence(child, start)

        if child.BPs in dictionary:
            dictionary[child.BPs].append(child)
        else:
            dictionary[child.BPs] = [child] 
    
    while True:
        # number = 2
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

                    boolean, list_of_states = child.unique(list_of_states)

                    if boolean:

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


        dictionary3 = {}
        residue = uppervalue
        while True:
            for key in dictionary:
                length = len(dictionary[key])

                if length <= residue:
                    residue -= length
                    dictionary3[key] = dictionary[key]
                    if residue == 0:
                        break

                else:
                    randomlist = random.sample(dictionary[key], residue)
                    dictionary3[key] = randomlist
                    break
            break

        dictionary = dictionary3


        counter = 0
        for key in dictionary:
            for value in dictionary[key]:
                counter += 1
        print counter


    a= dictionary[0][0]
    print len(dictionary[0])
    print len(list_of_states)
    history = []
    while a != None:
        history.append(a)
        a = a.parent

    history = history[::-1]

    for e in history:
        print e.sequence, "depth: ",e.depth

    answers = []
    for value in dictionary[0]:
        if value.path not in answers:
            answers.append(value.path)
    print len(dictionary[0])
    print len(answers)

    print "-----------duplicates???!------------"
    a = len(dictionary[0]) - len(answers)
    if len(answers) < len(dictionary[0]):
        print "duplicate found :'("
        print "this many duplicates were found: ", a
    else:
        print "hooray, no duplicates :D"

    delta_time = time.time() - start_time
    return str(number) + "," + str(uppervalue) + "," + str(len(answers)) + "," + str(delta_time) + '\n'


uppervalue = 50
number = 1
text_file = open("resultaten.txt", 'a')
while True:
    for i in range (1, 3+ 1):
        for j in range(50, 700 + 1, 50):
            number = i
            uppervalue = j
            text_file.write(Beamsearch2(Melanogaster,uppervalue,number))
    text_file.close()
    break

