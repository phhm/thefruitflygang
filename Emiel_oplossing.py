import time
import Queue

fruitfly = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]

easier = [23, 1, 2, 11, 22, 19, 6, 10, 7, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]

genome = [3, 9, 10, 12, 15, 11, 2, 1, 8, 7, 6, 4, 5, 13, 14]

easy = [5, 3, 4, 1, 2]

# Should convert genome to tuple
genome = tuple(genome)


class GenomeObject(object):
    def __init__(self, genome, parent, breakpoints):
        self.genome = genome
        self.parent = parent
        self.breakpoints = breakpoints
        
        if parent == None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1


class Brain(object):
    def __init__(self, genome):
        # Check if valid genome
        for i in genome:
            if i not in range(1, len(genome) + 1):
                raise ValueError
    
        self.dictionary = {}
        self.length = len(genome)
        self.min = min(genome)
        self.max = max(genome)
        
        # target genome
        self.target = tuple(range(self.min, self.max + 1))
    
    def getBreakpoints(self, genome, left, right):
        """
        Get breakpoints withit bounds
        """
        count = 2

        for i in xrange(left, right - 1):
            if genome[i] - genome[i + 1] < -1 or genome[i] - genome[i + 1] > 1:
                count += 1

        return count
    
    def getExactBreakpoints(self, genome):
        """
        Get breakpoints without bounds
        """
        count = 0
        
        if genome[0] != self.min:
            count += 1
    
        if genome[-1] != self.max:
            count += 1
        
        for i in xrange(0, self.length - 1):
            if genome[i] - genome[i + 1] < -1 or genome[i] - genome[i + 1] > 1:
                count += 1

        return count
    
    def futureMoves(self, genome):
        count = 0
        memory = 0
        
        if genome[0] != self.min:
            count += 1

        for i in xrange(self.length - 1):
            if genome[i] - genome[i + 1] < -1 or genome[i] - genome[i + 1] > 1:
                count += 1
    
                if i > 0:
                    # More of a guess than anything else. Seems to hold most of the time.
                    if genome[i] - genome[i - 1] == 1 and genome[i] != i + 1:
                        if genome[i] < memory:
                            count += 1
                
                        memory = genome[i]

        if genome[-1] != self.max:
            count += 1
            
            if genome[-1] - genome[-2] == 1:
                if genome[-1] < memory:
                    count += 1
        
        return (count + 1) / 2
    
    def reverse(self, genome, left, right):
        if left > 0:
            return genome[:left] + genome[right:left - 1:-1] + genome[right + 1:]

        else:
            return genome[:left] + genome[right::-1] + genome[right + 1:]

    def unique(self, genome, depth):
        if genome in self.dictionary:
            if depth < self.dictionary[genome]:
                self.dictionary[genome] = depth
                return True
            else:
                return False

        self.dictionary[genome] = depth
        return True

    def correct(self, genome):
        if genome == self.target:
            return True
        return False


def greedyAStar(genome):
    """
    A* algorithm that only excepts the best new mutations. All items are ordered in the same
    PriorityQueue.
    """
    brain = Brain(genome)
    object = GenomeObject(genome, None, brain.getBreakpoints(genome, 0, brain.length))
    
    queue = Queue.PriorityQueue()
    queue.put((0, object))
    
    while True:
        parent = queue.get()[1]
        candidates = []
        
        reduction = 0

        for i in xrange(brain.length - 1):
            for j in xrange(i + 1, brain.length):
            
                genome = brain.reverse(parent.genome, i, j)

                if brain.unique(genome, parent.depth + 1):
                    
                    breakpoints = brain.getBreakpoints(genome, 0, brain.length)
                    
                    if parent.breakpoints - breakpoints < reduction:
                        continue

                    if parent.breakpoints - breakpoints > reduction:
                        reduction = parent.breakpoints - breakpoints

                    object = GenomeObject(genome, parent, breakpoints)
                    candidates.append(object)
                    
                    if brain.correct(genome):
                        print "Moves:", object.depth
                        return object

        # Important: A* only improves performance due to "gut feeling" heuristic.
        for i in xrange(len(candidates)):
            if parent.breakpoints - candidates[i].breakpoints == reduction:
                queue.put((candidates[i].depth + brain.futureMoves(candidates[i].genome), candidates[i]))


def breadthFirst(genome):
    """
    Breadth first search algorithm, guaranteed to find optimal solution (minimum moves).
    """
    brain = Brain(genome)
    object = GenomeObject(genome, None, brain.getBreakpoints(genome, 0, brain.length))

    queue = Queue.Queue()
    queue.put(object)
    
    index = 0
    while True:
        parent = queue.get()
        
        left = 0
        while parent.genome[left] == left + 1:
            left += 1
            
        right = brain.length
        while parent.genome[right - 1] == right:
            right -= 1
        
        for i in xrange(left, brain.length):
            for j in xrange(i + 1, right):

                genome = brain.reverse(parent.genome, i, j)

                if brain.unique(genome, parent.depth + 1):
                    breakpoints = brain.getBreakpoints(genome, left, right)
                    
                    if breakpoints > parent.breakpoints:
                        continue
                    
                    object = GenomeObject(genome, parent, breakpoints)
                    queue.put(object)
                    
                    
                    if brain.correct(genome):
                        print "Moves:", object.depth
                        return object


def a_star(genome):
    """
    A* algorithm, but does NOT accept a worse mutation
    """
    brain = Brain(genome)
    object = GenomeObject(genome, None, brain.getBreakpoints(genome, 0, brain.length))

    queue = Queue.PriorityQueue()
    queue.put((0, object))
    
    while True:
        parent = queue.get()[1]
        
        left = 0
        while parent.genome[left] == left + 1:
            left += 1
            
        right = brain.length
        while parent.genome[right - 1] == right:
            right -= 1
    
    
        for i in xrange(left, right):
            for j in xrange(i + 1, right):

                genome = brain.reverse(parent.genome, i, j)

                if brain.unique(genome, parent.depth + 1):
                    breakpoints = brain.getBreakpoints(genome, left, right)
                    
                    # Reject worse mutation
                    if breakpoints > parent.breakpoints:
                        continue
                    
                    object = GenomeObject(genome, parent, breakpoints)
                

                    if brain.correct(genome):
                        print "Moves:", object.depth
                        return object
                
                    score = object.depth + brain.futureMoves(genome)
                    queue.put((score, object))


start = time.time()
object = a_star(genome)
print "Time:", time.time() - start

history = []
while object != None:
    history.append(object)
    object = object.parent

history = history[::-1]

for object in history:
    print object.genome

