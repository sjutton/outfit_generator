import random

def lister(dictionary, question):
    lista = list(dictionary.keys())
    for n in range(0, len(lista)):
        print(str(n+1)+")", lista[n])
    try:
        userChoice = int(input(question))
    except:
        choosenItem = ""
    else:
        choosenItem = lista[userChoice-1]
    return choosenItem

def view_wardrobe(tröjor, byxor, skor, jackor, listaTröjor, listaByxor, listaSkor, listaJackor):
    menuChoice = int(input("Vilken kategori av plagg vill du visa?\n1) Tröjor \n2)Byxor \n3)Skor \n4)Jackor\n"))
    if menuChoice == 1:
        lister(tröjor, "Tryck enter för att gå tillbaka")
    elif menuChoice == 2:
        lister(byxor, "Tryck enter för att gå tillbaka")
    elif menuChoice == 3:
        lister(skor, "Tryck enter för att gå tillbaka")
    elif menuChoice == 4:
        lister(jackor, "Tryck enter för att gå tillbaka")

def wardrobe(tröjor, byxor, skor, jackor, listaTröjor, listaByxor, listaSkor, listaJackor):
    print("Välkommen till din garderob!\n")
    while True:
        menuChoice = int(input("Välj ett alternativ \n1) Visa plagg \n2)Lägg till plagg \n3)Huvudmeny\n" ))
        if menuChoice == 1:
            view_wardrobe(tröjor, byxor, skor, jackor, listaTröjor, listaByxor, listaSkor, listaJackor)
        elif menuChoice == 2:
            pass
        elif menuChoice == 3:
            return False
        
#_________________ View Outfits ___________________

def save_outfit(savedOutfitsDict,listOfClothes):
    while True:
        outfitNamn = input("Vad ska outfiten heta?\n")
        savedOutfitsList = savedOutfitsDict.keys()
        if savedOutfitsList.count(outfitNamn) != 0:
            print("Det finns redan en outfit med detta namn.")
            menuChoice = int(input("1) Ersätt den\n2) Välj ett annat namn\n"))
            if menuChoice == 1:
                break
            if menuChoice == 2:
                continue
    savedOutfitsDict.update({outfitNamn:listOfClothes})
    print(savedOutfitsDict)

def view_outfits(savedOutfits):
    outfitKeys = ["Tröja: ", "Byxor: ", "Skor: ", "Kappa: "]
    print("Här är alla dina outfits:")
    outfit = lister(savedOutfits,"Välj outfit: \n")
    outfitList = savedOutfits.get(outfit)
    
    for n in range(0,4):
        print(outfitKeys[n]+outfitList[n])

#________________ Outfit Generator _____________________
          
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
    print("------------------------------------")
    svar = int(input("Regnar det? \n\n1)Vattentät \n2)Ej vattentät \n"))
    if svar == 1:
        vattentät = True
    elif svar == 2:
        vattentät = False
    
    print("------------------------------------")
    svar = int(input("Vilken temperatur ska outfiten vara anpassad för? \n\n1)Varmt väder \n2)Kallt väder \n"))
    if svar == 1:
        värme = "hot"
    elif svar == 2:
        värme = "cold"
    
    print("------------------------------------")
    svar = int(input("Vill du ha en jacka? \n\n1)Ja \n2)Nej \n"))
    if svar == 1:
        jacka = True
    elif svar == 2:
        jacka = False

    return vattentät, värme, jacka

def randomizer(lista):
    if len(lista) > 1:
        index = random.randint(0, (len(lista)-1))
        choosen = lista[index]
    elif len(lista) == 1:
        choosen = lista[0]
    else: choosen = "Tom"
    return choosen

def editor(lista, dictionary):
    if len(lista) > 1:
        for n in range(0,len(lista)):
            print(str(n+1)+ ")", lista[n])
        userChoice = int(input("Vilket alternativ?\n"))
        plagg = lista[userChoice-1]    
    else:
        answer = int(input("Det finns inga andra alternativ som passar dina krav. \n\nVill du välja mellan alla tillgängliga plagg? \n1)Ja \n2)Nej\n"))
        if answer == 1:
           plagg = lister(dictionary,"Vilket alternativ?\n")
        elif answer == 2:
            pass
    return plagg

