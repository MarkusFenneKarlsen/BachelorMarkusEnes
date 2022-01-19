function [source_index] = the_source_index(G, source)
% convert source node into source index

number_of_nodes = length(G.nodes);

if isnumeric(source)
    if and(gt(source,0), le(source, number_of_nodes))
        source_index = source;
        return
    else
        error(['invalid source index : ', int2str(source)]); 
    end
end

% given source is a node
source_name = source.name;
source_index = 0; % initially source_index not found yet 

for i = 1:number_of_nodes
    if strcmpi(G.nodes(i).name, source_name)
         source_index = i;
         return
    end
end

if not(source_index)
    error(['unknown source: ', source.name]); 
end
