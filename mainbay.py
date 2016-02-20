# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 23:32:26 2016

@author: Mariène
"""
from bayesienne import *
from huffman_bis import *
from Entropie import *




liste = ["bouleDeSuif.txt","arseneLupin.txt","montecristo.txt"]     
probas = proba_textes(liste)
#print(proba_textes(liste))
moy = moyenne_texte(probas)

l=liste_couples(moy)
francais = liste_couples(moyenne_texte(proba_textes(["bouleDeSuif.txt","arseneLupin.txt","montecristo.txt"])))
anglais = liste_couples(moyenne_texte(proba_textes(["warandpeace.txt","moby.txt""astro.txt"])))
allemand = liste_couples(moyenne_texte(proba_textes(["faust.txt","kleine.txt","Iphiginie.txt"])))

l=liste_couples(DicoToDicoProba(count_ngrams("moby.txt",1)))

print(l)
print('\n')
#print(allemand)
#print('\n')
print(anglais)
#print('\n')
#print(francais)
#print(meme_position(francais,anglais))

