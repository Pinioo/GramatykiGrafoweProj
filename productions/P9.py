from lib import Production, attr, next_nodes
from utils.graph_utils import __get_node_pos
from networkx import Graph

E0, E1, E2, E3, E4, E5,i0, i1, I2, I3, i4, I5, I6 = next_nodes(13)

#### PRODUCTION DEFINITION

# LEFT SIDE
#
#      --------------------- i0 ----------------------
#     /                                               \
#    i1                                               i4
#  / |                                                 |\
# /  | E0(x1, y1)                           E3(x1, y1) | \
# |  | / |                                        |  \ |  |
# |  I2  |                                        |   I5  |
# |    \ |                                        |  /    |
# |  E1([x1+x2]/2, [y1+y2]/2)    E4([x1+x2]/2, [y1+y2]/2) |
# | /    |                                        |      \|
# I3     |                                        |      I6
#   \    |                                        |     /
#    E2(x2, y2)                                 E5(x2, y2)

# RIGHT SIDE
#
#      ---------- i0 -----------
#     /                         \
#    i1                         i4
#  / |                           |
# /  | E0(x1, y1) -------------  |
# |  | / |                     \ |
# |  I2  |                      I5
# |    \ |                     / |
# |  E1([x1+x2]/2, [y1+y2]/2)--  |
# | /    |                     \ |
# I3     |                      I6
#   \    |                     /
#    E2(x2, y2) ---------------


def production_left_side():
    left = Graph()
    left.add_nodes_from([(i0, attr("i")),
        (i1, attr("i")), (I2, attr("I")), (I3, attr("I")), (i4, attr("i")),
        (E0, attr("E")), (E1, attr("E")), (E2, attr("E")), (E5, attr("E")),
        (I5, attr("I")), (I6, attr("I")), (E3, attr("E")), (E4, attr("E"))])
    left.add_edges_from([(i0, i1), (i1, I2), (i1, I3), (I2, E0), (I2, E1), (I3, E1), (I3, E2), (E0, E1), (E1, E2),
                         (i0, i4), (i4, I5), (i4, I6), (I5, E3), (I5, E4), (I6, E4), (I6, E5), (E3, E4), (E4, E5)])

    return left

def left_side_pos_constraints(graph: Graph, mapping: dict) -> bool:
    E1_pos = __get_node_pos(graph, mapping[E0])
    E2_pos = __get_node_pos(graph, mapping[E1])
    E3_pos = __get_node_pos(graph, mapping[E2])
    E4_pos = __get_node_pos(graph, mapping[E3])
    E5_pos = __get_node_pos(graph, mapping[E4])
    E6_pos = __get_node_pos(graph, mapping[E5])
    return E1_pos == E4_pos and E2_pos == E5_pos and E3_pos == E6_pos and E2_pos == ((E1_pos[0] + E3_pos[0])/2, (E1_pos[1] + E3_pos[1])/2)

def production_modification(graph: Graph, mapping: dict):
    mapping_values = set(mapping.values())
    nodes_to_delete = [mapping[E3], mapping[E4], mapping[E5]]
    replacement_nodes = [mapping[E0], mapping[E1], mapping[E2]]
    for node, replacement_node in zip(nodes_to_delete, replacement_nodes):
      node_neighbours = graph.neighbors(node)
      for neighbour in node_neighbours:
        if neighbour not in mapping_values:
          graph.add_edges_from([(replacement_node, neighbour)])
    graph.remove_nodes_from(nodes_to_delete)
    graph.add_edges_from([(mapping[I5], mapping[E0]), (mapping[I5], mapping[E1]), (mapping[I6], mapping[E1]), (mapping[I6], mapping[E2])])

P9 = Production(production_left_side(), production_modification, left_side_pos_constraints)
