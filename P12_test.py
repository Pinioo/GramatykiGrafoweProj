from productions.P1 import P1
from productions.P12 import P12
from productions.P2 import P2
from lib import next_nodes, attr, visualize_graph
from networkx import Graph


if __name__ == "__main__":
    g1 = Graph()
    EL, = next_nodes(1)
    g1.add_nodes_from([(EL, attr("El", 0, 0, 0))])
    g2 = P1.perform_modification(g1, level=0)
    g2_2 = P2.perform_modification(g2, level=1)
    g3 = P12.perform_modification(g2_2, level=2)
    g3_2 = P12.perform_modification(g3, level=2)
    visualize_graph(g2)
    visualize_graph(g2_2)
    visualize_graph(g3)
    visualize_graph(g3_2)
