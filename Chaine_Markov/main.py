# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 23:16:36 2016

@author: Mariène
"""

from nanowebs import *
from internautes import Internaute
from Simulation import Simulation
import matplotlib.pyplot as plt
import numpy as np

 #creat ion du SimpleWeb
nanoweb3=creeNanoWeb3( )
nanoweb2=creeNanoWeb2( )
nanoweb1=creeNanoWeb1( )

# Bob se ba l lade dans l e nanoweb
bob=Internaute(nanoweb1)
alice = Internaute(nanoweb2)
camille = Internaute(nanoweb3)

 # bob es t dans l e noeud 3
bob.goTo(4)
alice.goTo(4)
camille.goTo(4)

# bob se ba l lade 10000 f o i s
# ou jusque esp i lon <0.01
bob.walk(1000,0.001)
alice.walk(1000,0.001)
camille.walk(1000,0.001)

#plt.xlabel(u'iteration i')
#plt.ylabel(u'epsilon')
#plt.title(u"Courbes indiquant la convergences au cours du temps pour les 3 nanoWebs")
#x1=np.arange(len(alice.liste_epsilon))
#x2=np.arange(len(bob.liste_epsilon))
#x3=np.arange(len(camille.liste_epsilon))
#p1=plt.plot(x1,alice.liste_epsilon,label=ur"$NanoWeb2$")
#p2=plt.plot(x2,bob.liste_epsilon,label=ur"$NanoWeb1$")
#p3=plt.plot(x3,camille.liste_epsilon,label=ur"$NanoWeb3$")
#plt.legend()
#
#plt.show()

# bob conserve les valeurs de epsilon
# toutes l e s 100 i t e r a t i on s
# dans ce f i c h i e r
bob.trace (100,"epsilons1.txt")
alice.trace (100,"epsilons2.txt")
camille.trace (100,"epsilons3.txt")

bob.getGraphEpsilon()

# bob a f f i ch e la frequence de sa presence
# dans chaque noeud durant sa promenade

#print bob.showFrequencies()*bob.graph.matrice,"\n",bob.ti2

po=Simulation(nanoweb1)
po.simul(100,0.0005,bob.ti2)
