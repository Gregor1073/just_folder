

przesuniecie=int(input("O ile chcesz przesunąć swój tekst?\n"))


def szyfruj(txt):
    zaszyfrowny = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - przesuniecie:
            zaszyfrowny += chr(ord(txt[i]) + przesuniecie - 26)
        else:
            zaszyfrowny += chr(ord(txt[i]) + przesuniecie)
    return zaszyfrowny


def main(args):
    tekst = input("Podaj tekst, który chcesz zaszyfrować:\n")
    print("Tekst zaszyfrowany:\n", szyfruj(tekst))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))