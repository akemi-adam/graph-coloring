from abc import ABC
from graph import Graph, paint
from copy import deepcopy
from random import sample
from collections import Counter


POPULATION_SIZE = 100

class MutationOperator(ABC):
    pass


class FitnessFunction(ABC):
    def evaluate(self, graph: Graph):
        pass


class LessConflictFitness(FitnessFunction):
    def evaluate(self, graph: Graph) -> int:
        conflicts = 0
        visited = set()
        for node in graph.nodes:
            visited.add(node.label)
            for neighbor_label in node.neighbors:
                if neighbor_label in visited:
                    continue
                neighbor = graph.find_node(neighbor_label)
                if neighbor is not None and node.color == neighbor.color:
                    conflicts += 1
        return conflicts



class CrossoverOperator(ABC):
    def __init__(self, fitness: FitnessFunction):
        self.fitness = fitness
    
    def execute(self, parents):
        pass


class OrderCrossover(CrossoverOperator):
    def execute(self, parents):
        children = []
        if len(parents) % 2 != 0:
            parents = parents[:-1]
        for i in range(0, len(parents), 2):
            g1 = parents[i][0]
            g2 = parents[i + 1][0]
            child = self.ox(g1, g2)
            fitness_value = self.fitness.evaluate(child)
            children.append((child, fitness_value))
        return children

    def ox(self, g1: Graph, g2: Graph) -> Graph:
        n = g1.order
        c1, c2 = sorted(sample(range(n), 2))

        child = deepcopy(g1)
        p1 = [node.color for node in g1.nodes]
        p2 = [node.color for node in g2.nodes]
        child_colors = [None] * n
        child_colors[c1:c2] = p1[c1:c2]

        p2_counts = Counter(p2)
        for color in child_colors[c1:c2]:
            # if color is not None:
            p2_counts[color] -= 1

        j = 0
        for i in range(n):
            if child_colors[i] is not None:
                continue
            while j < n:
                color = p2[j]
                j += 1
                if p2_counts[color] > 0:
                    child_colors[i] = color
                    p2_counts[color] -= 1
                    break

        for node, color in zip(child.nodes, child_colors):
            node.color = color

        return child
    

class PopulationStrategy(ABC):
    def __init__(self, graph: Graph, fitness: FitnessFunction):
        self.graph = graph
        self.fitness = fitness
        
    def start(self, k: int):
        pass


class RandomPopulation(PopulationStrategy):
    def __init__(self, graph: Graph, fitness: FitnessFunction):
        super().__init__(graph, fitness)
    
    def start(self, k: int):
        population = []
        while len(population) < POPULATION_SIZE:
            graph: Graph = paint(self.graph, k)
            individual = (graph, self.fitness.evaluate(graph))
            population.append(individual)
        return sorted(population, key=lambda x: x[1])
        
    
def ag(graph: Graph, k: int, epochs: int):
    '''
    Algoritmo genético para coloração de grafos.
    
    :param graph: Grafo a ser colorido
    :type graph: Graph
    :param k: Número de cores
    :type k: int
    :param epochs: Número de gerações
    :type epochs: int
    '''
    fitness: FitnessFunction = LessConflictFitness()
    population_strategy: PopulationStrategy = RandomPopulation(graph, fitness)
    population = population_strategy.start(k)
    crossover_operator: CrossoverOperator = OrderCrossover(fitness)
    while epochs > 0:
        # Dá pra quebrar isso ao verificar se achou uma solução válida
        # print(population[0])
        parents = population[:(POPULATION_SIZE // 2)]
        children = crossover_operator.execute(parents)
        population += children
        population = sorted(population, key=lambda x: x[1])
        population = population[:POPULATION_SIZE]
        epochs -= 1
    return population[0][0]
        