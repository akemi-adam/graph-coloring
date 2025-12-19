from random import randint, shuffle, random as rd
from copy import deepcopy


class Node:
    def __init__(self, label: str, neighbors: set = (), color: int = None):
        self.label = label
        self.neighbors = set(neighbors)
        self.color = color

    def set_color(self, color: int):
        self.color = color

    def __str__(self):
        return f'V{self.label}{(" with color " + str(self.color)) if self.color is not None else "" }: {self.neighbors}\n'


class Graph:
    def __init__(self, nodes: list[Node], order: int):
        self.nodes = nodes
        self.order = order
        self._node_index = {node.label: node for node in nodes}

    def find_node(self, label: int) -> Node:
        '''
        Busca um nó no grafo baseado em sua label.
        
        :param label: Nome de referência do nó
        :type label: int
        :return: Vértice do grafo
        :rtype: Node or None
        '''
        return self._node_index.get(label)

    def is_valid(self):
        '''
        Verifica se a coloração do grafo é válida, fazendo uma comparação entre os nós
        '''
        for node in self.nodes:
            for label in node.neighbors:
                neighbor: Node = self.find_node(label)
                if node.color == neighbor.color:
                    return False
        return True

    
    def __str__(self) -> str:
        nodes_str: str = ''
        for node in self.nodes:
            nodes_str += ' ' + str(node)
        return f'G:\n{nodes_str}\n'
    
