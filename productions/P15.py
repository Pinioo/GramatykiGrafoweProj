from lib import Production, attr, next_nodes
from utils.graph_utils import __get_node_pos
from networkx import Graph

E0, E1, E2, E3, E4, i1, i2, I1, I2 = next_nodes(9)

#### PRODUCTION DEFINITION

# LEFT SITE
#
#     --------- E0 ---------
#    /                      \
#   i1                       i2
#   |                        |
#   | E1(x1, y1)   E3(x1, y1)|
#   | / |                | \ |
#   I1  |                |  I2
#     \ |                |  /
#     E2(x2, y2)   E4(x2, y2)


# RIGHT SIDE
#
#     --- E0 --
#    /         \
#   i1         i2
#   |           |
#   | E1(x1,y1) |
#   | /   |   \ |
#   I1    |    I2
#     \   |   /
#     E2(x2,y2)


def production_left_side():
    left = Graph()
    left.add_nodes_from([(E0, attr("E")), (i1, attr("i")), (i2, attr("i")), (I1, attr("I")), (I2, attr("I")),
                         (E1, attr("E")), (E2, attr("E")), (E3, attr("E")),(E4, attr("E"))])
    left.add_edges_from([(E0, i1), (i1, I1), (I1, E1), (I1, E2), (E1, E2), (E0, i2), (i2, I2), (I2, E3), (I2, E4), (E3, E4)])

    return left


def left_side_pos_constraints(graph: Graph, mapping: dict) -> bool:
    E1_pos = __get_node_pos(graph, mapping[E1])
    E2_pos = __get_node_pos(graph, mapping[E2])
    E3_pos = __get_node_pos(graph, mapping[E3])
    E4_pos = __get_node_pos(graph, mapping[E4])
    return E1_pos == E3_pos and E2_pos == E4_pos


def production_modification(graph: Graph, mapping: dict):
    graph.remove_edge(mapping[E3], mapping[E4])
    # Reconnect neighbours of nodes we are about to delete
    for neigh_of_E3 in graph.neighbors(mapping[E3]):
        graph.add_edges_from([(mapping[E1], neigh_of_E3)])
    for neigh_of_E4 in graph.neighbors(mapping[E4]):
        graph.add_edges_from([(mapping[E2], neigh_of_E4)])
    # Remove nodes we don't need
    graph.remove_nodes_from([mapping[E3], mapping[E4]])

P15 = Production(production_left_side(), production_modification, left_side_pos_constraints)
