from random import randint

user_pass = input("Enter your password : ")
caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v',
              'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def crack_password():
    guess = ""
    essaies = 0
    while guess != user_pass:
        guess = ""
        for _ in range(len(user_pass)):  # _ nom de variable utilisé quand on ne veut pas réutiliser le résultat.
            guess_letter = caracteres[randint(0, 35)]
            guess = str(guess_letter) + str(guess)
            essaies += 1
    print("le mot de passe est : " + guess + " Après ", essaies, "essaies")


def permutations(iterable, r=None):
    if len(iterable) == r:
        return
    permutations(iterable, len(iterable))
    # Source : https://docs.python.org/fr/3/library/itertools.html#itertools.permutations
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n - r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return












def permutations_mock(iterable, r=None):
    if len(iterable) == r:
        return
    permutations_mock(iterable, len(iterable))
    # Source : https://docs.python.org/fr/3/library/itertools.html#itertools.permutations
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    """
    The mocked part
    """
    return



































def verification(password):
    for permutation in permutations(caracteres):
        if "".join(permutation) == password:
            return permutation


mot_de_passe = verification(user_pass)
print(mot_de_passe)
