from productions.P1 import P1
from productions.P10 import P10, production_left_side
from lib import next_nodes, attr, visualize_graph
from networkx import Graph


E0, E1, E2, E3, E4, E5, I1, I2, I3, I4, I5, I6 = next_nodes(12)
x1, y1 = 0, -1
x2, y2 = -2, -2
x0, y0 = 0, 0

if __name__ == "__main__":
    graph = Graph()
    graph.add_nodes_from([(E0, attr("E", -2, 0)),
         (I1, attr("I", -3, -1)), 
         (I2, attr("I", -3, -2)), 
         (I3, attr("I", -3, -3)), 
         (I4, attr("I", -1, -1)), 
         (I5, attr("I", -1, -2)), 
         (I6, attr("I", -1, -3)),
         (E1, attr("E", -2, -1)), 
         (E2, attr("E", -2, -2)), 
         (E3, attr("E", -2, -3)), 
         (E4, attr("E", -2, -2)), 
         (E5, attr("E", -2, -3))])
    graph.add_edges_from([(E0, I1), (I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (E2, E3), (E2, E1), (I3, E3),
                          (E0, I4), (I4, I5), (I4, I6), (I5, E1), (I5, E4), (E4, E5), (E4, I6), (E1, E4), (E5, I6)])
    visualize_graph(graph)
    g10 = P10.perform_modification(graph, level=0)
    visualize_graph(g10)
