BAD DRAFT FOR RANDOM MATRIX
Psuedokode for adjacency matrix: 
1: Set user specified parameters:
    -MinRange
    -MaxRange
    -MinWeight
    -MaxWeight
    -NodeCount/Size
    -Terminal_count
    (Randomness_weighting_type:Binomial, low-weighted, high-weighted) -usikker 

2: Generate square matrix of zeroes with the specified size
    use numpy zeroes function 
    Adjacency matrixes are always square, and always symmetrical -
        meaning matrix[i][j] = matrix[j][i]
    If an adjacency matrix doesnt connect to itself, which it never should in praxis, 
        then matrix[i][i] == 0, for any i
3: Generate a random number for each node, in the range MinRange-MaxRange
    - if the sum of all numbers is odd:
        * +1 to the first node that is not already at MaxWeight
        OR
        * -1 to the first node that is not already at MinWeight 
    
4: Find the highest number, find another random node
    -make sure the nodes arent already conneceted
    - -1 to both nodes , these are now connected:
    -example: Node1-Node5, Node3-Node4, Node5-Node4 
    - keep going until all node numbers are 0

ISSUES:
    -There could be issues with connectivity on the last connections, if this occures
        *dont connect the last nodes:
        *issues with nodes falling out of MinWeight range should be negated by always connecting  
            from the highest count nodes first