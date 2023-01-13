from lib import attr, next_nodes, NoIsomorphicSubgraphException

import unittest
from networkx import Graph
from networkx import is_isomorphic
import networkx.algorithms.isomorphism as iso

from productions.P13 import P13


class P13_test(unittest.TestCase):

    def test_empty_graph(self):
        with self.assertRaises(NoIsomorphicSubgraphException):
            P13.perform_modification(Graph())

    def test_should_apply_with_vertical_edges(self):
        E0, E1, E2, E3, E4, E5, I1, I2, I3, I4, I5 = next_nodes(11)
        g1 = Graph()
        g1.add_nodes_from([(E0, attr("E", 0, 6)),
                           (I1, attr("I", -1, 4)), (I2, attr("I", -2, 1)), (I3, attr("I", -2, -1)), (I4, attr("I", 1, 4)), (E1, attr("E", 0, 1)), (E2, attr("E", 0, 0)),
                           (E3, attr("E", 0, -1)),
                           (I5, attr("I", 2, 0)), (E4, attr("E", 0, 1)), (E5, attr("E", 0, -1))])
        g1.add_edges_from([(E0, I1), (I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (I3, E3),
                           (E0, I4), (I4, I5), (I5, E4), (I5, E5), (E4, E5), (E1, E2), (E2, E3)])

        g2 = P13.perform_modification(g1)
        self.assertTrue(is_isomorphic(g1, g1, node_match=iso.categorical_node_match))
        self.assertFalse(is_isomorphic(g1, g2, node_match=iso.categorical_node_match))

    def test_should_apply_with_horizontal_edges(self):
        E0, E1, E2, E3, E4, E5, I1, I2, I3, I4, I5 = next_nodes(11)
        g1 = Graph()
        g1.add_nodes_from([(E0, attr("E", 6, 0)),
                           (I1, attr("I", 4, -1)), (I2, attr("I", 1, -2)), (I3, attr("I", -1, -2)), (I4, attr("I", 4, 1)), (E1, attr("E", 1, 0)), (E2, attr("E", 0, 0)),
                           (E3, attr("E", -1, 0)),
                           (I5, attr("I", 0, 2)), (E4, attr("E", 1, 0)), (E5, attr("E", -1, 0))])
        g1.add_edges_from([(E0, I1), (I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (I3, E3),
                           (E0, I4), (I4, I5), (I5, E4), (I5, E5), (E4, E5), (E1, E2), (E2, E3)])

        g2 = P13.perform_modification(g1, level=0)
        self.assertTrue(is_isomorphic(g1, g1, node_match=iso.categorical_node_match))
        self.assertFalse(is_isomorphic(g1, g2, node_match=iso.categorical_node_match))

    def test_should_apply_if_sth_is_adjacent(self):
        E0, E1, E2, E3, E4, E5, I1, I2, I3, I4, I5, E11, E12 = next_nodes(13)
        g1 = Graph()
        g1.add_nodes_from([(E0, attr("E", 6, 0)),
                           (I1, attr("I", 4, -1)), (I2, attr("I", 1, -2)), (I3, attr("I", -1, -2)), (I4, attr("I", 4, 1)), (E1, attr("E", 1, 0)), (E2, attr("E", 0, 0)),
                           (E3, attr("E", -1, 0)), (E11, attr("E", -4, -4)), (E12, attr("E", -5, -5)),
                           (I5, attr("I", 0, 2)), (E4, attr("E", 1, 0)), (E5, attr("E", -1, 0))])
        g1.add_edges_from([(E0, I1), (I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (I3, E3), (I2, E11), (I2, E12),
                           (E0, I4), (I4, I5), (I5, E4), (I5, E5), (E4, E5), (E1, E2), (E2, E3)])

        g2 = P13.perform_modification(g1, level=0)
        self.assertTrue(is_isomorphic(g1, g1, node_match=iso.categorical_node_match))
        self.assertFalse(is_isomorphic(g1, g2, node_match=iso.categorical_node_match))

    def test_shouldnt_modify_if_wrong_labels(self):
        E0, E1, E2, E3, E4, E5, I1, I2, I3, I4, I5 = next_nodes(11)
        graph = Graph()
        graph.add_nodes_from([(E0, attr("E", 0, 6)),
                           (I1, attr("I", -1, 4)), (I2, attr("I", -2, 1)), (I3, attr("I", -2, -1)), (I4, attr("I", 1, 4)), (E1, attr("E", 0, 1)), (E2, attr("E", 0, 0)),
                           (E3, attr("E", 0, -1)),
                           (I5, attr("I", 2, 0)), (E4, attr("E", 0, 1)), (E5, attr("I", 0, -1))])
        graph.add_edges_from([(E0, I1), (I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (I3, E3),
                           (E0, I4), (I4, I5), (I5, E4), (I5, E5), (E4, E5), (E1, E2), (E2, E3)])
        with self.assertRaises(NoIsomorphicSubgraphException):
            P13.perform_modification(graph)

    def test_shouldnt_modify_if_wrong_distances(self):
        E0, E1, E2, E3, E4, E5, I1, I2, I3, I4, I5 = next_nodes(11)
        graph = Graph()
        graph.add_nodes_from([(E0, attr("E", 0, 6)),
                           (I1, attr("I", -1, 4)), (I2, attr("I", -2, 1)), (I3, attr("I", -2, -1)), (I4, attr("I", 1, 4)), (E1, attr("E", 0, 1)), (E2, attr("E", 0, 0)),
                           (E3, attr("E", 0, -1)),
                           (I5, attr("I", 2, 0)), (E4, attr("E", 0, 1)), (E5, attr("E", 0, -2))])
        graph.add_edges_from([(E0, I1), (I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (I3, E3),
                           (E0, I4), (I4, I5), (I5, E4), (I5, E5), (E4, E5), (E1, E2), (E2, E3)])
        with self.assertRaises(NoIsomorphicSubgraphException):
            P13.perform_modification(graph)


if __name__ == "__main__":
    unittest.main()
