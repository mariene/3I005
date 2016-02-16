# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 23:06:07 2016

@author: Mariène
"""
import TME2 as tme

#codage(liste) qui prend une liste de couples (wi, pi) 
#(la lettre et sa probabilit´e d’apparition) et renvoie l’arbre de codage optimal


def cmpval(x,y):
    if x[1]<y[1]:
        return -1
    elif x[1]==y[1]:
        return 0
    else:
        return 1

#print(dico)    

def liste_couples(d):
    #d = tme.count_ngrams("moby.txt",1)
    liste = list()
    cle = d.keys()
    val = d.values()
    nb = len(d)
    for i in range (nb) :
        couple = (cle[i],val[i])
        liste.append(couple)
    return liste
   
#print(liste_couples(tme.count_ngrams("moby.txt",1)))
liste = liste_couples(tme.count_ngrams("test.txt",1))
liste.sort(cmpval)
print(liste)

#liste =[(('a', 78959), ('c', 23122)),  ('q', 1567), (('v', 8721), ('y', 17209)), ('z', 636)]
#print(liste[0][1][1])
# liste [0] -> (('a', 78959), ('c', 23122))
#liste [0][1] -> ('c', 23122)
# liste [0][1][1] -> 23122

#
#def petit_arbre(couple1, couple2):
#    couple = (couple1, couple2)
#    return couple
#
##print petit_arbre(('a',2),('c',3))
# 
#def arbre (liste):
#    arbre = []
#    sous_arbre_gauche =[]
#    sous_arbre_droit = []
#    for i in liste : 

        
        