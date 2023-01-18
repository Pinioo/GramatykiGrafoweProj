from lib import Production, attr, next_nodes, LABEL
from networkx import Graph

#    E-----E          E-----E
#    |\   /|          |\   /|
#    |  I  |   =>     |  i  |
#    |/   \|          |/ | \|
#    E-----E          E--|--E
#                        |
#                        |
#                     E--|--E
#                     |\ | /|
#                     |  I  |
#                     |/   \|
#                     E-----E


EL1, EL2, EL3, EL4, IL = next_nodes(5)


def __get_node_pos(graph, node_id):
  return graph.nodes[node_id]["x"], graph.nodes[node_id]["y"]


def production_left_side():
    left = Graph()
    left.add_nodes_from([(EL1, attr("E")), (EL2, attr("E")), (EL3, attr("E")), (EL4, attr("E")), (IL, attr("I"))])
    left.add_edges_from([(EL1, EL2), (EL2, EL3), (EL3, EL4), (EL4, EL1), (EL1, IL), (EL2, IL), (EL3, IL), (EL4, IL)])
    return left


def production_modification(graph: Graph, mapping: dict) -> Graph:
    E1, E2, E3, E4 = next_nodes(4)
    I1 = next_nodes(1)
    level = graph.nodes[mapping[EL1]]["level"] + 1
    graph.nodes[mapping[IL]][LABEL] = "i"

    x1, y1 = __get_node_pos(graph, mapping[EL1])
    x2, y2 = __get_node_pos(graph, mapping[EL2])
    x3, y3 = __get_node_pos(graph, mapping[EL3])
    x4, y4 = __get_node_pos(graph, mapping[EL4])
    xi, yi = __get_node_pos(graph, mapping[IL])

    graph.add_nodes_from([
        (E1, attr("E", x1, y1, level)),
        (E2, attr("E", x2, y2, level)),
        (E3, attr("E", x3, y3, level)),
        (E4, attr("E", x4, y4, level)),
    ])
    graph.add_nodes_from([(I1, attr("I", xi, yi, level))])

    graph.add_edges_from([(E1, E2), (E2, E3), (E3, E4), (E4, E1)])
    graph.add_edges_from([(E1, I1), (E2, I1), (E3, I1), (E4, I1)])
    graph.add_edges_from([(mapping[IL], I1)])


P12 = Production(production_left_side(), production_modification)
