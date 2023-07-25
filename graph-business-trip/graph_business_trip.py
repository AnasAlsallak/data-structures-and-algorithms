from graph.graph import Graph

def business_trip(graph,cities):
    if graph is None or not isinstance(graph, Graph):
        raise TypeError("Invalid input: 'graph' must be an instance of the Graph class")

    if cities is None or not isinstance(cities, list):
        raise TypeError("Invalid input: 'cities' must be a non-empty list of city names")

    for city in cities:
        if not isinstance(city, str):
            raise TypeError("Invalid city name in 'cities' list. All city names must be strings.")

    if len(cities) < 2:
        return False, '$0'

    for city in cities:
        if city not in graph.get_vertices():
            raise KeyError(f"City '{city}' is not present in the graph")
    cost = 0
    for i in range(len(cities)-1):
        neighbors = graph.get_neighbors(cities[i])
        for neighbor in neighbors:
            if neighbor[0] == cities[i+1]:
                cost += neighbor[1]
                break
        else:
            return False, '$0'
    return True, f'${cost}'
    
    