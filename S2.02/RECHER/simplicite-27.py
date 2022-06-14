class Main :
    
    def main(args) :
        str = Main.removeSpaces()
        print("\n" + str)

    def  removeSpaces() :
        print("\nEntrez une chaine de caractères :")
        scanner =  "Python-inputs"
        str = input()
        tmp = ""
        espace = 0
        i = 0
        while (i < len(str.strip())) :
            j = i
            while (str[j] == ' ') :
                espace += 1
                j += 1
            if (espace == 1) :
                if (str[i - 1] == ' ') :
                    tmp += str[i]
            else :
                tmp += str[i]
            espace = 0
            i += 1
        return tmp
    

if __name__ == "__main__" :
    Main.main([])
