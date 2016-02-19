# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:35:42 2016

@author: 3202002
"""
#from TME2 import *
from huffman_bis import *
from Entropie import *
import string
from TME2 import *

# on suppose que la liste de texte est de meme langue 
# probabilité pour chaque caractère
def proba_textes(liste):
    d = {}
    for i in range (len(liste)):
        compte = count_ngrams(liste[i],1)
        liste_proba = getdico(compte.items())
        d[i]=liste_proba
        return d

#moyenne des proba obtenu avec plusieurs textes d'une meme langue             
def moyenne_texte(dico):
    d = {}
    for dico in dico.values():
        for char in dico:
            if d.has_key(char):
                d[char] += dico[char]
            else:
                d.update({char:dico[char]})
    for elem in d:
        d[elem] = d[elem]/3
    return d

def comparaison (texte):
    francais = liste_couples(moyenne_texte(proba_textes(["bouleDeSuif.txt","arseneLupin.txt","montecristo.txt"])))
    anglais = liste_couples(moyenne_texte(proba_textes(["warandpeace.txt","moby.txt","astro.txt"])))
    allemand = liste_couples(moyenne_texte(proba_textes(["faust.txt","kleine.txt","Iphiginie.txt"])))
    texte = liste_couples(DicoToDicoProba(count_ngrams(texte,1)))
    ger = 0
    ang = 0
    fr = 0
    alpha = []
    for j in range (len(francais)) :
        alpha.append(francais[j][0])
    print alpha
    i = 0    
    for i in range (26):
        print(abs(francais[i][1]-texte[i][1]))
        print(abs(anglais[i][1]-texte[i][1]))
        print(abs(allemand[i][1]- texte[i][1]))
        if alpha[i] == texte[i][0]:
            if abs(francais[i][1]-texte[i][1])> abs(anglais[i][1]-texte[i][1]):
                if abs(allemand[i][1]-texte[i][1])< abs(anglais[i][1]-texte[i][1]):
                    ger = ger + 1
                else :
                    ang = ang + 1
            else:
                if abs(allemand[i][1]-texte[i][1])> abs(francais[i][1]-texte[i][1]):
                    fr = fr + 1
                else : 
                    ger = ger + 1
    print (fr)
    print (ger)
    print(ang)       
    
    if ((ger > ang) and (ger > fr)) :
        print ("allemand")
    if ((ang > fr) and (ang > ger)) :
        print("anglais")
    if ((fr > ger) and (fr > ang)) :
        print ("francais")

#comparaison("moby.txt")
l = liste_couples(DicoToDicoProba(count_ngrams("texte.txt",1)))  
#print (len(l))          
    


     
    
    

