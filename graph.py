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

