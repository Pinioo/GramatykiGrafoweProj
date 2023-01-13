from productions.P1 import P1
from productions.P3 import P3
from productions.P9 import P9
from productions.P10 import P10
from productions.P13 import P13
from lib import next_nodes, attr, visualize_graph
from networkx import Graph

from networkx.algorithms import isomorphism as iso


if __name__ == "__main__":
  E0, E1, E2, E3, E4, E5, i0, i1, I2, I3, i4, I5, I6 = next_nodes(13)
  g1 = Graph()
  g1.add_nodes_from([
    (i0, attr("i", 0, 0)),
    (i1, attr("i", -1, -1)),
    (I2, attr("I", -1, -2)),
    (I3, attr("I", -2, -3)),
    (i4, attr("i", 1, -1)),
    (E0, attr("E", 0, -2)),
    (E1, attr("E", 0, -2.5)),
    (E2, attr("E", 0, -3)),
    (I5, attr("I", 1, -2)),
    (I6, attr("I", 2, -3)),
    (E3, attr("E", 0, -2)),
    (E4, attr("E", 0, -2.5)),
    (E5, attr("E", 0, -3)),
  ])
  g1.add_edges_from([(i0, i1), (i1, I2), (i1, I3), (I2, E0), (I2, E1), (I3, E1), (I3, E2), (E0, E1), (E1, E2),
                        (i0, i4), (i4, I5), (i4, I6), (I5, E3), (I5, E4), (I6, E4), (I6, E5), (E3, E4), (E4, E5)])

  visualize_graph(g1)
  g2 = P9.perform_modification(g1)  
  visualize_graph(g2)

  graph = Graph()
  EL, = next_nodes(1)
  graph.add_nodes_from([(EL, attr("El", 0, 0, 0))])
  graph = P1.perform_modification(graph, level=0)
  graph = P3.perform_modification(graph, level=1)
  graph = P3.perform_modification(graph, level=2)
  graph = P3.perform_modification(graph, level=2)
  graph = P3.perform_modification(graph, level=2)
  graph = P3.perform_modification(graph, level=2)
  visualize_graph(graph, level=3)
  graph = P9.perform_modification(graph)
  graph = P9.perform_modification(graph)
  graph = P9.perform_modification(graph)
  visualize_graph(graph, level=3)
