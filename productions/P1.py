from lib import Production, attr, LABEL, next_nodes
from networkx import Graph

#             el
#          E--|--E
# el  =>   |\ | /|
#          |  I  |
#          |/   \|
#          E-----E

el, E1, E2, E3, E4, I = next_nodes(6)

def production_left_side():
    left = Graph()
    left.add_nodes_from([(el, attr("el"))])
    return left

def production_modification(graph: Graph, mapping: dict) -> Graph:
    level = graph.nodes[mapping[el]]["level"]+1
    graph.add_nodes_from([(E1, attr("E", 0, 0, level)), (E2, attr("E", 0, 1, level)), (E3, attr("E", 1, 1, level)), (E4, attr("E", 1, 0, level)), (I, attr("I", 0.5, 0.5, level))])
    graph.add_edges_from([(E1, E2), (E2, E3), (E3, E4), (E4, E1), (E1, I), (E2, I), (E3, I), (E4, I), (mapping[el], I)])

P1 = Production(production_left_side(), production_modification)