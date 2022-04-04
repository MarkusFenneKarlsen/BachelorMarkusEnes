import numpy as np

def steiner_tree(mst,sizeA):
    Terminals = mst.Terminals 
    nodes = mst.nodes
    A = mst.A
    no_of_terminals = len(Terminals)
    terminal_indices = []
    for i in range(no_of_terminals):
        for j in range(len(nodes)):
            t = Terminals[i]
            n = nodes[j]
            if t == n:
                terminal_indices.append(j)
                break
    edgesOfMST = np.size(A,axis=1)
    #feeding the entire original matrix into the steiner fuction in order to get its size-
    #is unesseccary, instead provide the length as an additional input to the function
    A2 = np.zeros(sizeA)
    for i in range(edgesOfMST):
       A2[A[i][1], A[i][2]] = A[i,3]
       A2[A[i][2], A[i][1]] = A[i,3]
    
    Iterations_Complete = False
    while not Iterations_Complete:
        Iterations_Complete = True
        for i in range(nodes):
            if not np.isin(i, terminal_indices):
                edgesOfi = A2[i][:]
                no_connections = sum(edgesOfi > 0)
            if np.array_equal(no_connections,1):
                pass
                #j = np.where(edgesOfi)
                #Linear indexing - need to find or make some alternate function

