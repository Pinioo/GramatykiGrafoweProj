from lib import Production, attr, next_nodes
from networkx import Graph

E0, E1, E2, E3, E4, E5, I1, I2, I3, I4, I5, I6 = next_nodes(11)

#### PRODUCTION DEFINITION

# LEFT SITE
#
#      ----------- E0 ------------
#     /                           \
#    I1                            I4
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
#    I1                         I4
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


# TODO: Move x, y positions to method that helps find the subgraph
def production_left_side():
    left = Graph()
    left.add_nodes_from([(E0, attr("E")),
        (I1, attr("I")), (I2, attr("I")), (I3, attr("I")), (I4, attr("I")), (E1, attr("E", x1, y1)), (E2, attr("E"), (x1+x2)/2, (y1+y2)/2), (E3, attr("E", x1, y1)),
        (I5, attr("I")), (I6, attr("I")), (E4, attr("E", x1, y1)), (E5, attr("E", x2, y2))])
    left.add_edges_from([(E0, I1), (I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (I3, E3),
                         (E0, I4), (I4, I5), (I5, E4), (I5, E5), (E4, E5)])

    return left

def production_modification(graph: Graph, mapping: dict) -> Graph:
  # Remove nodes we don't need
  graph.remove_nodes_from([E4, E5])
  # Connect I5 to nodes at same posisions as deleted nodes
  graph.add_edges_from([(I5, E1), (I5, E3)])

P2 = Production(production_left_side(), production_modification)
