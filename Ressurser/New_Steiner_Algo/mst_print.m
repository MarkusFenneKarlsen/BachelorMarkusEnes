function [] = mst_print(V)
% function [] = mst_print(V)
% print the minimum-spanning-tree
%
% Reggie Davidrajuh (c) August 2011

TotalWT = 0;
MST = V.MST;

disp(' ');
disp('Printing the edges that are scanned to make MST ... ');
% now print complete MST
for i=1:length(V.nodes)-1
    mst = MST(i, :);
    u = mst(1); v = mst(2); wt = mst(3);
    TotalWT = TotalWT + wt;
    
    disp(['Edge-', int2str(i), ':  ', V.nodes(v).name, '-',...
        V.nodes(u).name, '    Wt: ', int2str(wt)]);
end

% finally, display the total weight
disp(['Total Weight : ', int2str(TotalWT)]);   
