# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 16:14:34 2016

@author: 3202002
"""

import random
from math import *
import numpy as np
import matplotlib.pyplot as plt

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
        #print nodeID
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
        
        fichier.write("la derniere valeur ("+str(i)+" eme) est: "+str(self.liste_epsilon[len(self.liste_epsilon)-1]))
        
        fichier.close()
    
    def getGraphEpsilon(self):
        plt.xlabel(u'iteration i')
        plt.ylabel(u'epsilon')
        plt.title(u"Courbes indiquant la convergences au cours du temps pour les 3 nanoWebs")
        x=np.arange(len(self.liste_epsilon))
        plt.plot(x,self.liste_epsilon)
        plt.show()

        
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
        """
        Fonction permettant de faire balader l'internaute.
        Il s'arrete a nbPas pas, ou un epsilon plus petit que e
        """
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
    
    
    def showFrequencies(self):
        """
        affiche la frequence
        """
       
        somme = 0.0
        
        for i in range (len(self.ti2)):
            somme += self.ti2[i]
            
        liste =[]
        
        for j in range (len(self.ti2)):
            liste.append(self.ti2[j]/somme)
        
        return np.mat(liste)
        