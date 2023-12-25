import divistion

#Variabler för hela filen
only_remove: bool

alla_tecken: list = ["+", "-", "*", "/", "^", "'", "%"]
to_remove: list = []
decimal_tecken = "."
komma = ","


def list_to_str(lista: list):
    s = ""

    # Lägg till varje element från listan till en ny sträng
    for n in lista:
        s += n

    return s


def list_to_int(lista: list) -> int:
    i = 0

    for n in lista:
        i += n

    return i


def get_list(tal):
    #Delar upp en lista i två delar, en för varje sida av decimal tecknet
    tal_list = list(tal)
    # Temp används för att skära listen i decimaltecknet
    temp = tal_list.index(decimal_tecken)
    # Vänster sida av decimaltecknet
    res = tal_list[:temp]
    # Högra sidan av decimaltecknet
    res2 = tal_list[temp + 1:]
    forsta_delen = ""
    andra_delen = ""

    for n in res:
        forsta_delen += n
    for n in res2:
        andra_delen += n

    hela_talet = [forsta_delen, andra_delen]
    return hela_talet


def get_decimal(tal):
    #Det här är en funktion som gör om decimaltal till heltal
    deci_tal = 1 / float(tal)

    if float.is_integer(deci_tal):
        deci_tal = int(deci_tal)

    return str(deci_tal)


def replace_komma(uttryck):
    #Byt ut alla kommatecken mot decimal tecken
    for n in range(len(uttryck)):
        if komma in uttryck[n]:
            uttryck[n] = decimal_tecken

    return uttryck


def remove_characters(_uttryck: str):
    #Den här tar bort överblivna bokstäver i inputen
    temp = []
    uttryck = list(_uttryck)
    uttryck = replace_komma(uttryck)

    #Kollar igenom hela lista och kollar om det är en bokstav eller inte
    for n in range(len(uttryck)):
        if alla_tecken[0] in uttryck[n]:
            pass
        elif alla_tecken[1] in uttryck[n]:
            pass
        elif alla_tecken[2] in uttryck[n]:
            pass
        elif alla_tecken[3] in uttryck[n]:
            pass
        elif alla_tecken[4] in uttryck[n]:
            pass
        elif alla_tecken[5] in uttryck[n]:
            pass
        elif alla_tecken[6] in uttryck[n]:
            pass
        elif decimal_tecken in uttryck[n]:
            pass
        else:
            #Här kollar den om elementet är en siffra eller inte
            try:
                float(uttryck[n])
            except ValueError:
                temp.append(n)

    #Så att den börjar från höger för att ta bort bokstäverna
    temp.reverse()
    for i in temp:
        del uttryck[i]

    index = len(uttryck) - 1

    while index >= 0:
        if decimal_tecken in uttryck[index]:
            #Om det finns flera decimal tecken på rad så ta bort ett av dom
            if decimal_tecken in uttryck[index + 1] or decimal_tecken in uttryck[index - 1]:
                del uttryck[index]

            #Om det finns ett tecken på någon sida av decimal tecknet så ta bort det
            if alla_tecken[0] in uttryck[index + 1] or alla_tecken[0] in uttryck[index - 1]:
                del uttryck[index]
            elif alla_tecken[1] in uttryck[index + 1] or alla_tecken[1] in uttryck[index - 1]:
                del uttryck[index]
            elif alla_tecken[2] in uttryck[index + 1] or alla_tecken[2] in uttryck[index - 1]:
                del uttryck[index]
            elif alla_tecken[3] in uttryck[index + 1] or alla_tecken[3] in uttryck[index - 1]:
                del uttryck[index]
            elif alla_tecken[4] in uttryck[index + 1] or alla_tecken[4] in uttryck[index - 1]:
                del uttryck[index]
            elif alla_tecken[5] in uttryck[index + 1] or alla_tecken[5] in uttryck[index - 1]:
                del uttryck[index]
            elif alla_tecken[6] in uttryck[index + 1] or alla_tecken[6] in uttryck[index - 1]:
                del uttryck[index]

        index -= 1

    return list_to_str(uttryck)


