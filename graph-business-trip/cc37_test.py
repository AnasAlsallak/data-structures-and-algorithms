import pytest
from graph.graph import Graph
from graph_business_trip import business_trip

def create_sample_graph():
    graph = Graph()

    city_a = graph.add_vertex('A')
    city_b = graph.add_vertex('B')
    city_c = graph.add_vertex('C')

    graph.add_edge(city_a, city_b, 150)
    graph.add_edge(city_b, city_c, 200)

    return graph

def test_business_trip_happy_path():
    graph = create_sample_graph()
    cities = ['A', 'B', 'C']
    assert business_trip(graph, cities) == (True, '$350')

def test_business_trip_unreachable_city():
    graph = create_sample_graph()
    cities = ['A', 'C']  # No direct connection between A and C
    assert business_trip(graph, cities) == (False, '$0')

def test_business_trip_single_city():
    graph = create_sample_graph()
    cities = ['A']
    assert business_trip(graph, cities) == (False, '$0')  # No cost for a single city trip

def test_business_trip_invalid_city():
    graph = create_sample_graph()
    cities = ['A', 'D']  
    with pytest.raises(KeyError):
        business_trip(graph, cities)

def test_business_trip_empty_city_list():
    graph = create_sample_graph()
    cities = []
    assert business_trip(graph, cities) == (False, '$0') 

def test_business_trip_expected_failure():
    graph = create_sample_graph()
    cities = ['A', 'B', 'C', 'D']  
    assert business_trip(graph, cities) == (False, '$0')

print(create_sample_graph())