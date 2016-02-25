# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:31:44 2016

@author: 3202002
"""
from bayesienne_bis import *
from random import *
francais = liste_couples(moyenne_texte(proba_textes(["bouleDeSuif.txt","arseneLupin.txt","montecristo.txt"])))
anglais = liste_couples(moyenne_texte(proba_textes(["warandpeace.txt","moby.txt","astro.txt"])))
allemand = liste_couples(moyenne_texte(proba_textes(["faust.txt","kleine.txt","Iphiginie.txt"])))

francais_nb = liste_couple_nb(count_ngrams("bouleDeSuif.txt",2))
anglais_nb = liste_couple_nb(count_ngrams("warandpeace.txt",2))
allemand_nb = liste_couple_nb(count_ngrams("faust.txt",2))
print(francais)
def generation(n,langue):
        
    i = randrange(26)
    alphabet = string.lowercase
    premierelettre = alphabet[i]  # on prend la premiere lettre aleatoirement
    
    fichier = open("data.txt", "w")
    
    fichier.write("Bonjour monde")
    
    fichier.close()

#generation("aa")