# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 16:14:34 2016

@author: 3202002
"""

import random
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
        
        self.affiche()
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
            else:
                self.matrice[node.id][node.id] = 1
        


class Internaute():
    
    def __init__(self, web):
        """
        constructeur d'internaute, qui associe l'internaute au graph passé par argument
        et garde sa position actuelle en attribut position 0 par défaut
        """
        
        self.graph = web
        self.pos = "undefined"
        #self.cpt_node = []
        self.ti = []
        self.ti2 = []
        self.diff = []
        self.liste_epsilon = [] #une liste qui contient les valeurs d'epsilon (superflu?)
        for i in range(len(web.liste_node)): # initialise deux listes de compteurs à zeros
            self.ti.append(0)
            self.ti2.append(0)
        
        
    def __str__(self):
        return "I'm the robo, I have at the node "+str(pos)
     
     
    def goTo(self,nodeID):
        """
        permet au robot de se positionner dans le noeud passé en paramètre
        """
        self.pos = nodeID
        
        self.ti = np.copy(self.ti2)
        self.ti2[nodeID] = self.ti2[nodeID]+1 # on incremente le compteur du noeud de 1
        
        #print "je suis a ",nodeID
    
    def trace(self,nbIte, filename):
        """
        internaute conserve les valeurs de epsilon
        toutes les 100 iterations
        dans ce fichier 
        """        
        
        fichier = open(filename,"w")
        
        for i in range(len(self.liste_epsilon)):
            if i%nbIte == 0: 
                value = self.liste_epsilon[i]
                fichier.write(str(i)+" eme valeur d'epsilon est: "+str(value)+"\n")
        
        fichier.write("la derniere valeur est: "+str(self.liste_epsilon[len(self.liste_epsilon)-1]))
        
        fichier.close()
        
    def epsilon(self):
        """
        calcule la valeur d'epsilon, la fonction est appelee a chaque deplacement de l'internaute
        """
    
        somme1=np.sum(self.ti)
        somme2=np.sum(self.ti2)            
        #comme ti2 contient la liste de compteur à l'instant t+1, donc les deux sommes sont differentes

        for i in range(len(self.ti2)):  
        
            self.diff.append(abs(float(self.ti[i])/somme1-float(self.ti2[i])/somme2)) 
            #pour chaque noeud on calcule leur difference de compteur entre l'instant ti et ti+1
        self.liste_epsilon.append(max(self.diff))
        
        self.diff = []
        
        return self.liste_epsilon[len(self.liste_epsilon)-1]
    
    
    def walk(self,nbPas, e):
        if self.pos=="undefined":  # quand on appelle cette fonction juste apres la creation de l'objet
            self.goTo(0)  # on met l'internaute sur le noeud 0 par defaut
            
            
        possibleNodes=[]
        for i in range(nbPas):  # on s'arrete lorsque l'on a fait nbPas deplacement
            
            possibleNodes = self.graph.matrice[self.pos] #une liste contenant les probas d'aller a un noeud i
            
            possibleNodes = np.cumsum(possibleNodes) #transforme cette liste en une liste proba cumulee
            
            proba = random.random()
        
            goal = 0
            
            for goal in range(len(possibleNodes)):
                if(proba>possibleNodes[goal]):
                    goal = goal + 1
                else:
                    break
                """ 
                goal < len(possibleNodes) pour eviter de boucler sur une liste contenant que des 0 (qui ne doit pas se passer normalement)
                a la fin de cette boucle, goal est le noeud ou l'internaute doit aller
                """
                
               
            
            self.goTo(goal) #faire deplacer l'internaute
            
            if self.epsilon() <= e: #on s'arrete lorsqu'on a une convergence
                break
    