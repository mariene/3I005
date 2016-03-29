# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 16:09:31 2016
@author:   3202002
"""
#pour faire les calculs des différentes equations
from math import *
#pour tracer les courbes
import numpy as np
import matplotlib.pyplot as plt

#on suppose qu'il y ait au moins 1 acide aminé
alpha = {'A':1,'C':1,'D':1,'E':1,'F':1,'G':1,'H':1,'I':1,'K':1,'L':1,'M':1,'N':1,'P':1,'Q':1,'R':1,'S':1,'T':1,'V':1,'W':1,'Y':1,'-':1}

"""
la fonction permet de récupérer les données du fichier sous
forme de matrice (contenu du fichier ligne par ligne)
 @param nom du texte
 @return une liste avec chaque sequence 
"""
def lire_texte(texte):
   
    contenu = open(texte, "r")
   
    ss_liste = ""
    liste=[]

    for i in contenu:
        if (i[0] <> '>'):
            ss_liste = ""
            for char in i:
                if (char <>'\n'):
                    ss_liste = ss_liste + char
            liste.append(ss_liste)
    contenu.close()
    return liste

"""
 @param liste, la liste qu'on a obtenu avec lire_texte()
 @return une liste contenant plusieurs dictionnaires
 chaque colonne a un dictionnaire : {acide aminé:nb occurence} 
"""
def comparaison(liste):
    d =[]
    dico ={}
    for i in range (48): 
        dico = alpha.copy()     
        for j in range (len(liste)):
            for char in alpha.keys():
                if (liste[j][i] == char):
                   #print char
                   dico[char]= dico[char] + 1
        d.append(dico)
    return d
   
"""   
la fonction permet de calculer le poids d'UN acide aminé
 @param M = longueur du texte
 @param n = entier, correspondant au nb occurence de l'acide aminé
 @return son poids
""" 
def calPoids (M,n):
    w = n / (M + 21.0) # M = nb ligne sans commentaire et q = taille de l'alphabet 
    return w
    
"""
pour chaque colonne on calcule le poids de chaque acide aminé 
@param M la longueur de texte
@param liste la liste de dico retourné par comparaison()
@return retourne une liste de dico, chaque dico represente les
poids de chaque acide aminé : {acide:poids}
"""
def weight(M,liste):
    poids = {}
    l2 = []
    for i in range(len(liste)) : 
        poids = {}
        for l in liste[i].keys():           
            #appel de la fonction calPoids pour chaque acide de chaque colonne
            a = calPoids(M,liste[i][l])           
            poids.update({l:a})
        l2.append(poids)
    return l2

"""
 on calcule ici l'entropie relative d'une distribution d'une seule colonne
