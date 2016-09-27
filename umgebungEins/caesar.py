
standardalphabetSimple = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                          "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                          "t", "u", "v", "w", "x", "y", "z"]


def encryptCaesar(klartext, shift):
    klartextListe = list(klartext)
    i = 0
    for buchstabe in klartextListe:
        ausgangsbuchstabenindex = standardalphabetSimple.index(buchstabe)
        klartextListe[i] = standardalphabetSimple[
                                   (ausgangsbuchstabenindex + shift) % 27]
        i = i + 1
    print(''.join(klartextListe))
    return ''.join(klartextListe)


def decryptCaesar(chiffretext, shift):
    chiffretextListe = list(chiffretext)
    i = 0
    for buchstabe in chiffretextListe:
        ausgangsbuchstabenindex = standardalphabetSimple.index(buchstabe)
        chiffretextListe[i] = standardalphabetSimple[
                                   (ausgangsbuchstabenindex - shift) % 27]
        i = i + 1
    print(''.join(chiffretextListe))
    return ''.join(chiffretextListe)
