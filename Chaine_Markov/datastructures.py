# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 22:23:00 2016

@author: Mariène
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#Node,Arc,simple web
class Node():
    def __init__(self,identifiant):
        self.id = identifiant
        self.liste_ent = []
        self.liste_sort=[]     
        
    def __str__(self):
        return "I'm a node, my ID is "+str(self.id)+"\n"

class Arc():
    
    def __init__(self,tail,head):
        
        """
        constructeur 
        @param tail, l'id du noeud sortant
        @param head, l'id du noeud entrant
        et la valeur de prob est initialisée à 0 par défaut.
        """
        
        self.prob = 0.0
        self.tail = tail
        self.head = head
        
        
    def __str__(self):
        
        string = "I'm an edge, from "+str(self.tail)+" to "+str(self.head)
        string += " with a proba " + str(self.prob)+"\n" 
        return string
     
    def equals(self,arc):
        return arc.head == self.head and arc.tail == self.tail

       
class SimpleWeb():
    
    def __init__(self,taille):
        
        """
        @param taille, la taille maximale du nombre de noeud dans le graphe
        la liste_node est une liste vide par défaut.
        """
        self.taille = taille
        self.liste_node = []
        self.matrice = np.zeros((taille,taille))
        for i in range(taille):
            self.liste_node.append(Node(i))
        
    def __str__(self):
        
        string = "I'm the graph, I have got "+str(len(self.liste_node))+" nodes.\n"
        string += " They are:\n"
        
        for node in self.liste_node:
            string += node.__str__()
        
        string += "My edges are:\n"
        
        for node in self.liste_node:
            for arc in node.liste_sort:
                string += arc.__str__()
                
        return string
        
        
    def AddArc(self,tail,head):
        
        """
        @param tail, id du noeud sortant
        @param head, id du noeud entrant
        Création d'un nouvel arc, du tail à head (pas de doublon)
        et puis on ajoute cet arc dans les bonnes listes des noeuds
        """

        #liste_node_id est la variable stockant la liste d'identifiants des noeuds du graph
        liste_node_id = [node.id for node in self.liste_node]
        #si un noeud n'est pas dans le graph alors Exception   
        if(tail not in liste_node_id or head not in liste_node_id):
            raise Exception("impossible d'ajouter l'arc "+str(tail)+" "+str(head))
            
            
        arc1 = Arc(tail,head)

         #verifier l'unicité de l'arc
        for node in self.liste_node:
            for arc2 in node.liste_sort:
                if arc2.equals(arc1):
                    raise Exception("impossible d'ajouter deux arcs identiques")


        for node in self.liste_node:
            if node.id == tail:
                node.liste_sort.append(arc1)
            if node.id ==head:
                node.liste_ent.append(arc1)
        #updateProbas() 
        
       # self.matrice[tail][head]=1
     
    def getGraph(self,filename):
        G = nx.DiGraph()
        G.add_nodes_from(self.liste_node) # ajout de noeuds dans graph
        
        labels_nodes = {} #dico permettant de redefinir les labels de noeuds
        
        for node in G.nodes():
            labels_nodes[node] = node.id
        
        H=nx.relabel_nodes(G,labels_nodes)     #graph H qui va s'afficher
        
        liste_edges = [] #variable contenant les arcs
        
        for node in self.liste_node:
            for arc in node.liste_sort:
                liste_edges.append((arc.tail,arc.head)) 
        
        print liste_edges
        
        H.add_edges_from(liste_edges)
        nx.draw(H,with_labels=True)
        plt.savefig(filename) # save as png
        plt.show()
       
    def affiche (self):
        print self.matrice
        
    def updateProbas(self):
        
        """
        mettre à jour les probabilités suivant la matrice 
        faite par PageRank
        """        
        
        for node in self.liste_node:
            if len(node.liste_sort)!=0: 
            # si ce noeud a au moins 1 arc sortant
                proba = 1./len(node.liste_sort)
                for arc in node.liste_sort:
                    arc.prob = proba
                    self.matrice[arc.tail][arc.head] = proba
            else:
                self.matrice[node.id][node.id] = 1
        

    def nextStep(self,pi_t):
        """
        calcule le pi_t+1 a partir de pi_t
        """
        return pi_t*(self.matrice)
        
    
    def convergePuissance(self,epsilon):
        """
        les valeurs d'epsilon sont calculées ici avec la difference entre deux puissances
        de matrice de transition.
        """
        eps = 1
        puissM = self.matrice
        while(eps > epsilon):
            temp = np.copy(puissM)
            puissM = self.matrice*puissM
            eps = np.matrix.max(temp-puissM)
            