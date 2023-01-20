from productions.P1 import P1
from productions.P2 import P2, P2_vert, P2_horiz
from productions.P3 import P3
from productions.P12 import P12
from productions.P13 import P13, P13_horiz, P13_vert
from productions.P15 import P15
from productions.P15b import P15b
from lib import attr, visualize_graph, next_nodes
from networkx import Graph


if __name__ == "__main__":
    g0 = Graph()
    EL, = next_nodes(1)
    g0.add_nodes_from([(EL, attr("El", 0, 0, 0))])
    g1 = P1.perform_modification(g0, level=0)
    g2 = P3.perform_modification(g1, level=1)
    g3 = g2
    g3 = P2_vert.perform_modification(g3, level=2)
    g3 = P2_horiz.perform_modification(g3, level=2)
    g3 = P2_horiz.perform_modification(g3, level=2)
    g3 = P12.perform_modification(g3, level=2)
    g4 = g3
    for i in range(2):
        g4 = P13_horiz.perform_modification(g4)
    g5 = g4
    g5 = P13.perform_modification(g5)
    g5 = P15b.perform_modification(g5)
    visualize_graph(g1)
    visualize_graph(g2)
    visualize_graph(g3)
    visualize_graph(g4)
    visualize_graph(g5)
    visualize_graph(g3, level=3)
    visualize_graph(g4, level=3)
    visualize_graph(g5, level=3)
