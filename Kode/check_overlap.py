import numpy as np;

def check_overlap(matrix, NodeCount) -> bool:
    nodedict = {}
    for i in range(NodeCount):
        nodedict[i] = []
        for j in range(NodeCount):
            if matrix[i][j] != 0 :
                nodedict[i] += [j] 

    connected = nodedict[0]
    i = 0
    lastentry = 0
    comptletedLoops = 0
    while(True):
        i += 1
        for j in range(len(nodedict[i])):
            if nodedict[i][j] in connected:
                print(f"j: {nodedict[i][j]} exists in {nodedict[i]} and {connected}, therefore, append")
                connected.extend(nodedict[i])
                connected.append(i)
                lastentry = i
                break 
        connected = list( dict.fromkeys(connected))
        print(connected)
        print(f"index: {i}, lastentry: {lastentry}")
        if i == lastentry and comptletedLoops >1:
            return False 
        if lastentry==0 and i == NodeCount-1:
            return False 
        for j in range(NodeCount):
            if j not in connected:
                break 
            if j == NodeCount-1 and j in connected:
                print(f"value of j: {j}")
                return True     
        if i == NodeCount-1:
            i = 1
            comptletedLoops+=1
        print(f"index: {i}")
    