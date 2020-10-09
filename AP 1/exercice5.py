#Date :
#Version :
#Description :

def port():
    
    nom_voilier = input("Entrez un nom de voilier :")
    
    longueur_voilier =float(input("Entrez la longueur du voilier :"))
    
    categorie = int(input("Entrez la categorie du voilier :"))
    
    #cout mensuel que doit payer le proprio du voilier
   
    if(longueur_voilier < 5):
        #longueur_voilier < 5
        cout_mensuel = 100
        
    elif (longueur_voilier <=10):
        cout_mensuel = 200
    elif(longueur_voilier <=12):
        cout_mensuel = 400
    else : 
        cout_mensuel = 600
        
    #taxe speciale anuelle que doit payer le proprio du voilier
    
    if(categorie ==1 or categorie ==2 or categorie== 3):
        if(categorie == 1):
            taxe_speciale_annuelle = 100
        elif(categorie == 2):
            taxe_speciale_annuelle = 150
        else :
            taxe_speciale_annuelle = 250
    else :   
        message = "Categorie invalide"
        
    #cout annuel de la place au port 
    cout_annuel = taxe_speciale_annuelle + 12*cout_mensuel

    
    message = "Le cout annuel d'une place obtenu au port pour le voilier " + nom_voilier + " est de " + str(cout_annuel) + " euros" 
    return message

print(port())
    
    