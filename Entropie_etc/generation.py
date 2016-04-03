# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 14:27:35 2016

@author: 3300432
#"""
import random
import string
from huffman_bis import *
from Entropie import *
import string
from bayesienne import *
import math
import numpy as np


##########################Variable globales############################"

# trois distributions en probabilite que l'on va utiliser pour comparer
francais = liste_couples(moyenne_texte(proba_textes(["bouleDeSuif.txt","arseneLupin.txt","montecristo.txt"],2)))
anglais = liste_couples(moyenne_texte(proba_textes(["warandpeace.txt","moby.txt","astro.txt"],2)))
allemand = liste_couples(moyenne_texte(proba_textes(["faust.txt","kleine.txt","Iphiginie.txt"],2)))
#print francais
# trois distributions en nombre que l'on va utiliser
francais_nb = liste_couple_nb(count_ngrams("francais.txt",2))
anglais_nb = liste_couple_nb(count_ngrams("anglais.txt",2))
allemand_nb = liste_couple_nb(count_ngrams("allemand.txt",2))
#print(francais_nb)
###########################Variables globales##########################


def trie(dico):
    items = dico.items()
    comparateur = lambda a,b : cmp(a[1],b[1])
    return sorted(items, comparateur, reverse=False)
    
    
    
def generation(n,langue="fr",resultname="data.txt"):
    if(langue=="francais" or langue == "fr"):
        langue = francais
    elif(langue=="allemand" or langue =="ge"):        
        langue = allemand
    elif(langue=="anglais" or langue =="en"):
        langue = anglais
    else:
        print("langue inconnue, generation d'un texte en francais est effectué")
        langue = francais
    
    i = random.randrange(26)
    alphabet = list(string.lowercase)
    premierelettre = alphabet[i]  
    fichier = open(resultname, "w") # la premiere lettre du fichier etant generee aleatoirement
  
    fichier.write(premierelettre)
    dicoalphabet = {}
    
    for i in range(26):        # creation d'un dictionnaire
        dicoalphabet.update({alphabet[i]:{}})
        
    for lettre in dicoalphabet:
        for couple in langue:
            if couple[0][0] == lettre:
                resultat = DebutLettre([lettre,couple[0][1]],langue) #resultat[0]= le nombre total des couples commencant par  , resultat[1]= nbr d'occurence du couple (de lettre)
                dicoalphabet[lettre].update({couple[0][1]:resultat[1]})
        
    #deux boucles sur dicoalphabet car la premiere modifie les donnees dans ceci
    for lettre in dicoalphabet:
        somme = 0
        for secondelettre in dicoalphabet[lettre]:
            somme += dicoalphabet[lettre][secondelettre] # on recupere la somme des probabilite
        
        for secondelettre in dicoalphabet[lettre]:
            dicoalphabet[lettre][secondelettre] = dicoalphabet[lettre][secondelettre] / somme # en divisant chaque proba avec la somme , on obtient sa frequence

        somme_cumulee = np.cumsum(dicoalphabet[lettre].values())
        i=0        
        for secondelettre in dicoalphabet[lettre]:
           dicoalphabet[lettre][secondelettre] = somme_cumulee[i]  # on fait la somme cumulee des probabilites
           i += 1
    
    
    
    
#######################################################Commencement de la generation du fichier ################################# ###########################
    i=0
    nbmot=0
    while ( i<n):
        longmot = random.randrange(8) #longueur d'un mot est de max 8 caracteres
                           
        for j in range(longmot):
            alea = random.random()
            liste_cumulee = trie(dicoalphabet[premierelettre]) #car le dictionnaire n'est pas trie 
                                                                 #exemple liste_cumulee = [("a",0.5),("b",1)] 
            for index in range(len(liste_cumulee)):
                if liste_cumulee[index][1] - alea > 0:
                     secondelettre = liste_cumulee[index][0]
                     fichier.write(secondelettre)
                     premierelettre = secondelettre
                     i += 1
                     break
        fichier.write(" ")
        nbmot +=1
        if(nbmot==10):
            fichier.write("\n")
            nbmot=0
            
    fichier.close()

    return dicoalphabet

######################################################################test##################################################################################

d = generation(1000,"ge","ge.txt")

