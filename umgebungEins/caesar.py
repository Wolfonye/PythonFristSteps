standardalphabetSimple = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                          "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                          "t", "u", "v", "w", "x", "y", "z"]


def analyseCaesar(chiffretext):
    statistik = {' ': [0, 0], 'a': [1, 0], 'b': [2, 0], 'c': [3, 0],
                 'd': [4, 0], 'e': [5, 0], 'f': [6, 0], 'g': [7, 0],
                 'h': [8, 0], 'i': [9, 0], 'j': [10, 0], 'k': [11, 0],
                 'l': [12, 0], 'm': [13, 0], 'n': [14, 0], 'o': [15, 0],
                 'p': [16, 0], 'q': [17, 0], 'r': [18, 0], 's': [19, 0],
                 't': [20, 0], 'u': [21, 0], 'v': [22, 0], 'w': [23, 0],
                 'x': [24, 0], 'y': [25, 0], 'z': [26, 0]}

    chiffretextbuchstaben = list(chiffretext)
    for i in range(len(chiffretextbuchstaben)):
        statistik[chiffretextbuchstaben[i]][1] += 1

    maximum = 0
    maxindex = 0
    for j in statistik:
        if statistik[j][1] > maximum:
            maximum = statistik[j][1]
            maxindex = statistik[j][0]

    shift = maxindex - 5
    return shift


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
