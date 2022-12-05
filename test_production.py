from lib import Production, attr, LABEL, next_nodes
from networkx import Graph

# E---E    E---E
# |\ /|    |\  |
# | I | => | i |
# |/ \|    |  \|
# E---E    E---E

E1, E2, E3, E4, I = next_nodes(5)
def test_production_left_side():
    sm, gt = 0, 1
    left = Graph()
    left.add_nodes_from([
        (E1, attr("E")),
        (E2, attr("E")),
        (E3, attr("E")),
        (E4, attr("E")),
        (I, attr("I")),
    ])
    left.add_edges_from([(E1, E2), (E2, E3), (E3, E4), (E4, E1), (I, E1), (I, E2), (I, E3), (I, E4)])
    return left

def test_production_modification(graph: Graph, mapping: dict) -> Graph:
    graph.nodes.get(mapping[I])[LABEL] = "i"
    graph.remove_edges_from([(mapping[E1], mapping[I]), (mapping[E3], mapping[I])])

TestProduction = Production(test_production_left_side(), test_production_modification)