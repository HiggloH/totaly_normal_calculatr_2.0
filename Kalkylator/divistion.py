decimal_tecken = "."


def list_to_str(lista):
    s = ""

    # Lägg till varje element från listan till en ny sträng
    for n in lista:
        s += n

    return s


def ingen_float(tal1, tal2):
    if int(tal1) < 10 and int(tal2) < 10:
        #Om båda talen är under 10 är det bara talen plus varandra
        tal1 = int(tal1)
        tal2 = int(tal2)

        return str(tal1 + tal2)
    elif int(tal1) < 10:
        tal1 = str(tal1)
        list_tal2 = list(tal2)

        #Om ett av talen är mer än 10 så sätter den in det andra talet i mitten
        #Om talet som är mer än 10 är ett udda antal siffror så tar den talet i mitten plus det andra talet
        if len(list_tal2) % 2 == 0:
            list_tal2.insert(int(len(list_tal2) / 2), tal1)
        else:
            mitten = int(len(list_tal2) / 2)
            list_tal2[mitten] = str(int(list_tal2[mitten]) + int(tal1))

        return list_to_str(list_tal2)
    elif int(tal2) < 10:
        #Samma som om tal1 är mindre än tio
        tal2 = str(tal2)
        list_tal1 = list(tal1)

        if len(list_tal1) % 2 == 0:
            list_tal1.insert(round(len(list_tal1) / 2), tal2)
        else:
            mitten = int(len(list_tal1) / 2)
            list_tal1[mitten] = str(int(list_tal1[mitten]) + int(tal2))

        return list_to_str(list_tal1)
    else:
        tal2 = str(tal2)
        list_tal1 = list(tal1)

        if len(list_tal1) % 2 == 0:
            mitten = int(len(list_tal1) / 2)
            list_tal1.insert(mitten, tal2)
        else:
            mitten = int(len(list_tal1) / 2)
            list_tal1[mitten] = str(int(list_tal1[mitten]) + int(tal2))

        return list_to_str(list_tal1)


#Den är om ett av talen är en float
def tal1_float(tal1, tal2):
    #Om ett av talen är ett flyttal så ersätter den decimal tecknet med det andra talet
    list_tal1 = list(tal1)
    decimal_index = list_tal1.index(decimal_tecken)

    list_tal1[decimal_index] = tal2

    return list_to_str(list_tal1)


#Den än om båda är floats
def tal1_och_tal2_float(tal1, tal2):
    #Om båda talet är flyttal så tar den båda delarna av decimaltecknet plus varandra
    list_tal1 = list(tal1)
    list_tal2 = list(tal2)

    hela_talet = [(list_tal1[0] + list_tal2[0]), decimal_tecken, (list_tal1[2] + list_tal2[2])]

    return list_to_str(hela_talet)


def main(tal1, tal2):
    float_tal1: bool
    float_tal2: bool
    nya_talet = ""

    #Kolla om första talet är ett flyttal
    if float.is_integer(float(tal1)):
        float_tal1 = False
    else:
        float_tal1 = True

    #Kolla om andra talet är ett flyttal
    if float.is_integer(float(tal2)):
        float_tal2 = False
    else:
        float_tal2 = True

    #Kör rätt funktion beroende på vilka som är flyttal
    if float_tal1 and float_tal2:
        nya_talet = tal1_och_tal2_float(tal1, tal2)
    elif float_tal1 and not float_tal2:
        nya_talet = tal1_float(tal1, tal2)
    elif not float_tal1 and float_tal2:
        nya_talet = tal1_float(tal2, tal1)
    elif not float_tal1 and not float_tal2:
        nya_talet = ingen_float(tal1, tal2)

    return nya_talet
