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

def two_options_quiz(question, condition1, condition2):
    print("------------------------------------")
    answer = int(input(f"{question}"))
    if answer == 1:
        return condition1
    elif answer == 2:
        return condition2

def initiate_clothes():
    shirtsDict = {
        "stickad tröja":{"waterproof":False, "season":"cold"},
        "långärmad":{"waterproof":False, "season":"cold"},
        "hoodie":{"waterproof":False, "season":"cold"},
        "bikinitopp":{"waterproof":True, "season":"hot"},
        "linne":{"waterproof":False, "season":"hot"},
        "croptop":{"waterproof":False, "season":"hot"},
        "soppåse":{"waterproof":True, "season":"hot"},
        "tjock soppåse":{"waterproof":True, "season":"cold"}
     }
    pantsDict = {
        "jeans":{"waterproof":False, "season":"cold"},
        "kostymbyxor": {"waterproof":False, "season":"hot"},
        "leggings":{"waterproof":False, "season":"hot"},
        "bikinitrosor":{"waterproof":True, "season":"hot"},
        "shorts":{"waterproof":False, "season":"hot"},
        "galonisar":{"waterproof":True, "season":"hot"},
        "täckbyxor":{"waterproof":True, "season":"cold"},
        "kort kjol":{"waterproof":False, "season":"hot"},
        "lång kjol":{"waterproof":False, "season":"cold"}
    }
    shoesDict = {
        "stövlar":{"waterproof":True, "season":"cold"},
        "pumps":{"waterproof":False, "season":"hot"},
        "sneakers":{"waterproof":False, "season":"hot"},
        "barfota":{"waterproof":False, "season":"hot"},
        "flipflops":{"waterproof":True, "season":"hot"},
        "crocs":{"waterproof":False, "season":"hot"},
        "uggs":{"waterproof":False, "season":"cold"},
        "vandringskängor":{"waterproof":True, "season":"cold"}
    }
    jacketsDict = {
        "kappa":{"waterproof":True, "season":"cold"},
        "läderjacka":{"waterproof":False, "season":"cold"},
        "regnjacka":{"waterproof":True, "season":"hot"},
        "kofta":{"waterproof":False, "season":"hot"},
        "väst":{"waterproof":False, "season":"cold"},
        "regnponcho":{"waterproof":True, "season":"hot"}
    }

    shirtsList = ["stickad tröja", "långärmad", "hoodie", "bikinitopp", "linne", "croptop", "soppåse", "tjock soppåse"]
    pantsList = ["jeans", "kostymbyxor", "leggings", "bikinitrosor", "shorts", "galonisar", "täckbyxor", "kort kjol", "lång kjol"]
    shoesList = ["stövlar","pumps","sneakers", "barfota", "flipflops", "crocs", "uggs", "vandringskängor"] 
    jacketsList = ["kappa", "läderjacka", "regnjacka", "kofta", "väst", "regnponcho"]
    
    return shirtsDict, pantsDict, shoesDict, jacketsDict, shirtsList, pantsList, shoesList, jacketsList

def add_item(clothingList, clothingDictionary):
    print("------------------------------------")
    clothingName = input("Vad vill du kalla ditt plagg?\n")
    clothingList.append(clothingName)
    #---------Quiz------
    waterproof = two_options_quiz("Är ditt plagg vattentätt?\n\n1)Ja \n2)Nej \n", True, False)
    season = two_options_quiz("Vilket väder är plagget anpassat för?\n\n1)Varmt väder \n2)Kallt väder \n", "hot", "cold")
    clothingDictionary.update({clothingName:{"waterproof":waterproof, "season": season}})
    print(f"\nPlagget '{clothingName}' har lagts till.")

