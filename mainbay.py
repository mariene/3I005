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
plw("really")

