def erase(string):
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


string = " Bon jour je  suis    f  "
print(erase(string))

