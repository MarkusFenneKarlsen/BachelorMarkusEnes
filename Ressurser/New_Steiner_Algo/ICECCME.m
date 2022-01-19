% Minimum-Spanning-Tree with Prim's algorithm 
% Example for the conference ICARTI, 2021
%    Reggie.Davidrajuh@uis.no (c) June 2021

clear all; clc;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% get an example
G = sample_graph();


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% call the function prim_modified
G = prim_modified(G);
mst_print(G);  % print the result of prim_modified


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% call the function for iterative Steiner node elimination
G = steiner_tree(G);
steiner_print(G); % print the results

    



    




       
