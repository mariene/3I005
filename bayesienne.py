# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:35:42 2016

@author: 3202002
"""

import TME2 as tme
import huffman_bis as huff
# on suppose que la liste de texte est de meme langue 
def proba_textes(liste):
    d = {}
    for i in range (len(liste)):
        compte = tme.count_ngrams(liste[i],1)
        liste_proba = tme.getdico(compte.items())
        d[i]=liste_proba
    return d

liste =["bouleDeSuif.txt","arseneLupin.txt","montecristo.txt"]
probas = proba_textes(liste)
#print(proba_textes(liste))

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
        
moy =moyenne_texte(probas)

l=huff.liste_couples(moy)
l.sort(huff.cmpval)
print(l)