@param p une distribution (d'une colonne)
@return l'entropie calculé
"""
def e_relative(p): 
    somme = log(21,2)
    for key in p.keys() :#pour chaque acide amine      
        somme += p[key]* log(p[key],2)       
    return somme

"""
fonction permet de calculer l'entropie pour les 48 colonnes
@param liste , est la liste retourné par weight()
@return les entropie calculée stockée dans une liste
"""
def e_touteColonne(liste):
    liste_entropie = []    
    for i in range(len(liste)):       
        res = e_relative(liste[i]) # entropie relative pour chaque colonne       
        liste_entropie.append(res)
    return liste_entropie # et les valeurs d'entropies sont stockées dans l'ordre
    
"""    
fonction permettant de recuperer l'acide le plus conservé de chaque colonne
@param liste, resultat de weight()
@return la liste des acides les plus representants de chaque colonne
"""
def liste_argmax(liste): 
    liste_max = []
    for i in range(len(liste)):
        indice_max = liste[i].values().index(max(liste[i].values()))
        lettre_max = liste[i].keys()[indice_max]
        #on stocke les lettres dominantes de chaque colonne dans la liste_max
        liste_max.append(lettre_max)
    return liste_max

"""
la fonction qui permet de calculer f0 d'UN acide aminé
@param acidea, un acide aminé donné
@return le resultat trouvé
"""
def f0_bis(acidea):
    sommepoids=0
    for i in range (len(we)): # cle est un acide aminé 
            sommepoids += we[i][acidea]
    return sommepoids / len(we)

"""
la fonction permet de calculer le modele nul
 fonction sans argument car "we"(resultat de weight())
 et "alpha" sont des variables globales 
@return la liste contenant les f0 de chaque acide
"""
def f0():  
    liste_poids_moyen = {}
    for acide in alpha.keys():
        liste_poids_moyen[acide]=f0_bis(acide)        
    return liste_poids_moyen

"""
fonction qui permet de calculer le log-vraisemblance d'une sequence
@param seq, une sequence donnée
@return le resultat du calcul
"""
def eq(seq): 
    res=0.
    for i in range(len(seq)):
        if(seq[i] in alpha):
            frac = float(we[i][seq[i]])/liste_poids_moyen[seq[i]]
            res += log(frac,2)           
    return res

"""
fonction permettant de calculer tous les log-vraisemblance 
de toutes les sous-sequences du texte
@param texte, le texte contenant la sequence à comparer
@return la liste des log-vraisemblance
"""
def ss_seq(texte):
    liste = ""
    res = []
    contenu = lire_texte(texte)[0]
    #print "contenu est:"+str(contenu)
    for i in range (len(contenu)-48):
        liste = contenu[i:i+48]
        #print liste
        res.append(eq(liste))
    return res
       
       
#################################Variables globales######################    
matrice = lire_texte("Dtrain.txt")    
#print matrice

count = comparaison(matrice) #liste de dico qui contient les nb occ de chaque acide amine pour toutes les colonnes(len(count)=48 ici)
#print count
#print count[46]

we = weight(len(matrice),count)
#print we

liste_entropie = e_touteColonne(we)
#print liste_entropie

liste = liste_argmax(we)
#print liste

liste_poids_moyen =  f0()
#print liste_poids_moyen

#print eq("PPAAAPQPKEPRYKALYDFAGQSAGELSLGKDEIILVTQKENNGWWLA")
#print(ss_seq("test_seq.txt"))

#################################Variables globales######################
            
            
                      
#############################graphe###############################################
"""
Fonction qui permet de tracer la courbe de l'entropie
"""
def graphe():
    plt.xlabel(u'position i') #nom abscisse
    plt.ylabel(u'entropie relative') # nom ordonné
    plt.title(u"graphe représentant l'entropie relative en fonction de la position i")#titre du graphe
    x=np.arange(48)#valeur abscisse
    plt.plot(x,liste_entropie) #liste_entropie variable globale : liste des entropies de chaque colonne
    plt.show()
    
#graphe()

"""
Fonction qui permet de tracer la courbe de vraisemblance
"""
def g_vraisemblance():
    plt.xlabel(u'position i') #nom abscisse
    plt.ylabel(u'log de vraisemblance') # nom ordonné
    plt.title(u"log de vraisemblance en fonction de sa première position i") #titre du graphe
    contenu = lire_texte("test_seq.txt")[0] #pour calculer le nombre de première position i
    x=np.arange(len(contenu)-48) #pour chaque i premiere position (valeur abscisse)
    liste = ss_seq("test_seq.txt")#calcul du log-vraisemblance
    plt.plot(x,liste) # creer graphe de x en fonction d'y
    plt.show()
#g_vraisemblance()

"""
Fonction qui permet de tracer la courbe de fraction
"""
def g_fraction():
    plt.xlabel(u'nombre de paires considérées')#nom abscisse
    plt.ylabel(u'fraction')# nom ordonné
    plt.title(u"fraction en fonction du nombre de paires considérées")#titre du graphe
    liste = [] #creation d'une liste pour les valeurs de l'axe des ordonnées
    for i in range (10,60,10):
        p=select_paires(i,Infos_Mutuelles()) 
        liste.append(frac(p,lire_texte_dico()))#ajoute dans une liste la fraction obtenue pour 10,20,30,40,50 paires
    x= np.arange(10,60,10) #[10,60[ valeur de l'axe des abscisse
    plt.plot(x,liste)
    plt.show()

#g_fraction()
################################graphe############################################









#################################2epartie#######################################

"""
la fonction qui calcule le = nombre de s´equences avec acide amin´ee a en position i 
ET avec acide aminée b en position j
@param a, premier acide 
@param i, la position de l'acide 'a'
@param b, le second acide 
@param j, la position de l'acide 'b'
@param matrice, le resultat de la lecture du fichier avec la méthode lire_texte(filename)
@return le nombre ainsi calculé
"""
def n(a,i,b,j,matrice): # on utilise la variable global matrice
    nombre_sequence=0
    for sequence in matrice:
        if(sequence[i]==a and sequence[j]==b):
            nombre_sequence += 1
    return nombre_sequence

"""
calcul du poids Wij(a,b) de l'équation (11)
@params les memes que la fonction n()
@return le poids calculé
"""
def wab(a,i,b,j,matrice):
    return (n(a,i,b,j,matrice) + (1/21.0))/ (len(matrice) + 21.0)

"""
fonction qui calcule pour chaque paire de i,j et de a,b
le nombre de Nij(a,b) et Wij(a,b)
@param filename le nom du fichier à calculer , le texte "Dtrain.txt" par défaut
@return deux dictionnaires contenant les resultat, avec clés: [A1A2 i j]
"""
def seconde_fonc(filename="Dtrain.txt"): 
    matrice = lire_texte(filename)
    count = comparaison(matrice)
    dico_nij = {}
    dico_wij = {}
    for acide1 in alpha:
       for i in range(len(count)-1): #len(c) = 48 car on doit calculer Wi(a) pour chaque colonne
            for acide2 in alpha:
                
                    for j in range(i+1,len(count)):
                        dico_nij[acide1+acide2+" "+str(i)+" "+str(j)] = n(acide1,i,acide2,j,matrice)
                        dico_wij[acide1+acide2+" "+str(i)+" "+str(j)] = (dico_nij[acide1+acide2+" "+str(i)+" "+str(j)]+1/21.0)/ (len(matrice)+21.0)
                        
    return dico_nij,dico_wij
                        

##########################bout de code permettant d'afficher M0,1############################
"""
 @param position (la colonne)
 @param un acide aminé
 @return le nombre d'occurrence
"""
def occ(pos,char):
    dico = count[pos]
    for i in dico:
        if i == char :
            return dico[i]

#print occ(46,'P')

"""
 @param i : position du premier acide aminé
 @param j : position du second acide aminé
 @param matrice :  le resultat de la lecture du fichier avec la méthode lire_texte(filename)
 pour tout les acides aminées qui sont en position i et j on calcule leur 'information mutuelle'
""" 
def M(i,j,matrice):
    somme = 0
    resultat =0 
    for acide in alpha:
        for a in alpha:
            poidsab = wab(a,i,acide,j,matrice)
            somme += poidsab*log(poidsab/(calPoids(len(matrice),occ(i,a))*calPoids(len(matrice),occ(j,acide))),2)
        resultat = resultat + somme
        somme = 0        
    return resultat
    
print "la valeur de correlation pour M0,1 est:",M(0,1,matrice),"\n"
print ("Si vous voulez voir tout autre chose, ouvrez ce fichier, les appels des fonctions sont commentés,il suffit d'enlever '#' pour voir ce qui se passe. \nBonne lecture!!")

##########################bout de code permettant d'afficher M0,1############################


###########################generation de fichier txt ########################################
    
def paires_de_positions():
    m = 0
    fichier = open("paires_de_positions.txt", "w")
    fichier.write("couple_ij \t Mij")
    for i in range(1,len(count)):
        for j in range(i+1,len(count)+1):
            m = M(i-1,j-1,matrice)
            fichier.write("\n"+str(i)+","+str(j)+'\t'+ str(m))
    fichier.close()
#paires_de_positions()

def log_vraisemblance():
    fichier = open("log_vraisemblance.txt", "w")
    fichier.write("position \t log_vraisemblance")
    contenu = lire_texte("test_seq.txt")[0]
    liste = ss_seq("test_seq.txt")
    for i in range(1,len(contenu)-48+1):
            fichier.write("\n"+str(i)+'\t'+ str(liste[i-1]))
    fichier.close()
#log_vraisemblance()


def entropie_relative():
    fichier = open("entropie_relative.txt", "w")
    fichier.write("position entropie_relative arg_max")
    for i in range(1,len(liste)+1):
        #print "\n"+str(i)+'\t'+ str(liste_entropie[i-1])+'\t'+ str(liste[i-1])
        fichier.write("\n"+str(i)+'\t'+ str(liste_entropie[i-1])+'\t'+ str(liste[i-1]))
    fichier.close()
#entropie_relative()

###############################generation de fichier txt ############################################




"""
calculs des informations_mutuelles pour chaque paire de i,j et de a,b
@param filename le nom du fichier, "Dtrain.txt" par défaut
@return un dictionnaire contenant toutes les infos calculées
avec cles sous forme de [i j]
"""
def Infos_Mutuelles(filename="Dtrain.txt"):
    matrice = lire_texte(filename)
    
    count = comparaison(matrice)
    
    liste_poids = weight(len(matrice),count)
    #print count
    resultat =0
    somme = 0
    dicoM = {}
    dico_nij,dico_wij = seconde_fonc(filename)
    
    for i in range(len(count)-1):
        for j in range(i+1,len(count)):
            resultat = 0
            for acide1 in alpha:
                for acide2 in alpha:
                   
                        poids = dico_wij[acide1+acide2+" "+str(i)+" "+str(j)] #poids = Wij(a,b)
                        
                        somme += poids*log(poids/(liste_poids[i][acide1]*liste_poids[j][acide2]),2)
                resultat = resultat +somme
                somme = 0
                
            dicoM[str(i)+" "+str(j)] = resultat
            resultat=0
    return dicoM

#print Infos_Mutuelles()


"""
fonction permettant d'inverser un dictionnaire, cle:valeur en valeur:cle 
@dico le dictionnaire de depart
@return le dictionnaire inversé
"""
def inverseDico(dico):
    d = {}
    for cle,valeur in dico.items():
        d.update({valeur:cle})
    return d


"""
fonction qui permet de selectionner n paires dont les valeurs Mij sont plus grand
@param n le nombre de paires que l'on veut 
@param dico le resultat de l'appel de fonction Infos_Mutuelles()
@return la liste de paires récupérée
"""
def select_paires(n,dico):
    dic_temp =  inverseDico(dico)
    liste_info_mutuelle = dic_temp.keys()
    res = []
    for i in range(n):
        maxi = max(liste_info_mutuelle)
        liste_info_mutuelle.remove(maxi)
        res.append(dic_temp[maxi])  
    return res
    
#paires = select_paires(50,Infos_Mutuelles())

"""
 stockage des données du fichier distace.txt dans un dictionnaire 
 @param un nom de fichier (utilisation du fichier distances.txt)
 @return un dictionnaire {position : valeur}
""" 
def lire_texte_dico(filename="distances.txt"):
    liste = []
    gd_liste =[]
    fichier = open(filename,"r")
    
    for i in fichier :
        liste = i.split()
        gd_liste.append(liste)

    dico = {}

    for i in range (len(gd_liste)):
        dico[gd_liste[i][0]+" "+gd_liste[i][1]]=gd_liste[i][2]
    
    return dico    
    
"""
fonction permettant de calculer la portion de couple de position ayant une distance < 8 sur le nombre total
de couple récupére, c'est-à-dire len(paires)
@param paires, la liste des couples de position récupérée par la fonction select_paires()
@param dico, le dictionnaire contenant les distances de tout couple, ce dictionnaire est extrait du fichier "distance.txt"
@return la portion ainsi calculée.
""" 
def frac(paires,dico):
    nb_inf_8 = 0
    a = 0.0
    for paire in paires:
        a = dico[paire]        
        if (float(a) < 8):
            nb_inf_8 += 1
    #print nb_inf_8
    return float(nb_inf_8)/len(paires)
        
        
#print frac(paires,lire_texte_dico())
#dico_M = Infos_Mutuelles("Dtrain.txt")
#print(quatrieme_fonction(50,dico_M))



 
