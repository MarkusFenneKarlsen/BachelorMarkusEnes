import numpy as np;
import random as rand;
from sample_graph import SampleGraph;
from check_overlap import check_overlap;

def rand_adjacency_matrix(Range,Weight,NodeCount,TerminalCount):
    #Generate an empty matrix of the correct size
    A = np.zeros((NodeCount,NodeCount),dtype=int)
    #A = A.tolist()
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
            if nodedict[i] == 0 and i in randrange:
                randrange.remove(i)
        if(len(randrange) == 0): 
            break
        randnode = rand.choice(randrange)
        A[highestValIndex][randnode] = -1
        A[randnode][highestValIndex] = -1
        connectedNodes.add((highestValIndex,randnode))
        nodedict[highestValIndex] -=1
        nodedict[randnode] -=1
    if not check_overlap(A,NodeCount):
        try:
            print("Invalid matrix, trying again") 
            return rand_adjacency_matrix(Range,Weight,NodeCount,TerminalCount)
        except RecursionError:
            print("Unable to generate a fully connected adjacency with the chosen parameters, try increasing the max Range or lovering the nodecount")
            quit()
    else: 
        for i in range(NodeCount):
            for j in range(NodeCount):
                if A[i][j] == -1:
                    A[i][j] = rand.randint(Weight[0],Weight[1])
                    A[j][i] = A[j][i]
    nodes = []
    TerminalNodes = []
    for i in range(NodeCount): 
        nodes.append(str(i))
    tempnodes = nodes.copy()
    for i in range(TerminalCount):
        randTerminal = rand.choice(tempnodes)
        TerminalNodes.append(randTerminal)
        tempnodes.remove(randTerminal)
    return(SampleGraph(nodes,A,TerminalNodes))
        