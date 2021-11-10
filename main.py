def printMenu():
    print("1. Citire date ")
    print("2. Cea mai lungă subsecvență cu proprietatea 2 ")
    print("3. Cea mai lungă subsecvență cu proprietatea 3 ")
    print("4. Cea mai lungă subsecvență cu proprietatea 13 ")
    print("x. Iesire ")


def citire_lista():
    lst = []
    n = int(input("Dati numarul de elemente al listei: "))
    for i in range(n):
        lst.append(int(input("lst[" + str(i) + "]=")))
    return lst


def NrPrim(n):
    '''
    Determina daca un numar este prim
    :param n numar intreg:
    :return adevarat sau fals:
    '''
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def toateElementelePrime(lst):
    """
    Determina daca toate numerele dintr-o secventa a listei lst sunt prime
    :param lst - lista de numere:
    :return True sau False:
    """
    for x in lst:
        if NrPrim(x) is False:
            return False
    return True


def get_longest_all_primes(lst: list[int]):
    """
    Determina cea mai lunga subsecventa de numere prime
    :param lst - lista de numere:
    :return lista cu cea mai lunga subsecventa de numere prime din lst:
    """
    subsecventaMax1 = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if toateElementelePrime(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventaMax1):
                subsecventaMax1 = lst[i:j + 1]
    return subsecventaMax1


def test_get_longest_all_primes():
    assert get_longest_all_primes([12, 7, 3, 5, 6]) == [7, 3, 5]
    assert get_longest_all_primes([2, 4, 6]) == [2]
    assert get_longest_all_primes([8, 4, 6]) == []


test_get_longest_all_primes()


def semnNumar(x):
    """
    Determina semnul x
    :param x:
    :return true semnul +, false semnul -:
    """
    if (x < 0):
        return False
    else:
        return True


def toateSemneleAlternante(lst):
    """
    Determina daca numerele din lista au semnul alternant sau nu
    :param lst:
    :return True sau False:
    """
    if len(lst) > 1:
        for i in range(0, len(lst) - 1):
            if semnNumar(lst[i]) == semnNumar(lst[i + 1]):
                return False
    return True


def get_longest_alternating_signs(lst: list[int]):
    """
    Determina cea mai lunga subsecventa de numere cu semne alternante
    :param lst - lista de numere:
    :return lista cu cea mai lunga subsecventa de numere cu semne alternante din lst:
    """
    subsecventaMax2 = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if toateSemneleAlternante(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventaMax2):
                subsecventaMax2 = lst[i:j + 1]
    return subsecventaMax2


def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([-3, 3, -3, 7, 9]) == [-3, 3, -3, 7]
    assert get_longest_alternating_signs([7, 8, 9, 10]) == [7]
    assert get_longest_alternating_signs([7, 8, -4, 9, -5, 3, 9, -4]) == [8, -4, 9, -5, 3]


test_get_longest_alternating_signs()


def toateNumereleAuCifrePrime(lst):
    """
    Determina daca toate numerele dintr-o lista au cifrele prime
    :param lst:
    :return True sau False:
    """
    for x in lst:
        k = x
        while k != 0:
            aux = k % 10
            if NrPrim(aux) is False:
                return False
            k = k // 10
    return True


def get_longest_prime_digits(lst: list[int]):
    """
    Determina cea mai lunga subsecventa de numere formate din cifre prime
    :param lst:
    :return:
    """
    subsecventaMax3 = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if toateNumereleAuCifrePrime(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventaMax3):
                subsecventaMax3 = lst[i:j + 1]
    return subsecventaMax3


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([1, 72, 73, 84, 2]) == [72, 73]
    assert get_longest_prime_digits([-3, 7, 3, 5, 8, 3, 7, 72, 5]) == [3, 7, 72, 5]
    assert get_longest_prime_digits([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3]


test_get_longest_prime_digits()

while True:
    printMenu()
    optiune = input("Dati optiunea: ")
    if optiune == "1":
        l = citire_lista()
    elif optiune == "2":
        l1 = get_longest_all_primes(l)
        print(l1[:])
    elif optiune == "3":
        l2 = get_longest_alternating_signs(l)
        print(l2[:])
    elif optiune == "4":
        l3 = get_longest_prime_digits(l)
        print(l3[:])
    elif optiune == "x":
        break