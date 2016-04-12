# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 23:16:36 2016

@author: Mariène
"""

from nanowebs import *
from internautes import Internaute
from Simulation import Simulation
 #creat ion du SimpleWeb
nanoweb=creeNanoWeb3 ( )

# Bob se ba l lade dans l e nanoweb
bob=Internaute(nanoweb)

 # bob es t dans l e noeud 3
bob.goTo(4)

# bob se ba l lade 10000 f o i s
# ou jusque esp i lon <0.01
bob.walk(1000,0.001)

# bob conserve les valeurs de epsilon
# toutes l e s 100 i t e r a t i on s
# dans ce f i c h i e r
bob.trace (100,"epsilons.txt")

bob.getGraphEpsilon()

# bob a f f i ch e la frequence de sa presence
# dans chaque noeud durant sa promenade

#print bob.showFrequencies()*bob.graph.matrice,"\n",bob.ti2

po=Simulation(nanoweb)
po.simul(100,0.0005,bob.ti2)
