# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 23:16:36 2016

@author: Mariène
"""

from nanowebs import creeNanoWeb1
from internautes import Internaute

 #creat ion du SimpleWeb
nanoweb=creeNanoWeb1 ( )

# Bob se ba l lade dans l e nanoweb
bob=Internaute(nanoweb)

 # bob es t dans l e noeud 3
bob.goTo(2)

# bob se ba l lade 10000 f o i s
# ou jusque esp i lon <0.01
#bob.walk(1,0.001)

# bob conserve les valeurs de epsilon
# toutes l e s 100 i t e r a t i on s
# dans ce f i c h i e r
#bob.trace (100,"epsilons.txt")

# bob a f f i ch e la frequence de sa presence
# dans chaque noeud durant sa promenade
<<<<<<< HEAD
#print bob.showFrequencies()*bob.graph.matrice,"\n",bob.ti2
=======
print "PI t*p =",bob.showFrequencies()*bob.graph.matrice,"\n PIt+1",bob.ti2
>>>>>>> refs/remotes/origin/master