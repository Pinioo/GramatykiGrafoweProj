from productions.P1 import P1
from productions.P3 import P3
from lib import next_nodes, attr, visualize_graph
from networkx import Graph


if __name__ == "__main__":
    g1 = Graph()
    EL, = next_nodes(1)
    g1.add_nodes_from([(EL, attr("El", 0, 0, 0))])
    g2 = P1.perform_modification(g1, level=0)
    g3 = P3.perform_modification(g2, level=1)
    g4 = P3.perform_modification(g3, level=1)
    # g5 = P3.perform_modification(g4, level=2)
    visualize_graph(g3)
    visualize_graph(g4)
    # visualize_graph(g5)