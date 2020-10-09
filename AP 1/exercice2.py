#Auteur: Watt_Registe
#Date: 07/09/20
#Version: 1
#Description: Calcul de salaire

def caracteres(caractere: str):
     
    if (ord(caractere)>=48 and ord(caractere)<=57):
        resultat = "chiffre"
    elif (ord(caractere)>=65 and ord(caractere)<=90):
        resultat = "lettre majuscule"
    elif (ord(caractere)>=97 and ord(caractere)<=122):
        resultat = "lettre miniscule"
    else:
        resultat = "caractere special"
        
    return resultat

print(caracteres("A"))
print(caracteres("a"))
print(caracteres("1"))
print(caracteres("/"))