from .graph import Graph

graph = Graph()

pandora = graph.add_vertex('Pandora')
arendelle = graph.add_vertex('Arendelle')
metroville = graph.add_vertex('Metroville')
monstropolis = graph.add_vertex('Monstropolis')
naboo = graph.add_vertex('Naboo')
narnia = graph.add_vertex('Narnia')

graph.add_edge(pandora, arendelle)
graph.add_edge(arendelle, pandora)
graph.add_edge(arendelle, metroville)
graph.add_edge(arendelle, monstropolis)
graph.add_edge(metroville, arendelle)
graph.add_edge(metroville, monstropolis)
graph.add_edge(metroville, naboo)
graph.add_edge(metroville, narnia)
graph.add_edge(monstropolis, arendelle)
graph.add_edge(monstropolis, metroville)
graph.add_edge(monstropolis, naboo)
graph.add_edge(naboo, monstropolis)
graph.add_edge(naboo, metroville)
graph.add_edge(naboo, narnia)
graph.add_edge(narnia, naboo)
graph.add_edge(narnia, metroville)

print(graph)

