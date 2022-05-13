import numpy as np;
from sample_graph import SampleGraph;


def steiner_print(Steiner):
    TotalWT = 0
    A2 = Steiner.A
    print(' ')
    print("Printing the edges of Steiner tree ...")
    print(f"Terminal nodes: {Steiner.Terminals}")
    for i in range(len(Steiner.Nodes)-1):
        for j in range(i+1,len(Steiner.Nodes)):
            if A2[i][j]: 
                wt = A2[i][j]
                print(f"Edge-{i}:{Steiner.Nodes[i]}-{Steiner.Nodes[j]}    Wt: {wt}")
                TotalWT += wt

           

    print(f"Total Weight: {TotalWT}")