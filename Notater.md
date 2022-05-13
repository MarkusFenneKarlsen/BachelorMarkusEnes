Prims algorithm: 

Start by importing the necessary libraries, in this case: numpy,sys,
and our custom Graph class SampleGraph

Set the necessary variables as easy to reach local variables 
In the given file a matrix of zeroes given by the number of terminals is defined, but this sees no use in the rest of the algoritm so we disregard. 

set the variables m and n to be the size of the matrix, in python this can be done in one function, but in python we use the numpy funciton size(), and along a specific axis, axis 0 being rows, and axis 1 being columns. 

do a nested for loop, with the range from 0-m in the outer loop and from 0-n in the inner loop. In matlab these for loops start at 1, but due to the indexing difference in python we instead start at 0. 

Then, if a given element of the graph A[i][j] is set to 0, we instead set it to infinite. In matlab there is a variable type named infinite, but this does not exist in python. We cant use numpys equivalent of infinite either, because this is a floating infinity type number, which cannot be converted into an integer. We instead set it to sys.maxsize, which is the highest possible integer python allows for, this number is so unrealistically high it is not going to cause problems for the algorithm. 

After we have our array of small and high integers, we define some new variables. We register the number of vertices, a starting list named tree vertice, and an empty array for our minimum spanning tree. 

We then enter a while loop, with the condition of: while the length of tree vertices is smaller than the number of vertices

In this loop we first set a new variable named minWeight to infinite, again, in our version of the algoritm we instead set it to sys.maxsize. Then, disregarding the MATLAB debugging code, we next enter a new for loop, from 0-length of tree vertices 

We next set a new variable named minU to be the value in the tree vertices list that corrosponds with the index of the for loop. We then use this variable as the row for the graph, and check for the smallest weight within the row, we then extract the weight and ints corrosponding column data. We now know the edge from the starting node minU with the smallest weight, and what other node it connects to. 
We then check if this edge is smaller than minWeight, and if it does not already exist in the tree vertices list. If these conditons are met, we set minWeight to be the new weight, and set u and v variables to be their min counterparts.   

In matlab it is possible to simply say "min(A(minU,:))" in order to get the minimum weight and minV variables, but in python we have to write a custom function, we simply set minwt and minV to be whatever the first corrosponding values within A[minU][0] is, after we have a starting value, we can compare the other weights to se if they are smaller or not, if they are then we replace the existing minwt and minV values. 

Next we mark whatever edge we found to be the smallest as visited, meaning we set the nodes value to be sys.maxsize. Then, we append v to the tree vertice list, meaning we now have a new row we can check for a minimum weight in. the MATLAB version also sets nodes(v).pi = v, but this sees no use so it is disregarded from the python implementation. 

Next we extend the Minimum spanning tree matrix with the values of u,v, and minWeight, with each set of variables forming a new row, meaning the first column holds the u values, the second colummn holds the v values, and the third column has their corrosponding weights. 
In the python version, things are a bit more complicated. This is because the first assignment has to set the structure of the matrix, and after this first assignment we can then stack the rest of the inputs under the first one. We also do a check to make sure the value of minWeight is not sys.maxsize, just in case some assignment issue occurs. This becomes more prevolent when working with randomly assigned adjacency matrix, as they may cause erratic or unpredictable behaviour.

This assignment continues until the while loop is over, at which point the finished minimum spanning tree is returned. In the matlab version this is done by assigning the MST to the input of the function V, in python we instead create a new SampleGraph class, containing the existing node names, and terminals, but now with a new graph. This is done for the sake of consistency, as well as making sure we can transfer the other properties of the existing graph into the future steps of the algorithm. 




STEINER ALGORITM: 

The steiner algoritm starts in much the same fashion, by setting the input variables as local variables. This time around we assign the list of terminals, the list of nodes, the number of terminals, and an empty list for the terminal indecies.

Then we enter a for nested for loop, from 0-number of terminals in the outer loop, and 0-length of nodes in the inner loop. We then assign t to the value of the terminals list that corrosponds with the index of the outer loop, and n to the value of the nodes list that corrosponds with the inner loop. We then compare the two variables, and if they match, the index of the inner loop is appended to the terminal indices list. Essentialy what this means is that we are finding the node indexes that corrospond with the given set of terminal nodes. These functions are pretty much the same in both python and MATLAB 

Next, we make a edges of MST variable, this is the size if the MST graph, along its first axis, in MATLAB this is 1, and in python its 0. 

We also make a matrix of zeroes named A2, which is the same size as the matrix we originally started with. In the matlab version, this is done by taking the size of the original graph, which was automatically imported, but in python we dont. Instead, we export the size of the graph from the prims_modified function, and import it as a variable. This makes it so that we dont have to import the entire matrix over, which would be unesseccary, because it is only used in this one circumstance. 

The next step is filling in the values from the mst graph, into the new empty A2 graph. The first and second column of the MST graph being the coordinates, and the third column being the value to insert. It is done twice per value, because this matrix is symmertric, meaning for any i,j, the values A[i][j] and A[j][i] are always the equal to each other. 

Now we have a graph that contains our extracted minimum spanning tree. The next step is to reduse it into a steiner tree. 

A variable called Iterations_Complete is set to false, we then make a while loop that runs so long as Iterations_Complete remains false. 

Inside the loop, we first set Iterations_Complete to True, then we enter a for loop from 0-Amount of nodes. 
We then check if the current index is not a terminal index, if it isnt, we check how many connections the node has. If the number of connections is only one, meaning the node is an end node, having no nodes relying on it to be a part of the tree, we then remove the node from the tree, and set Iterations_Complete back to false

This continues until there are no more nodes to remove, meaning we have completed the steiner tree, in a similar manor as in the prism algoritm, the python version returns an entire instance of the SampleGraph class. 

