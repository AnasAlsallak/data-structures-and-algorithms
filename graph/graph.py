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
        return self.adjacency_list.keys()

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