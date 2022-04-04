import numpy as np;
from sample_graph import SampleGraph;

def prims_modifed(graph):
    A = graph.A
    nodes = graph.Nodes
    T = graph.Terminals
    #N_Terminals  = len(T)
    #using numpy.zeros library for python equivalent of MATLAB zeros 
    #Z = np.zeros([1,N_Terminals], dtype=int)
    m = np.size(A,axis=0)
    n = np.size(A,axis=1)
    #MATLAB matrix strats at 1, while python matrix starts at 0
    for i in range(0,m):
        for j in range(0,n):
            if not A[i][j]: A[i][j] = np.inf
    No_of_vertices = len(nodes)
    tree_vertices = [1]
    MST = []

    #add one vertice at a time to "tree_verices"
    while len(tree_vertices) < No_of_vertices:
        minWeight = np.Inf
        #from all the vertices in the tree, search for minimum edge
        for i in range(len(tree_vertices)):
            minU = tree_vertices[i]
            #exists no equivalent command for the MATLAB "min" that returns both value and index
            #use for loop instead
            minwt = A[minU][0]
            minV = 0
            
            for i,el in enumerate(A[minU][:]):
                if el < minwt:
                    minwt = el
                    minV = i
                    

            if minwt < minWeight and not np.isin(minV, tree_vertices):
                minWeight = minwt
                v = minV 
                u = minU
        #when a minimum is found 
        A[u][v] = np.inf
        A[v][u] = np.inf #mark edges as visited
        tree_vertices.append(v)
        #nodes[v].pi = u ##Unsure of application for this line
        if len(MST) != 0:
            MST = np.column_stack((MST, [u,v,minWeight]))
        else:
            MST = [u,v,minWeight]

            
    return SampleGraph(nodes, MST, T) , len(A)
