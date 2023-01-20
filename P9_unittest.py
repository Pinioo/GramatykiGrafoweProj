from lib import attr, next_nodes, NoIsomorphicSubgraphException, LABEL, visualize_graph
from productions.P9 import P9

import unittest
from networkx import Graph
from networkx import is_isomorphic
import networkx.algorithms.isomorphism as iso

class P9_test(unittest.TestCase):
    E0, E1, E2, E3, E4, E5, i0, i1, I2, I3, i4, I5, I6 = next_nodes(13)
    correct_graph = Graph()
    correct_graph.add_nodes_from([
      (i0, attr("i", 0, 0)),
      (i1, attr("i", -1, -1)),
      (I2, attr("I", -1, -2)),
      (I3, attr("I", -2, -3)),
      (i4, attr("i", 1, -1)),
      (E0, attr("E", 0, -2)),
      (E1, attr("E", 0, -2.5)),
      (E2, attr("E", 0, -3)),
      (I5, attr("I", 1, -2)),
      (I6, attr("I", 2, -3)),
      (E3, attr("E", 0, -2)),
      (E4, attr("E", 0, -2.5)),
      (E5, attr("E", 0, -3)),
    ])
    correct_graph.add_edges_from([
      (i0, i1),
      (i1, I2),
      (i1, I3),
      (I2, E0),
      (I2, E1),
      (I3, E1),
      (I3, E2),
      (E0, E1),
      (E1, E2),
      (i0, i4),
      (i4, I5),
      (i4, I6),
      (I5, E3),
      (I5, E4),
      (I6, E4),
      (I6, E5),
      (E3, E4),
      (E4, E5)
    ])

    def test_correct_graph(self):
        graph_after_production = Graph()
        E0, E1, E2, i0, i1, I2, I3, i4, I5, I6 = next_nodes(10)
        graph_after_production.add_nodes_from([
          (i0, attr("i", 0, 0)),
          (i1, attr("i", -1, -1)),
          (I2, attr("I", -1, -2)),
          (I3, attr("I", -2, -3)),
          (i4, attr("i", 1, -1)),
          (E0, attr("E", 0, -2)),
          (E1, attr("E", 0, -2.5)),
          (E2, attr("E", 0, -3)),
          (I5, attr("I", 1, -2)),
          (I6, attr("I", 2, -3)),
        ])
        graph_after_production.add_edges_from([
          (i0, i1),
          (i1, I2),
          (i1, I3),
          (I2, E0),
          (I2, E1),
          (I3, E1),
          (I3, E2),
          (E0, E1),
          (E1, E2),
          (i0, i4),
          (i4, I5),
          (i4, I6),
          (I5, E0),
          (I5, E1),
          (I6, E1),
          (I6, E2),
        ])
        new_graph = P9.perform_modification(self.correct_graph)
        self.assertTrue(is_isomorphic(new_graph, graph_after_production, node_match=iso.categorical_node_match))

    def test_shouldnt_modify_without_node(self):
        with self.assertRaises(NoIsomorphicSubgraphException):
            new_graph = self.correct_graph.copy()
            new_graph.remove_node(self.E5)
            P9.perform_modification(new_graph)
    
    def test_shouldnt_modify_without_edge(self):
        new_graph = self.correct_graph.copy()
        new_graph.remove_edge(self.i1, self.I2)
        with self.assertRaises(NoIsomorphicSubgraphException):
            P9.perform_modification(new_graph)

    def test_shouldnt_modify_if_incorrect_label(self):
        new_graph = self.correct_graph.copy()
        new_graph.nodes[self.I2][LABEL] = "i"
        with self.assertRaises(NoIsomorphicSubgraphException):
            P9.perform_modification(new_graph)

    def test_shouldnt_modify_if_different_coords(self):
        new_graph = self.correct_graph.copy()
        new_graph.nodes[self.E1]["x"] = 0.1
        with self.assertRaises(NoIsomorphicSubgraphException):
            P9.perform_modification(new_graph)
    def test_should_modify_if_part_of_bigger_graph(self):
        new_graph = self.correct_graph.copy()
        E0, E1 = next_nodes(2)
        new_graph.add_nodes_from([E0,E1])
        new_graph.add_edges_from([
          (E0, self.E0),
          (E1, self.E1),
          (E0, E1)
        ])
        P9.perform_modification(new_graph)

    def test_should_modify_bigger_graph_correctly(self):
        new_graph = self.correct_graph.copy()
        E0, E1 = next_nodes(2)
        new_graph.add_nodes_from([
          (E0, attr("E", -3, -4)),
          (E1, attr("E", 3, -4)),
        ])
        new_graph.add_edges_from([
          (E0, self.E0),
          (E1, self.E1),
          (E0, E1)
        ])

        graph_after_production = Graph()
        E0, E1, E2, i0, i1, I2, I3, i4, I5, I6, E3, E4 = next_nodes(12)
        graph_after_production.add_nodes_from([
          (i0, attr("i", 0, 0)),
          (i1, attr("i", -1, -1)),
          (I2, attr("I", -1, -2)),
          (I3, attr("I", -2, -3)),
          (i4, attr("i", 1, -1)),
          (E0, attr("E", 0, -2)),
          (E1, attr("E", 0, -2.5)),
          (E2, attr("E", 0, -3)),
          (I5, attr("I", 1, -2)),
          (I6, attr("I", 2, -3)),
          (E3, attr("E", -3, -4)),
          (E4, attr("E", 3, -4)),
        ])
        graph_after_production.add_edges_from([
          (i0, i1),
          (i1, I2),
          (i1, I3),
          (I2, E0),
          (I2, E1),
          (I3, E1),
          (I3, E2),
          (E0, E1),
          (E1, E2),
          (i0, i4),
          (i4, I5),
          (i4, I6),
          (I5, E0),
          (I5, E1),
          (I6, E1),
          (I6, E2),
          (E3, E4),
          (E3, E0),
          (E4, E1),
        ])

        new_graph = P9.perform_modification(new_graph)
        visualize_graph(new_graph)
        visualize_graph(graph_after_production)

        self.assertTrue(is_isomorphic(new_graph, graph_after_production, node_match=iso.categorical_node_match))


if __name__ == "__main__":
    unittest.main()