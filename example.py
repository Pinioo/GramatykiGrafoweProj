from lib import next_nodes, attr, LABEL, visualize_graph
from networkx import Graph
from test_production import TestProduction

if __name__ == "__main__":
    g1 = Graph()
    sm, gt = 0, 1
    E1, E2, E3, E4, I = next_nodes(5)
    g1.add_nodes_from([
        (E1, attr("E", sm, sm)),
        (E2, attr("E", gt, sm)),
        (E3, attr("E", gt, gt)),
        (E4, attr("E", sm, gt)),
        (I, attr("I", 0.5, 0.5)),
    ])
    g1.add_edges_from([(E1, E2), (E2, E3), (E3, E4), (E4, E1), (I, E1), (I, E2), (I, E3), (I, E4)])
    g2 = TestProduction.perform_modification(g1)
    visualize_graph(g1)
    visualize_graph(g2)