def check_minus(lista: list, index):
    #Här kollar den om talet i listan är ett negativt tal eller inte
    minus = False
    index -= 1

    #Om det är ett tecken brevid minuset är det ett negativt tal
    if alla_tecken[0] in lista[index]:
        minus = True
    elif alla_tecken[1] in lista[index]:
        minus = True
    elif alla_tecken[2] in lista[index]:
        minus = True
    elif alla_tecken[3] in lista[index]:
        minus = True
    elif alla_tecken[4] in lista[index]:
        minus = True
    elif alla_tecken[5] in lista[index]:
        minus = True
    elif alla_tecken[6] in lista[index]:
        pass

    return minus


def get_minus(lista) -> list:
    #Här kollar den om slut talet ska vara negativ eller inte och ta bort alla minus tecken som är för ett negativt tal
    minus: bool = False
    minus_list = []
    nya_tal = []

    for n in lista:
        if alla_tecken[1] in list(n):
            minus_list.append(True)
            n = list(n)
            del n[0]
            n = list_to_str(n)
            nya_tal.append(n)
        else:
            nya_tal.append(n)

    #Om det är ett jämt antal negativa tal så är slut talet inte ett negativt tal
    if len(minus_list) % 2:
        minus = True

    return [nya_tal, minus]


def get_tal(lista, index) -> str:
    #Ta ut tal från en lista
    if not index == 0:
        index += 1

    #Spita listan innan indexen
    tal = lista[index:]

    return list_to_str(tal)


def split_list(lista, index) -> list:
    lista = lista[:index]
    return lista


def hitta_procent(lista) -> list:
    #Här kollar den efter procent tecken och sedan tar bort dom från listan
    temp = []
    _procent = []

    for n in range(len(lista)):
        if alla_tecken[6] in lista[n]:
            temp.append(n)

    for n in temp:
        #Det är plus två för att den inkluderar inte talet efter annars
        res = lista[n:n+2]
        #För att få procent tecknet sist i listan
        res.reverse()
        _procent.append(res)
        del lista[n+1]
        del lista[n]

    return [_procent, lista]


def generera_uttryck(lista):
    #Här tar den fram alla uttryck från inputen
    global only_remove
    only_remove = False

    temp = []
    alla_uttryck = []

    _procent = hitta_procent(lista)

    lista = _procent[1]
    index = len(lista) - 1

    #Kolla efter'tecken och ta bort dom
    while index >= 0:
        if alla_tecken[5] in lista[index]:
            lista = add_remove(lista, index)
            index -= 1

        index -= 1

    #Går igenom hela lista och tar ut uttrycken
    index = len(lista) - 1
    while index >= 0:
        if alla_tecken[0] in lista[index]:
            temp.append(index)
            index -= 1
        elif alla_tecken[1] in lista[index]:
            temp.append(index)
            index -= 1
        elif alla_tecken[2] in lista[index]:
            temp.append(index)
            index -= 1
        elif alla_tecken[3] in lista[index]:
            temp.append(index)
            index -= 1
        elif alla_tecken[4] in lista[index]:
            temp.append(index)
            index -= 1

        index -= 1

    #Klipp ut delar av listan från temp
    if not temp == []:
        for n in temp:
            res = lista[n - 1:]
            alla_uttryck.append(res)
            lista = lista[:n - 1]
    elif not to_remove == []:
        alla_uttryck.append(lista)
        only_remove = True
    else:
        alla_uttryck.append(lista)

    #Lägg till procenten i slutet av uttrycks listan
    for n in _procent[0]:
        alla_uttryck.append(n)

    return alla_uttryck


