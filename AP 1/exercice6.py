#Date :
#Version :
#Description :

def frais_mensuel(nbre_km: float, type_carburant: str, cylindree: int, prix_carburant: float):
    
    if(type_carburant=="E" or type_carburant=="D"):
    
        if (type_carburant=="E"):
            if(cylindree>2000):
                frais_mensuel=(0.1*(nbre_km/12)*prix_carburant)*1.5
            elif (cylindree<2000):
                frais_mensuel=(0.08*(nbre_km/12)*prix_carburant)*1.5
        else:
            frais_mensuel=0.08*(nbre_km/12)*prix_carburant*1.7
    else:
        frais_mensuel= "type_carburant non valide"
        
    return frais_mensuel

print(frais_mensuel(1200, "E", 2100, 1))
print(frais_mensuel(1200, "f", 2100, 1))

#15