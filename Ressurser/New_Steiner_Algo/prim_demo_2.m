% Minimum-Spanning-Tree with Prim's algorithm 
% Example: 
%
%    Reggie.Davidrajuh@uis.no  (c) August 2011

clear all; clc;

global global_info;
global_info.debug_mode = true;  % turn this ON for intermediate results

% 1: Adjacency matrix A
%    r  s  t  u  v  w  x  y  
A = [0  6  0  0  14 0  0  0;...  %r
     6  0  0  0  0  3  0  0;... %s
     0  0  0  6  0  10 7  0;...  %t
     0  0  6  0  0  0  9  8;...  %u
     14 0  0  0  0  0  0  0;...  %v
     0  3  10 0  0  0  1  0;...  %w
     0  0  7  9  0  1  0  2;...  %x
     0  0  0  8  0  0  2  0];... %y

% 2: Nodes
nodes = [];
for i = double('r'):double('y'),
    nodeI.name = char(ceil(i)); % 'r' -> 'y'
    nodes = [nodes nodeI]; 
end;

% 3: Graph
G.nodes = nodes;
G.A = A;

% 4: call prim
p2 = prim(G); 

% 5: print results
mst_print(p2);

