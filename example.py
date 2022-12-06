from lib import next_nodes, attr, LABEL, visualize_graph
from networkx import Graph
from productions.P1 import P1

if __name__ == "__main__":
    g1 = Graph()
    sm, gt = 0, 1
    el = next_nodes(1)
    g1.add_nodes_from([(el, attr("el", 0, 0, 0))])
    g2 = P1.perform_modification(g1)
    print(g1.nodes[(6,)])
    print(g2.nodes)
    visualize_graph(g1)
    visualize_graph(g2)
