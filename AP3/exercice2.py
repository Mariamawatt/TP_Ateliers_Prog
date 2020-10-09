# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 14:39:59 2020

@author: Mariama
"""

# ***********************L[i] toujours en crochets**************************
#1
def position(L: list, e:int)->int :
    i = 0
    taille = len(L)
    indice = -1
    for i in range(taille):
        if L[i] == e :
            indice = i
            
    return indice
#print(position([2, 5, 4], 5))

def position_while(L: list, e:int)->int:
    i = 0
    taille = len(L)
    isFound = False
    indice = -1
    while (not isFound and i<taille):
        if(e == L[i]):
           indice = i
           isFound = True
           i += 1
    return indice
#print(position([2, 5, 4], 2))
#2

def nb_occurrences(L: list, e: int)-> int:
    i = 0
    taille = len (L)
    nomb_occ = 0
    for i in range (taille):
        if L[i] == e:
            nomb_occ += 1
    return nomb_occ
#print(nb_occurrences([2, 2, 3], 3))
