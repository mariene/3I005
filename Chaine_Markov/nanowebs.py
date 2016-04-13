# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 22:19:40 2016

@author: Mariène
"""

from datastructures import SimpleWeb
#import networkx as nx

def creeNanoWeb1() :
    n=SimpleWeb (10) # 10 noeuds de 0 a 9
    n.AddArc (0,1) ;n.AddArc(0,4) ;
    n.AddArc (1,2)
    n.AddArc (2,3) ;n.AddArc(2,4) ;
    n.AddArc (3,9)
    n.AddArc (4,2) ;n.AddArc(4,5) ;n.AddArc(4,6) ;
    n.AddArc (5,6)
    n.AddArc (6,5) ;n.AddArc(6,7) ;
    n.AddArc (7,8)
    n.AddArc (8,7)
    n.updateProbas()
    #print n.matrice
    #n.updateTransitionMatrix()
    return n ;

def creeNanoWeb2():
    n=SimpleWeb(10)
    n.AddArc(0,9)
    n.AddArc(1,0);n.AddArc(1,5);
    n.AddArc(2,1);n.AddArc(2,4);
    n.AddArc(3,2);
    n.AddArc(4,3)
    n.AddArc(5,4)
    n.AddArc(6,5)
    n.AddArc(7,6);n.AddArc(7,3);
    n.AddArc(8,7)
    n.AddArc(9,2);n.AddArc(9,8);
    n.updateProbas()
    return n
    
def creeNanoWeb3():
    n=SimpleWeb(10)
    n.AddArc(0,1)
    n.AddArc(1,2);n.AddArc(1,3);
    n.AddArc(2,3);n.AddArc(2,9);
    n.AddArc(4,5)
    n.AddArc(5,4)
    n.AddArc(6,7)
    n.AddArc(7,8)
    n.AddArc(8,7)
    n.updateProbas()
    return n
    
#if __name__ == " __main__ " :
#    graph=creeNanoWeb1()
#    print(graph) # a f f i ch e la representat ion t ex t e
#    graph.getGraph("nano1.png")
    
#i = SimpleWeb(3)
#i.generateurSimple()
#print i
#i.getGraph("g.png")
