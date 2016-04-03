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
        #self.cpt_node = []
        #self.epsilon = 0.0
        self.ti=[]
        self.ti2=[]
        self.diff=[]
        self.nbPas =0
        self.noeud=[]
        
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
        self.ti[node]=self.ti2[node]
        self.ti2[node] = self.ti2[node]+1 # on incremente le compteur du noeud de 1
       # print self.pos
        self.noeud[node]=self.noeud[node]+1
    
    def trace(self,nbIte,filename):
        """
        internaute conserve les valeurs de epsilon
        toutes les 100 iterations
        dans ce fichier 
        """        
        fichier = open(filename,"w")
        for i in range (self.nbPas): 
            a = self.epsilon()
            if (i%nbIte == 0):
                fichier.write("\n"+str(a))
        """
        for i un range (len(self.diff)):
            if (i%nbIte == 0):
                fichier.write("\n"+str(self.diff[i]))
        """
            
        
    def epsilon(self,noeud):        
        somme1=0.0
        somme2=0.0
        for i in range(len(self.ti2)):
            somme1 = somme1 + self.ti[i]
            somme2 = somme2 + self.ti2[i]
        
        if (somme1 ==0):
            div1 =0
        else :
            div1 = self.ti[noeud]/somme1
            
        if (somme2 ==0):
            div2=0 
        else :    
            div2= self.ti2[noeud]/somme2
        
        print "div2 " + str(div2)
        print "div1 " + str(div1)
        
        diff = abs(div1-div2)
        self.diff.append(diff)
        print self.diff
        return max(self.diff)
        
    
    def walk(self,nbPas,e):
        self.nbPas=nbPas
        #possibleNodes=[]
       # j=0
        for i in range(nbPas-1):
            
            possibleNodes = (self.graph.matrice[self.pos]) #une liste contenant les probas d'aller a un noeud i
            #print possibleNodes
            possibleNodes = np.cumsum(possibleNodes) #transforme cette liste en une liste proba cumulee
            proba = random.random()
            #print proba
           # print possibleNodes
          
            
            #prev_pos = self.pos #position Ti
            for j in range (len(possibleNodes)) :
                #print "j" + str(j) + " "+str(possibleNodes[j]) + " "+ str(proba > possibleNodes[j])

                
                # j < len(possibleNodes) pour de boucler sur une liste contenant que des 0             
                if (proba < possibleNodes[j]) or (proba == possibleNodes[j]):
                #if ((proba < possibleNodes[j]) and  (proba > possibleNodes[j+1])) or (proba == possibleNodes[j]) :
                    break
                
                #print j
            #print j
            #self.pos = j
            
            eps = self.epsilon(self.pos)  
            print eps
            
            #self.ti=self.ti2
            self.goTo(j)

                
            if eps <= e:
                break
            
    def showFrequencies():
        somme =0.0
        for i in range (len(self.noeud)):
            somme = somme + self.noeud[i]
        
        liste =[]
        for j in range (len(self.noeud)):
            liste[j]=self.noeud[j]/somme
        return liste
        
