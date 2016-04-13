# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 17:10:44 2016

@author: 3202002
"""

from markov import *
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from nanowebs import *


graph = creeNanoWeb3()

print graph.matrice


#bob = Internaute(graph)
"""
bob.goTo(3)
print bob.ti, bob.ti2
bob.goTo(9)
print bob.ti, bob.ti2
bob.goTo(8)
print bob.ti, bob.ti2
"""
#bob.walk(3000,0.0002)

graph.convergePuissance(0.001)

print graph.liste_eps

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



