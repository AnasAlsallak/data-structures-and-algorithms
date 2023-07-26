from .node import Node

class Edge :     
    def __init__(self, vertex, weight = 0) :
        self.vertex = vertex
        self.weight = weight

class   Graph :
    def __init__(self) :
        self.adjacency_list = {}
    
    def add_vertex(self, value):
        vertex = Node(value)
        self.adjacency_list[vertex] = []
        return vertex

    def add_edge(self, node1, node2, weight = 0) :
        if node1 not in self.adjacency_list:
            raise KeyError('Node 1 is not in the graph')
        if node2 not in self.adjacency_list:
            raise KeyError('Node 2 is not in the graph')

        edge1 = Edge(node2, weight)
        edge2 = Edge(node1, weight)  # here it adds the reverse edge for the undirected graph
        self.adjacency_list[node1].append(edge1)
        self.adjacency_list[node2].append(edge2)
        
    def get_vertices(self) :
        return list(self.adjacency_list.keys())

    def get_neighbors(self, node) :
        return self.adjacency_list[node]
    
    def size(self) :
        return len(self.adjacency_list)
    
    def __str__(self) -> str:
        output = ''
        
        for vertex in self.adjacency_list :
            output += vertex.value
            output += '\n'
            
            for edge in self.adjacency_list[vertex] :
                output += f'  {edge.vertex.value}, {edge.weight}'
                output += '\n'
                
        return output 

    def breadth_first(self, vertex):
        if vertex is None:
            raise TypeError("Input vertex cannot be None")
        
        if vertex not in self.adjacency_list:
            raise KeyError("Input vertex not in graph")

        queue = []
        visited = set()

        queue.append(vertex)
        visited.add(vertex)

        while len(queue) > 0:
            current = queue.pop(0)

            for edge in self.adjacency_list[current]:
                if edge.vertex not in visited:
                    visited.add(edge.vertex)
                    queue.append(edge.vertex)

        return visited
    
    def depth_first (self, vertex):
        if vertex is None:
            raise TypeError("Input vertex cannot be None")
        
        if vertex not in self.adjacency_list:
            raise KeyError("Input vertex not in graph")

        stack = []
        visited = set()

        stack.append(vertex)
        visited.add(vertex)

        while len(stack) > 0:
            current = stack.pop()

            for edge in self.adjacency_list[current]:
                if edge.vertex not in visited:
                    visited.add(edge.vertex)
                    stack.append(edge.vertex)

        return visited
    

graph = Graph()

vertex_a = graph.add_vertex("A")
vertex_b = graph.add_vertex("B")
vertex_c = graph.add_vertex("C")
vertex_d = graph.add_vertex("D")

graph.add_edge(vertex_a, vertex_b)
graph.add_edge(vertex_a, vertex_c)
graph.add_edge(vertex_c, vertex_d)

starting_vertex = vertex_a
result = graph.breadth_first(starting_vertex)

print(result)  

