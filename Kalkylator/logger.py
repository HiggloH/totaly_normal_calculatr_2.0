import os


#Ta inputen och svaret och lägg till det till log.txt
#Den kan också skapa en ny fil som heter log.txt om den inte redan finns
def log(uttryck, svar):
    data = str(uttryck + "=" + svar)
    with open("log.txt", "a+") as file:
        file.write(data)
        file.write('\n')


#Skriv ut hela logen
def print_file():
    file = open("log.txt", "r")
    lines = file.read().splitlines()

    for line in lines:
        print(line)

    file.close()


#Reseta hela logen genom att ta bort filen
def reset():
    if os.path.exists("log.txt"):
        os.remove("log.txt")