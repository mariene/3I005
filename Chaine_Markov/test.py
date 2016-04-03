# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 17:10:44 2016

@author: 3202002
"""

from markov import *
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

graph = SimpleWeb(10)
#graph.liste_node.append(node0)
#graph.liste_node.append(node1)
#graph.liste_node.append(node2)
#graph.liste_node.append(node3)
#graph.liste_node.append(node4)
#graph.liste_node.append(node5)
#graph.liste_node.append(node6)
#graph.liste_node.append(node7)
#graph.liste_node.append(node8)
#graph.liste_node.append(node9)

graph.AddArc(0,9)
graph.AddArc(9,8)
graph.AddArc(8,7)
graph.AddArc(7,6)
graph.AddArc(6,5)
graph.AddArc(5,4)
graph.AddArc(4,3)
graph.AddArc(7,3)
graph.AddArc(3,2)
graph.AddArc(2,4)
graph.AddArc(1,1)
graph.AddArc(2,9)
graph.AddArc(2,9)
#graph.AddArc(1,5)
#graph.AddArc(1,0)

graph.updateProbas()
graph.affiche()
print graph

##############################################graphe########################################


G = nx.DiGraph()
G.add_nodes_from(graph.liste_node) # ajout de noeuds dans graph

labels_nodes = {} #dico permettant de redefinir les labels de noeuds

for node in G.nodes():
    labels_nodes[node] = node.id

H=nx.relabel_nodes(G,labels_nodes)     #graph H qui va s'afficher


liste_edges = [] #variable contenant les arcs

for node in graph.liste_node:
    for arc in node.liste_sort:
        liste_edges.append((arc.tail,arc.head)) 

print liste_edges

H.add_edges_from(liste_edges)
nx.draw(H,with_labels=True)



