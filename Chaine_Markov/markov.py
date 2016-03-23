# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 16:14:34 2016

@author: 3202002
"""

from math import *
import numpy as np
#Node,Arc,simple web
class Node():
    def __init__(self,identifiant):
        self.id = identifiant
        self.liste_ent = []
        self.liste_sort=[]        

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



class SimpleWeb():
    def __init__(self,taille):
        """
        @param taille, la taille maximale du nombre de noeud dans le graphe
        la liste_node est une liste vide par défaut.
        """
        self.liste_node = []
        self.matrice = zeros(taille,taille)
    
    def AddArc(tail,head):
        """
        @param tail, id du noeud sortant
        @param head, id du noeud entrant
        Création d'un nouvel arc, du tail à head
        et puis on ajoute cet arc dans les bonnes listes des noeuds
        """
        Arc = Arc(tail,head)
        liste_node[tail].liste_sort.append(Arc)
        liste_node[head].liste_ent.append(Arc)
        
    def updateProbas():
        """
        mettre à jour les probabilités suivant la proposition 
        faite par PageRank
        """        
        for node in liste_node:
            proba = 1./len(node.liste_sort)
            for arc in node.liste_sort:
                arc.prob = proba
              