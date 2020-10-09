# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:46:41 2020

@author: Mariama
"""
import matplotlib.pyplot as plt
def histo (F: list)-> list:
    
    liste_fin = []
    
    for i in range (min(F), max(F)+1):
        compteur = 0
        for e in F :
            if e == i:
                compteur += 1
        liste_fin.append(compteur)
                
    return liste_fin

print(histo([-1, 5, 8, -1, -4, 3, 0])) 

#2
def inj(f):
    bool=True
    liste=histo(f)
    for e in liste:
        if(e>2):
            bool=False
    return(bool)
f = [1, 2, 3]
#print(inj(f))

#3
def surj(test):
    bool = True
    liste_2=histo(test)
    for e in liste_2 :
        if(e==0):
            bool=False
    return(bool)
test = [1, 2, 2, 4]
#print(surj(test))

#4
def bij(test2):
    
    return (inj(test2) and surj(test2))

test2 = [1,2, 3]
#print (bij(test2))

#question 2
def affichage_histo(f :list) :
    return (plt.hist(f, rwidth = 0.7))
#affichage_histo([3, 2, 2, 7], )
#plt.hist([1,0,2,1,2,1,3,7,3,2], rwidth = 0.7)