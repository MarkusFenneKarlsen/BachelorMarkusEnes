% Minimum-Spanning-Tree with Prim's algorithm 
% Example: Special Example for ICARTI 
%
%    Reggie.Davidrajuh@uis.no  (c) June 18 2021

clear all; clc;

global global_info;
global_info.debug_mode = true;  % turn this ON for intermediate results

% 1: Adjacency matrix
%    I  J  K  L  M  N  O  P  Q
A = [0  5  0  0  0  0  0  10 0; ...  % I
     5  0  6  0  0  0  0  10 0;...   % J
     0  6  0  6  0  8  0  0  8;...   % K
     0  0  6  0  8  12 0  0  0;...   % L
     0  0  0  8  0  12 0  0  0;...   % M
     0  0  8  12 12 0  4  0  0;...   % N
     0  0  0  0  0  4  0  4  9;...   % O
     10 10 0  0  0  0  4  0  8;...   % P
     0  0  8  0  0  0  9  8  0];...  % Q     

% 2: nodes
nodes = [];
for i = double('I'):double('Q')
    nodeI.name = char(ceil(i)); % 'I' -> 'Q'
    nodes = [nodes nodeI]; 
end

% 3: Graph
G.nodes = nodes;
G.A = A;


% 4: call prim
p1 = prim(G);

% 5: print results
mst_print(p1);
       
