# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:15:01 2020

@author: Mariama
"""

import io
#1
def mots_Nlettres(lst_mot : list, n: int)->list :
    #taille = len(lst_mot)
    nb_mots = []
    
    for mot in lst_mot :
        if  len(mot) == n:
            nb_mots.append(mot)
    return nb_mots
        
#print(mots_Nlettres(["loi", "jouet", "rire"], 4)) 

#2

def commence_par(mot: str, prefixe:str)->bool:
    resultat_prefixe = mot.startswith(prefixe)
    return resultat_prefixe 
#print(commence_par("professeur", "pof"))

#3

def finit_par(mot: str, suffixe:str)->bool:
    resultat_suffixe = mot.endswith(suffixe)
    return resultat_suffixe 
#print(finit_par("mère", "ère"))

#4

def finissent_par(lst_mot:list, suffixe:str)->list:
    nb_mots_suffixe = []
    for mot_suffixe in lst_mot :
        if finit_par (mot_suffixe, suffixe):
            nb_mots_suffixe.append(mot_suffixe)
    return nb_mots_suffixe

#print(finissent_par(["mère","pire","ère"], "ère"))

#5
def commencent_par(lst_mot:list, prefixe:str)->list:
    nb_mots_prefixe = []
    for mot_prefixe in lst_mot :
        if commence_par (mot_prefixe, prefixe):
            nb_mots_prefixe.append(mot_prefixe)
    return nb_mots_prefixe
#print(commencent_par(["professeur", "prof", "prio", "professionnel"], "prof"))
            
#6
def liste_mots (lst_mot: list, prefixe: str, suffixe:str, n: int)-> list :
    liste_finale = mots_Nlettres (lst_mot, n)
    liste_finale = commencent_par(liste_finale, prefixe)
    liste_finale = finissent_par(liste_finale, suffixe)
    
    return liste_finale

#mot qui commence par "p", qui finit par "ère" et qui comporte 4 lettres
#print(liste_mots (["professeur", "prof", "mère", "ère"], "p", "ère", 4))

#7
def dictionnaire(fichier:str)->list:
    with io.open(fichier, 'r', encoding='utf8') as f:
        # splitlines = ça coupe à chaque fois qu'il y a un retour à la ligne et mets les mots dans une liste
        contenue = f.read().splitlines()

    return contenue
print (dictionnaire("littre.txt"))