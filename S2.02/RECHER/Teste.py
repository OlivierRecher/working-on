import time
from random import randint

#creation des chaines
court = ''.join([chr(randint(32, 126)) for i in range(100)])
long = ''.join([chr(randint(32, 126)) for i in range(100000)])
# inspire du code de Hugo Castell



#efficacite134
def erase_efficacite134(text):
    """
    Removes only single spaces from given string.
    :param text : string to edit
    :return : edited string
    """
    listedText = list(text)
    for i, char in enumerate(listedText):
        tailleText = len(listedText)
        if (char == " " and tailleText == 1) or (char == " "
          and listedText[max(i-1, int(tailleText > 1))] != " "
          and listedText[min(i+1, tailleText-int(tailleText > 1)*2)] != " "):
            del listedText[i]
    return "".join(char for char in listedText)



#simplicite50
def erase_simplicite50(string):
    """
    Supprime les espaces simples d'une chaine de caractères

    Parameters
    ----------
    string : str
        Une chaine de caractères 

    Returns
    -------
    str
        Une chaine de caractères sans les espaces de plus d'un caractère
    """
    new_string = ""
    for i in range(len(string)):
        if string[i] != " ":
            new_string += string[i]
        else:
            if i==0:
                if string[i+1] == " ":
                    new_string += string[i]
            elif i==len(string)-1:
                if string[i-1] == " ":
                    new_string += string[i]
            else:
                if string[i-1] == " " or string[i+1] == " ":
                    new_string += string[i]
    return new_string



#sobriete161
def bonmot(var):

   if var ==" " or var=="":
       return ("")
   space=0
   for i in var:
       if i == " ":
           space+=1
   if space==len(var):
       return(var)

   else:
       o=0
       if var[0] == " " and var[1] != " ":
            var = var[:0] + "" + var[1:]

       if var[-1] == " " and var[-2] != " ":
           var = var[:-1] + ""


       fin=0
       for i in range(-1,-len(var),-1):
          if var[i]==" ":
              fin +=1
          else:
            break


       print(fin)
       if (fin%2 ==0):
           o=0
       else:
           o=1
       NvMot=""
       strlen = len(var)

       i=0

       while i<strlen-o:
           if var[i]==" ":
               if var[i+1] ==" " or var[i-1]==" ":
                       NvMot+= var[i]
                       NvMot+= var[i+1]
                       i+=1
           else:
               NvMot += var[i]
           i+=1

       if (o>0):
          NvMot+=" "
       return (NvMot)





#Test de vérification courte chaine

start = time.process_time()

#enlever le "#" de l'algo a teste

#erase_efficacite134(court)
erase_simplicite50(court)
#bonmot(court)
end = time.process_time()


print("Temps d'execution courte chaine:")
print(end - start)


#Test de vérification longue chaine

start = time.process_time()

#enlever le "#" de l'algo a teste

#erase_efficacite134(long)
erase_simplicite50(long)
#bonmot(long)
end = time.process_time()


print("Temps d'execution longue chaine:")
print(end - start)