"""

#Auteur: Watt_Registe
#Date: 08/09/20
#Version: 1
#Description: Calcul année bissextile"""

#1

def somme (L: list)->int:
    taille = len (L)
    i = 0
    s = 0
    for i in range (taille):
        s += L[i]
    return s

def somme1 (L: list)->int:
    s = 0
    for e in L :
        s += e
    return s

def somme2 (L:list)->int:
    taille = len (L)
    s = 0
    i=0
    while i<taille:
        s += L[i]
        i += 1
    return s

#2
def test_exercice1 ():
    print("TEST SOMME")
    #test liste vide
    print("Test liste vide :",somme2([]))
    #test somme 11111
    So=[1,10,100,1000,10000]
    print("Test somme 1111:",somme2(So))
    
test_exercice1 ()

#3
def moyenne (L: list)->float:
    taille= len (L)
    if taille ==0 :
        moyenne_liste = 0 
    else :
        moyenne_liste = somme (L) / len(L)
        
    return moyenne_liste
#print + appelation de la fonction
#print (moyenne([1,10,100,1000,10000])) 

#4
def nb_sup (L: list, e: int)->int:
    i=0
    taille = len(L)
    n = 0
    for i in range(taille):
        if e< L[i]:
            n+=1
    return n

def nb_sup1 (L: list, e:int)-> int:
    n =0
    for element in L:
       if e< element:
        n+= 1
    return n
#5
def moy_sup (L:list, e:int)-> float:
    L_superieur = []
    taille = len(L)
    i=0
    for i in range(taille) :
        if e< L[i]:
            L_superieur.append(L[i])
   
    return moyenne(L_superieur)
# le prog récupère les valeurs supérieures à 3 et calcule la moyenne, ici ((5+3)/2) = 4
#print (moy_sup([1, 2, 3, 5], 3)) 

#6
def val_max(L: list)-> int:
    i=0
    taille=len(L)
    valeur_max = L[i] 
    for i in range(taille):
        if valeur_max < L[i]: 
            valeur_max = L[i] #remplacer
    return valeur_max
#print (val_max([8, 2, 9, 5])) 

#7
def ind_max(L:list)->int :
    i=0
    taille=len(L)
    valeur_max = i
    for i in range(taille):
        if valeur_max < L[i]: 
            valeur_max = i #remplacer
    return valeur_max
print (ind_max([8, 2, 9, 5])) 
    
    
    