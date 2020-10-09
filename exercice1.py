 #Auteur: Watt_Registe
#Date: 07/09/20
#Version: 1
#Description: Calcul de salaire


def salaire(salaire_horaire: float, nombre_heures:float):
    
    if nombre_heures <= 160:
        salaire_mensuel = salaire_horaire*nombre_heures
    else:
        salaire_mensuel = salaire_horaire*160
        if nombre_heures <= 200 :
        #salaire_mensuel = salaire_horaire*(160+1.25*nombre_heures)
           salaire_mensuel += (salaire_horaire*(nombre_heures-160))*1.25
        else:
            #salaire_mensuel = salaire_horaire*(210+(1.25*(nombre_heures-200)))
            
            salaire_mensuel += salaire_horaire*40*1.25
            salaire_mensuel += (salaire_horaire*(nombre_heures-200))*1.5
    
    return salaire_mensuel


print("Test1", salaire(1,220))
print("Test2", salaire(30,200))
print("Test3", salaire(30,200))