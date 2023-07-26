import pytest
from graph.graph import Graph

# Assume depth_first method is implemented in the Graph class

def create_sample_graph():
    graph = Graph()

    city_a = graph.add_vertex('A')
    city_b = graph.add_vertex('B')
    city_c = graph.add_vertex('C')

    graph.add_edge(city_a, city_b)
    graph.add_edge(city_b, city_c)

    return graph

def test_depth_first_happy_path():
    graph = create_sample_graph()
    starting_vertex = graph.get_vertices()[0]  # Let's assume 'A' is the first vertex in the graph
    result = graph.depth_first(starting_vertex)
    assert result == {'A', 'B', 'C'}

def test_depth_first_edge_case_single_vertex():
    graph = create_sample_graph()
    starting_vertex = graph.get_vertices()[0]
    result = graph.depth_first(starting_vertex)
    assert result == {starting_vertex}  # Use set comparison

def test_depth_first_edge_case_empty_graph():
    graph = Graph()
    starting_vertex = None
    with pytest.raises(TypeError):
        graph.depth_first(starting_vertex)

def test_depth_first_edge_case_invalid_vertex():
    graph = create_sample_graph()
    starting_vertex = graph.add_vertex('D')  # 'D' is not present in the graph
    with pytest.raises(KeyError):
        graph.depth_first(starting_vertex)

def test_depth_first_expected_failure():
    graph = create_sample_graph()
    starting_vertex = graph.get_vertices()[0]  # Let's assume 'A' is the first vertex in the graph
    result = graph.depth_first(starting_vertex)
    # Add some expected failure condition here (e.g., result == {'A', 'B'})
    assert result != {'A', 'B'}

def test_depth_first_expected_failure_empty_input():
    graph = create_sample_graph()
    with pytest.raises(TypeError):
        graph.depth_first(None)
