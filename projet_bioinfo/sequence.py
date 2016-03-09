# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 16:09:31 2016
@author:   3202002
"""
from math import *
import numpy as np
import matplotlib.pyplot as plt
import collections

alpha = {'A':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,'I':1,'K':1,'L':1,'M':1,'N':1,'P':1,'Q':1,'R':1,'S':1,'T':1,'V':1,'W':1,'Y':1,'-':1}

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

def lire_texte_bis(texte):
    #contenu = ""
    contenu = open(texte, "r")
    #contenu = open("test_bis.txt", "r")
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
   


# @param n = entier, correspondant au nb occurence de l'acide aminé
# @return son poids 
def calPoids (n):
    w = n / (5643.0 + 21.0) # M = nb ligne sans commentaire et q = taille de l'alphabet 
    return w
    


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
    

#@param liste est une liste de dico contenant les poids de chaque acide amine
def liste_argmax(liste): 
    liste_max = []
    for i in range(len(liste)):
        indice_max = liste[i].values().index(max(liste[i].values()))
        lettre_max = liste[i].keys()[indice_max]
        #on stocke les lettres dominantes de chaque colonne dans la liste_max
        liste_max.append(lettre_max)
    return liste_max



def f0():  # fonction sans argument car "we" et "alpha" sont des variables globales 
    liste_poids_moyen = {}
    for acide in alpha.keys():
        liste_poids_moyen[acide]=f0_bis(acide)
        
    return liste_poids_moyen


def f0_bis(acidea):
    sommepoids=0
    #liste = we
    for i in range (len(we)): # cle est un acide aminé 
            sommepoids += we[i][acidea]
    return sommepoids / len(we)

#print liste_poids_moyen

def eq(seq): 
    res=0.
    for i in range(len(seq)):
        if(seq[i] in alpha):
            frac = float(we[i][seq[i]])/liste_poids_moyen[seq[i]]
            res += log(frac,2)
    return res

def ss_seq(texte):
    liste = ""
    res = []
    contenu = lire_texte_bis(texte)[0]
    #print "contenu est:"+str(contenu)
    for i in range (len(contenu)-48):
        liste = contenu[i:i+48]
        #print liste
        res.append(eq(liste))
    return res
    
#################################Variables globales######################    
matrice = lire_texte()        
#print matrice
count = comparaison(matrice) #liste de dico qui contient les nb occ de chaque acide amine pour toutes les colonnes(len(count)=48 ici)

we = weight(count)
#for elem in we:
#    for key in elem:
#        if key=='A':
#            print elem[key]

liste_entropie = e_touteColonne(we)
#print liste_entropie
liste = liste_argmax(we)
#print liste
liste_poids_moyen =  f0()
#print liste_poids_moyen
#print eq("PPAAAPQPKEPRYKALYDFAGQSAGELSLGKDEIILVTQKENNGWWLA")    
#print(ss_seq("test_seq.txt"))
            
#############################graphe###############################################
def graphe():
    plt.xlabel(u'position i')
    plt.ylabel(u'entropie relative')
    plt.title(u"graphe représentant l'entropie relative en fonction de la position i")
    x=np.arange(48)
    plt.plot(x,liste_entropie)
    plt.show()
#graphe()

def g_vraisemblance():
    plt.xlabel(u'position i')
    plt.ylabel(u'log de vraisemblance')
    plt.title(u"log de vraisemblance en fonction de sa première position i")
    contenu = lire_texte_bis("test_seq.txt")[0]
    x=np.arange(len(contenu)-48)
    liste = ss_seq("test_seq.txt")
    plt.plot(x,liste)
    plt.show()
#g_vraisemblance()
################################graphe############################################

#################################2epartie#######################################
# nb de seq avec AA a en position i et avec AA b en position j
def n(a,i,b,j): # on utilise la variable global matrice
    nombre_sequence=0
    for sequence in matrice:
        if(sequence[i]==a and sequence[j]==b):
            nombre_sequence += 1
    return nombre_sequence


def wab(a,i,b,j):
    return (n(a,i,b,j) + (1/21.0))/ (5643.0 + 21.0)


def seconde_fonc(filename="Dtrain.txt"):  #par defaut on manipule le fichier Dtrain.txt
    matrice = lire_texte_bis(filename)
    count = comparaison(matrice)
#    somme = 0
    dico_nij = {}
    dico_wij = {}
    for acide1 in alpha:
       for i in range(len(count)-1): #len(c) = 48 car on doit calculer Wi(a) pour chaque colonne
            for acide2 in alpha:
                if(acide2!=acide1):
                    for j in range(i+1,len(count)):
                        dico_nij[acide1+acide2+" "+str(i)+" "+str(j)] = n(acide1,i,acide2,j)
                        dico_wij[acide1+acide2+" "+str(i)+" "+str(j)] = (dico_nij[acide1+acide2+" "+str(i)+" "+str(j)]+1/21.0)/ (len(matrice)+21.0)
    return dico_wij                       
                        
print(seconde_fonc())

#def troisieme_fonction():
#    dico_nij,dico_wij = seconde_fonc()
#    for i in range(len(c)):
#        for j in range(len(c)):
#            dico_nij["AV"+str(i)+" "+str(j)]
            