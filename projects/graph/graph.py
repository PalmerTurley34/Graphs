"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            return
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].update({v2})

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        already_visited = {starting_vertex}
        curr = starting_vertex
        while curr:
            for neighbor in self.get_neighbors(curr):
                if neighbor not in already_visited:
                    q.enqueue(neighbor)
                    already_visited.add(neighbor)
            print(curr)
            curr = q.dequeue() 

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        already_visited = {starting_vertex}
        curr = starting_vertex
        while curr:
            for neighbor in self.get_neighbors(curr):
                if neighbor not in already_visited:
                    stack.push(neighbor)
                    already_visited.add(neighbor)
            print(curr)
            curr = stack.pop()

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        self.dft_recursive_helper(starting_vertex, visited)

    def dft_recursive_helper(self, curr_vertex, visited):
        print(curr_vertex)
        visited.add(curr_vertex)
        for neighbor in self.get_neighbors(curr_vertex):
            if neighbor not in visited:
                self.dft_recursive_helper(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        already_visited = {starting_vertex}
        curr_path = [starting_vertex]
        while curr_path:
            if curr_path[-1] == destination_vertex:
                return curr_path
            for neighbor in self.get_neighbors(curr_path[-1]):
                if neighbor not in already_visited:
                    q.enqueue(curr_path + [neighbor])
                    already_visited.add(neighbor)
            
            curr_path = q.dequeue()
        return None 

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        already_visited = {starting_vertex}
        curr_path = [starting_vertex]
        while curr_path:
            if curr_path[-1] == destination_vertex:
                return curr_path
            for neighbor in self.get_neighbors(curr_path[-1]):
                if neighbor not in already_visited:
                    stack.push(curr_path + [neighbor])
                    already_visited.add(neighbor)
            curr_path = stack.pop()
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        visited = set()
        return self.dfs_recursive_helper([starting_vertex], destination_vertex, visited)

    def dfs_recursive_helper(self, curr_path, destination_vertex, visited):
        if curr_path[-1] == destination_vertex:
            return curr_path
        visited.add(curr_path[-1])
        for neighbor in self.get_neighbors(curr_path[-1]):
            if neighbor not in visited:
                new_path = curr_path + [neighbor]
                result =  self.dfs_recursive_helper(new_path, destination_vertex, visited)
                if len(result) > 0:
                    return result
        return []
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