def add_remove(lista, index):
    tal = lista[index + 1]

    #Om talet är en float så ska den göra om den till en int för att göra det lättare
    #I framtiden kanske det ska ändras
    if not float.is_integer(float(tal)):
        tal = round(float(tal))

    if not to_remove == []:
        to_remove[0] = to_remove[0] + tal
    else:
        to_remove.append(tal)

    #Ta bort'tecken och elementet efter
    del lista[index]
    del lista[index]

    return lista


def get_uttryck(uttryck: str):
    #Sätt ihop talen så de inte siffrorna är olika strings
    lista = list(uttryck)
    temp = []
    tecken = []
    alla_tal = []
    # Det är minus ett för att inkludera 0 som sista tal
    length = len(uttryck) - 1

    #Lägg till alla tecken och vart dom är i listan
    for i in range(length):
        if alla_tecken[0] in lista[i]:
            temp.append(i)
            tecken.append(alla_tecken[0])
        elif alla_tecken[1] in lista[i]:
            if i == 0:
                pass
            elif check_minus(lista, i):
                pass
            else:
                temp.append(i)
                tecken.append(alla_tecken[1])
        elif alla_tecken[2] in lista[i]:
            temp.append(i)
            tecken.append(alla_tecken[2])
        elif alla_tecken[3] in lista[i]:
            temp.append(i)
            tecken.append(alla_tecken[3])
        elif alla_tecken[4] in lista[i]:
            temp.append(i)
            tecken.append(alla_tecken[4])
        elif alla_tecken[5] in lista[i]:
            temp.append(i)
            tecken.append(alla_tecken[5])
        elif alla_tecken[6] in lista[i]:
            temp.append(i)
            tecken.append(alla_tecken[6])

    #Lägg till 0 i temp listan om den inte redan finns
    #För att inkludera 0 i uppdelningen av listan sen
    if 0 not in temp:
        temp.append(0)
    #Sortera temp så den är högsta talet till lägsta
    temp.sort(reverse=True)

    #Ta ut talen och sen lägg ihop dom med tecknen
    for n in temp:
        alla_tal.append(get_tal(lista, n))
        lista = split_list(lista, n)

    alla_tal.reverse()

    #Kolla efter minus i tal om det finns ta bort dom
    minus_lista = get_minus(alla_tal)
    alla_tal = minus_lista[0]  # Det är de nya talen efter att den har tagit bort minus tecknen
    minus = minus_lista[1]  # Om det är True så är slut talet ett negativt tal annars är det inte det

    n = 0
    t = 0
    while n < len(alla_tal) - 1:
        n += 1
        alla_tal.insert(n, tecken[t])
        t += 1
        n += 1

    alla_uttryck = generera_uttryck(alla_tal)

    return [alla_uttryck, minus]


def plus_och_minus(tal1, tal2):
    if not float.is_integer(float(tal1)) and not float.is_integer(float(tal2)):
        #Körs om båda talen är flyttal
        hela_talet_1 = get_list(tal1)
        hela_talet_2 = get_list(tal2)

        #Den lägger ihop båda sidorna av decimal tecknet för sig och sen lägger ett decimaltecken i mitten
        hela_talet = [(hela_talet_1[0] + hela_talet_2[0]), decimal_tecken, (hela_talet_1[1] + hela_talet_2[1])]

        nya_tal = list_to_str(hela_talet)
    elif not float.is_integer(float(tal1)) and float.is_integer(float(tal2)):
        #Körs om tal1 är ett flyttal
        hela_talet = get_list(tal1)

        #Här gör den samma sak som den ovanför fast bara på ena sidan av decimal tecknet
        hela_talet = [(hela_talet[0] + tal2), decimal_tecken, hela_talet[1]]

        nya_tal = list_to_str(hela_talet)
    elif float.is_integer(float(tal1)) and not float.is_integer(float(tal2)):
        #Körs om tal2 är ett flyttal
        hela_talet = get_list(tal2)

        hela_talet = [(hela_talet[0] + tal1), decimal_tecken, hela_talet[1]]

        nya_tal = list_to_str(hela_talet)
    else:
        #Här är ingen av talen ett flyttal så då bara lägger den ihop talen
        nya_tal = tal1 + tal2

    return nya_tal


