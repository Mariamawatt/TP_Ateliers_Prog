"""

#Auteur: Watt_Registe
#Date: 08/09/20
#Version: 1
#Description: Calcul date"""

def est_bissextile (annee: int)-> bool :
    resultat = 0
    #"""renseigne si l'année est bissextile ou non"""
    if ((annee%4 == 0 and annee%100 != 0) or annee%400 == 0 ) :
        resultat = 1
        return resultat

### EX4
## 4.1
def date_est_valide(jour : int, mois : int , annee : int):
    ## on convertis les valeurs en int (dans le cas où elles sont rentrées en format str)
    ## On vérifie la validité des dates : mois à 30/31 jours, nombre de jours du mois de février en fonction de l'année (bissextile ou pas)
    try:
        jour = int(jour)
        mois = int(mois)
        annee = int(annee)
        return ((jour in range(1,30)) & (mois in [4,5,9,11]) &
                    (annee >=1900 and annee <=2020))|((jour in range(1,31)) & (mois in [1,3,5,7,8,10,12]) &
                                                      (annee >=1900 and annee <=2020))|((jour in range(1,28)) & (mois==2) & (est_bissextile(annee)==False) & 
                                                                                        (annee >=1900 and annee <=2020))|((jour in range(1,29)) & (mois==2) & (est_bissextile(annee)==True) & (annee >=1900 and annee <=2020))
    except :
        print("Le format des paramètres n'est pas correct. Veuillez rentrer des nombres")

## 4.2        
import datetime
def saisie_date_naissance() :
    ## On invite la personne à rentrer les valeurs
    ## on vérfie la validité de la date avec la fonction date_est_valide
    ## on renvoie une valeur de type date avec la fonction date du librarie datetime
    annee = int(input("saisissez une année"))
    mois = int(input("saisissez un mois"))
    jour = int(input("saisissez un jour"))
    if date_est_valide(jour, mois, annee) : 
        return(http://datetime.date q(annee, mois, jour))

    from datetime import date, timedelta

## 4.3       
import datetime
from datetime import date

def age(date_naissance) :
    ## on utilise le format date anglais ici : aaaa-mm-jj
    ## on renvoie l'age en nombre d'année (arrondi)
    date_naissance = datetime.datetime.strptime(date_naissance, '%Y-%m-%d')
    age = (http://datetime.datetime.today() - date_naissance) // datetime.timedelta(days=365.2425)
    return(age)

### 4.4
def est_majeur(date_naissance) :
    ## on fait appel à la fonction age pour calculer l'age 
    ## on vérifie si l'age dépasse 18 ans
    age_cal =  age(date_naissance) 
    return (age_cal>=18)

##4.5 
def test_acces() :
    ## On invite la personne à rentrer  une date sous le format YYYY-MM-DD
    ## on utilise les fonctipns age et est_majeur pour calculer son age et afficher un message d'accueil en conséquence
    date_naissance = input('Entrez une date sous le format YYYY-MM-DD')
    age_cal =  age(date_naissance) 
    if est_majeur(date_naissance)==True :
        print("Bonjour, vous avez", age_cal, "ans, Accès autorisé")
    else:
        print("Désolé, vous avez", age_cal, "ans, Accès interdit")

## 4.6
#4.1
print(date_est_valide(10,10, 2020))
print(date_est_valide(30,2, 2020))

#4.2
saisie_date_naissance()

#4.3
age("2000-4-4")

#4.4
est_majeur("2000-4-4")
est_majeur("2005-4-4")

#4.5
test_acces()