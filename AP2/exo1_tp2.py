
"""

#Auteur: Watt_Registe
#Date: 08/09/20
#Version: 1
#Description: Calcul de l'imc"""

#1

def message_imc (imc: float):
    """ renvoie la chaine de caractère imc"""
    IMC_FAM = 16.5
    IMC_MAIG = 18.5
    IMC_NORM = 25
    IMC_SURP = 30
    IMC_OB_MOD = 35
    IMC_OB_SEV = 40 
    
    if imc<IMC_FAM :
        message = "dénutrition ou famine"
    elif imc<IMC_MAIG :
        message = "maigreur"
    elif imc<IMC_NORM :
        message = "corpulence normale"
    elif imc<IMC_SURP :
        message = "surpoids"
    elif imc<IMC_OB_MOD :
        message = "obésité modéré"
    elif imc<IMC_OB_SEV :
        message = "obésité sévère"
    else : 
        message = "obésité morbide"
    return message

#2
    
def test_imc():
    print (message_imc(15))
    print (message_imc(17))
    print (message_imc(23))
    print (message_imc(28))
    print (message_imc(33))
    print (message_imc(39))
    print (message_imc(45))
    
   #3
    
test_imc()

