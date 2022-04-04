from sample_graph import generate_graph;
from prims_modified import prims_modifed;
from steiner_tree import steiner_tree;

if __name__ == "__main__":
    graph = generate_graph()
    mst,sizeofA = prims_modifed(graph)
    steiner = steiner_tree(mst,sizeofA)


