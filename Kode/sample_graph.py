#     I   J   K   L   M   N   O   P    Q
from xml.dom.minicompat import NodeList




class SampleGraph:
    def __init__(self,Nodes,A,Terminals):
        self.Nodes = Nodes
        self.A = A
        self.Terminals = Terminals

def generate_graph() -> SampleGraph:
    A = [[0,  5,  0,  0,  0,  0,  0,  10,  0], #I
     [5,  0,  6,  0,  0,  0,  0,  10,  0], #J
     [0,  6,  0,  6,  0,  8,  0,  0,   8], #K
     [0,  0,  6,  0,  8,  12, 0,  0,   0], #L
     [0,  0,  0,  8,  0,  12, 0,  0,   0], #M
     [0,  0,  8,  12, 12, 0,  4,  0,   0], #N
     [0,  0,  0,  0,  0,  4,  0,  4,   9], #O
     [10, 10, 0,  0,  0,  0,  4,  0,   8], #P
     [0,  0,  8,  0,  0,  0,  9,  8,   0]] #Q

    for i in range(ord("I"),ord("Q")):
        print(i)


if __name__ == "__main__":
    generate_graph()
    
