from lib import attr, next_nodes, NoIsomorphicSubgraphException

import unittest
from networkx import Graph
from networkx import is_isomorphic
import networkx.algorithms.isomorphism as iso

from productions.P1 import P1

class P1_test(unittest.TestCase):

    def test_correct_left_side(self):
        El, = next_nodes(1)
        graph_skeleton = Graph()
        graph_skeleton.add_nodes_from([(El, attr("El"))])
        new_graph = P1.perform_modification(graph_skeleton)

        E1, E2, E3, E4, I, el = next_nodes(6)
        correct_graph = Graph()
        correct_graph.add_nodes_from([
            (E1, attr("E", 0, 0, 1)), 
            (E2, attr("E", 0, 1, 1)), 
            (E3, attr("E", 1, 1, 1)), 
            (E4, attr("E", 1, 0, 1)), 
            (I, attr("I", 0.5, 0.5, 1)),
            (el, attr("el", 0, 0, 0)),
        ])
        correct_graph.add_edges_from([
            (E1, E2), 
            (E2, E3), 
            (E3, E4), 
            (E4, E1), 
            (E1, I), 
            (E2, I), 
            (E3, I), 
            (E4, I), 
            (el, I),
        ])
        self.assertTrue(is_isomorphic(new_graph, correct_graph, node_match=iso.categorical_node_match))

    def test_empty_graph(self):
        with self.assertRaises(NoIsomorphicSubgraphException):
            P1.perform_modification(Graph())
    
    def test_shouldnt_modify_if_lowercased(self):
        el, = next_nodes(1)
        graph_skeleton = Graph()
        graph_skeleton.add_nodes_from([(el, attr("el"))])
        with self.assertRaises(NoIsomorphicSubgraphException):
            P1.perform_modification(graph_skeleton)

if __name__ == "__main__":
    unittest.main()