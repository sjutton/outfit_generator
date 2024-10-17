def outfitGenerator():
    print("yes")

def menu():
    menuChoice = input("Vill du generera en outfit?\n1. ")
    if menuChoice == "Ja":
        outfitGenerator() 
    if menuChoice == "Nej":
        print("boo")


def main():
    print("Welcome to this outfit generator!")
    while True:
        menu()

main()

#WOOOO SLAY