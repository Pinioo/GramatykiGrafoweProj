from lib import attr, next_nodes, NoIsomorphicSubgraphException, LABEL
from productions.P3 import P3

import unittest
from networkx import Graph
from networkx import is_isomorphic
import networkx.algorithms.isomorphism as iso

class P3_test(unittest.TestCase):
    
    E1, E2, E3, E4, I = next_nodes(5)
    graph_skeleton = Graph()
    graph_skeleton.add_nodes_from([
        (E1, attr("E", 0, 0, 1)), 
        (E2, attr("E", 0, 1, 1)), 
        (E3, attr("E", 1, 1, 1)), 
        (E4, attr("E", 1, 0, 1)), 
        (I, attr("I", 0.5, 0.5, 1)),
    ])
    graph_skeleton.add_edges_from([
        (E1, E2), 
        (E2, E3), 
        (E3, E4), 
        (E4, E1), 
        (E1, I), 
        (E2, I), 
        (E3, I), 
        (E4, I), 
    ])

    def __add_subgraph_edges(self, graph, e1, e2, e3, e4, i):
        graph.add_edges_from([(e1, e2), (e2, e3), (e3, e4), (e4, e1), (e1, i), (e2, i), (e3, i), (e4, i)])

    def test_correct_left_side(self):
        E1, E2, E3, E4, E5, E6, E7, E8, E9 = next_nodes(9)
        I1, I2, I3, I4 = next_nodes(4)

        correct_graph = self.graph_skeleton.copy()
        correct_graph.nodes[self.I][LABEL] = "i"

        correct_graph.add_nodes_from([
            (E1, attr("E", 0, 0, 2)), 
            (E2, attr("E", 0.5, 0, 2)), 
            (E3, attr("E", 1, 0, 2)),
            (E4, attr("E", 0, 0.5, 2)),
            (E5, attr("E", 0.5, 0.5, 2)),
            (E6, attr("E", 1, 0.5, 2)),
            (E7, attr("E", 0, 1, 2)),
            (E8, attr("E", 0.5, 1, 2)),
            (E9, attr("E", 1, 1, 2)),
        ])

        correct_graph.add_nodes_from([
            (I1, attr("I", 0.25, 0.25, 2)),
            (I2, attr("I", 0.75, 0.25, 2)),
            (I3, attr("I", 0.25, 0.75, 2)),
            (I4, attr("I", 0.75, 0.75, 2)),
        ])

        self.__add_subgraph_edges(correct_graph, E1, E2, E5, E4, I1)
        self.__add_subgraph_edges(correct_graph, E2, E3, E6, E5, I2)
        self.__add_subgraph_edges(correct_graph, E4, E5, E8, E7, I3)
        self.__add_subgraph_edges(correct_graph, E5, E6, E9, E8, I4)

        correct_graph.add_edges_from([
            (self.I, I1), 
            (self.I, I2), 
            (self.I, I3), 
            (self.I, I4),
        ])

        new_graph = P3.perform_modification(self.graph_skeleton)

        self.assertTrue(is_isomorphic(new_graph, correct_graph, node_match=iso.categorical_node_match))

    def test_empty_graph(self):
        with self.assertRaises(NoIsomorphicSubgraphException):
            P3.perform_modification(Graph())
    
    def test_shouldnt_modify_if_lowercased_i(self):
        test_graph = self.graph_skeleton.copy()
        test_graph.nodes[self.I][LABEL] = "i"
        with self.assertRaises(NoIsomorphicSubgraphException):
            P3.perform_modification(test_graph)

    def test_shouldnt_modify_if_no_i(self):
        test_graph = self.graph_skeleton.copy()
        test_graph.remove_node(self.I)
        with self.assertRaises(NoIsomorphicSubgraphException):
            P3.perform_modification(test_graph)

    def test_shouldnt_modify_if_not_a_full_square(self):
        test_graph = self.graph_skeleton.copy()
        test_graph.remove_node(self.E1)
        with self.assertRaises(NoIsomorphicSubgraphException):
            P3.perform_modification(test_graph)

    def test_shouldnt_modify_if_edge_is_divided(self):
        test_graph = self.graph_skeleton.copy()
        E, = next_nodes(1)
        test_graph.remove_edge(self.E1, self.E2)
        test_graph.add_nodes_from([(E, attr("E", 0, 0.5, 1))])
        test_graph.add_edges_from([
            (self.E1, E),
            (self.E2, E),
        ])
        with self.assertRaises(NoIsomorphicSubgraphException):
            P3.perform_modification(test_graph)

if __name__ == "__main__":
    unittest.main()