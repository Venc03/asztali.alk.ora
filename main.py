#megoldas


def eredmeny(jLap: list[int], gLap: list[int]):
    s = ""
    jOssz = osszegzes(jLap)
    gOssz = osszegzes(gLap)
    jdb = lapDb(jLap)
    gdb = lapDb(gLap)

    if jOssz <= 21 and gOssz <= 21:
        if jOssz < gOssz:
            s = "Játékos vesztett"
        elif gOssz < jOssz:
            s = "Gép vesztett"
        elif jOssz == gOssz:
            if jdb < gdb:
                s = "Játékos vesztett"
            elif gdb < jdb:
                s = "Gép vesztett"
            else:
                s = "A jatek dontetlen"
    else:
        if jOssz > 21:
            s = "Játékos vesztett"
        if gOssz > 21:
            s = "Gép vesztett"
        if jOssz > 21 and gOssz > 21:
            s = "dontetlen"
    return s

def osszegzes(lista: list[int]):
    i = 0
    ossz = 0
    while i < len(lista):
        ossz += lista[i]
        i += 1
    return ossz

def lapDb(lista: list[int]):
    return lista


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
    kap = eredmeny(jLap, gLap)
    vart = "dontetlen"
    if kap == vart:
        print("A teszt sikeres")
    else:
        print("A teszt megbukott")

def dontetlen_teszt_2():
    jLap = [10, 7, 6]
    gLap = [11, 5, 10]
    kap = eredmeny(jLap, gLap)
    vart = "dontetlen"
    if kap == vart:
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