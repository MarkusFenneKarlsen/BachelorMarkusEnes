from sample_graph import generate_graph;
from prims_modified import prims_modifed;
from steiner_tree import steiner_tree;
from mst_print import mst_print;
from steiner_print import steiner_print;

if __name__ == "__main__":
    graph = generate_graph()
    mst,sizeofA = prims_modifed(graph)
    mst_print(mst)
    steiner = steiner_tree(mst,sizeofA)
    steiner_print(steiner)


