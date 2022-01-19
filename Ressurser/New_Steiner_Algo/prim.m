function [V] = prim(V)
% function [V] = prim(V)
% Kruskal algorithm for finding minimum-weight-spanning-tree
% MST will be returned as V.MST, containing a set of rows
%   each represent an edge [u v weight]
%
% Reggie Davidrajuh (c) August 2011

% only for debugging
global global_info

DBM = false;
if isfield(global_info, 'debug_mode')
    DBM = global_info.debug_mode; 
end

A = V.A;
nodes = V.nodes;

[m, n] = size(A);

% adjust A, so that elements that are zero becomes Inf
for i = 1:m 
    for j = 1:n
        if not(A(i,j)), A(i,j) = Inf; end
    end
end


No_of_vertices = length(V.nodes);

tree_vertices = 1;
MST = [];

% add one vertice at a time to "tree_vertices"
while lt(length(tree_vertices), No_of_vertices)
    minWeight = Inf;
    if DBM
        disp(' ');  disp_str = 'Tree vertices: [';
        for i = 1:length(tree_vertices)
            disp_str = [disp_str, nodes(tree_vertices(i)).name, ' '];
        end
        disp_str = ([disp_str, ']']);
        disp(disp_str); 
    end
    
    % from all the vertices in the tree, search for minimum edge
    for i = 1:length(tree_vertices)
        minU = tree_vertices(i);
        [minwt, minV] = min(A(minU, :));
        % edge must be minimum and must be a "safe edge" 
        if and(lt(minwt, minWeight), not(ismember(minV, tree_vertices)))
            minWeight = minwt;
            v = minV;
            u = minU;            
        end
    end
    % when am minimum is found 
    A(u, v) = inf; A(v, u) = inf;   % mark the edge as visited
    tree_vertices = [tree_vertices v];
    nodes(v).pi = u;
    if DBM
        disp([nodes(u).name, ' to ', nodes(v).name, ...
            '   wt: ', int2str(minWeight)]);
    end
    MST = [MST; u, v, minWeight];
end

V.MST = MST;
