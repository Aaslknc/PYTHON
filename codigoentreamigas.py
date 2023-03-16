def traduzir(string, traducao = ""):
    for numero in string.split():
        
        if numero == "0":
            traducao += " "
        elif numero == "1":
            traducao += "a"
        elif numero == "2":
            traducao += "b"
        elif numero == "3":
            traducao += "c"
        elif numero == "4":
            traducao += "d"
        elif numero == "5":
            traducao += "e"
        if numero == "6":
            traducao += "f"
        elif numero == "7":
            traducao += "g"
        elif numero == "8":
            traducao += "h"
        elif numero == "9":
            traducao += "i"
        elif numero == "10":
            traducao += "j"
        elif numero == "11":
            traducao += "k"
        if numero == "12":
            traducao += "l"
        elif numero == "13":
            traducao += "m"
        elif numero == "14":
            traducao += "n"
        elif numero == "15":
            traducao += "o"
        elif numero == "16":
            traducao += "p"
        elif numero == "17":
            traducao += "q"
        if numero == "18":
            traducao += "r"
        elif numero == "19":
            traducao += "s"
        elif numero == "20":
            traducao += "t"
        elif numero == "21":
            traducao += "u"
        elif numero == "22":
            traducao += "v"
        elif numero == "23":
            traducao += "w"
        elif numero == "24":
            traducao += "x"
        elif numero == "25":
            traducao += "y"
        elif numero == "26":
            traducao += "z"
    
    return traducao

entrada = input()
if traduzir(entrada) == "fim":
    print("")
else:
    while traduzir(entrada) != "fim":
        print(traduzir(entrada))
        entrada = input()
        