def multiplication(tal1, tal2) -> str:
    if not float.is_integer(float(tal1)) and not float.is_integer(float(tal2)):
        hela_talet = get_list(tal1)
        tal2 = get_decimal(tal2)

        #Här så gör den som när bara tal2 är ett flyttal fast på båda sidorna av decimaltecknet
        hela_talet = [(divistion.main(hela_talet[0], tal2)), decimal_tecken, (divistion.main(hela_talet[1], tal2))]

        nya_tal = list_to_str(hela_talet)
    elif not float.is_integer(float(tal1)) and float.is_integer(float(tal2)):
        hela_talet = get_list(tal1)
        tal2 = int(tal2)
        #Här kör den gånger på båda sidorna av decimaltecknet
        hela_talet = [(hela_talet[0] * tal2), decimal_tecken, (hela_talet[1] * tal2)]

        nya_tal = list_to_str(hela_talet)
    elif float.is_integer(float(tal1)) and not float.is_integer(float(tal2)):
        tal2 = get_decimal(tal2)
        #När tal2 är ett flyttal så gör den om det till ett heltal med get_decimal funktionen så delar den det med tal1
        nya_tal = divistion.main(tal1, tal2)
    else:
        #Här är vanligt gånger fast med strings
        nya_tal = tal1 * int(tal2)

    return nya_tal


def power(tal1, tal2):
    #Upphöjt fungerar typ som vanligt fast tal1 är en sträng
    n = 1
    nya_tal = tal1

    if int(tal2) >= 12:
        return "Talet är för stort"

    if not float.is_integer(float(tal1)) and not float.is_integer(float(tal2)):
        hela_talet = get_list(tal1)
        hela_talet_bas = hela_talet
        del_1 = int(hela_talet[0])
        del_2 = int(hela_talet[1])
        tal2 = int(get_decimal(tal2))

        while n < tal2:
            del_1 = del_1 * hela_talet_bas[0]
            del_2 = del_2 * hela_talet_bas[1]

            n += 1

        hela_talet = [del_1, decimal_tecken, del_2]
        nya_tal = list_to_str(hela_talet)
    elif not float.is_integer(float(tal1)) and float.is_integer(float(tal2)):
        hela_talet = get_list(tal1)
        hela_talet_bas = hela_talet
        del_1 = int(hela_talet[0])
        del_2 = int(hela_talet[1])
        tal2 = int(tal2)

        while n < tal2:
            del_1 = del_1 * hela_talet_bas[0]
            del_2 = del_2 * hela_talet_bas[1]

            n += 1

        hela_talet = [del_1, decimal_tecken, del_2]
        nya_tal = list_to_str(hela_talet)
    elif float.is_integer(float(tal1)) and not float.is_integer(float(tal2)):
        tal2 = round(float(get_decimal(tal2)))
        tal1_bas = int(tal1)

        while n < tal2:
            nya_tal = tal1 * tal1_bas
            n += 1
    else:
        tal2 = int(tal2)
        tal1_bas = int(tal1)

        while n < tal2:
            nya_tal = nya_tal * tal1_bas
            n += 1

    return nya_tal


def procent(tal1, tal2):
    tal2 = float(tal2) / 100

    nya_tal = multiplication(tal1, tal2)

    return str(nya_tal)


