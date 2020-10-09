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
def str_equation (a: float, b:float, c: float)-> float:
    if(a>0 and b>=0 and c>=0):
    
        equation = "{}x² + {}x + {} =0".format(a,b,c)
        if b == 0:
            equation = "{}x² + {} =0".format(a,c)
        elif c== 0:
            equation = "{}x² + {}x =0".format(a,b)
    elif(a<0 and b<=0 and c<=0):
        
#5
def solution_equation(a: float, b: float, c:float)->float:
    
   
    