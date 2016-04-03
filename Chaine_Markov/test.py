# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 17:10:44 2016

@author: 3202002
"""

from markov import *
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

graph = SimpleWeb(10)

graph.AddArc(0,1)
graph.AddArc(0,4)
graph.AddArc(1,2)
graph.AddArc(2,4)
<<<<<<< HEAD
graph.AddArc(1,1)
graph.AddArc(2,9)
graph.AddArc(2,9)
#graph.AddArc(1,5)
#graph.AddArc(1,0)

=======
graph.AddArc(2,3)
graph.AddArc(3,9)
graph.AddArc(4,2)
graph.AddArc(4,5)
graph.AddArc(5,6)
graph.AddArc(6,5)
graph.AddArc(6,7)
graph.AddArc(7,8)
graph.AddArc(8,7)
>>>>>>> fcdd1929ca9a89d0bdb32323b3a6b6e7a82e1bbf
graph.updateProbas()

print graph

bob = Internaute(graph)
"""
bob.goTo(3)
print bob.ti, bob.ti2
bob.goTo(9)
print bob.ti, bob.ti2
bob.goTo(8)
print bob.ti, bob.ti2
"""
bob.walk(3000,0.0002)

bob.trace(100,"epsilon_values.txt")


##############################################graphe########################################

#
#G = nx.DiGraph()
#G.add_nodes_from(graph.liste_node) # ajout de noeuds dans graph
#
#labels_nodes = {} #dico permettant de redefinir les labels de noeuds
#
#for node in G.nodes():
#    labels_nodes[node] = node.id
#
#H=nx.relabel_nodes(G,labels_nodes)     #graph H qui va s'afficher
#
#
#liste_edges = [] #variable contenant les arcs
#
#for node in graph.liste_node:
#    for arc in node.liste_sort:
#        liste_edges.append((arc.tail,arc.head)) 
#
#print liste_edges
#
#H.add_edges_from(liste_edges)
#nx.draw(H,with_labels=True)



