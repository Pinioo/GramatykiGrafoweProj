from lib import Production, attr, next_nodes
from utils.graph_utils import __get_node_pos
from networkx import Graph

E0, E1, E2, E3, E4, E5, I1, I2, I3, I4, I5 = next_nodes(11)

#### PRODUCTION DEFINITION

# LEFT SITE
#
#      ----------- E0 ------------
#     /                           \
#    i1                            i4
#  / |                             |
# /  | E1(x1, y1)       E4(x1, y1) |
# |  | / |                    | \  |
# |  I2  |                    |  \ |
# |    \ |                    |   \|
# |  E2([x1+x2]/2, [y1+y2]/2) |    I5
# | /    |                    |   /
# I3     |                    |  /
#   \    |                    | /
#    E3(x2, y2)         E5(x2, y2)

# RIGHT SIDE
#
#      ---------- E0 -----------
#     /                         \
#    i1                         i4
#  / |                           |
# /  | E1(x1, y1) ------------   |
# |  | / |                    \  |
# |  I2  |                     \ |
# |    \ |                      \|
# |  E2([x1+x2]/2, [y1+y2]/2)   I5
# | /    |                      /
# I3     |                     /
#   \    |                    /
#    E3(x2, y2) --------------


def production_left_side():
    left = Graph()
    left.add_nodes_from([(E0, attr("E")),
        (I1, attr("i")), (I2, attr("I")), (I3, attr("I")), (I4, attr("i")), (E1, attr("E")), (E2, attr("E")), (E3, attr("E")),
        (I5, attr("I")), (E4, attr("E")), (E5, attr("E"))])
    left.add_edges_from([(E0, I1), (I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (I3, E3),
                         (E0, I4), (I4, I5), (I5, E4), (I5, E5), (E4, E5), (E1, E2), (E2, E3)])

    return left


def left_side_pos_constraints(graph: Graph, mapping: dict) -> bool:
    E1_pos = __get_node_pos(graph, mapping[E1])
    E2_pos = __get_node_pos(graph, mapping[E2])
    E3_pos = __get_node_pos(graph, mapping[E3])
    E4_pos = __get_node_pos(graph, mapping[E4])
    E5_pos = __get_node_pos(graph, mapping[E5])
    return E1_pos == E4_pos and E3_pos == E5_pos and E2_pos == ((E1_pos[0] + E3_pos[0])/2, (E1_pos[1] + E3_pos[1])/2)


def production_modification(graph: Graph, mapping: dict):
    # Reconnect neighbours of nodes we are about to delete
    graph.remove_edges_from([(mapping[E4], mapping[E5])])
    for neigh_of_E4 in graph.neighbors(mapping[E4]):
        graph.add_edges_from([(mapping[E1], neigh_of_E4)])
    for neigh_of_E5 in graph.neighbors(mapping[E5]):
        graph.add_edges_from([(mapping[E3], neigh_of_E5)])
    # Remove nodes we don't need
    graph.remove_nodes_from([mapping[E4], mapping[E5]])
    print(f"P13: Merged node at {__get_node_pos(graph, mapping[E2])}")


P13 = Production(production_left_side(), production_modification, left_side_pos_constraints)

def left_side_pos_constraints_vert(graph: Graph, mapping: dict) -> bool:
    E1_pos = __get_node_pos(graph, mapping[E1])
    E2_pos = __get_node_pos(graph, mapping[E2])
    E3_pos = __get_node_pos(graph, mapping[E3])
    E4_pos = __get_node_pos(graph, mapping[E4])
    E5_pos = __get_node_pos(graph, mapping[E5])
    return E1_pos == E4_pos and E3_pos == E5_pos and E2_pos == ((E1_pos[0] + E3_pos[0])/2, (E1_pos[1] + E3_pos[1])/2) and E1_pos[1] == E3_pos[1]
P13_vert = Production(production_left_side(), production_modification, left_side_pos_constraints_vert)


def left_side_pos_constraints_horiz(graph: Graph, mapping: dict) -> bool:
    E1_pos = __get_node_pos(graph, mapping[E1])
    E2_pos = __get_node_pos(graph, mapping[E2])
    E3_pos = __get_node_pos(graph, mapping[E3])
    E4_pos = __get_node_pos(graph, mapping[E4])
    E5_pos = __get_node_pos(graph, mapping[E5])
    return E1_pos == E4_pos and E3_pos == E5_pos and E2_pos == ((E1_pos[0] + E3_pos[0])/2, (E1_pos[1] + E3_pos[1])/2) and E1_pos[0] == E3_pos[0]
P13_horiz = Production(production_left_side(), production_modification, left_side_pos_constraints_horiz)
