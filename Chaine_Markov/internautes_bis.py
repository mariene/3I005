# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 23:13:46 2016

@author: Mariène
"""

from datastructures import *
import random

class Internaute():   
    def __init__(self, web):
        """
        constructeur d'internaute, qui associe l'internaute au graph passé par argument
        et garde sa position actuelle en attribut position 0 par défaut
        """
        
        self.graph = web
        self.pos = 0
        self.ti=[]
        self.ti2=[]
        self.diff=[]
        self.noeud=[]
        self.liste_epsilon=[]
        
        for i in range(len(web.liste_node)):
            self.ti.append(0)
            self.ti2.append(0)
            self.noeud.append(0)
    
    
    def __str__(self):
        return "I'm the robo, I have ",self.nbPas," steps"
    
    
    def goTo(self,node):
        """
        permet au robot de se positionner dans le noeud passé en paramètre
        """
        self.pos = node  
       
        self.ti = np.copy(self.ti2)
        self.ti2[node] = self.ti2[node]+1 # on incremente le compteur du noeud de 1
       # print self.pos
        self.noeud[node]=self.noeud[node]+1
      
    
    def trace(self,nbIte,filename):
        """
        internaute conserve les valeurs de epsilon
        toutes les 100 iterations
        dans ce fichier 
        """              
        """
        for i in range (self.nbPas): 
            a = self.epsilon()
            if (i%nbIte == 0):
                fichier.write("\n"+str(a))
        """
        fichier = open(filename,"w")
        for i in range (len(self.diff)):
            if (i%nbIte == 0):
                fichier.write("\n"+str(self.diff[i]))
        
            
        
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
        
    """
    def walk(self,nbPas,e):
        self.nbPas=nbPas
        #possibleNodes=[]
       # j=0
        for i in range(nbPas-1):
            
            possibleNodes = (self.graph.matrice[self.pos]) #une liste contenant les probas d'aller a un noeud i
            #print possibleNodes
            possibleNodes = np.cumsum(possibleNodes) #transforme cette liste en une liste proba cumulee
            proba = random.random()
            
            #prev_pos = self.pos #position Ti
            for j in range (len(possibleNodes)) :
                #print "j" + str(j) + " "+str(possibleNodes[j]) + " "+ str(proba > possibleNodes[j])               
                # j < len(possibleNodes) pour de boucler sur une liste contenant que des 0             
                if (proba < possibleNodes[j]) or (proba == possibleNodes[j]):
                    break
           
            eps = self.epsilon()  
            print eps
            self.goTo(j)
             
            if eps <= e:
                break
     """       
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
            
    def showFrequencies(self):
        somme =0.0
        for i in range (len(self.noeud)):
            somme = somme + self.noeud[i]
            
        liste =[]
        for j in range (len(self.noeud)):
            liste.append(self.noeud[j]/somme)
        return liste
        