def matcha_tecken(tal1, tal2, tecken):
    nya_tal = ""

    #Matcha upp tecknet och talet med rätt uttrycks funktion
    if tecken == alla_tecken[0]:
        nya_tal = plus_och_minus(tal1, tal2)
    elif tecken == alla_tecken[1]:
        nya_tal = plus_och_minus(tal2, tal1)
    elif tecken == alla_tecken[2]:
        nya_tal = multiplication(tal1, tal2)
    elif tecken == alla_tecken[3]:
        nya_tal = divistion.main(tal1, tal2)
    elif tecken == alla_tecken[4]:
        nya_tal = power(tal1, tal2)
    elif tecken == alla_tecken[6]:
        nya_tal = procent(tal1, tal2)

    return nya_tal


def remove(tal1, tal2):
    #Remove är till tecknet'och den tar bort så många tal som tal2 är från tal1
    tal1 = list_to_str(tal1)

    talet = split_list(tal1, len(tal1) - int(tal2))

    return list_to_str(talet)


def remove_zeros(tal):
    #Ta bort onödiga nollor i början av slut talet
    tal_list = list(tal)

    while tal_list[0] == "0":
        del tal_list[0]

    if tal_list[0] == decimal_tecken:
        tal_list.insert(0, "0")

    tal = list_to_str(tal_list)

    return tal


def main(uttryck: str):
    #Generera uttrycken från inputen
    rent_uttryck = remove_characters(uttryck)
    hela_alla_uttryck = get_uttryck(rent_uttryck)
    alla_uttryck = hela_alla_uttryck[0]
    minus = hela_alla_uttryck[1]

    alla_tal = []

    if not alla_uttryck == [['']]:
        if only_remove:
            #Körs om det ända tecknet är remove
            tal1 = alla_uttryck[0]
            tal2 = to_remove[0]

            alla_tal.append(remove(tal1, tal2))
            #Annars körs remove funktionen två gånger
            clear_remove()
        else:
            for n in alla_uttryck:
                if len(n) == 3:
                    #Första uttrycket är alltid tre element och de andra är två
                    tal1 = n[0]
                    tecken = n[1]
                    tal2 = n[2]

                    alla_tal.append(matcha_tecken(tal1, tal2, tecken))

                    if alla_tal[0] == "Talet är för stort":
                        return "Talet är för stort"
                else:
                    # Ifall alla_tal är tom betyder det att det bara är procent
                    if not alla_tal == []:
                        tal1 = n[0]
                        tecken = n[1]
                        tal2 = alla_tal[len(alla_tal) - 1]

                        if tecken == alla_tecken[6]:
                            tal1 = alla_tal[len(alla_tal) - 1]
                            tal2 = n[0]

                        alla_tal.append(matcha_tecken(tal1, tal2, tecken))

                        if alla_tal[len(alla_tal) - 1] == "Talet är för stort":
                            return "Talet är för stort"
                    else:
                        #Ifall n är mindre eller en index lång så är det bara ett tal
                        if len(n) <= 1:
                            resten_av_talet = alla_uttryck[1]

                            tal1 = resten_av_talet[0]
                            tal2 = n[0]
                            tecken = resten_av_talet[1]

                            alla_tal.append(matcha_tecken(tal1, tal2, tecken))

                            if alla_tal[len(alla_tal) - 1] == "Talet är för stort":
                                return "Talet är för stort"

                            return alla_tal[len(alla_tal) - 1]
                        else:
                            return "Tal saknas"

        #Lägg till ett minus i början av talet om det ska vara ett negativt tal
        if minus:
            slut_tal = alla_tecken[1] + str(alla_tal[len(alla_tal) - 1])
        else:
            slut_tal = str(alla_tal[len(alla_tal) - 1])

        #Remove händer sist om det finns andra uttryck
        if not to_remove == []:
            slut_tal = remove(alla_tal[len(alla_tal) - 1], to_remove[0])

        if slut_tal == "":
            return "Talet försvann"
        else:
            slut_tal = remove_zeros(slut_tal)

            return slut_tal
    else:
        return "Fattas tal"


def clear_remove():
    #Återställ remove listan
    to_remove.clear()
