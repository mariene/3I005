# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:51:23 2016

@author: 3202002
"""
import random
import matplotlib.pyplot as plt

# Exercice 1
def moyenne(l):
    s=0
    for i in l:
        s=s+i
    s = s / (len(l))
    return s

liste = [5,5,6,4,4,6,2]
#print(moyenne(liste))

def histo(l):
    d = dict()
    for i in l :
        cpt = 0
        for j in l:
            if j == i :
                cpt = cpt+1
        d[i]= cpt
    return d

#print(histo(liste))


def histo_trie(l):
    d = histo(l)
    liste = list()
    cle = d.keys()
    val = d.values()
    nb = len(d)
    for i in range (nb) :
        couple = (cle[i],val[i])
        liste.append(couple)
    return liste
   
#print(histo_trie(liste))
#plt.hist(liste)

# Exercice 2

def paquet():
    c = ["C","K","P","T"]
    liste=list()
    for k in c:
        for j in range (1,14):
            couple = (j,k)
            liste.append(couple)
    random.shuffle(liste)
    return liste

#print(paquet())

def meme_position(p,q):
    indice = list()
    for i in range (52):
        if p[i] == q[i]:
            indice.append(i)
    return indice


#a = paquet()
#b = paquet()
#print(a)
#print(b)
#print (meme_position(a,b))

#plt.plot(liste_x,liste_y)
#plt.show()            

# Exercice 3

def de():
    nb = random.randint(1,6)
    return nb

#print(de())

#somme
def kde(k):
    return sum([de() for i in range (k)])
    

def proba_somme_bis(k,n):
    lancers = [kde(k) for i in range (n)] # liste somme
    return histo(lancers)

def proba_somme(k,n):
    d=dict()
    for i in range(0,n):
        som=0
        for i in range(1,k+1):
            val=de()
            som+=val
        if som in d:
            d[som]+=1
        else:
            d[som]=1.
    for elt in d.keys():
        d[elt]=d[elt]/n #pour obtenir proba (freq/nb tot)
    sorted(d)
    return d
    
#print (proba_somme(2,10))  
#print (proba_somme_bis(2,10))
    
def roulette(dist): #ou dist est un dico {(evnt,proba)}
    val = random.random() #valeur entre 0 et 1
    print (val)
    aire = 0
    for elt in dist.keys():
        aire+= dist[elt]	 #pour definir l'encadrement courant
        if aire >= val:
            return elt   #on a alors determine le bon evenement		
    print('on a eu un prb pour le rand() verification a faire..')

dist=dict([('P',0.7),('F',0.3)])
#print(roulette(dist))
d = dict([(1,0.2),(2,0.1),(3,0.3),(4,0.25),(5,0.15),(6,0.1)])
#print(roulette(d))