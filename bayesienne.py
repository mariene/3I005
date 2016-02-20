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
import math

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


def somme_log(mot,liste):
    p = 0.0
    for i in mot:
        for j in range (len(liste)):
            #print liste[j][0]
            if i == liste[j][0]:
                p = p + math.log(liste[j][1])
    return p


def plw (mot):
    francais = liste_couples(moyenne_texte(proba_textes(["bouleDeSuif.txt","arseneLupin.txt","montecristo.txt"])))
    anglais = liste_couples(moyenne_texte(proba_textes(["warandpeace.txt","moby.txt","astro.txt"])))
    allemand = liste_couples(moyenne_texte(proba_textes(["faust.txt","kleine.txt","Iphiginie.txt"])))
    fr = (somme_log(mot,francais)*(1.0/3))
    print('\n')
    ang = (somme_log(mot,anglais)*(1.0/3))
    ger = (somme_log(mot,allemand)*(1.0/3))
    if ((ger > ang) and (ger > fr)) :
        print ("allemand")
    if ((ang > fr) and (ang > ger)) :
        print("anglais")
    if ((fr > ger) and (fr > ang)) :
        print ("francais")
 
plw("really")
    

