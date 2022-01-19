function [] = steiner_print(G)
% function [] = steiner_print(G)
% print the steiner minimum-spanning-tree after computing 
%   the steiner tree with the function Steiner_Tree
%
% Reggie.Davidrajuh@uis.no (c) August 2011

TotalWT = 0;
A2 = G.Steiner;

disp(' ');
disp('Printing the edges of Steiner tree ... ');

for i = 1 : length(G.nodes)-1
    for j = i+1 : length(G.nodes)
        if A2(i, j)
            wt = A2(i, j);
            disp(['Edge-', int2str(i), ':  ', G.nodes(i).name, '-',...
                  G.nodes(j).name, '    Wt: ', int2str(wt)]);
            TotalWT = TotalWT + wt;
        end
    end    
end

% finally, display the total weight
disp(['Total Weight : ', int2str(TotalWT)]);   
