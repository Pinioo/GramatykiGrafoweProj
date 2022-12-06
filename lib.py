from networkx import Graph
from networkx.algorithms import isomorphism as iso
from dataclasses import dataclass
from typing import Callable

import networkx as nx
import itertools as it
import matplotlib.pyplot as plt

LABEL = "label"
NODE_GENERATOR = it.count()

def next_nodes(count=1):
    """Global generator for node numbers to provide uniqueness"""
    return tuple(next(NODE_GENERATOR) for _ in range(count))


def attr(label, x=0, y=0, level=0):
    """Generator of standard set of attributes fo grammar"""
    return {
        LABEL: label,
        "x": x, "y": y-level*2,
        "level": level,
    }


def visualize_graph(g: Graph) -> None:
    pos = {n: (a["x"], a["y"]) for n, a in g.nodes.items()}
    labels = {n: a[LABEL] for n, a in g.nodes.items()}
    nx.draw(g, pos)
    nx.draw_networkx_labels(g, pos, labels, font_color='w')
    plt.show()


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
    def perform_modification(self, graph: Graph, in_place: bool = False) -> Graph:
        """Performs production on provided graph. Either creates a copy or changes provided graph."""

        mapping = self.get_mapping_if_applicable(graph)
        if mapping is None:
            raise Exception()
        if not in_place:
            graph = graph.copy()
        self.modification(graph, mapping)
        return graph

    def get_mapping_if_applicable(self, graph: Graph):
        """Returns a mapping {left_side_node, input_graph_node} for isomorphism if found."""

        graph_matcher = iso.GraphMatcher(graph, self.left_side,
                              node_match=lambda u, v: u[LABEL] == v[LABEL])
        return {v: k for k, v in graph_matcher.mapping.items()} if graph_matcher.subgraph_is_isomorphic() else None
