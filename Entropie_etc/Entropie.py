# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:24:12 2016

@author: 3300432
"""
import string
import math
import collections
import codecs
import unicodedata
import random
import matplotlib.pyplot as plt
import numpy as np

def Entropie(liste): 
    #plus la distribution est proche de l'uniforme plus l'entropie est grande.
    somme = 0;    
    for elem in liste:
        somme += elem * math.log(elem,2)
    somme = somme*-1
    return   somme
    
    
def Divergence(p,q):
    # divergence=0 pour deux distributions identiques.
    if(len(p)!=len(q)):
        print("deux listes doivent avoir une taille identique")
        return False
    somme = 0
    for index in range(len(p)):
        if(p[index]==0 or q[index]==0):
            continue
        somme += p[index]* math.log(p[index]/q[index],2)
    return somme



def mult2list(l1,l2):
    liste=[]
    for i in range(len(l1)):
        for j in range(len(l2)):
            liste.append(l1[i]+l2[j])
    return liste



def DicoToList(dico): #@param dico est le dictionnaire renvoyé par l'appel de la fonction count_ngrams()
    liste=[]
    somme=0
    for cle in dico:
        somme  += dico[cle]
        liste.append(dico[cle])
    for index in range(len(liste)):
        liste[index] = float(liste[index])/somme
    return liste
    

def DicoToList_bis(dico):  #@param dico est le dictionnaire de DicoToDicoProba
#la meme chose avec DicoToList, seule difference: on renvoie une liste dans l'ordre alphabetique
    liste = []
    alphabet = list(string.ascii_lowercase)
    for i in range(len(alphabet)):
        for cle in dico:
            if (cle == alphabet[i]):
                liste.append(dico[cle])
    return liste
        
def DicoToDicoProba(dico): #@param dico est le dictionnaire renvoyé par l'appel de la fonction count_ngrams()
                           #@return un dictionnaire avec les clés, les ngrams et valeurs leurs probabilites
    somme = 0
    for cle in dico:
        somme  += dico[cle]
    for cle in dico:
        dico[cle] = float(dico[cle])/somme
    return dico

def count_ngrams(text,n): # à refaire avec le retour d'un dico pour 10/02
    count = collections.Counter() # renvoie un dico: {caractere:occurence}
    contenu=""
    with codecs.open(text,encoding="utf-8") as f:
       contenu = f.read()#lecture fichier + copie dans contenu
       contenu = contenu.lower()
    contenu=unicodedata.normalize("NFKD",contenu).encode("ascii","ignore")
    if(n==1):
        for char in contenu:
            if char.isalpha():
                count[char] += 1    
        return count
    else:
        i=1
        alphabet = list(string.ascii_lowercase)
        res = list(string.ascii_lowercase)
        while i < n:
            res = mult2list(res,alphabet)
            i += 1
        resultat = {}
        for elem in res:
            resultat[elem]=contenu.count(elem)
        return resultat


def Classificateur(filename):  
    liste = {}
    fr = Divergence(DicoToList(count_ngrams(filename,2)),DicoToList(count_ngrams("bouleDeSuif.txt",2)))
    an = Divergence(DicoToList(count_ngrams(filename,2)),DicoToList(count_ngrams("warandpeace.txt",2)))
    al = Divergence(DicoToList(count_ngrams(filename,2)),DicoToList(count_ngrams("faust.txt",2)))
    liste.update({"francais":fr})
    liste.update({"anglais":an})
    liste.update({"allemand":al})
    min=11
    for elem in liste.keys():
        if liste[elem]<min:
            min = liste[elem]
            langue = elem
    return "la langue du texte doit etre : "+ langue

    