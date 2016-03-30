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
        


class Internaute():
    
    def __init__(self, web):
        """
        constructeur d'internaute, qui associe l'internaute au graph passé par argument
        et garde sa position actuelle en attribut position 0 par défaut
        """
        
        self.graph = web
        self.pos = 0
        self.cpt_node = []
        for i in range(len(web.liste_node)):
            self.cpt_node.append(0)
        
    def __str__(self):
        return "I'm the robo, I have ",nbPas," steps"
     
    def goTo(self,node):
        """
        permet au robot de se positionner dans le noeud passé en paramètre
        """
        self.pos = node.id
    
    def trace(nbIte, filename):
        """
        internaute conserve les valeurs de epsilon
        toutes les 100 iterations
        dans ce fichier 
        """        
        
        fichier = open(filename,"w")
        
        
    def walk(nbPas, epsilon):
        
        for i in range(nbPas-1):
            prev_pos = self.pos #position Ti
            dis = web.matrice[prev_pos] #la distribution de proba de la position Ti
            dis = [prob for ]
            epsi = max(self.cpt_node)
            if epsi <= epsilon:
                break