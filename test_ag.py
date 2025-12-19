from graph import Graph, random, export_graph_to_markdown
from ag import ag

order: int = int(input('Ordem do grafo: '))
k: int = int(input('Número de cores: '))

graph: Graph = random(order)

print('Grafo normal: \n', graph, end='\n')

graph_colored: Graph = ag(graph, k, 50)
print('Grafo colorido: ', graph_colored, end='\n')
print('É válido? ', 'Sim' if graph_colored.is_valid() else 'Não')

export_graph_to_markdown(graph_colored, k)