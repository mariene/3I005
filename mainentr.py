# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 18:19:10 2016

@author: 3202002
"""
import Entropie as ent
import string
import matplotlib.pyplot as plt
import numpy as np

###########################################################Tests######################################################################
listefr = ent.DicoToList_bis(ent.DicoToDicoProba(ent.count_ngrams("bouleDeSuif.txt",1)))
listean = ent.DicoToList_bis(ent.DicoToDicoProba(ent.count_ngrams("warandpeace.txt",1)))
listeal = ent.DicoToList_bis(ent.DicoToDicoProba(ent.count_ngrams("faust.txt",1)))
alphabet = list(string.ascii_uppercase)
plt.xlabel(u'Alphabet')
plt.ylabel(u'Probabilité')
plt.title(u"Les probabilités de chaque lettre en fonction des langues")
x=np.arange(26)
ax = plt.axes()
ax.set_xticks(x + 0.5)
ax.set_xticklabels(alphabet)
plt.bar(x,listefr,1, alpha=0.5, color='b',label="francais")
#plt.bar(x,listean,1, alpha=0.5, color='r',label="anglais")
plt.bar(x,listeal, 1, alpha=0.5,color='g',label="allemand")
plt.legend()
plt.show()

#print(ent.Classificateur("test.txt"))
