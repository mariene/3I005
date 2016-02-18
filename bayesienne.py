# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:35:42 2016

@author: 3202002
"""
from TME2 import *
from huffman_bis import *

# on suppose que la liste de texte est de meme langue 
def proba_textes(liste):
    d = {}
    for i in range (len(liste)):
        compte = count_ngrams(liste[i],1)
        liste_proba = getdico(compte.items())
        d[i]=liste_proba
        return d

# probabilité des lettres par rapport a une lettre            
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

