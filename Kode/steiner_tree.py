import numpy as np

def steiner_tree(mst,sizeA):
    Terminals = mst.Terminals 
    nodes = mst.Nodes
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
    sizeA2 = (sizeA,sizeA)
    A2 = np.zeros(sizeA2,dtype=int)
    for i in range(edgesOfMST):
        A2[A[0][i], A[1][i]] = A[2][i]
        A2[A[1][i], A[0][i]] = A[2][i]
    Iterations_Complete = False
    while not Iterations_Complete:
        Iterations_Complete = True
        for i in range(len(nodes)):
            if not np.isin(i, terminal_indices):
                edgesOfi = A2[i][:]
                no_connections = sum(edgesOfi > 0)
                if np.array_equal(no_connections,1):
                    j = np.where(edgesOfi != 0)[0][0]
                    A2[i][j] = 0
                    A2[j][i] = 0
                    Iterations_Complete = False
    return A2

