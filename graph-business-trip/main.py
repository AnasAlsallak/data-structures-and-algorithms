from graph.graph import Graph
from graph_business_trip import business_trip

graph = Graph()

pandora = graph.add_node('Pandora')
arendelle = graph.add_node('Arendelle')
metroville = graph.add_node('Metroville')
monstropolis = graph.add_node('Monstropolis')
narnia = graph.add_node('Narnia')
naboo = graph.add_node('Naboo')

graph.add_edge(pandora,arendelle,150)
graph.add_edge(arendelle,metroville,99)
graph.add_edge(arendelle,monstropolis,42)
graph.add_edge(metroville,monstropolis,105)
graph.add_edge(metroville,narnia,37)
graph.add_edge(metroville,naboo,26)
graph.add_edge(monstropolis,naboo,73)
graph.add_edge(narnia,naboo,250)

print(business_trip(graph,[arendelle,metroville,naboo])) # True, $115 