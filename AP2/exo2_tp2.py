"""

#Auteur: Watt_Registe
#Date: 08/09/20
#Version: 1
#Description: Calcul année bissextile"""

#1

def est_bissextile (annee: int)-> bool:
    
    """renseigne si l'année est bissextile ou non"""
    resultat = 0
    
    if ((annee%4 == 0 and annee%100 != 0) or annee%400 == 0 ):
        
        resultat = 1
    return resultat

#2

def test():
    
    print (est_bissextile(2020))
    print (est_bissextile(2024))
    print (est_bissextile(2023))
    print (est_bissextile(2010))
    
    
    
 #3
 
test ()