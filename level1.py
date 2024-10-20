import random

def cleanup(tröjor, byxor, skor, vattentätQuiz, säsongQuiz, listaTröjor, listaByxor, listaSkor):
    
    for item in listaTröjor:
        placeholder = tröjor.get(item)
        if placeholder.get("vattentät") != vattentätQuiz:
            listaTröjor.remove(item)
        elif säsongQuiz == "all":
            continue
        elif placeholder.get("säsong") != säsongQuiz:
            listaTröjor.remove(item)

    for item in listaByxor:
        placeholder = byxor.get(item)
        if placeholder.get("vattentät") != vattentätQuiz:
            listaByxor.remove(item)
        elif säsongQuiz == "all":
            continue
        elif placeholder.get("säsong") != säsongQuiz:
            listaByxor.remove(item)

    for item in listaSkor:
        placeholder = skor.get(item)
        if placeholder.get("vattentät") != vattentätQuiz:
            listaSkor.remove(item)
        elif säsongQuiz == "all":
            continue
        elif placeholder.get("säsong") != säsongQuiz:
            listaSkor.remove(item)
    print(listaTröjor, listaByxor, listaSkor)



def quiz():
    svar = input("Ska outfiten vara vattentät? ja/nej")
    if svar == "ja":
        vattentät = True
    elif svar == "nej":
        vattentät = False
    
    svar = input("Vilken säsong ska outfiten vara anpassad för? (s)ommar/(h)öst/(v)år")
    if svar == "s":
        säsong = "sommar"
    elif svar == "h":
        säsong = "höst"
    elif svar == "v":
        säsong = "vår"
    elif svar == "a":
        säsong = "all"
    
    return vattentät, säsong

def outfitGenerator():
    tröjor = {
        "tshirt":{"vattentät":False, "säsong":"sommar"},
        "hoodie":{"vattentät":True, "säsong":"höst"}
     }
    byxor = {
        "byxor":{"vattentät":False, "säsong":"höst"},
        "finbyxor": {"vattentät":False, "säsong":"sommar"},
        "shorts":{"vattentät":False, "säsong":"sommar"},
        "galonisar":{"vattentät":True, "säsong":"sommar"}
    }
    skor = {
        "stövlar":{"vattentät":True, "säsong":"höst"},
        "pumps":{"vattentät":False, "säsong":"sommar"},
        "sneakers":{"vattentät":False, "säsong":"vår"},
        "barfota":{"vattentät":False, "säsong":"vår"}
    }

    listaTröjor = ["tshirt", "hoodie"]
    listaByxor = ["byxor","finbyxor","shorts","galonisar"]
    listaSkor = ["stövlar","pumps","sneakers"]    

    vattentätQuiz, säsongQuiz = quiz()

    cleanup(tröjor, byxor, skor, vattentätQuiz, säsongQuiz, listaTröjor, listaByxor, listaSkor)

    if len(tröjor) != 1:
        index = random.randint(0, (len(listaTröjor)-1))
        choosen_tröja = listaTröjor[index]
    else:
        choosen_tröja = listaTröjor[0]

    if len(byxor) != 1:
        index = random.randint(0, len(listaByxor)-1)
        choosen_byxa = listaByxor[index]
    else:
        choosen_byxa = listaByxor[0]

    if len(skor) != 1:
        index = random.randint(0, len(listaSkor)-1)
        choosen_sko = listaSkor[index]
    else:
        choosen_sko = listaSkor[0]
    
    return choosen_tröja, choosen_byxa, choosen_sko

def menu():
    while True:
        menuChoice = input("Välj ett alternativ:\ng) Generera en outfit \na) Avsluta \n ")
        if menuChoice == "g":
            tröja, byxa, sko = outfitGenerator()
            print(f"Här är din outfit:\n {tröja}\n {byxa} \n {sko}")
        if menuChoice == "a":
            exit()
            return False

def main():
    print("Welcome to this outfit generator!")
    menu()

main()

#WOOOO SLAY