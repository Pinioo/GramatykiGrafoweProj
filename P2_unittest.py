from productions.P1 import P1
from productions.P2 import P2
from lib import attr, next_nodes
from networkx import Graph
import unittest

""" TESTS SCENARIOS:
1: change node label
2: delete vertex from graph
3: add vertex to graph between two vertices
4: delete vertex
"""


class P2_test(unittest.TestCase):

    def test_wrong_vertex(self):
        """ Scenario 1 """
        g1 = Graph()
        EL, E7 = next_nodes(2)
        g1.add_nodes_from([(EL, attr("El", 0, 0, 0))])
        g2 = P1.perform_modification(g1, level=0)
        g2.nodes[27]['label'] = 'I'

        with self.assertRaises(Exception):
            P2.perform_modificationa(g2, level=1)

    def test_delete_vertex(self):
        """ Scenario 2 """
        g1 = Graph()
        EL, E7 = next_nodes(2)
        g1.add_nodes_from([(EL, attr("El", 0, 0, 0))])
        g2 = P1.perform_modification(g1, level=0)
        g2.remove_node(8)
        with self.assertRaises(Exception):
            P2.perform_modification(g2, level=1)

    def test_new_vertex_in_half(self):
        """ Scenario 3 """
        g1 = Graph()
        EL, = next_nodes(1)
        g1.add_nodes_from([(EL, attr("El", 0, 0, 0))])
        g2 = P1.perform_modification(g1, level=0)
        g3 = P2.perform_modification(g2, level=1)
        E7, = next_nodes(1)
        g3.add_nodes_from([(E7, attr("E", 1, 1, 1))])
        g3.remove_edges_from([(17, 18)])
        g3.add_edges_from([(17, E7), (E7, 18)])
        with self.assertRaises(Exception):
            P2.perform_modification(g3, level=1)

    def test_delete_vertex(self):
        """ Scenario 4 """
        g1 = Graph()
        EL = next_nodes(1)
        g1.add_nodes_from([(EL, attr("El", 0, 0, 0))])
        g2 = P1.perform_modification(g1, level=0)
        with self.assertRaises(Exception):
            g3 = P2.perform_modification(g2, level=0)
            g3.remove_edges_from([(17, 18)])
        with self.assertRaises(Exception):
            P2.perform_modification(g3, level=1)


if __name__ == "__main__":
    unittest.main()
