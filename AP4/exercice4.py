# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:56:54 2020

@author: Mariama
"""

def buildDict(fileName:str)->list:
    with io.open(fichier, 'r', encoding='utf8') as f:
        # splitlines = ça coupe à chaque fois qu'il y a un retour à la ligne et mets les mots dans une liste
        contenue = f.read().splitlines()

    return contenue
print (buildDict("littre.txt"))