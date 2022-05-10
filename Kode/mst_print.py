import numpy as np;
from sample_graph import SampleGraph;

def mst_print(MST):
    print("Printing the MST with the vertices and edges:")
    TotalWT = 0
    for i in range(len(MST.Nodes)-1):
        mst = MST.A[:][i]
        u = mst[0]
        v = mst[1]
        wt = mst[2]
        TotalWT += wt
        print(f"Edge-{i}: {MST.Nodes[u]}-{MST.Nodes[v]} Wt:{wt}")
    print(f"Total Weight: {TotalWT}")
