# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 16:09:31 2016

@author:   3202002
"""
from math import *
import numpy as np
import matplotlib.pyplot as plt
import collections
#je suis un commentaire#
alpha = {'A':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,'I':1,'K':1,'L':1,'M':1,'N':1,'P':1,'Q':1,'S':1,'T':1,'V':1,'W':1,'Y':1,'-':1}

#lis le fichier Dtrain et enleve les commentaires
#@return liste avec que les sequences
def lire_texte():
    #contenu = ""
    #contenu = open("Dtrain.txt", "r")
    contenu = open("test_bis.txt", "r")
    #contenu = mon_fichier.read()

    ss_liste = ""
    liste=[]
#    i = 1
    for i in contenu:
        if (i[0] <> '>'):
            ss_liste = ""
            for char in i:
                if (char <>'\n'):
                    ss_liste = ss_liste + char
            liste.append(ss_liste)
    contenu.close()
    return liste

matrice = lire_texte()
#print len(matrice)

#print matrice 

# @param liste, plus exactement la liste qu'on a obtenue avec lire_texte()
# @return une liste contenant plusieurs dictionnaires
# chaque colonne a un dictionnaire : {acide aminé:nb occurence} 
def comparaison(liste):
    d =[]
    dico ={}
    for i in range (48): 
        dico = alpha.copy()     
        for j in range (len(liste)):
            for char in alpha.keys():
                if (liste[j][i] == char):
                   #print char
                   dico[char]= dico[char] + 1
        d.append(dico)
    return d
   
c = comparaison(matrice)
#print c

# @param n = entier, correspondant au nb occurence de l'acide aminé
# @return son poids 
def calPoids (n):
    w = n / (5643.0 + 21.0) # M = nb ligne sans commentaire et q = taille de l'alphabet 
    return w
    
#print calPoids(c[47]['V'])

#pour chaque colonne on calcule le poids de chaque acide aminé 
def weight(liste):
    poids = {}
    l2 = []
    for i in range(len(liste)) : 
        poids = {}
        for l in liste[i].keys():
            #print l
            a = calPoids(liste[i][l])
            poids.update({l:a})
        l2.append(poids)
    return l2

we = weight(c)

#print we

# on calcule ici l'entropie relative d'une distribution d'une seule colonne
def e_relative(p): 
    somme = log(21,2)
    for key in p.keys() :#pour chaque acide amine
        #print p[key]
        somme += p[key]* log(p[key],2)
    return somme

def e_touteColonne(liste):
    liste_entropie = []    
    for i in range(len(liste)):
        res = e_relative(liste[i]) # entropie relative pour chaque colonne
        liste_entropie.append(res)
    return liste_entropie # et les valeurs d'entropies sont stockées dans l'ordre
    
liste_entropie = e_touteColonne(we)
#print(liste_entropie) 
#print(liste_entropie.index(max(liste_entropie)))

#@param liste est une liste de dico contenant les poids de chaque acide amine
def liste_argmax(liste): 
    liste_max = []
    for i in range(len(liste)):
        indice_max = liste[i].values().index(max(liste[i].values()))
        lettre_max = liste[i].keys()[indice_max]
        #on stocke les lettres dominantes de chaque colonne dans la liste_max
        liste_max.append(lettre_max)
    return liste_max
#print we[1]
liste = liste_argmax(we)
#print len(liste)

#############################graphe###############################################
def graphe():
    plt.xlabel(u'position i')
    plt.ylabel(u'entropie relative')
    plt.title(u"graphe représentant l'entropie relative en fonction de la position i")
    x=np.arange(48)
    plt.plot(x,liste_entropie)
    #plt.show()
#graphe()
##################################################################################

#nb occurence de chaque lettre pour chaque alignement
def f(liste):
    d =[]
    dico ={}
    for i in range (len(liste)): 
        dico = alpha.copy()     
        for j in range (48):
            for char in alpha.keys():
                if (liste[i][j] == char):
                   #print char
                   dico[char]= dico[char] + 1
        d.append(dico)
    return d
   
freq = f(lire_texte())


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
