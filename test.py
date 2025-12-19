from graph import Graph, paint, random

order: int = int(input('Ordem do grafo: '))
k: int = int(input('Número de cores: '))

graph = random(order)
graph_colored = paint(graph, k)

print('Grafo normal: \n', graph, end='\n')
print('Grafo colorido: ', graph_colored, end='\n')
print('É válido? ', 'Sim' if graph_colored.is_valid() else 'Não')