def outfit_generator(savedOutfits, tröjor, byxor, skor, jackor, listaTröjor, listaByxor, listaSkor, listaJackor):
    
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
    print("--------------")
    print(f"Här är din outfit:\n Topp:{tröja}\n\n Byxor:{byxa}\n\n Skor:{sko}\n\n Jacka:{jacka}")
    print("--------------")
    
    userEdit = int(input("Vill du göra ändringar till outfiten? \n\n1)Ja \n2)Nej\n"))
    print("--------------")
    if userEdit == 1:
        while True:
            userItem = int(input("Vilket plagg vill du ändra?\n1)tröja \n2)byxor \n3)skor \n4)jacka\n"))
            if userItem == 1:
                tröja = editor(listaTröjor, tröjor)
            elif userItem == 2:
                byxa = editor(listaByxor, byxor)
            elif userItem == 3:
                sko = editor(listaSkor, skor)
            elif userItem == 4:
                jacka = editor(listaJackor, jackor)
            print("--------------")
            print(f"Här är din outfit:\n Topp:{tröja}\n\n Byxor:{byxa}\n\n Skor:{sko}\n\n Jacka:{jacka}")
            print("--------------")
            userMood = int(input("Vill du göra fler ändringar? \n\n1)Ja \n2)Nej \n"))
            if userMood == 1:
                continue
            if userMood == 2:
                return False
    
    userSave = input(("Vill du spara outfiten? \n\n1)Ja \n2)Nej "))
    if userSave == 1:
        save_outfit(savedOutfits,[tröja, byxa, sko, jacka])

def menu():
    savedOutfits = {"slayer":["linne", "jeans", "crocs", "väst"]}
    tröjor = {
        "stickad tröja":{"vattentät":False, "värme":"hot"},
        "långärmad":{"vattentät":False, "värme":"hot"},
        "hoodie":{"vattentät":False, "värme":"cold"},
        "bikinitopp":{"vattentät":True, "värme":"hot"},
        "linne":{"vattentät":False, "värme":"hot"},
        "croptop":{"vattentät":False, "värme":"hot"},
        "soppåse":{"vattentät":True, "värme":"hot"},
        "tjock soppåse":{"vattentät":True, "värme":"cold"}
     }
    byxor = {
        "jeans":{"vattentät":False, "värme":"cold"},
        "kostymbyxor": {"vattentät":False, "värme":"hot"},
        "leggings":{"vattentät":False, "värme":"hot"},
        "bikinitrosor":{"vattentät":True, "värme":"hot"},
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
        "flipflops":{"vattentät":True, "värme":"hot"},
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

    listaTröjor = ["stickad tröja", "långärmad", "hoodie", "bikinitopp", "linne", "croptop", "soppåse", "tjock soppåse"]
    listaByxor = ["jeans", "kostymbyxor", "leggings", "bikinitrosor", "shorts", "galonisar", "täckbyxor", "kort kjol", "lång kjol"]
    listaSkor = ["stövlar","pumps","sneakers", "barfota", "flipflops", "crocs", "uggs", "vandringskängor"] 
    listaJackor = ["kappa", "läderjacka", "regnjacka", "kofta", "väst", "regnponcho"]
    
    while True:
        menuChoice = int(input("Välj ett alternativ:\n\n1) Generera en outfit  \n2) Visa sparade outfits \n3) Visa garderob \n4) Avsluta\n"))
        if menuChoice == 1:
            outfit_generator(savedOutfits, tröjor, byxor, skor, jackor, listaTröjor, listaByxor, listaSkor, listaJackor)
        elif menuChoice == 2:
            view_outfits(savedOutfits)
        elif menuChoice == 3:
            wardrobe(tröjor, byxor, skor, jackor, listaTröjor, listaByxor, listaSkor, listaJackor)
        elif menuChoice == 4:
            return False

def main():
    print("------------------------------------")
    print("\n  Välkommen till outfitgeneratorn!\n")
    print("------------------------------------")
    menu()

main()

#WOOOO SLAY