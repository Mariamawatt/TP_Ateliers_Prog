# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:47:34 2020

@author: Mariama
"""
import random 
#1
def places_lettres(ch: str, mot:str)->list:
    liste_finale =[]
    i = 0
    for i in range (len(mot)):
        if mot [i] == ch :
            liste_finale.append(i)
    return liste_finale

#print(places_lettres("o", "bonjour"))

#2
def outputStr(mot: str, lpos:list)-> str:
    chr_fin = ""
   
    #for num_indice in range (len(lpos)):
    for i in range (len(mot)):
        if i in lpos :
            chr_fin += mot [i]
        else :
            chr_fin += "_"
                
    return chr_fin 

#print(outputStr("bonjour", [0,2 ]))

#3
def rungame ():
    findujeu = False
    compteur = 10
    #lst =["paris","londres","madrid","berlin","new-york", "mariama_watt"]
    lst = ["mariama_watt"]
    #lst_len = len(lst)
    indices_trouves = []
    
    mot_alea = random.choice(lst)
    print("mot a trouver :", outputStr(mot_alea, []))
    print(mot_alea)
    while (not findujeu and compteur > 0):
        proposition = input("saisir un char:")
        compteur -= 1
        indices_trouves += places_lettres(proposition ,mot_alea)
        resultat = outputStr(mot_alea, indices_trouves)
        print("mot a trouver:", resultat)
        if resultat == mot_alea :
            findujeu = True
    if findujeu:
        print ("win")
    else :
        print ("lose")
rungame()      

    
    
    
    