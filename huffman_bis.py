# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 23:06:07 2016

@author: Mariène
"""
import TME2 as tme
from heapq import *
#codage(liste) qui prend une liste de couples (wi, pi) 
#(la lettre et sa probabilit´e d’apparition) et renvoie l’arbre de codage optimal


def cmpval(x,y):
    if x[1]>y[1]:
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

def changer(liste):
    liste2=[]
    for i in range (len(liste)):
        liste2.append((liste[i][1],liste[i][0]))
    return liste2
    
#print(liste_couples(tme.count_ngrams("moby.txt",1)))
liste = liste_couples(tme.count_ngrams("test.txt",1))
#liste.sort(cmpval)
#print(changer(liste))

#return l'arbre sous forme [(poids, {dictionnaire -> arbre de codage})]
def arbre (liste):
    liste = changer(liste)
    liste.sort(cmpval)
    while len(liste) >= 2: 
        occ1, noeud1 = heappop(liste) #heapop(liste) renvoie un couple 
        occ2, noeud2 = heappop(liste)
        #ordonne la liste en arbre binaire 
        # heappush(liste dans lequel on rajoute un truc, le truc a rajouter)
        # et heappush ordonne en ordre croissant 
        heappush(liste,(occ1+occ2,{0: noeud1, 1:noeud2}))    
    return liste

print(arbre(liste))   
        