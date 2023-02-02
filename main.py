#megoldas


def eredmeny(jLap: list[int], gLap: list[int]):
    if osszegzes(jLap) > 21:
        return "Játékos vesztett"
    elif osszegzes(gLap) > 21:
        return "Gép vesztett"


def osszegzes(list: list[int]):
    i = 0
    ossz = 0
    while i < len(list):
        ossz += list[i]
        i += 1
    return ossz


#teszt esetek


def jatekos_vesztett_teszt():
    jLap = [10, 5, 7]
    gLap = [2, 7, 9]
    kap = eredmeny(jLap, gLap)
    vart = "Játékos vesztett"
    if kap == vart:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")


def gep_vesztett_teszt():
    jLap = [10, 5, 4]
    gLap = [6, 7, 10]
    kap = eredmeny(jLap, gLap)
    vart = "Gép vesztett"
    if kap == vart:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")



def dontetlen_teszt():
    jLap = [10, 5, 7]
    gLap = [6, 7, 9]

    if osszegzes(jLap) == osszegzes(gLap):
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")

def tesztek():
    jatekos_vesztett_teszt()
    gep_vesztett_teszt()
    dontetlen_teszt()


tesztek()