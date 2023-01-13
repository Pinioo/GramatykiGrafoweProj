from productions.P1 import P1
from productions.P2 import P2
from productions.P3 import P3
from productions.P13 import P13
from lib import attr, visualize_graph, next_nodes
from networkx import Graph


def test_only_P13():
    E0, E1, E2, E3, E4, E5, I1, I2, I3, I4, I5 = next_nodes(11)
    g1 = Graph()
    g1.add_nodes_from([(E0, attr("E", 0, 6)),
                       (I1, attr("I", -1, 4)), (I2, attr("I", -2, 1)), (I3, attr("I", -2, -1)), (I4, attr("I", 1, 4)), (E1, attr("E", 0, 1)), (E2, attr("E", 0, 0)),
                       (E3, attr("E", 0, -1)),
                       (I5, attr("I", 2, 0)), (E4, attr("E", 0, 1)), (E5, attr("E", 0, -1))])
    g1.add_edges_from([(E0, I1), (I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (I3, E3),
                       (E0, I4), (I4, I5), (I5, E4), (I5, E5), (E4, E5), (E1, E2), (E2, E3)])

    g2 = P13.perform_modification(g1, level=0)

    visualize_graph(g1)
    visualize_graph(g2)


def test_only_P13_horiz():
    E0, E1, E2, E3, E4, E5, I1, I2, I3, I4, I5 = next_nodes(11)
    g1 = Graph()
    g1.add_nodes_from([(E0, attr("E", 6, 0)),
                       (I1, attr("I", 4, -1)), (I2, attr("I", 1, -2)), (I3, attr("I", -1, -2)), (I4, attr("I", 4, 1)), (E1, attr("E", 1, 0)), (E2, attr("E", 0, 0)),
                       (E3, attr("E", -1, 0)),
                       (I5, attr("I", 0, 2)), (E4, attr("E", 1, 0)), (E5, attr("E", -1, 0))])
    g1.add_edges_from([(E0, I1), (I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (I3, E3),
                       (E0, I4), (I4, I5), (I5, E4), (I5, E5), (E4, E5), (E1, E2), (E2, E3)])

    g2 = P13.perform_modification(g1, level=0)

    visualize_graph(g1)
    visualize_graph(g2)

def test_P13_with_sth_adjacent():
    E0, E1, E2, E3, E4, E5, I1, I2, I3, I4, I5, E11, E12 = next_nodes(13)
    g1 = Graph()
    g1.add_nodes_from([(E0, attr("E", 6, 0)),
                       (I1, attr("I", 4, -1)), (I2, attr("I", 1, -2)), (I3, attr("I", -1, -2)), (I4, attr("I", 4, 1)), (E1, attr("E", 1, 0)), (E2, attr("E", 0, 0)),
                       (E3, attr("E", -1, 0)), (E11, attr("E", -4, -4)), (E12, attr("E", -5, -5)),
                       (I5, attr("I", 0, 2)), (E4, attr("E", 1, 0)), (E5, attr("E", -1, 0))])
    g1.add_edges_from([(E0, I1), (I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (I3, E3), (E4, E11), (E5, E12),
                       (E0, I4), (I4, I5), (I5, E4), (I5, E5), (E4, E5), (E1, E2), (E2, E3)])

    g2 = P13.perform_modification(g1, level=0)

    visualize_graph(g1)
    visualize_graph(g2)

if __name__ == "__main__":
    test_only_P13()
    test_only_P13_horiz()
    test_P13_with_sth_adjacent()
