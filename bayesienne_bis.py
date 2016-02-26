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
    
    
    
    
    
    
##########################Variable globales############################"

# trois distributions en probabilite que l'on va utiliser pour comparer
francais = liste_couples(moyenne_texte(proba_textes(["bouleDeSuif.txt","arseneLupin.txt","montecristo.txt"])))
anglais = liste_couples(moyenne_texte(proba_textes(["warandpeace.txt","moby.txt","astro.txt"])))
allemand = liste_couples(moyenne_texte(proba_textes(["faust.txt","kleine.txt","Iphiginie.txt"])))

# trois distributions en nombre que l'on va utiliser
francais_nb = liste_couple_nb(count_ngrams("bouleDeSuif.txt",2))
anglais_nb = liste_couple_nb(count_ngrams("warandpeace.txt",2))
allemand_nb = liste_couple_nb(count_ngrams("faust.txt",2))
#print(francais_nb)
###########################Variables globales##########################





#permet de calculer la probabilité du mot sachant langue
def pwl(mot,liste):
    p = 0.0
    for i in mot:
        for j in range (len(liste)):
            if i == liste[j][0]:
                p = p + math.log(liste[j][1])
    return p


#permet la detection de langue du mot passé en argument 
def plw_mot (mot):
 
    fr = (pwl(mot,francais)*(1.0/3))
    ang = (pwl(mot,anglais)*(1.0/3))
    ger = (pwl(mot,allemand)*(1.0/3))
    # la plus grande proba l'emporte
    if ((ger > ang) and (ger > fr)) :
        #print ("allemand")
        return 2
    if ((ang > fr) and (ang > ger)) :
        #print("anglais")
        return 1
    if ((fr > ger) and (fr > ang)) :
        #print ("francais")
        return 0
        
#permet la detection de langue du texte passé en argument
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
    
    for char in contenu:
        if ((char <> ' ') and (char <> "\n") and (char <> "\r")) :
            liste.append(char)
        else :
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

#plw_texte("texte.txt")   
 
def Amelioree(texte):  
    contenu = ""
    with codecs.open(texte,encoding="utf-8") as f:
       for char in f.read():#lecture fichier + copie dans contenu
           contenu += char.lower()
    contenu=unicodedata.normalize("NFKD",contenu).encode("ascii","ignore")
    #print(contenu)
    f.close()
    mot = []
    
    cpt_fr = 0 # compteur pour chaque langue, si un mot est suppose en francais alors cpt_fr += 1
    cpt_an = 0
    cpt_al = 0
    
    
    for char in contenu:
        if ((char <> ' ') and (char <> "\n") and (char <> "\r")) :
            mot.append(char)
            
        else: #lorsque l'on a un espace, un saut de ligne, une tabulation , on peut considerer qu'on a stocké un mot dans "mot"
        
        
            totale_fr = 0 #compteur de nombre des couples commencant par une meme lettre
                       #distribution = aa:500, ab:200, ba:800  et le mot= "aa" alors totale_fr = 700
            totale_an = 0
            totale_al = 0
            
            proba_fr = 0 #recuperer le nombre d'apparition du couple "XY" dans le texte
                        #distribution = aa:500, ab:200, ba:800 et mot="ab" alors proba_fr = 200/500.0
            proba_an = 0
            proba_al = 0
            
            
            res_fr = 1 #stocke le produit des probabilites conditionnelles
            res_an = 1
            res_al = 1
            
           # print(mot)
            
            
            for i in range (1,len(mot)):
            #parcours du mot a partir de deuxieme lettre
            
                totale_fr = 0
                for couple in francais_nb:
                # parcours de la distribution francais
                
                    if couple[0][0] == mot[i-1]:
                    # si la premiere lettre de la liste de distribution est égale à la i-1_eme lettre du mot
                    
                        totale_fr += couple[1]
                        # on ajoute le nombre dans totale
                        
                        if couple[0][1] == mot[i]:
                           # print(couple)
                            # si la deuxieme lettre du couple est egale à la i_eme lettre du mot
                        
                            proba_fr = couple[1]
                
                if(totale_fr != 0 and proba_fr != 0):  #on sort de la boucle dans distribution car on a recupere totale et proba
                                                        #test pour eviter division par 0 et le produit des proba soit 0
                
                    proba_fr = float(proba_fr) / totale_fr
                    res_fr = res_fr * proba_fr
                    #ici, proba_fr = P(Xi|X1...Xi-1)
                    
                else:
                    continue
                    
            for i in range (1,len(mot)): 
                totale_an = 0
                for couple in anglais_nb:
                # parcours de la distribution anglais
                
                    if couple[0][0] == mot[i-1]:
                    
                        totale_an += couple[1]
                        
                        if couple[0][1] == mot[i]:                        
                            proba_an = couple[1]
                if(totale_an!=0 and proba_an!=0):
                    proba_an = float(proba_an) / totale_an
                    res_an = res_an * proba_an
                else:
                    continue
                    
                    
                    
            for i in range (1,len(mot)): 
                 totale_al = 0
                 for couple in allemand_nb:
                # parcours de la distribution allemand
                 
                    if couple[0][0] == mot[i-1]:
                    
                        totale_al += couple[1]
                        
                        if couple[0][1] == mot[i]:
                            proba_al = couple[1]
                 if(totale_al!=0 and proba_al!=0):
                     proba_al = float(proba_al) / totale_al
                     res_al = res_al * proba_al
                 else:
                     continue
                 
                 
                 
            
            if (res_fr > res_al) and (res_fr > res_an):
               cpt_fr += 1
            if (res_an > res_al) and (res_an > res_fr):
               cpt_an += 1    
            if (res_al > res_an) and (res_al > res_fr):
               cpt_al += 1
                
            mot = [] # on associe mot a un tableau vide pour stocker le prochain mot
            
            
            
    print(cpt_al,cpt_an,cpt_fr)
    if (cpt_fr > cpt_an) and (cpt_fr > cpt_al):
        print("bayesienne amelioree dit que le texte doit etre en francais")
    else : 
        if (cpt_an > cpt_al) and (cpt_an > cpt_fr):
            print("bayesienne amelioree dit que le texte doit etre en anglais")
        else:
            if (cpt_al > cpt_an) and (cpt_al > cpt_fr):
                print("bayesienne amelioree dit que le texte doit etre en allemand") 
            else:
                print("bayesienne amelioree a du mal à déterminer la langue du texte, peut etre un texte plus long?")
                

#def GenerationTexte(n):
    
    
#Amelioree("texte.txt")
    
    
