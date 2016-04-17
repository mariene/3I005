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
import time
"""------------------------creation du SimpleWeb----------------"""
nanoweb3=creeNanoWeb3( )
nanoweb2=creeNanoWeb2( )
nanoweb1=creeNanoWeb1( )
"""------------------------creation du SimpleWeb----------------"""


"""---------------------internautes se ballade dans le nanoweb----------------------"""
#bob=Internaute(nanoweb1)
#alice = Internaute(nanoweb2)
#camille = Internaute(nanoweb3)

<<<<<<< HEAD
 # bob es t dans l e noeud 3
bob.goTo(3)
alice.goTo(3)
camille.goTo(3)
=======
 # bob est dans le noeud 3
#bob.goTo(0)
#alice.goTo(0)
#camille.goTo(0)
>>>>>>> 5fb7778c04382572cffff302c28f90f86aa8e2a9

# bob se ballade 10000 fois
# ou jusque esp i lon <0.01
#bob.walk(1000,0.1)
#alice.walk(1000,0.1)
#camille.walk(1000,0.1)
"""---------------------internautes se ballade dans le nanoweb----------------------"""


<<<<<<< HEAD
plt.xlabel(u'iteration i')
plt.ylabel(u'epsilon')
plt.title(u"Courbes indiquant la convergences au cours du temps pour les 3 nanoWebs")
x1=np.arange(len(alice.liste_epsilon))
x2=np.arange(len(bob.liste_epsilon))
x3=np.arange(len(camille.liste_epsilon))
p1=plt.plot(x1,alice.liste_epsilon,label=ur"$NanoWeb2$")
p2=plt.plot(x2,bob.liste_epsilon,label=ur"$NanoWeb1$")
p3=plt.plot(x3,camille.liste_epsilon,label=ur"$NanoWeb3$")
plt.legend()
#plt.savefig("graphe.png")

plt.show()
=======

""""-------------------------courbes---------------------------------------"""
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
#plt.savefig("graphe.png")
#
#plt.show()
""""-------------------------courbes---------------------------------------"""
>>>>>>> 5fb7778c04382572cffff302c28f90f86aa8e2a9

"""---------------------------stocker valeurs d'epsilon dans un fichier-----------------------"""
# bob conserve les valeurs de epsilon
# toutes l e s 100 i t e r a t i on s
# dans ce f i c h i e r
#bob.trace (100,"epsilons1.txt")
#alice.trace (100,"epsilons2.txt")
#camille.trace (100,"epsilons3.txt")
"""---------------------------stocker valeurs d'epsilon dans un fichier-----------------------"""

"""-------------------------afficher  distribution de bob --------------------------"""
#bob.getGraphEpsilon()

# bob affiche la frequence de sa presence
# dans chaque noeud durant sa promenade

#print bob.showFrequencies()*bob.graph.matrice,"\n",bob.ti2

#po=Simulation(nanoweb1)
#po.simul(100,0.0005,bob.ti2)
"""-------------------------afficher distribution de bob --------------------------"""


"""Generation d'un graphe ergodique avec generateurErgo()"""
graphErgo = SimpleWeb(20)

graphErgo.generateurErgo()

 

bob_question10 = Internaute(graphErgo)
bob_question10.goTo(0)

start = time.time() #debut

bob_question10.walk(1000,0.001)

print "bob_question10 a mis : ", time.time()-start ," de ms "
#print graphErgo.matrice

pi_0 = np.zeros(graphErgo.taille)
pi_0[3] = 1
simula = Simulation(graphErgo)
start = time.time()
simula.simul(1000,0.001,pi_0)

print "simulation vecteur * matrice a mis : ", time.time()-start," de ms"

start = time.time()
graphErgo.convergePuissance(0.001)
print "simulation puissance matrice a mis : ",time.time() - start, " de ms"

"""Generation d'un graphe ergodique avec generateurErgo()"""


