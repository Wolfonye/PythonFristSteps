def product(x, y):
    return x*y


def callMeSpecki(name):
    print(name + " ist ein fetter schwabbeliger Specki!")


if __name__ == "__main__":
    import sys
    callMeSpecki(str(sys.argv[1]))
