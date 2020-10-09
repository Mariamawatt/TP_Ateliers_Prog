# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:49:41 2020

@author: Mariama
"""

def separer(L_non_triee : list)->list:
    LSEP = []
    liste_negative =[]
    liste_nulle = []
    liste_positive = []
    
    for elt in L_non_triee:
        if elt < 0 :
            liste_negative.append(elt)
        elif elt == 0 :
            liste_nulle.append(elt)
        elif elt > 0 :
            liste_positive.append(elt)
    LSEP = liste_negative + liste_nulle + liste_positive
    
    return LSEP

print (separer ([1, -1, 0, 3, -2, 5, 0]))