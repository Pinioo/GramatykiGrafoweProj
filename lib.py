from networkx import Graph
from networkx.algorithms import isomorphism as iso
from dataclasses import dataclass
from typing import Callable

import networkx as nx
import itertools as it
import matplotlib.pyplot as plt
import random

LABEL = "label"
NODE_GENERATOR = it.count()
LEVEL_OFFSET = 1.5
OVERLAPPING_OFFSET = 0.03

def next_nodes(count=1):
    """Global generator for node numbers to provide uniqueness"""
    return tuple(next(NODE_GENERATOR) for _ in range(count))


def attr(label, x=0, y=0, level=0):
    """Generator of standard set of attributes fo grammar"""
    return {
        LABEL: label,
        "x": x, "y": y,
        "level": level,
    }


def visualize_graph(g: Graph, level: int = None) -> None:
    if level != None:
        this_level_nodes = [node for node, attr in g.nodes.items() if attr["level"]==level]
        g = g.subgraph(this_level_nodes)
    list_of_coords = {n: (a["x"]+LEVEL_OFFSET*a["level"], a["y"]) for n, a in g.nodes.items()}
    list_of_coords = {n: __move_if_overlapping(list_of_coords, coords) for n, coords in list_of_coords.items()}
    labels = {n: a[LABEL] for n, a in g.nodes.items()}
    nx.draw(g, list_of_coords, node_size=100, node_color="y")
    nx.draw_networkx_labels(g, list_of_coords, labels, font_color='k', font_size=8)
    plt.axis('scaled')
    plt.show()

def __move_if_overlapping(list_of_coords, coords):
    x, y = coords
    how_many_matches = 0
    for _, (x_i, y_i) in list_of_coords.items():
        if  x == x_i and y == y_i:
            how_many_matches+=1
    if how_many_matches > 1:
        return (x+random.random()*OVERLAPPING_OFFSET, y)
    else:
        return (x, y)
        

@dataclass
class Production:
    """
    Attributes:
    ---
    left_side: Graph
        Left side of production to check applicability
    modification: Callable[[Graph, dict], None]
        Function with production implementation, it has to perform modification directly in the
        graph provided as the first parameter. Second parameter is a isomorphism mapping of nodes from 
        left side into working graph.        
    """

    left_side: Graph
    modification: Callable[[Graph, dict], None]

    # Return graph after
    def perform_modification(self, graph: Graph, in_place: bool = False, level: int = None) -> Graph:
        """Performs production on provided graph. Either creates a copy or changes provided graph."""

        if level != None:
            this_level_nodes = [node for node, attr in graph.nodes.items() if attr["level"]==level]
            graph_to_search = graph.subgraph(this_level_nodes)
        else:
            graph_to_search = graph
        mapping = self.get_mapping_if_applicable(graph_to_search)
        if mapping is None:
            raise Exception("No isomorphic subgraph has been found")
        if not in_place:
            graph = graph.copy()
        self.modification(graph, mapping)
        return graph

    def get_mapping_if_applicable(self, graph: Graph):
        """Returns a mapping {left_side_node, input_graph_node} for isomorphism if found."""

        graph_matcher = iso.GraphMatcher(graph, self.left_side,
                              node_match=lambda u, v: u[LABEL] == v[LABEL])
        return {v: k for k, v in graph_matcher.mapping.items()} if graph_matcher.subgraph_is_isomorphic() else None
