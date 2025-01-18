def suite(n):
    c = 0
    for k in range(n + 1):
        c = c + k
    return c


def triangle(n):
    for j in range(1, n + 1):
        for i in range(1, j + 1):
            print(i, end="")
        print()


def diamant(h):
    for i in range(h):  # Partie supérieure
        print(" " * (h - i - 1) + "*" * (2 * i + 1))
    for i in range(h - 1):  # Partie inférieure
        print(" " * (i + 1) + "*" * (2 * (h - i - 1) - 1))


def compare(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    return "Ils sont égaux."
