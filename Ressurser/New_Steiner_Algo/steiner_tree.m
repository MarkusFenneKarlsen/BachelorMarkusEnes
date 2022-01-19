function [G] = steiner_tree(G)
% function [G] = steiner_tree(G)
%   This function takes a minimum spanning tree and then
%   eliminates the Steiner node.
%   The algorithm for elimination is described in the paper
%   Jaiswal, R. and Davidrajuh, R. (2011) "A Simple Algorithm for 
%       finding "


Terminals = G.Terminals;
nodes = G.nodes;
no_of_terminals = numel(Terminals);
terminal_indices = []; 
for i = 1:no_of_terminals
        for j = 1:numel(nodes)
            t = Terminals(i).name;
            n = nodes(j).name;
            if strcmp(t, n)
                terminal_indices = [terminal_indices j]; break
            end
        end
end

G.terminal_indices = terminal_indices;

MST = G.MST;
edgesOfMST = size(MST, 1);
A2 = zeros(size(G.A));

for i = 1:edgesOfMST
    A2(MST(i,1), MST(i,2)) = MST(i,3); A2(MST(i,2), MST(i,1)) = MST(i,3);
end

Iterations_Complete = false;
while not(Iterations_Complete) 
    Iterations_Complete = true;
    for i = 1:numel(G.nodes)
        if not(ismember(i, terminal_indices))
            edgesOfi = A2(i, :);
            no_connections = sum(edgesOfi > 0); 
            if eq(no_connections, 1)
                j = find(edgesOfi);
                A2(i, j) = 0; A2(j, i) = 0; 
                Iterations_Complete = false;        
            end
        end
    end
end
G.Steiner = A2;
