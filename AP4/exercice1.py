# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 20:39:58 2020

@author: Mariama
"""

def full_name(str_arg : str)-> str:
   liste = str_arg.split() 
   prenom = liste [0]
   nom = liste [1]
   
   prenom_f = prenom.capitalize()
   nom_f = nom.upper()
   
   return (prenom_f + " " + nom_f)

print(full_name("paul dupont"))