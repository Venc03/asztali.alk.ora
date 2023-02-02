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
    jLap = [10, 12]
    gLap = [10, 8]
    kap = eredmeny(jLap, gLap)
    vart = "Játékos vesztett"
    if kap == vart:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")

def jatekos_vesztett_teszt_2():
    jLap = [11, 5, 2]
    gLap = [9, 10]
    kap = eredmeny(jLap, gLap)
    vart = "Játékos vesztett"
    if kap == vart:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")

def jatekos_vesztett_teszt_3():
    jLap = [5, 3, 5]
    gLap = [9, 5, 6]
    kap = eredmeny(jLap, gLap)
    vart = "Játékos vesztett"
    if kap == vart:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")


def gep_vesztett_teszt():
    jLap = [10, 11]
    gLap = [10, 10]
    kap = eredmeny(jLap, gLap)
    vart = "Gép vesztett"
    if kap == vart:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")


def gep_vesztett_teszt_2():
    jLap = [7, 10, 4]
    gLap = [11, 8]
    kap = eredmeny(jLap, gLap)
    vart = "Gép vesztett"
    if kap == vart:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")

def gep_vesztett_teszt_3():
    jLap = [10, 5, 6]
    gLap = [5, 3, 5]
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

def dontetlen_teszt_2():
    jLap = [10, 7, 6]
    gLap = [11, 11]

    if osszegzes(jLap) == osszegzes(gLap):
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")

def tesztek():
    jatekos_vesztett_teszt()
    jatekos_vesztett_teszt_2()
    jatekos_vesztett_teszt_3()
    gep_vesztett_teszt()
    gep_vesztett_teszt_2()
    gep_vesztett_teszt_3()
    dontetlen_teszt()
    dontetlen_teszt_2()


tesztek()