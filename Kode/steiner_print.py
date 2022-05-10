import numpy as np;
from sample_graph import SampleGraph;


def steiner_print(Steiner):
    TotalWT = 0
    A2 = Steiner.A
    print(' ')
    print("Printing the edges of Steiner tree ...")
    for i in range(len(Steiner.Nodes)-1):
        for j in range(1,len(Steiner.Nodes)):
            if A2[i][j]: 
                wt = A2[i][j]
                print(f"Edge-{i+1}:{Steiner.Nodes[i]}-{Steiner.Nodes[j]}    Wt: {wt}")
                TotalWT += wt

           

    print(f"Total Weight: {TotalWT}")