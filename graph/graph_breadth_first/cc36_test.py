from ..node import Node
from ..graph import Graph
import pytest

# Helper function to create a sample graph for testing
def create_sample_graph():
    graph = Graph()
    vertex_a = graph.add_vertex('A')
    vertex_b = graph.add_vertex('B')
    vertex_c = graph.add_vertex('C')
    vertex_d = graph.add_vertex('D')
    graph.add_edge(vertex_a, vertex_b)
    graph.add_edge(vertex_a, vertex_c)
    graph.add_edge(vertex_b, vertex_d)
    return graph

# Test the breadth_first method
def test_breadth_first_happy_path():
    graph = create_sample_graph()
    vertices = list(graph.get_vertices())
    vertex_a = vertices[0]
    vertex_b = vertices[1]
    vertex_c = vertices[2]
    vertex_d = vertices[3]
    assert graph.breadth_first(vertex_a) == {vertex_a, vertex_b, vertex_c, vertex_d}

def test_breadth_first_empty_graph():
    graph = Graph()
    vertex = graph.add_vertex('A')
    assert graph.breadth_first(vertex) == {vertex}

def test_breadth_first_single_vertex_graph():
    graph = Graph()
    vertex = graph.add_vertex('A')
    assert graph.breadth_first(vertex) == {vertex}

def test_breadth_first_disconnected_graph():
    graph = create_sample_graph()
    vertices = list(graph.get_vertices())
    vertex_a = vertices[0]
    vertex_b = vertices[1]
    vertex_c = vertices[2]
    vertex_d = vertices[3]
    assert graph.breadth_first(vertex_d) == {vertex_a, vertex_b, vertex_c, vertex_d}

def test_breadth_first_non_existent_vertex():
    graph = create_sample_graph()
    vertex_z = Node('Z')  # Create a vertex not in the graph
    with pytest.raises(KeyError):
        graph.breadth_first(vertex_z)

def test_breadth_first_none_input():
    graph = create_sample_graph()
    with pytest.raises(TypeError):
        graph.breadth_first(None)

# Run the tests
if __name__ == '__main__':
    pytest.main()
