from lib import Production, attr, LABEL, next_nodes
from networkx import Graph

EL1, EL2, EL3, EL4, IL = next_nodes(5)

vertically = False


# HELPERS
def __get_node_pos(graph, node_id):
    return graph.nodes[node_id]["x"], graph.nodes[node_id]["y"]


def __get_center_of_four(graph, n1, n2, n3, n4):
    x1, y1 = __get_node_pos(graph, n1)
    x2, y2 = __get_node_pos(graph, n2)
    x3, y3 = __get_node_pos(graph, n3)
    x4, y4 = __get_node_pos(graph, n4)
    return (x1 + x2 + x3 + x4) / 4, (y1 + y2 + y3 + y4) / 4


#### PRODUCTION DEFINITION

#        LEFT SITE                       RIGHT SITE
# 
# (x2, y2)-------- (x4, y4)            E2-------E6------ E4 
#   |    \        /  |                 | \     /| \    /|      
#   |     \      /   |                 |  \   / |  \  / |      
#   |      \    /    |                 |   \ /  |   \/  |      
#   |        I       |       ->        |   I1   |   I2  |      
#   |      /   \     |                 |   / \  |   /\  |      
#   |     /     \    |                 |  /   \ |  /  \ |      
#   |    /       \   |                 | /     \| /    \|      
#   |   /         \  |                 E1-------E5------E3       
# (x1, y1)------- (x3, y3)            


def production_left_side():
    left = Graph()
    left.add_nodes_from([(EL1, attr("E")), (EL2, attr("E")), (EL3, attr("E")), (EL4, attr("E")), (IL, attr("I"))])
    left.add_edges_from([(EL1, EL2), (EL2, EL4), (EL4, EL3), (EL3, EL1), (EL1, IL), (EL2, IL), (EL3, IL), (EL4, IL)])

    return left


def production_modification(graph: Graph, mapping: dict) -> Graph:
    E1, E2, E3, E4, E5, E6 = next_nodes(6)
    I1, I2 = next_nodes(2)
    # calculate the level of the nodes
    level = graph.nodes[mapping[EL1]]["level"] + 1
    # change the left side node label
    graph.nodes[mapping[IL]][LABEL] = "i"

    # get positions of left site nodes
    x1, y1 = __get_node_pos(graph, mapping[EL1])
    x2, y2 = __get_node_pos(graph, mapping[EL2])
    x3, y3 = __get_node_pos(graph, mapping[EL3])
    x4, y4 = __get_node_pos(graph, mapping[EL4])

    if vertically:
        # prepare edges' splitting positions
        e1_mid_x, e1_mid_y = (x1 + x3) / 2, (y1 + y3) / 2
        e2_mid_x, e2_mid_y = (x2 + x4) / 2, (y2 + y4) / 2

        # add new nodes of type "E" in the place where the edges are split
        graph.add_nodes_from([
            (E1, attr("E", x1, y1, level)),
            (E2, attr("E", x2, y2, level)),
            (E3, attr("E", x3, y3, level)),
            (E4, attr("E", x4, y4, level)),
            (E5, attr("E", e1_mid_x, e1_mid_y, level)),
            (E6, attr("E", e2_mid_x, e2_mid_y, level))
        ])

        # prepare centers of subsquares
        i1_x, i1_y = __get_center_of_four(graph, E1, E2, E6, E5)
        i2_x, i2_y = __get_center_of_four(graph, E6, E4, E5, E3)

        # add nodes of type "I" in place of the centers of the nodes
        graph.add_nodes_from([
            (I1, attr("I", i1_x, i1_y, level)),
            (I2, attr("I", i2_x, i2_y, level))])

        # add edges between new nodes
        graph.add_edges_from([(E1, E5), (E5, E3), (E3, E4), (E4, E6), (E6, E2), (E6, E5), (E1, E2)])
        graph.add_edges_from([(E2, I1), (E6, I1), (E5, I1), (E1, I1)])
        graph.add_edges_from([(E3, I2), (E6, I2), (E4, I2), (E5, I2)])

        # add edges between previous level nodes and new nodes
        graph.add_edges_from([(mapping[IL], I1), (mapping[IL], I2)])

    else:
        # prepare edges' splitting positions
        e1_mid_x, e1_mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        e2_mid_x, e2_mid_y = (x3 + x4) / 2, (y3 + y4) / 2

        # add new nodes of type "E" in the place where the edges are split
        graph.add_nodes_from([
            (E1, attr("E", x1, y1, level)),
            (E2, attr("E", x2, y2, level)),
            (E3, attr("E", x3, y3, level)),
            (E4, attr("E", x4, y4, level)),
            (E5, attr("E", e1_mid_x, e1_mid_y, level)),
            (E6, attr("E", e2_mid_x, e2_mid_y, level))
        ])

        # prepare centers of subsquares
        i1_x, i1_y = __get_center_of_four(graph, E2, E5, E6, E4)
        i2_x, i2_y = __get_center_of_four(graph, E1, E5, E6, E3)

        # add nodes of type "I" in place of the centers of the nodes
        graph.add_nodes_from([
            (I1, attr("I", i1_x, i1_y, level)),
            (I2, attr("I", i2_x, i2_y, level))])

        # add edges between new nodes
        graph.add_edges_from([(E1, E5), (E5, E2), (E2, E4), (E4, E6), (E6, E3), (E3, E1), (E5, E6)])
        graph.add_edges_from([(E2, I1), (E4, I1), (E5, I1), (E6, I1)])
        graph.add_edges_from([(E1, I2), (E5, I2), (E6, I2), (E3, I2)])

        # add edges between previous level nodes and new nodes
        graph.add_edges_from([(mapping[IL], I1), (mapping[IL], I2)])


P2 = Production(production_left_side(), production_modification)
