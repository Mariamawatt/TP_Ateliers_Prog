import math
"""

#Auteur: Watt_Registe
#Date: 08/09/20
#Version: 1
#Description: Associer un tarif d'assurance"""

def assurance():
    age = int(input("Entrez votre age:"))
    duree_permis = int(input("Depuis quand etes vous titulaire de votre permis? :"))
    nombre_accident = int(input("Combien d'acidents avez vous provoque?:"))
    
    if(age<25):   
        if(duree_permis<2):
            if(nombre_accident<1):
                tarif=1
            else:   
                tarif=0
        else:  
            if(nombre_accident<1):  
                tarif=2
            elif(nombre_accident==1):  
                tarif=1
            else:  
                tarif=0
    else: 
        
         
        if(duree_permis<2):
            if(nombre_accident<1):  
                tarif=2
            elif(nombre_accident==1):  
                tarif=1
            else:  
                tarif=0
        else:  
            nombre_annee_assurance = int(input("Entrez le nombre d'annees.....:")) 
            if(nombre_accident<1):
                tarif=3
            elif(nombre_accident==1):  
                tarif=2
            elif(nombre_accident==2):  
                tarif=1
            else:  
                tarif=0
                
            if(nombre_annee_assurance>1 and tarif!=0):
               tarif +=1
    
    if(tarif==0):
        tarif="Assurance refusee"
    elif(tarif==1):  
        tarif="rouge"
    elif(tarif==2):
        tarif="orange"
    elif(tarif==3):   
        tarif="vert"
    else:
        tarif="bleu"
    
    return tarif

print(assurance())
         