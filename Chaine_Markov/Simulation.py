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
            
graph = creeNanoWeb3()
sim = Simulation(graph)
pi0 = [1,0,0,0,0,0,0,0,0,0]
sim.simul(1000,0.001,pi0)
print sim.liste_epsilon
            

        