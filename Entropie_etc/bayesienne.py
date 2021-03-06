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


def pwl(mot,liste):
    p = 0.0
    for i in mot:
        for j in range (len(liste)):
            if i == liste[j][0]:
                p = p + math.log(liste[j][1])
    return p

francais = liste_couples(moyenne_texte(proba_textes(["bouleDeSuif.txt","arseneLupin.txt","montecristo.txt"])))
anglais = liste_couples(moyenne_texte(proba_textes(["warandpeace.txt","moby.txt","astro.txt"])))
allemand = liste_couples(moyenne_texte(proba_textes(["faust.txt","kleine.txt","Iphiginie.txt"])))

def plw_mot (mot):
 
    fr = (pwl(mot,francais)*(1.0/3))
    ang = (pwl(mot,anglais)*(1.0/3))
    ger = (pwl(mot,allemand)*(1.0/3))
    if ((ger > ang) and (ger > fr)) :
        #print ("allemand")
        return 2
    if ((ang > fr) and (ang > ger)) :
        #print("anglais")
        return 1
    if ((fr > ger) and (fr > ang)) :
        #print ("francais")
        return 0
        
    
#print(plw_mot("see"))
# prend trop de temps quand c'est un long texte  

def plw_texte(text):
    #texte    
    contenu = ""
    #punc = set(string.punctuation)
    with codecs.open(text,encoding="utf-8") as f:
       for char in f.read():#lecture fichier + copie dans contenu
           contenu += char.lower()
    contenu=unicodedata.normalize("NFKD",contenu).encode("ascii","ignore")
    
    contenu = "".join([c for c in contenu])
    liste = []   
    ger = 0
    ang = 0
    fr = 0
    #print contenu
    for char in contenu:
        if ((char <> ' ') and (char <> "\n") and (char <> "\r")) :
            liste.append(char)
        else :
           # print liste
            l = plw_mot(liste)            
            if l == 0 :
                fr = fr + 1
                #print "francais "+str(fr)
            if l == 2:
                ger = ger +1
                #print "allemand "+str(ger)
            if l == 1:
                ang = ang +1
                #print "anglais "+str(ang)
            liste=[]
    
    f.close()
    if ((ger > ang) and (ger > fr)) :
        print ("allemand")
        #return 2
    if ((ang > fr) and (ang > ger)) :
        print("anglais")
        #return 1
    if ((fr > ger) and (fr > ang)) :
        print ("francais")
        #return 0

#print(plw_texte("moby.txt"))

def plw_texte_bis(text):
    #texte    
    contenu = ""
    with codecs.open(text,encoding="utf-8") as f:
       for char in f.read():#lecture fichier + copie dans contenu
           if char.isalpha():
               contenu += char.lower()
    contenu=unicodedata.normalize("NFKD",contenu).encode("ascii","ignore")
    ger = 0
    ang = 0
    fr = 0
    for n in range(1,8):
        for index in range(0,len(contenu),1000):
            l = plw_mot(contenu[index:index+n])          
            if l == 0 :
                fr = fr + 1
            if l == 2:
                ger = ger +1
            if l == 1:
                ang = ang +1
    f.close()
    if ((ger > ang) and (ger > fr)) :
        print ("allemand")
        #return 2
    if ((ang > fr) and (ang > ger)) :
        print("anglais")
        #return 1
    if ((fr > ger) and (fr > ang)) :
        print ("francais")
        #return 0

print(plw_texte_bis("moby.txt"))



    
    
