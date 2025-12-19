from abc import ABC
from graph import Graph


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

