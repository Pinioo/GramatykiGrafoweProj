from lib import NoIsomorphicSubgraphException, LABEL
from productions.P12 import P12

import unittest
from networkx import Graph
from networkx import is_isomorphic
import networkx.algorithms.isomorphism as iso
from lib import next_nodes, attr, visualize_graph


class P12_test(unittest.TestCase):
    E1, E2, E3, E4, I = next_nodes(5)
    correct_left_side_graph = Graph()
    correct_left_side_graph.add_nodes_from([
        (E1, attr("E", 0, 0, 1)),
        (E2, attr("E", 0, 1, 1)),
        (E3, attr("E", 1, 1, 1)),
        (E4, attr("E", 1, 0, 1)),
        (I, attr("I", 0.5, 0.5, 1)),
    ])
    correct_left_side_graph.add_edges_from([
        (E1, E2),
        (E2, E3),
        (E3, E4),
        (E4, E1),
        (E1, I),
        (E2, I),
        (E3, I),
        (E4, I),
    ])

    def test_correct_left_side(self):
        E1, E2, E3, E4 = next_nodes(4)
        I1 = next_nodes(1)

        correct_graph = self.correct_left_side_graph.copy()
        visualize_graph(correct_graph)
        correct_graph.nodes[self.I][LABEL] = "i"

        correct_graph.add_nodes_from([
            (E1, attr("E", 0, 0, 2)),
            (E2, attr("E", 0, 1, 2)),
            (E3, attr("E", 1, 1, 2)),
            (E4, attr("E", 1, 0, 2)),
            (I1, attr("I", 0.5, 0.5, 2)),
        ])
        correct_graph.add_edges_from([
            (E1, E2), (E2, E3), (E3, E4), (E4, E1), (E1, I1), (E2, I1), (E3, I1), (E4, I1)
        ])
        correct_graph.add_edges_from([(self.I, I1)])
        visualize_graph(correct_graph)

        new_graph = P12.perform_modification(self.correct_left_side_graph)
        visualize_graph(new_graph)

        self.assertTrue(is_isomorphic(new_graph, correct_graph, node_match=iso.categorical_node_match))

    def test_shouldnt_modify_if_edge_missing(self):
        test_graph = self.correct_left_side_graph.copy()
        test_graph.remove_edge(self.E1, self.E2)
        visualize_graph(test_graph)
        with self.assertRaises(NoIsomorphicSubgraphException):
            P12.perform_modification(test_graph)

    def test_shouldnt_modify_if_node_missing(self):
        test_graph = self.correct_left_side_graph.copy()
        test_graph.remove_node(self.E1)
        visualize_graph(test_graph)
        with self.assertRaises(NoIsomorphicSubgraphException):
            P12.perform_modification(test_graph)

    def test_shouldnt_modify_if_node_with_wrong_etiquete(self):
        test_graph = self.correct_left_side_graph.copy()
        test_graph.nodes[self.E1][LABEL] = "T"
        visualize_graph(test_graph)
        with self.assertRaises(NoIsomorphicSubgraphException):
            visualize_graph(P12.perform_modification(test_graph))


if __name__ == "__main__":
    unittest.main()
