#Auteur : Zakaria Ezzaatari et Mariama Watt
#Date : 15/09/2020
#Version : 1.0
#Description : Atelier de programmation 4
import re

def full_name(str_arg:str)->str:
    """Cette fonction renvoie le nom en majuscule et le prenom
    avec la premiere lettre en majuscule"""
    nom=""
    prenom=""
    res=""
    longeur=len(str_arg)
    esp=str_arg.find(" ")
    for i in range(0,longeur):
        if i < esp:
            nom+=str_arg[i]
        elif i>esp:
            prenom+=str_arg[i]
    res+=nom.upper()+" "+prenom.capitalize()
    return res
    

def is_mail(str_arg:str)->(int,int):

    longeur=len(str_arg)
    corp=""
    domaine=""
    pos_aro=str_arg.find("@")
    pos_esp=str_arg.find(" ")
    if pos_aro==0 or (pos_esp!=-1 and pos_esp<pos_aro):
        valide=(0,1)
    elif pos_aro==-1:
        valide=(0,2)
    else:  
        rex='[A-Z áàâäãéèêëíìîïóòôöõúùûüýÿÁÀÂÄÃÉÈÊËÍÌÎÏÓÒÔÖÕÚÙÛÜÝ:/?(()<>@,;:"[]|ç%&]'
        for i in range(0,longeur):
            if i<pos_aro:
                corp+=str_arg[i]
            elif i>pos_aro:
                domaine+=str_arg[i]
        if re.search(rex,domaine) is not None:
            valide=(0,3)
        elif domaine.find(".")==-1:
            valide=(0,4)
        else:
            valide=(1,5)
    return valide

print(is_mail("a a@bb.cc"))
