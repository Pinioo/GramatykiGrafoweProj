from lib import Production, attr, LABEL, next_nodes
from networkx import Graph

EL1, EL2, EL3, EL4, IL = next_nodes(5)

# HELPERS
def __add_subgraph_edges(graph, e1, e2, e3, e4, i):
  graph.add_edges_from([(e1, e2), (e2, e3), (e3, e4), (e4, e1), (e1, i), (e2, i), (e3, i), (e4, i)])

def __get_node_pos(graph, node_id):
  return graph.nodes[node_id]["x"], graph.nodes[node_id]["y"]

def __get_center_of_four(graph, n1, n2, n3, n4):
  x1, y1 = __get_node_pos(graph, n1)
  x2, y2 = __get_node_pos(graph, n2)
  x3, y3 = __get_node_pos(graph, n3)
  x4, y4 = __get_node_pos(graph, n4)
  return (x1+x2+x3+x4)/4, (y1+y2+y3+y4)/4


#### PRODUCTION DEFINITION

# LEFT SITE
# (x3, y3) ---- edge 3 ---- (x4, y4)
#   |                         |
#   |                         | 
#   |                         |
#  edge 4                   edge 2
#   |                         |
#   |                         |
#   |                         |
#   |                         |
# (x1, y1) ---- edge 1 ---- (x2, y2)
def production_left_side():
    left = Graph()
    left.add_nodes_from([(EL1, attr("E")), (EL2, attr("E")), (EL3, attr(
        "E")), (EL4, attr("E")), (IL, attr("I"))])
    left.add_edges_from([(EL1, EL2), (EL2, EL4), (EL4, EL3), (EL3, EL1), (EL1, IL), (EL2, IL), (EL3, IL), (EL4, IL)])

    return left

def production_modification(graph: Graph, mapping: dict) -> Graph:
  E1, E2, E3, E4, E5, E6, E7, E8, E9 = next_nodes(9)
  I1, I2, I3, I4 = next_nodes(4)
  # calculate the level of the nodes
  level = graph.nodes[mapping[EL1]]["level"]+1
  # change the left side node label
  graph.nodes[mapping[IL]][LABEL] = "i"

  # get positions of left site nodes
  x1, y1 = __get_node_pos(graph, mapping[EL1])
  x2, y2 = __get_node_pos(graph, mapping[EL2])
  x3, y3 = __get_node_pos(graph, mapping[EL3])
  x4, y4 = __get_node_pos(graph, mapping[EL4])

  # prepare edges' splitting positions
  e1_mid_x, e1_mid_y = (x1+x2)/2, (y1+y2)/2
  e2_mid_x, e2_mid_y = (x2+x4)/2, (y2+y4)/2
  e3_mid_x, e3_mid_y = (x3+x4)/2, (y3+y4)/2
  e4_mid_x, e4_mid_y = (x3+x1)/2, (y3+y1)/2

  # add new nodes of type "E" in the place where the edges are split
  graph.add_nodes_from([
    (E1, attr("E", x1, y1, level)), 
    (E2, attr("E", e1_mid_x, e1_mid_y, level)), 
    (E3, attr("E", x2, y2, level)),
    (E4, attr("E", e4_mid_x, e4_mid_y, level)),
    (E5, attr("E", (e1_mid_x+e3_mid_x)/2, (e2_mid_y+e4_mid_y)/2, level)),
    (E6, attr("E", e2_mid_x, e2_mid_y, level)),
    (E7, attr("E", x3, y3, level)),
    (E8, attr("E", e3_mid_x, e3_mid_y, level)),
    (E9, attr("E", x4, y4, level))])

  # prepare centers of subsquares
  i1_x, i1_y = __get_center_of_four(graph, E1, E2, E4, E5)
  i2_x, i2_y = __get_center_of_four(graph, E2, E3, E5, E6)
  i3_x, i3_y = __get_center_of_four(graph, E4, E5, E7, E8)
  i4_x, i4_y = __get_center_of_four(graph, E5, E6, E8, E9)

  # add nodes of type "I" in place of the centers of the nodes
  graph.add_nodes_from([
    (I1, attr("I", i1_x, i1_y, level)),
    (I2, attr("I", i2_x, i2_y, level)),
    (I3, attr("I", i3_x, i3_y, level)),
    (I4, attr("I", i4_x, i4_y, level))])

  # add edges between new nodes
  __add_subgraph_edges(graph, E1, E2, E5, E4, I1)
  __add_subgraph_edges(graph, E2, E3, E6, E5, I2)
  __add_subgraph_edges(graph, E4, E5, E8, E7, I3)
  __add_subgraph_edges(graph, E5, E6, E9, E8, I4)

  # add edges between previous level nodes and new nodes
  graph.add_edges_from([(mapping[IL], I1), (mapping[IL], I2), (mapping[IL], I3), (mapping[IL], I4)])

P3 = Production(production_left_side(), production_modification)
