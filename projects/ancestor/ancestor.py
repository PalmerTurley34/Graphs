from graph import Graph
from util import Stack
# vertices are the children
# edges are the connections to parents
# use a dft to count how many ancesters there are in each line and return the largest number
def earliest_ancestor(ancestors, starting_node):
    # load the data inta a graph
    graph = Graph()
    for relation in ancestors:
        graph.add_vertex(relation[1])
        graph.add_edge(relation[1], relation[0])
    # find all the paths that go to the end
    paths = []
    stack = Stack()
    curr_path = [starting_node]
    while curr_path:
        if graph.get_neighbors(curr_path[-1]):
            for neighbor in graph.get_neighbors(curr_path[-1]):
                stack.push(curr_path + [neighbor])
        else:
            paths.append(curr_path)
        curr_path = stack.pop()
    # find the longest path(s)
    longest = []
    max_len = len(paths[0])
    for path in paths:
        if len(path) == max_len:
            longest.append(path)
        elif len(path) > max_len:
            max_len = len(path)
            longest = [path]
    # return the earliest ancestor in the path
    if len(longest) == 1:
        if len(longest[0])>1:
            return longest[0][-1]
        else:
            return -1
    elif len(longest) >1:
        return min([path[-1] for path in longest])
    


