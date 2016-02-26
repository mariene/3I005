# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:31:44 2016

@author: 3202002
"""
from bayesienne_bis import *
from random import *
from string import *

francais = liste_couples(moyenne_texte(proba_textes(["bouleDeSuif.txt","arseneLupin.txt","montecristo.txt"])))
anglais = liste_couples(moyenne_texte(proba_textes(["warandpeace.txt","moby.txt","astro.txt"])))
allemand = liste_couples(moyenne_texte(proba_textes(["faust.txt","kleine.txt","Iphiginie.txt"])))

francais_nb = liste_couple_nb(count_ngrams("bouleDeSuif.txt",2))
anglais_nb = liste_couple_nb(count_ngrams("warandpeace.txt",2))
allemand_nb = liste_couple_nb(count_ngrams("faust.txt",2))
#print(francais)

#def lettre_associe():

def count_ngrams_bis(text,n): 
    count = collections.Counter() # renvoie un dico: {caractere:occurence}
    contenu=""
    punc = set(string.punctuation)
    with codecs.open(text,encoding="utf-8") as f:
       for char in f.read():#lecture fichier + copie dans contenu
           if char.isalpha():
               contenu += char.lower()
    contenu=unicodedata.normalize("NFKD",contenu).encode("ascii","ignore")
    contenu = "".join([c for c in contenu if c not in punc])
    #print contenu
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

print(count_ngrams_bis("horla.txt",1))
    
def generation(n,langue):
        
    i = randrange(26)
    alphabet = string.lowercase
    premierelettre = alphabet[i]  # on prend la premiere lettre aleatoirement
    
    fichier = open("data.txt", "w")
    
    fichier.write("Bonjour monde")
    
    fichier.close()

#generation("aa")