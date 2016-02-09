# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 16:03:16 2016

@author: 3202002
"""
import string
import math
import collections
import codecs
import unicodedata


def getdico(liste):
    #Supposons que liste est la liste obtenue de l'appel de fonction count_ngrams
    taille = 0
    dico = {}
    for elem in liste:
        taille = taille + elem[1]
        if (dico.has_key(elem[0])): # si elem est une cle du dictionnaire
            dico[elem[0]] = dico[elem[0]]+1
        else: #sinon
            dico.update({elem[0]:elem[1]})
    for elem in dico:
        dico[elem] = float(dico[elem])/float(taille)
    return dico

def entropie(l):
    s = 0
    for i in l :
        s = s + (i * math.log(i,2))
    s = s *(-1)
    return s
    
def divergence(p,q):  #plus les deux listes sont "éloignées" plus l'entropie est grande
    s=0    
    for i in range(len(p)):
        s = s + p[i]*math.log(float(p[i])/q[i],2)
    return s

# ne prend pas en compte les caractères spéciaux cad "à ê ë ...", les espaces et la ponctuation
def count_ngrams(text,n): # à refaire avec le retour d'un dico pour 10/02
    count = collections.Counter() # renvoie un dico: {caractere:occurence}
    contenu=""
    file = open(text,"r")   
    for char in file.read():#lecture fichier + copie dans contenu
        if char.isalpha(): #vérifie si c'est une lettre 
            char = char.lower()#met les majuscules en minuscules
            contenu = contenu+char
    for char in contenu:
       count[char] += 1    
    file.close()
    return count

# version où on compte les caractères propres à chaque langue
#on a aussi le nombre d'occurence selon n caractères
# Max n=3 si n > 3 -> String index out of range
def count_ngrams_bis(text,n): 
    count = collections.Counter() # renvoie un dico: {caractere:occurence}
    contenu=""
    with codecs.open(text,encoding="utf-8") as f:
        for char in f.read():
            if char.isalpha():
                char = char.lower()
                contenu = contenu+char
    contenu=unicodedata.normalize("NFKD",contenu).encode("ascii","ignore")     
    if (n == 1):# pour chaque caractère
        for char in contenu:
            count[char] += 1  
    else :#pour chaque n caractère
        i=0
        while i < len(contenu)-1:
            s=""
            j = 1         
            for j in range (n):
                if i+j != len(contenu): 
                    s = s + contenu[i+j]
            if s in contenu:
                count[s] += 1
            i=i+1    
    f.close()
    return count

#################test###################

liste =[0.05,0.7,0.15,0.1]
liste2 = [0.95,0.01,0.01,0.03]
compte = count_ngrams("guten.txt",1)
compte1=count_ngrams_bis("test.txt",1)
dico = getdico(compte.items())
L=[]
for elem in dico.keys():
    L.append(dico[elem])


#print(entropie(liste))
#print(divergence(liste,liste2))
print(compte1)
#print(compte)
#print(dico)
#print(L)
#print(entropie(L))
#    