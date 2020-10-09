import math
"""

#Auteur: Watt_Registe
#Date: 08/09/20
#Version: 1
#Description: résolution d'une équation du second degré"""

#1
def discriminant(a: float, b: float, c: float)-> float :
    delta = (b*b) - 4*a*c
    return delta

#2
def racine_unique (a: float, b:float)-> float :
    x = -b/(2*a)
    
    return x

#3
def racine_double (a: float, b:float, delta: float, num: int)-> float:
    if (num ==1 or num==2):
        if num == 1:
            x = (-b + math.sqrt(delta))/(2*a)
        else: 
            x = (-b - math.sqrt(delta))/(2*a)
    else:
        x = "pas de solution"
    return x
    
#4
def str_equation (a: float, b:float, c: float)-> str:
    
    #cas ou a ou b egal a 1 ou a -1 omettre le chiffre1
    
    if(abs(a)==1 or abs(b)==1 ):
        if(abs(a)==1):   
            if(a>0):
                a_final = ""
            else:
                a_final = "-"
            
        if(abs(b)==1):   
            if(b>0):
                b_final ="+"
            else:
                b_final = "-"      
    
        #cas ou b est positif
    if(b>0):
            b_final = "+" + str(b)
            
    if(c>0):
            c_final = "+" + str(c)
    
    
    if b == 0:
        equation = "{}x² {} =0".format(a_final,c_final)
    elif c== 0:
        equation = "{}x²  {}x =0".format(a_final,b_final)
    else:    
        equation = "{}x² {}x {} =0".format(a_final,b_final,c_final)
       
    return equation
#5





def solution_equation(a: float, b: float, c: float)-> str: 

    discri = discriminant(a,b,c) 
    if(discri<0):
        solution ="Solution de l'equation " + str_equation(a,b,c) + "Pas de racine reelle"
    elif(discri==0):
        solution ="Solution de l'equation " + str_equation(a,b,c) + "Racine unique : x =" + str(racine_unique(a,b))
    else:   
        solution ="Solution de l'equation " + str_equation(a,b,c) + "Deux racines : x1=" +str(racine_double(a,b,discri,1)) + "x2=" + str(racine_double(a,b,discri,2))


    return solution
#
#6
def equation(a: float, b:float, c: float):
    print(solution_equation(a,b,c))
    
def test_equation():
    equation(1,4,4) 
    
test_equation()