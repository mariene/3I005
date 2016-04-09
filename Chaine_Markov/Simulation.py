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
        self.res=pi0
        
        for i in range(nbIte):
            temp = np.copy(self.res)
            self.res = self.graph.nextStep(np.mat(self.res))
            """
            il nous reste :
            -> calculer epsilon (diff puissance matrice?)
            -> verifier condition epsilon
            -> courbe d'epsilon                        
            """
            eps = abs(np.matrix.max(self.res-temp))
            self.liste_epsilon.append(eps)
            if(eps<epsilon):
                break
            


            

        