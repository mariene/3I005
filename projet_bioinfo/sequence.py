# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 16:09:31 2016

@author:   3202002
"""

alpha = {'A':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,'I':1,'K':1,'L':1,'M':1,'N':1,'P':1,'Q':1,'S':1,'T':1,'V':1,'W':1,'Y':1,'-':1}

def lire_texte():
    #contenu = ""
    #contenu = open("Dtrain.txt", "r")
    contenu = open("test.txt", "r")
    #contenu = mon_fichier.read()

    ss_liste = ""
    liste=[]
#    i = 1
    for i in contenu:
        if (i[0] <> '>'):
            ss_liste = ""
            for char in i:
                if (char <>'\n'):
                    ss_liste = ss_liste + char
        liste.append(ss_liste)
    contenu.close()
    return liste

matrice = lire_texte()
print(matrice)

# probleme nombre d'occurence incohérent 
def comparaison(liste):
    d =[]
    dico ={}
    for i in range (2): 
        dico = alpha.copy()     
        for j in range (0,len(liste)):
            print liste[j][i]
            for char in alpha.keys():
                if (liste[j][i] == char):
                   dico[char]= dico[char] + 1
        d.append(dico)
    print d
   
##print matrice[1][3]
comparaison(matrice)

