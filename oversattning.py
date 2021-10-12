import sys
def oversattning(sys.argv[0], sys.argv[1]):
    if sys.argv[1] == "-v":
        print(visksprak(sys.argv[0]))
    elif sys.argv[1] == "-r":
        print(rovarsprak(sys.argv[0]))
    elif sys.argv[1] == "-f":
        print(fikonsprak(sys.argv[0]))
    elif sys.argv[1] == "-a":
        print(allsprak(sys.argv[0]))
    elif sys.argv[1] == "-b":
        print(bebissprak(sys.argv[0]))


def fikonsprak(inrad):
    x = inrad.split()
    utrad = ""
    slutlista = []
    for ord in x:
        tknlista = []
        popmätare = []
        for bokstav in ord:
            tknlista.append(bokstav)
        for sak in tknlista:
            if konsonantcheck(sak) is True:
                tknlista.append(sak)
                popmätare.append(0)
            elif vokalcheck(sak) is True:
                tknlista.append(sak)
                tknlista.append("kon ")
                popmätare.append(0)
                utrad += "fi"
                for p in popmätare:
                    tknlista.pop(p)
                break
        for a in tknlista:
            utrad += a
    return utrad


def allsprak(inrad):
    x = inrad.split()
    utrad = ""
    slutlista = []
    for ord in x:
        tknlista = []
        popmätare = []
        for bokstav in ord:
            tknlista.append(bokstav)
        for sak in tknlista:
            if konsonantcheck(sak) is True:
                tknlista.append(sak)
                popmätare.append(0)
            elif vokalcheck(sak) is True:
                tknlista.append("all ")
                for p in popmätare:
                    tknlista.pop(p)
                break
        for a in tknlista:
            utrad += a
    return utrad


def bebissprak(inrad):
    x = inrad.split()
    mening = ""
    for inord in x:
        n = 0
        utord = ""
        while n < len(inord):
            p = n
            if vokalcheck(inord[p]) is True:
                utord += inord[p]
                utord += utord + utord+ " "
                mening += utord
                n = len(inord)
            elif konsonantcheck(inord[p]) is True:
                utord += inord[p]
                n = n+1
    return mening

def visksprak(inrad):
    utrad = ""
    for tkn in inrad:
        if vokalcheck(tkn) is False:
            utrad += tkn
    return utrad

def rovarsprak(inrad):
    utrad = ""
    for tkn in inrad:
        if konsonantcheck(tkn) is True:
            utrad += tkn + "o" + tkn
        else:
            utrad += tkn
    return utrad

def antirovarsprak(inrad):
    utrad = ""
    n = 0
    while n < len(inrad):
        p = n
        if konsonantcheck(inrad[p]) is True:
            n = n+3
            utrad += inrad[p]
        else:
            utrad += inrad[p]
            n = n+1
    return utrad


def konsonantcheck(tkn):
    konsonantlista = "qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM"
    a = 0
    for x in konsonantlista:
        if tkn == x:
            a = 1
    if a == 1:
        return True
    else:
        return False

def vokalcheck(tkn):
    vokallista = "eyuioåaöäEYUIOÅAÖÄ"
    a = 0
    for x in vokallista:
        if tkn == x:
            a = 1
    if a == 1:
        return True
    else:
        return False