def view_wardrobe(shirtsDict, pantsDict, shoesDict, jacketsDict, shirtsList, pantsList, shoesList, jacketsList):
    print("------------------------------------")
    menuChoice = int(input("Vilken kategori vill du visa?\n\n1)Tröjor \n2)Byxor \n3)Skor \n4)Jackor\n"))
    if menuChoice == 1:
        print("------------------------------------")
        lister(shirtsDict, "\nTryck enter för att gå tillbaka\n")
    elif menuChoice == 2:
        print("------------------------------------")
        lister(pantsDict, "\nTryck enter för att gå tillbaka\n")
    elif menuChoice == 3:
        print("------------------------------------")
        lister(shoesDict, "\nTryck enter för att gå tillbaka\n")
    elif menuChoice == 4:
        print("------------------------------------")
        lister(jacketsDict, "\nTryck enter för att gå tillbaka\n")

def wardrobe(savedOutfits, shirtsDict, pantsDict, shoesDict, jacketsDict, shirtsList, pantsList, shoesList, jacketsList):
    print("------------------------------------")
    print("\nVälkommen till din garderob!\n")
    while True:
        print("------------------------------------")
        menuChoice = int(input("Välj ett alternativ \n\n1)Visa plagg \n2)Lägg till plagg \n3)Huvudmeny\n" ))
        if menuChoice == 1:
            view_wardrobe(shirtsDict, pantsDict, shoesDict, jacketsDict, shirtsList, pantsList, shoesList, jacketsList)
        elif menuChoice == 2:
            print("------------------------------------")
            menuChoice = int(input("Kategori: \n\n1)Tröja \n2)Byxa \n3)Skor \n4)Jacka\n"))
            if menuChoice == 1:
                add_item(shirtsList, shirtsDict)
            elif menuChoice == 2:
                add_item(pantsList, pantsDict)
            elif menuChoice == 3:
                add_item(shoesList, shoesDict)
            elif menuChoice == 4:
                add_item(jacketsList, jacketsDict)
        elif menuChoice == 3:
            return False
        
#_________________ View Outfits ___________________

def save_outfit(savedOutfitsDict,listOfClothes):
    while True:
        print("------------------------------------")
        outfitName = input("Vad ska outfiten heta?\n")
        savedOutfitsList = list(savedOutfitsDict.keys())
        if savedOutfitsList.count(outfitName) != 0:
            print("------------------------------------")
            print("Det finns redan en outfit med detta namn.")
            menuChoice = int(input("1) Ersätt den\n2) Välj ett annat namn\n"))
            if menuChoice == 1:
                break
            if menuChoice == 2:
                continue
        else: break
    savedOutfitsDict.update({outfitName:listOfClothes})
    print(f"Outfiten '{outfitName}' är nu sparad i din garderob.")

def view_outfits(savedOutfits):
    outfitKeys = ["Tröja: ", "Byxor: ", "Skor: ", "Kappa: "]
    print("------------------------------------")
    print("Här är alla dina sparade outfits:")
    outfit = lister(savedOutfits,"Välj outfit: \n")
    print("------------------------------------")
    outfitList = savedOutfits.get(outfit)
    
    for n in range(0,4):
        print(outfitKeys[n]+outfitList[n])
    input("tryck enter för att gå tillbaka")

#________________ Outfit Generator _____________________
          
def cleanup(lista, dictionary, waterproofQuiz, seasonQuiz):
    tempList = lista.copy()
    for x in range(len(lista)-1, -1, -1):
        item = tempList[x]
        infoDict = dictionary.get(item)
        if infoDict.get("waterproof") != waterproofQuiz:
            tempList.remove(item)
        elif infoDict.get("season") != seasonQuiz:
            tempList.remove(item)
    return tempList

def quiz():
    waterproof = two_options_quiz("Regnar det? \n\n1)Ja \n2)Nej \n", True, False) 
    season = two_options_quiz("Är det varmt/kallt ute? \n\n1)Varmt \n2)Kallt \n", "hot", "cold")
    jacket = two_options_quiz("Vill du ha en jacka? \n\n1)Ja \n2)Nej \n", True, False)
    return waterproof, season, jacket

def randomizer(lista):
    if len(lista) > 1:
        index = random.randint(0, (len(lista)-1))
        choosen = lista[index]
    elif len(lista) == 1:
        choosen = lista[0]
    else: choosen = "Tom"
    return choosen

