function [G] = sample_graph()
% function [G] = sample_graph()
% 
%  Reggie.Davidrajuh@uis.no  (c) 15.August.2021
%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% the example given in the paper
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% 1: Adjacency matrix
%    I  J  K  L  M  N  O  P  Q  
A = [0  5  0  0  0  0  0  10  0; ...  %I
     5  0  6  0  0  0  0  10 0;...   %J
     0  6  0  6  0  8  0  0  8;...   %K
     0  0  6  0  8  12 0  0  0;...   %L
     0  0  0  8  0  12 0  0  0;...   %M
     0  0  8  12 12 0  4  0  0;...   %N
     0  0  0  0  0  4  0  4  9;...   %O
     10 10 0  0  0  0  4  0  8;...   %P
     0  0  8  0  0  0  9  8  0];...  %Q     

% 2: nodes with their names
nodes = [];
for i = double('I'):double('Q')
    nodeI.name = char(ceil(i)); % 'a' -> 'i'
    nodes = [nodes nodeI]; 
end

nodeI.name = 'I'; nodeK.name = 'K'; 
nodeM.name = 'M'; nodeN.name = 'N'; 
Terminals = [nodeI, nodeK, nodeM, nodeN];


% 3: create the Graph node
G.nodes = nodes;
G.A = A;
G.Terminals = Terminals;

