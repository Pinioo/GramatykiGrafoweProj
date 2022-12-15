from lib import Production, attr, LABEL, next_nodes
from networkx import Graph

E0, E1, E2, E3, E4, E5, I1, I2, I3, I4, I5, I6 = next_nodes(12)

def __get_node_pos(graph, node_id):
  return graph.nodes[node_id]["x"], graph.nodes[node_id]["y"]

#### PRODUCTION DEFINITION

 #               LEFT SITE                                         RIGHT SITE                 
 #                                                                                                
 #           /------ E0 -------\                                  /-- E0 --\                
 #          /                   \                                /          \               
 #         I1                   I4                             I1           I4              
 #       / |                    | \                           / |           | \             
 #      /  |  /----- E1 ----\   |  \                         /  |  /- E1 -\ |  \            
 #      |  | /    /     \    \  |  |                         |  | /   |    \|  |            
 #      |  I2    /       \    I5   |                         |  I2    |     I5 |            
 #      |    \  /         \  /     |                         |    \   |    /   |            
 #      |     E2           E4      |           ->            |      \ |  /     |            
 #      |   / |            | \     |                         |        E2       |            
 #      |  /  |            |  \    |                         |      / |  \     |            
 #      | /   |            |   \   |                         |    /   |    \   |            
 #      I3    |            |     I6                          |  /     |      \ |            
 #        \   |            |   /                             I3 ----- E3 ---- I6            
 #         \  |            |  /                                                             
 #           E3             E5                                                              




def production_left_side():
     left = Graph()
     left.add_nodes_from([(E0, attr("E")),
         (I1, attr("I")), (I2, attr("I")), (I3, attr("I")), (I4, attr("I")), (I5, attr("I")), (I6, attr("I")),
         (E1, attr("E")), (E2, attr("E")), (E3, attr("E")), (E4, attr("E")), (E5, attr("E"))])
     left.add_edges_from([(E0, I1), (I1, I2), (I1, I3), (I2, E1), (I2, E2), (I3, E2), (E2, E3), (E2, E1), (I3, E3),
                          (E0, I4), (I4, I5), (I4, I6), (I5, E1), (I5, E4), (E4, E5), (E4, I6), (E1, E4), (E5, I6)])

     return left

def production_modification(graph: Graph, mapping: dict) -> Graph:
    # get positions of left site nodes
    x2, y2 = __get_node_pos(graph, mapping[E2])
    x3, y3 = __get_node_pos(graph, mapping[E3])
    x4, y4 = __get_node_pos(graph, mapping[E4])
    x5, y5 = __get_node_pos(graph, mapping[E5])
    
    
    if x2 == x4 and y2 == y4 and x3 == x5 and y3 == y5:
        print(mapping[E4], mapping[E5])
        graph.remove_nodes_from([mapping[E4], mapping[E5]])
        graph.remove_edges_from([(mapping[E1], mapping[E4]), (mapping[E4], mapping[I5]), (mapping[E4], mapping[E5]), (mapping[E4], mapping[I6])])
        graph.add_edges_from([(mapping[I5], mapping[E2]), (mapping[E2], mapping[I6]), (mapping[E3], mapping[I6])])

    

P10 = Production(production_left_side(), production_modification)