from productions.P13 import P13
from lib import attr, visualize_graph, next_nodes
from networkx import Graph

E0, E1, E2, E3, E4, E5, I1, I2, I3, I4, I5, I6 = next_nodes(12)

if __name__ == "__main__":
    g1 = Graph()
    g1.add_nodes_from([(E0, attr("E")),
        (I1, attr("I")), (I2, attr("I")), (I3, attr("I")), (I4, attr("I")), (E1, attr("E", -1, -1)), (E2, attr("E", 0, 0)), (E3, attr("E", 1, 1)),
        (I5, attr("I")), (I6, attr("I")), (E4, attr("E", -1, -1)), (E5, attr("E", 1, 1))])
    g1.add_edges_from([(E0, I1), (I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (I3, E3),
                         (E0, I4), (I4, I5), (I5, E4), (I5, E5), (E4, E5)])

    g2 = P13.perform_modification(g1, level=0)

    visualize_graph(g1)
    visualize_graph(g2)
