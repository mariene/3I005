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
""" ---------------------Generation des trois nanowebs -----------------"""
graph1 = creeNanoWeb1()
graph2 = creeNanoWeb2()
graph3 = creeNanoWeb3()
""" ---------------------Generation des trois nanowebs -----------------"""


"""---------------------Simulation avec un internaute appele "bob"------------------"""
#bob = Internaute(graph)
#
#bob.goTo(3)
#print bob.ti, bob.ti2
#bob.goTo(9)
#print bob.ti, bob.ti2
#bob.goTo(8)
#print bob.ti, bob.ti2

#bob.walk(3000,0.0002)
"""---------------------Simulation avec un internaute appele "bob"------------------"""


"""--------------------calcul de convergence avec puissance matrice --------------"""
graph3.convergePuissance(0.001)
graph2.convergePuissance(0.001)
graph1.convergePuissance(0.001)

print graph1.liste_eps
print graph3.liste_eps
print graph2.liste_eps
"""--------------------calcul de convergence avec puissance matrice --------------"""



"""Generation d'un graphe ergodique avec generateurErgo()"""
#graphErgo = SimpleWeb(9)
#
#graphErgo.generateurErgo()
#
#print graphErgo.matrice

"""Generation d'un graphe ergodique avec generateurErgo()"""



"""Affichage des courbes d'epsilon en fonction des nombres d'iterations"""
#plt.xlabel(u'iteration i')
#plt.ylabel(u'epsilon')
#plt.title(u"Courbes indiquant la convergences au cours du temps pour les 3 nanoWebs")
#x1=np.arange(len(graph1.liste_eps))
#x2=np.arange(len(graph2.liste_eps))
#x3=np.arange(len(graph3.liste_eps))
#p1=plt.plot(x1,graph1.liste_eps,label=ur"$NanoWeb1$")
#p2=plt.plot(x2,graph2.liste_eps,label=ur"$NanoWeb2$")
#p3=plt.plot(x3,graph3.liste_eps,label=ur"$NanoWeb3$")
#plt.legend()
#plt.savefig("graphe.png")

#plt.show()
"""Affichage des courbes d'epsilon en fonction des nombres d'iterations"""






"""------------------------graphe----------------------"""

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

"""------------------------graphe----------------------"""