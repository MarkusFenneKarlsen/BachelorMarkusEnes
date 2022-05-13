from sample_graph import generate_graph;
from prims_modified import prims_modifed;
from steiner_tree import steiner_tree;
from mst_print import mst_print;
from steiner_print import steiner_print;
from random_adjacency_matrix import rand_adjacency_matrix;

if __name__ == "__main__":
    """ Range = (2,3)
    Weight = (5,30)
    NodeCount = 20
    TerminalCount = 6 
    graph = rand_adjacency_matrix(Range,Weight,NodeCount,TerminalCount)
    print(graph.A) """
    graph = generate_graph()
    mst,sizeofA = prims_modifed(graph)
    for i in range(len(graph.A)):
        print(" ")
        print(graph.A[i])
    for i in range(len(mst.A)):
        print(" ")
        print(mst.A[i])
    mst_print(mst)
    steiner = steiner_tree(mst,sizeofA)
    steiner_print(steiner)
    print(steiner.A)


