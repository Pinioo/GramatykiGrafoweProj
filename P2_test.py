from productions.P1 import P1
from productions.P2 import P2
from lib import next_nodes, attr, visualize_graph
from networkx import Graph


if __name__ == "__main__":
    g1 = Graph()
    EL, = next_nodes(1)
    g1.add_nodes_from([(EL, attr("El", 0, 0, 0))])
    g2 = P1.perform_modification(g1, level=0)
    g3 = P2.perform_modification(g2, level=1)
    visualize_graph(g2)
    visualize_graph(g3)