from productions.P1 import P1
from productions.P2 import P2
from lib import next_nodes, attr, visualize_graph
from networkx import Graph


if __name__ == "__main__":
    g1 = Graph()
    EL = next_nodes(1)
    g1.add_nodes_from([(EL, attr("el", 0, 0, 0))])
    g2 = P1.perform_modification(g1, level=0)
    g3 = P2.perform_modification(g2, level=1)
    g4 = P2.perform_modification(g3, level=2)
    g5 = P2.perform_modification(g4, level=2)
    g6 = P2.perform_modification(g5, level=2)
    g7 = P2.perform_modification(g6, level=2)
    visualize_graph(g1)
    visualize_graph(g2)
    visualize_graph(g3)
    visualize_graph(g4)
    visualize_graph(g5)
    visualize_graph(g6)
    visualize_graph(g7)
    visualize_graph(g7, level=3)
