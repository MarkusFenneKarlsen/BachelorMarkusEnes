% Minimum-Spanning-Tree with Prim's algorithm 
% Example: Cormen et al, fig.23.5, p.635
%
%    Reggie.Davidrajuh@uis.no  (c) August 2011

clear all; clc;

global global_info;
global_info.debug_mode = true;  % turn this ON for intermediate results

% 1: Adjacency matrix
%    a  b  c  d  e  f  g  h  i
A = [0  4  0  0  0  0  0  8  0; ...  %a
     4  0  8  0  0  0  0  11 0;...   %b
     0  8  0  7  0  4  0  0  2;...   %c
     0  0  7  0  9  14 0  0  0;...   %d
     0  0  0  9  0  10 0  0  0;...   %e
     0  0  4  14 10 0  2  0  0;...   %f
     0  0  0  0  0  2  0  1  6;...   %g
     8  11 0  0  0  0  1  0  7;...   %h
     0  0  2  0  0  0  6  7  0];...  %i     

% 2: nodes
nodes = [];
for i = double('a'):double('i')
    nodeI.name = char(ceil(i)); % 'a' -> 'i'
    nodes = [nodes nodeI]; 
end

% 3: Graph
G.nodes = nodes;
G.A = A;


% 4: call prim
p1 = prim(G);

% 5: print results
mst_print(p1);
       
