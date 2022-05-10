import numpy as np;
import random as rand;
from check_overlap import check_overlap;

def rand_adjacency_matrix(Range,Weight,NodeCount,TerminalCount):
    #Generate an empty matrix of the correct size
    A = np.zeros((NodeCount,NodeCount),dtype=int)
    #Generate the correct amount of edges for each node, 
    #within the correct range, the sum of these numbers 
    #have to be even
    nodedict = {}
    nodesum = 0
    for i in range(NodeCount):
        randomNumber = rand.randint(Range[0],Range[1])
        nodedict[i] = randomNumber
        nodesum += randomNumber
    if nodesum % 2 != 0: 
        for i in range(NodeCount):
            if nodedict[i] != Range[0]:
                nodedict[i] -=1
                nodesum -=1
    #Start connecting nodes together, starting from the highest,
    #until no more nodes can be connected
    connectedNodes = set()
    while(True):
        highestValue = 0
        highestValIndex = 0
        for i in range(NodeCount):
            if nodedict[i] > highestValue:
                highestValue = nodedict[i]
                highestValIndex = i
        
        randrange = [*range(NodeCount)]
        randrange.remove(highestValIndex)
        for i in range(NodeCount):
            if (highestValIndex,i) in connectedNodes or (i,highestValIndex) in connectedNodes:
                randrange.remove(i)
                print(f"removed {i}, because {highestValIndex,i} already exists")
            if nodedict[i] == 0 and i in randrange:
                randrange.remove(i)
                print(f"removed {i} because it cant have any more connected nodes")
        print(randrange)

        if(len(randrange) == 0): 
            break
        randnode = rand.choice(randrange)
        A[highestValIndex][randnode] = 1
        A[randnode][highestValIndex] = 1
        connectedNodes.add((highestValIndex,randnode))
        nodedict[highestValIndex] -=1
        nodedict[randnode] -=1
        nodesum -=2
        print(connectedNodes)
        if nodesum == 0:
            break
    print(A)
    print(nodedict)
    print(nodesum)
    print(check_overlap(A,NodeCount))
    
