from networkx import Graph
from productions.P10 import P10, __get_node_pos
from lib import Production, attr, next_nodes

E0, E1, E2, E3, E4, E5, E6, E7, I1, I2, I3, I4, I5, I6 = next_nodes(14)
x1, y1 = 0, -1
x2, y2 = -2, -2
x0, y0 = 0, 0


def test_wrong_vertex():
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
         (E5, attr("I", -2, -3))])
    graph.add_edges_from([(E0, I1), (I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (E2, E3), (E2, E1), (I3, E3),
                          (E0, I4), (I4, I5), (I4, I6), (I5, E1), (I5, E4), (E4, E5), (E4, I6), (E1, E4), (E5, I6)])
    try:
        P10.perform_modification(graph, level=0)
        assert False
    except Exception:
        assert True


def test_delete_vertex():
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
         (E4, attr("E", -2, -2))])
    graph.add_edges_from([(E0, I1), (I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (E2, E3), (E2, E1), (I3, E3),
                          (E0, I4), (I4, I5), (I4, I6), (I5, E1), (I5, E4), (E4, E5), (E4, I6), (E1, E4), (E5, I6)])
    try:
        P10.perform_modification(graph, level=0)
        assert False
    except Exception:
        assert True


def test_new_vertex_in_half():
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
         (E6, attr("E", -2, -2.5)),
         (E5, attr("I", -2, -3))])

    graph.add_edges_from([(E0, I1), (I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (E2, E3), (E2, E1), (I3, E3),
                          (E0, I4), (I4, I5), (I4, I6), (I5, E1), (I5, E4), (E4, E6), (E6, E5), (E4, I6), (E1, E4), (E5, I6)])
    try:
        P10.perform_modification(graph, level=0)
        assert False
    except Exception:
        assert True


def test_delete_edge():
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
    graph.add_edges_from([(I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (E2, E3), (E2, E1), (I3, E3),
                          (E0, I4), (I4, I5), (I4, I6), (I5, E1), (I5, E4), (E4, E5), (E4, I6), (E1, E4), (E5, I6)])
    try:
        P10.perform_modification(graph, level=0)
        assert False
    except Exception:
        assert True


def test_new_edge_and_new_vertex():
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
         (E5, attr("I", -2, -3)),
         (E7, attr("E", -2, 0))])
    graph.add_edges_from([(E0, I1), (I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (E2, E3), (E2, E1), (I3, E3),
                          (E0, I4), (I4, I5), (I4, I6), (I5, E1), (I5, E4), (E4, E5), (E4, I6), (E1, E4), (E5, I6),
                          (E1, E7)])

    def production_left_side():
        left = Graph()
        left.add_nodes_from([(E0, attr("E", -2, 0)),
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
         (E5, attr("I", -2, -3)),
         (E7, attr("E", -2, 0))])
        left.add_edges_from([(E0, I1), (I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (E2, E3), (E2, E1), (I3, E3),
                          (E0, I4), (I4, I5), (I4, I6), (I5, E1), (I5, E4), (E4, E5), (E4, I6), (E1, E4), (E5, I6),
                          (E1, E7)])

        return left

    def production_modification(graph: Graph, mapping: dict) -> Graph:
        # get positions of left site nodes
        x2, y2 = __get_node_pos(graph, mapping[E2])
        x3, y3 = __get_node_pos(graph, mapping[E3])
        x4, y4 = __get_node_pos(graph, mapping[E4])
        x5, y5 = __get_node_pos(graph, mapping[E5])

        if x2 == x4 and y2 == y4 and x3 == x5 and y3 == y5:
            graph.remove_nodes_from([mapping[E4], mapping[E5]])
            graph.remove_edges_from([(mapping[E1], mapping[E4]), (mapping[E4], mapping[I5]), (mapping[E4], mapping[E5]),
                                     (mapping[E4], mapping[I6])])
            graph.add_edges_from([(mapping[I5], mapping[E2]), (mapping[E2], mapping[I6]), (mapping[E3], mapping[I6])])

    P10_new = Production(production_left_side(), production_modification)

    try:
        P10_new.perform_modification(graph, level=0)
        assert True
    except Exception:
        assert False
