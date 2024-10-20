import random

def cleanup(lista, dictionary, vattentätQuiz, värmeQuiz):
    
    for x in range(len(lista)-1, -1, -1):
        item = lista[x]
        infoDict = dictionary.get(item)
        if infoDict.get("vattentät") != vattentätQuiz:
            lista.remove(item)
        elif värmeQuiz == "all":
            continue
        elif infoDict.get("värme") != värmeQuiz:
            lista.remove(item)

def quiz():
    svar = input("Ska outfiten vara vattentät? ja/nej")
    if svar == "ja":
        vattentät = True
    elif svar == "nej":
        vattentät = False
    
    svar = input("Vilken värme ska outfiten vara anpassad för? (h)ot/(c)old")
    if svar == "h":
        värme = "hot"
    elif svar == "c":
        värme = "cold"
    
    svar = input("Vill du ha en jacka? (j)a/(n)ej")
    if svar == "j":
        jacka = True
    elif svar == "n":
        jacka = False

    return vattentät, värme, jacka


def generator(lista):
    if len(lista) != 1:
        index = random.randint(0, (len(lista)-1))
        choosen = lista[index]
    else:
        choosen = lista[0]
    
    return choosen


def wardrobe():
    tröjor = {
        "tshirt":{"vattentät":False, "värme":"hot"},
        "hoodie":{"vattentät":False, "värme":"cold"}
        "linne":{"vattentät":False, "värme":"hot"}
        "croptop":{"vattentät":False, "värme":"hot"}
     }
    byxor = {
        "byxor":{"vattentät":False, "värme":"cold"},
        "finbyxor": {"vattentät":False, "värme":"hot"},
        "shorts":{"vattentät":False, "värme":"hot"},
        "galonisar":{"vattentät":True, "värme":"hot"}
    }
    skor = {
        "stövlar":{"vattentät":True, "värme":"cold"},
        "pumps":{"vattentät":False, "värme":"hot"},
        "sneakers":{"vattentät":False, "värme":"hot"},
        "barfota":{"vattentät":False, "värme":"hot"}
    }
    jackor = {
        "kappa":{"vattentät":False, "värme":"cold"},
        "läderjacka":{"vattentät":False, "värme":"hot"},
        "regnjacka":{"vattentät":True, "värme":"cold"}
        "kofta":{"vattentät":False, "värme":"hot"}
        "läderjacka":{"vattentät":False, "värme":"cold"}
    }

    listaTröjor = ["tshirt", "hoodie"]
    listaByxor = ["byxor","finbyxor","shorts","galonisar"]
    listaSkor = ["stövlar","pumps","sneakers", "barfota"] 
    listaJackor = ["kappa", "läderjacka", "regnjacka", "kofta", "läderjacka"]   

    vattentätQuiz, värmeQuiz, jackaQuiz = quiz()
    
    cleanup(listaTröjor, tröjor, vattentätQuiz, värmeQuiz)
    cleanup(listaByxor, byxor, vattentätQuiz, värmeQuiz)
    cleanup(listaSkor, skor, vattentätQuiz, värmeQuiz)
    if jackaQuiz == True:
        cleanup(listaJacka)

    return generator(listaTröjor), generator(listaByxor), generator(listaSkor)
    

def menu():
    while True:
        menuChoice = input("Välj ett alternativ:\ng) Generera en outfit \na) Avsluta \n ")
        if menuChoice == "g":
            tröja, byxa, sko = wardrobe()
            print(f"Här är din outfit:\n {tröja}\n {byxa} \n {sko}")
        if menuChoice == "a":
            exit()
            return False

def main():
    print("Welcome to this outfit generator!")
    menu()

main()

#WOOOO SLAY