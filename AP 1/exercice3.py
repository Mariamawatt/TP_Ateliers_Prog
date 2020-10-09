#Auteur :
#Date :
#Version :
#Description :
def impots(age: int, sexe: str):
    
    
    if(sexe =="M" or sexe =="F"):
        if( (sexe == "M" and age >20) or (sexe == "F" and age >=18 and age <=35 )):
            resultat = "Paie les impots"
        else:
            resultat = "Ne paie pas les impots"
    else:
        resultat= "Votre sexe est incorrect, veuillez choisir entre M et F"

    return resultat

print(impots(16, "F"))
print(impots(30, "M"))



