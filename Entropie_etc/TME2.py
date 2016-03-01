# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 16:03:16 2016
@author: 3202002
"""
import string
import math
import collections
import codecs
import unicodedata
import random
import matplotlib.pyplot as plt
import numpy as np

#faire classificateur de langue 
#faire plot aussi

def getdico(liste):
    #Supposons que liste est la liste obtenue de l'appel de fonction count_ngrams
    taille = 0
    dico = {}
    for elem in liste:
        taille = taille + elem[1]
        if (dico.has_key(elem[0])): # si elem est une cle du dictionnaire
            dico[elem[0]] = dico[elem[0]]+1
        else: #sinon
            dico.update({elem[0]:elem[1]})
    for elem in dico:
        dico[elem] = float(dico[elem])/float(taille)
    return dico

def entropie(l):
    s = 0
    for i in l :
        s = s + (i * math.log(i,2))                                                  
    s = s *(-1)
    return s
    
    
    
def divergence(p,q):  #plus les deux listes sont "éloignées" plus l'entropie est grande
    s=0
    if len(p)<=len (q):
        print(p,q)
        for i in range(len(p)):
            s = s + p[i]*math.log(float(p[i])/q[i],2)
    else:  
        for i in range(len(q)):
            s = s + p[i]*math.log(float(p[i])/q[i],2)
    return s


def mult2list(l1,l2):
    liste=[]
    for i in range(len(l1)):
        for j in range(len(l2)):
            liste.append(l1[i]+l2[j])
    return liste

# prise en compte des espaces
def count_ngrams(text,n): # à refaire avec le retour d'un dico pour 10/02
    count = collections.Counter() # renvoie un dico: {caractere:occurence}
    contenu=""
    with codecs.open(text,encoding="utf-8") as f:
       contenu = f.read()#lecture fichier + copie dans contenu
       contenu = contenu.lower()
    contenu=unicodedata.normalize("NFKD",contenu).encode("ascii","ignore")
    if(n==1):
        for char in contenu:
            if char.isalpha():
                count[char] += 1    
        return count
    else:
        i=1
        alphabet = list(string.ascii_lowercase)
        res = list(string.ascii_lowercase)
        while i < n:
            res = mult2list(res,alphabet)
            i += 1
        resultat = {}
        for elem in res:
            if elem in contenu:
                resultat[elem]=contenu.count(elem)
        return resultat

    
# version où on compte les caractères propres à chaque langue
#on a aussi le nombre d'occurence selon n caractères
# ne prend pas en compte les espaces 
def count_ngrams_bis(text,n): 
    count = collections.Counter() # renvoie un dico: {caractere:occurence}
    contenu=""
    with codecs.open(text,encoding="utf-8") as f:
       for char in f.read():#lecture fichier + copie dans contenu
           if char.isalpha():
               contenu += char.lower()
    contenu=unicodedata.normalize("NFKD",contenu).encode("ascii","ignore")
    if (n == 1):# pour chaque caractère
        for char in contenu:
            count[char] += 1  
    else :#pour chaque n caractère.Counter() # renvoie un dico: {caractere:occurence}
        i=0
        while i < len(contenu)-1:
            s=""
            for j in range (n):
                if i+j < len(contenu): 
                    s = s + contenu[i+j]
            if (s in contenu) == True:
                count[s]+=1
            i=i+1    
    f.close()
    return count

def DicoToList(dico):
    liste=[]
    for elem in dico:
        liste.append(dico[elem])
    return liste

def trace_graphe():
    d = {}   
    for i in np.arange(0.01,0.99,0.01):
        d[i] = entropie([i,1.0-i])
    plt.plot([str(x) for x in d.keys()], [str(y) for y in d.values()],"+")
    plt.xlabel('proba p')
    plt.ylabel('entropie')
#trace_graphe()    
# 
# en cours / pb 
 # affiche courbe, pour un texte : entropie en fonction de n
def trace_histo(texte):
    d = {} 
    #plt.savefig permet de souvegarder 
    for n in range(2):
        compte = count_ngrams(texte,n)
        liste_proba = DicoToList(getdico(compte.items()))

        ent=entropie(liste_proba)
 
        d[n] = ent
    print d.keys()
    print d.values()
    plt.plot([str(x) for x in d.keys()], [str(y) for y in d.values()])
    plt.xlabel('n')
    plt.ylabel('entropie')
    
#trace_histo("bouleDeSuif.txt")       

#########################################bayesienne#########################################
# on suppose qu'on prend que 3 langues 
    
#################test###################
#
#liste =[0.05,0.7,0.15,0.1]
#liste2 = [0.95,0.01,0.01,0.03]
#
#francais
#compte1=count_ngrams("bouleDeSuif.txt",1)
#compte = count_ngrams("arseneLupin.txt",1)
#compte2=count_ngrams("montecristo.txt",1)
##print(compte1)
#
##allemand
#compted=count_ngrams("kleine.txt",1)
#compteb = count_ngrams("faust.txt",1)
##print(compted)
#
##anglais 
#comptec=count_ngrams("moby.txt",1)
#comptea=count_ngrams("warandpeace.txt",1)
##print(comptec)
#
##francais
#dico = getdico(compte.items())
#listeproba = DicoToList(dico)
#
#dico1 = getdico(compte1.items())
#listeproba1 = DicoToList(dico1)
#
#dico2 = getdico(compte2.items())
#listeproba2 = DicoToList(dico2)
#
#print(entropie(listeproba))
#print(entropie(listeproba1))
#print(entropie(listeproba2))
#
##allemand
#dico3 = getdico(compted.items())
#listeproba3 = DicoToList(dico3)
#print(entropie(listeproba3))
#
##anglais
#dico4 = getdico(comptea.items())
#listeproba4 = DicoToList(dico4)
#print(entropie(listeproba4))
#
#print("2 textes pareils "+ str(divergence(listeproba,listeproba)))
#print("2 textes de la meme langue "+ str(divergence(listeproba,listeproba1)))
#print("2 textes de langue différente francais/allemand "+ str(divergence(listeproba,listeproba3)))
#print("2 textes de langue différente francais/anglais "+ str(divergence(listeproba,listeproba4)))
#print("2 textes de langue différente anglais/allemand "+ str(divergence(listeproba4,listeproba3)))
#print("2 textes de langue différente allemand/anglais "+ str(divergence(listeproba3,listeproba4)))


#for elem in dico.keys():
#    L.append(dico[elem])

#print(entropie(liste))
#print(divergence(liste,liste2))
#print(compte1)
#print("\n\n\n\n2e texte\n\n\n\n")
#print(compte)
#print(dico)
#print(listeproba)



