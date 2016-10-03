from random import shuffle
from copy import deepcopy
alphabet = {' ': 0, 'a': 1, 'b': 2, 'c': 3,
            'd': 4, 'e': 5, 'f': 6, 'g': 7,
            'h': 8, 'i': 9, 'j': 10, 'k': 11,
            'l': 12, 'm': 13, 'n': 14, 'o': 15,
            'p': 16, 'q': 17, 'r': 18, 's': 19,
            't': 20, 'u': 21, 'v': 22, 'w': 23,
            'x': 24, 'y': 25, 'z': 26
            }
ranking = [' ', 'e', 'n', 'i', 's', 'r', 'a', 't', 'd', 'h', 'u', 'l', 'c',
           'g', 'm', 'o', 'b', 'w', 'f', 'k', 'z', 'p', 'v', 'j', 'y',
           'x', 'q'
           ]
# der erste Wert ist jeweils mein Index, der zweite Wert gibt indirekt die
# Häufigkeit an je höher desto häufiger kommt der entsprechende Buchstabe
# im deutschen Alphabet vor


def permutiereAlphabet():
    permutationsAlphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                            "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                            "t", "u", "v", "w", "x", "y", "z"]
    shuffle(permutationsAlphabet)
    return permutationsAlphabet


def findeMaxValueKey(woerterbuch):
    # fuer die wiederholte Anwendung ineffizient, aber fuer kleine Beispiele ok
    werte = list(woerterbuch.values())
    schluessel = list(woerterbuch.keys())
    return schluessel[werte.index(max(werte))]


def findeValueKey(woerterbuch, wert):
    werte = list(woerterbuch.values())
    schluessel = list(woerterbuch.keys())
    return schluessel[werte.index(wert)]


def swapRanking(rankingListe, buchstabeEins, buchstabeZwei):
    indexBuchstabeEins = rankingListe.index(buchstabeEins)
    indexBuchstabeZwei = rankingListe.index(buchstabeZwei)
    swappy = rankingListe[indexBuchstabeEins]
    rankingListe[indexBuchstabeEins] = buchstabeZwei
    rankingListe[indexBuchstabeZwei] = swappy
    return rankingListe


def analysePerm(chiffretext):
    chiffretextListe = list(chiffretext)
    haeufigkeiten = {" ": 0, "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0,
                     "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
                     "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
                     "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    for i in range(len(chiffretextListe)):
        haeufigkeiten[chiffretextListe[i]] += 1
    chiffreRanking = []
    for j in range(len(haeufigkeiten)):
        maxValKey = findeMaxValueKey(haeufigkeiten)
        chiffreRanking.append(maxValKey)
        del haeufigkeiten[maxValKey]
    return chiffreRanking


def encryptPerm(klartext):
    permutationsAlphabet = permutiereAlphabet()
    klartextListe = list(klartext)
    for i in range(len(klartextListe)):
        buchstabe = klartextListe[i]
        permutationsIndex = alphabet[buchstabe]
        klartextListe[i] = permutationsAlphabet[permutationsIndex]
    return ''.join(klartextListe), permutationsAlphabet


def berechneSchluesselAlphabet(chiffreRanking):
    schluesselAlphabetKandidat = {}
    for i in range(len(ranking)):
        schluesselAlphabetKandidat[chiffreRanking[i]] = ranking[i]
    return schluesselAlphabetKandidat


def simpleDecryptPerm(chiffretext, schluessel):
    # Idee: stelle Gegenüberstellungsdictionary 'schluesselAlphabet' her und
    # ersetze dementsprechend
    chiffretextListe = list(chiffretext)
    schluesselAlphabet = deepcopy(alphabet)
    for i in range(27):
        tempIndex = findeValueKey(schluesselAlphabet, i)
        schluesselAlphabet[tempIndex] = schluessel[i]
    # das schluesselAlphabet muss noch "gedreht" werden sonst mappen wir
    # in die falsche Richtung, das passiert in der nächsten Zeile
    schluesselAlphabet = {v: k for k, v in schluesselAlphabet.items()}
    tempIndex = 0
    for i in chiffretextListe:
        chiffretextListe[tempIndex] = schluesselAlphabet[i]
        tempIndex = tempIndex + 1
    print(''.join(chiffretextListe))
    return ''.join(chiffretextListe)


def decryptPerm(chiffretext, chiffreRanking=None):
    if chiffreRanking is None:
        chiffreRanking = analysePerm(chiffretext)
        # print(ranking)
    while True:
        schluesselAlphabet = berechneSchluesselAlphabet(chiffreRanking)
        chiffretextListe = list(chiffretext)
        tempIndex = 0
        for i in chiffretextListe:
            chiffretextListe[tempIndex] = schluesselAlphabet[i]
            tempIndex = tempIndex + 1
        print(''.join(chiffretextListe))
        userInput = input("Sieht das Ergebnis sinnvoll aus? j/n ")
        if userInput == "j":
            print("Super, das ist töfte!")
            return
        if userInput == "n":
            print("Wie willst du weiter vorgehen?")
            print("Ich möchte:")
            print("- einen Buchstaben durch einen anderen ersetzen(1)")
            print("- dass du mir einen neuen Vorschlag machst(2)")
            print("- aufgeben und Schande über mich bringen(3)")
        userInput = input("Nummer der Option meiner Wahl: ")
        if userInput == "1":
            buchstabeEins = input("Welchen Buchstaben möchtest du ersetzen? ")
            buchstabeZwei = input("Welcher Buchstabe soll ihn ersetzen? ")
            swapRanking(chiffreRanking, buchstabeEins, buchstabeZwei)
            print(ranking)
