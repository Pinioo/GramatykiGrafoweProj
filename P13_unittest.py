from lib import attr, next_nodes, NoIsomorphicSubgraphException

import unittest
from networkx import Graph

from productions.P13 import P13


class P13_test(unittest.TestCase):

    def test_empty_graph(self):
        with self.assertRaises(NoIsomorphicSubgraphException):
            P13.perform_modification(Graph())

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
