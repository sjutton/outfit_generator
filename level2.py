import random

def editor(lista, dictionary):
    if len(lista) > 1:
        for n in range(0,len(lista)):
            print(str(n+1)+ ")", lista[n])
        userChoice = int(input("Vilket alternativ?\n"))
        plagg = lista[userChoice-1] 
            
    else:
        answer = input("Det finns inga andra tillgängliga alternativ som passar dina krav, vill du välja mellan alla tillgängliga plagg? \n(j)a \n(n)ej")
        if answer == "j":
            lista = list(dictionary.keys())
            for n in range(0, len(lista)):
                print(n+1,")", lista[n])
            userChoice = int(input("Vilket alternativ?\n"))
            plagg = lista[userChoice-1] 
    return plagg
            
        

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
    svar = input("Ska outfiten vara vattentät? (j)a/(n)ej")
    if svar == "j":
        vattentät = True
    elif svar == "n":
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


def randomizer(lista):
    if len(lista) > 1:
        index = random.randint(0, (len(lista)-1))
        choosen = lista[index]
    elif len(lista) == 1:
        choosen = lista[0]
    else: choosen = "[Finns inget matchande plagg i databasen]"
    return choosen


def outfit_generator():
    tröjor = {
        "tshirt":{"vattentät":False, "värme":"hot"},
        "hoodie":{"vattentät":False, "värme":"cold"},
        "linne":{"vattentät":False, "värme":"hot"},
        "croptop":{"vattentät":False, "värme":"hot"},
        "soppåse":{"vattentät":True, "värme":"hot"},
        "tjock soppåse":{"vattentät":True, "värme":"cold"}
     }
    byxor = {
        "byxor":{"vattentät":False, "värme":"cold"},
        "finbyxor": {"vattentät":False, "värme":"hot"},
        "shorts":{"vattentät":False, "värme":"hot"},
        "galonisar":{"vattentät":True, "värme":"hot"},
        "täckbyxor":{"vattentät":True, "värme":"cold"},
        "kort kjol":{"vattentät":False, "värme":"hot"},
        "lång kjol":{"vattentät":False, "värme":"cold"}
    }
    skor = {
        "stövlar":{"vattentät":True, "värme":"cold"},
        "pumps":{"vattentät":False, "värme":"hot"},
        "sneakers":{"vattentät":False, "värme":"hot"},
        "barfota":{"vattentät":False, "värme":"hot"},
        "flipflops":{"vattentät":False, "värme":"hot"},
        "crocs":{"vattentät":False, "värme":"hot"},
        "uggs":{"vattentät":False, "värme":"cold"},
        "vandringskängor":{"vattentät":True, "värme":"cold"}
    }
    jackor = {
        "kappa":{"vattentät":True, "värme":"cold"},
        "läderjacka":{"vattentät":False, "värme":"hot"},
        "regnjacka":{"vattentät":True, "värme":"hot"},
        "kofta":{"vattentät":False, "värme":"hot"},
        "väst":{"vattentät":False, "värme":"cold"},
        "regnponcho":{"vattentät":True, "värme":"hot"}
    }

    listaTröjor = ["tshirt", "hoodie", "linne", "croptop"]
    listaByxor = ["byxor","finbyxor","shorts","galonisar"]
    listaSkor = ["stövlar","pumps","sneakers", "barfota"] 
    listaJackor = ["kappa", "läderjacka", "regnjacka", "kofta", "väst"]   

    vattentätQuiz, värmeQuiz, jackaQuiz = quiz()
    
    cleanup(listaTröjor, tröjor, vattentätQuiz, värmeQuiz)
    cleanup(listaByxor, byxor, vattentätQuiz, värmeQuiz)
    cleanup(listaSkor, skor, vattentätQuiz, värmeQuiz)
    cleanup(listaJackor, jackor, vattentätQuiz, värmeQuiz)
    
    if jackaQuiz == True:
        jacka = randomizer(listaJackor)
    else: jacka = "Ingen jacka"


    tröja = randomizer(listaTröjor)
    byxa = randomizer(listaByxor)
    sko = randomizer(listaSkor)

    print(f"Här är din outfit:\n {tröja}\n {byxa} \n {sko}\n {jacka}")

    
    userEdit = input("Vill du göra ändringar till outfiten? \n(j)a/(n)ej")
    while True:
        if userEdit == "j":
            userItem = input("Vilket plagg vill du ändra?\nt)tröja \nb)byxor \ns)skor \nj)jacka\n")
            if userItem == "t":
                tröja = editor(listaTröjor, tröjor)
            elif userItem == "b":
                byxa = editor(listaByxor, byxor)
            elif userItem == "s":
                sko = editor(listaSkor, skor)
            elif userItem == "j":
                jacka = editor(listaJackor, jackor)
        print(f"Här är din reviderade outfit:\n {tröja}\n {byxa} \n {sko}\n {jacka}")
        userMood = input("Vill du göra fler ändringar? \n(j)a/(n)ej")
        if userMood == "j":
            continue
        if userMood == "n":
            return False
    
    print(f"Här är din outfit:\n {tröja}\n {byxa} \n {sko}\n {jacka}")

    

def menu():
    while True:
        menuChoice = input("Välj ett alternativ:\ng) Generera en outfit \na) Avsluta \n ")
        if menuChoice == "g":
            outfit_generator()

        if menuChoice == "a":
            exit()
            return False

def main():
    print("Välkommen till outfitgeneratorn!")
    menu()

main()

#WOOOO SLAY