def editor(tempList, dictionary):
    if len(tempList) > 1:
        for n in range(0,len(tempList)):
            print(str(n+1)+ ")", tempList[n])
        userChoice = int(input("\nVilket alternativ?\n"))
        plagg = tempList[userChoice-1]    
    else:
        print("Det finns inga andra alternativ som passar dina krav.\n\nVälj ett av följande plagg:\n")
        plagg = lister(dictionary,"\nVilket alternativ?\n")
    return plagg
    
def outfit_generator(savedOutfits, shirtsDict, pantsDict, shoesDict, jacketsDict, shirtsList, pantsList, shoesList, jacketsList):
    
    waterproofQuiz, seasonQuiz, jacketQuiz = quiz()
    clothingList = [shirtsList, pantsList, shoesList, jacketsList]
    dictionaryList = [shirtsDict, pantsDict, shoesDict, jacketsDict]
    
    outfit = []
    tempListList = []
    
    for n in range(0,4):
        tempList = cleanup(clothingList[n], dictionaryList[n], waterproofQuiz, seasonQuiz)
        tempListList.append(tempList)
        plagg = randomizer(tempList)
        outfit.append(plagg)

    if jacketQuiz == False:
        outfit[3] = "Ingen jacka"
    
    # if jacketQuiz == True:
    #     tempJacket = cleanup(jacketsList, jacketsDict, waterproofQuiz, seasonQuiz)
    #     tempListList.append(tempJacket)
    #     jacket = randomizer(tempJacket)
    # else: jacket = "Ingen jacka"
    # outfit.append(jacket)


    print("------------------------------------")
    print(f"Här är din outfit:\n Topp:{outfit[0]}\n\n Byxor:{outfit[1]}\n\n Skor:{outfit[2]}\n\n Jacka:{outfit[3]}")
    print("------------------------------------")
    
    #______Edit created outfit:
    
    userEdit = int(input("Vill du göra ändringar till outfiten? \n\n1)Ja \n2)Nej\n"))
    if userEdit == 1:
        while True:
            print("------------------------------------")
            userItem = int(input("Vilket plagg vill du ändra?\n\n1)tröja \n2)byxor \n3)skor \n4)jacka\n"))
            userItem -= 1 #index
            print("------------------------------------")
            outfit[userItem] = editor(tempListList[userItem], dictionaryList[userItem]) #editor(sorteradLista, dictionary)
            
            print("------------------------------------")
            print(f"Här är din outfit:\n\n Topp:{outfit[0]}\n\n Byxor:{outfit[1]}\n\n Skor:{outfit[2]}\n\n Jacka:{outfit[3]}")
            print("------------------------------------")
            userMood = int(input("Vill du göra fler ändringar? \n\n1)Ja \n2)Nej \n"))
            if userMood == 1:
                continue
            if userMood == 2:
                break
    print("------------------------------------")
    userSave = int(input("Vill du spara outfiten? \n\n1)Ja \n2)Nej \n"))
    if userSave == 1:
        save_outfit(savedOutfits, outfit)

def menu():
    savedOutfits = {"slayer":["linne", "jeans", "crocs", "väst"]}
    shirtsDict, pantsDict, shoesDict, jacketsDict, shirtsList, pantsList, shoesList, jacketsList = initiate_clothes()
    while True:
        print("------------------------------------")
        menuChoice = int(input("Huvudmeny:\n\n1)Generera en outfit  \n2)Visa sparade outfits \n3)Öppna garderob \n4)Avsluta\n"))
        if menuChoice == 1:
            outfit_generator(savedOutfits, shirtsDict, pantsDict, shoesDict, jacketsDict, shirtsList, pantsList, shoesList, jacketsList)
        elif menuChoice == 2:
            view_outfits(savedOutfits)
        elif menuChoice == 3:
            wardrobe(savedOutfits, shirtsDict, pantsDict, shoesDict, jacketsDict, shirtsList, pantsList, shoesList, jacketsList)
        elif menuChoice == 4:
            return False

def main():
    print("------------------------------------")
    print("\n  Välkommen till outfitgeneratorn!\n")
    menu()

main()

#WOOOO SLAY