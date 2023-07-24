import pytest
from .node import Node
from .graph import Edge, Graph

@pytest.fixture
def empty_graph():
    return Graph()

@pytest.fixture
def single_vertex_graph():
    graph = Graph()
    vertex = graph.add_vertex("A")
    return graph

def test_add_vertex(empty_graph):
    graph = empty_graph
    vertex = graph.add_vertex("A")
    assert vertex.value == "A"
    assert len(graph.get_vertices()) == 1

def test_add_edge(empty_graph):
    graph = empty_graph
    vertex_a = graph.add_vertex("A")
    vertex_b = graph.add_vertex("B")
    graph.add_edge(vertex_a, vertex_b, weight=5)

    neighbors = graph.get_neighbors(vertex_a)
    assert len(neighbors) == 1
    assert neighbors[0].vertex == vertex_b
    assert neighbors[0].weight == 5

def test_get_vertices(empty_graph):
    graph = empty_graph
    vertex_a = graph.add_vertex("A")
    vertex_b = graph.add_vertex("B")

    vertices = graph.get_vertices()
    assert len(vertices) == 2
    assert vertex_a in vertices
    assert vertex_b in vertices

def test_get_neighbors(empty_graph):
    graph = empty_graph
    vertex_a = graph.add_vertex("A")
    vertex_b = graph.add_vertex("B")
    vertex_c = graph.add_vertex("C")

    graph.add_edge(vertex_a, vertex_b, weight=5)
    graph.add_edge(vertex_a, vertex_c, weight=10)

    neighbors_a = graph.get_neighbors(vertex_a)
    neighbors_b = graph.get_neighbors(vertex_b)
    neighbors_c = graph.get_neighbors(vertex_c)

    assert len(neighbors_a) == 2
    assert len(neighbors_b) == 1
    assert len(neighbors_c) == 1

    assert neighbors_a[0].vertex == vertex_b
    assert neighbors_a[0].weight == 5
    assert neighbors_a[1].vertex == vertex_c
    assert neighbors_a[1].weight == 10

    assert neighbors_b[0].vertex == vertex_a
    assert neighbors_b[0].weight == 5

    assert neighbors_c[0].vertex == vertex_a
    assert neighbors_c[0].weight == 10

def test_get_neighbors_with_weight(single_vertex_graph):
    graph = single_vertex_graph
    vertex_a = list(graph.get_vertices())[0]
    vertex_b = graph.add_vertex("B")

    graph.add_edge(vertex_a, vertex_b, weight=5)

    neighbors_a = graph.get_neighbors(vertex_a)
    neighbors_b = graph.get_neighbors(vertex_b)

    assert len(neighbors_a) == 1
    assert len(neighbors_b) == 1

    assert neighbors_a[0].vertex == vertex_b
    assert neighbors_a[0].weight == 5

    assert neighbors_b[0].vertex == vertex_a
    assert neighbors_b[0].weight == 5

def test_size(empty_graph):
    graph = empty_graph
    assert graph.size() == 0

    graph.add_vertex("A")
    assert graph.size() == 1

    graph.add_vertex("B")
    assert graph.size() == 2

def test_graph_with_one_vertex_and_edge(single_vertex_graph):
    graph = single_vertex_graph
    vertex_a = list(graph.get_vertices())[0]
    neighbors_a = graph.get_neighbors(vertex_a)

    assert len(list(graph.get_vertices())) == 1
    assert len(neighbors_a) == 0

    graph.add_vertex("B")
    graph.add_edge(vertex_a, list(graph.get_vertices())[1], weight=5)

    neighbors_a = graph.get_neighbors(vertex_a)
    assert len(list(graph.get_vertices())) == 2
    assert len(neighbors_a) == 1
    assert neighbors_a[0].vertex == list(graph.get_vertices())[1]
    assert neighbors_a[0].weight == 5
