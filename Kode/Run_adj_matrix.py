from random_adjacency_matrix import rand_adjacency_matrix;


#INSTRUCTIONS
#Range(start int,stop int): Amount of edges to randomly assign a given node
#Weight(start int,stop int): Value of assigned nodes
#Nodecount int: Total amount of nodes
#TerminalCount int: Amount of nodes to be assigned as terminals

if __name__ =="__main__":
    Range = (1,3)
    Weight = (5,20)
    NodeCount = 10
    TerminalCount = 4
    graph = rand_adjacency_matrix(Range,Weight,NodeCount,TerminalCount)
    print(graph.A)
    print(graph.Nodes)
    print(graph.Terminals)