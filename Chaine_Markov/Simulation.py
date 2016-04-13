# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 17:01:54 2016

@author: 3202002
"""

import random
from math import *
import numpy as np
from datastructures import *
from internautes import *
from nanowebs import *
class Simulation():
    
    def __init__(self,web):
        """
        Constructeur de la simulation, 
        @param web, le graph qui contient la matrice de transition
        """
        self.graph = web
        self.listepsilon = []
        self.res = []
        self.liste_epsilon = []
    def simul(self,nbIte,epsilon,pi0):
        """
        fonction qui, à chaque pas de temps, calcule πt
        à partir d’un π0, d’un nombre d’itérations limite,
        et toujours d’un seuil epsilon
        """        
        self.res= np.copy(pi0)
        temp = np.copy(pi0)
        
        for i in range(nbIte):
            
            def abs_mat(matrice):
                """
                fonction qui met toutes les valeurs d'une matrice en valeur absolue
                """
                for i in range(len(matrice)):
                    for j in range(len(matrice[0])):
                        matrice[i][j] = abs(matrice[i][j])
                return matrice
            
            self.res = self.graph.nextStep(np.mat(self.res))
            """
            il nous reste :
            -> calculer epsilon (diff puissance matrice?)
            -> verifier condition epsilon
            -> courbe d'epsilon                        
            """
            diff = abs_mat(temp-self.res)
            eps = np.matrix.max(np.matrix(diff))
            
            temp = np.copy(self.res)
            self.liste_epsilon.append(eps)
            if(eps<epsilon):
                break
       

graph3 = creeNanoWeb3()
sim3 = Simulation(graph3)
pi03 = [1,0,0,0,0,0,0,0,0,0]
sim3.simul(1000,0.0001,pi03)
print sim3.liste_epsilon

graph2 = creeNanoWeb2()
sim2 = Simulation(graph2)
pi02 = [1,0,0,0,0,0,0,0,0,0]
sim2.simul(1000,0.0001,pi02)
print sim2.liste_epsilon

graph = creeNanoWeb1()
sim = Simulation(graph)
pi0 = [1,0,0,0,0,0,0,0,0,0]
sim.simul(1000,0.0001,pi0)
print sim.liste_epsilon

plt.xlabel(u'iteration i')
plt.ylabel(u'epsilon')
plt.title(u"Courbes courbes d’epsilon pour les 3 nanoWebs")
x3=np.arange(len(sim3.liste_epsilon))
x2=np.arange(len(sim2.liste_epsilon))
x1=np.arange(len(sim.liste_epsilon))
p1=plt.plot(x1,sim.liste_epsilon,label=ur"$NanoWeb2$")
p2=plt.plot(x2,sim2.liste_epsilon,label=ur"$NanoWeb1$")
p3=plt.plot(x3,sim3.liste_epsilon,label=ur"$NanoWeb3$")
plt.legend()

plt.show()
            

        