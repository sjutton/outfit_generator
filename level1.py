import random

def outfitGenerator():
    tröjor = ["tshirt", "hoodie"]
    byxor = ["byxor","finbyxor","shorts"]
    skor = ["stövlar","pumps","sneakers"]

    if len(tröjor) != 1:
        index = random.randint(0, len(tröjor)-1)
        choosen_tröja = tröjor[index]
    else:
        choosen_tröja = tröjor[0]

    if len(byxor) != 1:
        index = random.randint(0, len(byxor)-1)
        choosen_byxa = byxor[index]
    else:
        choosen_byxa = byxor[0]

    if len(skor) != 1:
        index = random.randint(0, len(skor)-1)
        choosen_sko = skor[index]
    else:
        choosen_sko = skor[0]
    
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