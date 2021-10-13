'''
Numerele au semne alternante.
'''


def get_longest_alternating_signs(list):

    s = 0

    for i in list:
        if list[i] * list[i+1] > 0:
            return s
        s = s + 1
    return s





'''
Toate numerele sunt formate din cifre prime.
'''


def get_longest_prime_digits(list):
    s = 0
    for i in list:
        if list[i]%10 != 2:
            return False
        elif list[i]%10 != 3:
            return False
        elif list[i] % 10 != 5:
            return False
        elif list[i] % 10 != 7:
            return False
        s = s + 1
    return s

'''
Numerele sunt ordonate crescător.
'''
def get_longest_sorted_asc(list):
    s = 0
    for i in list:
        if (list[i] > list[i+1]):
            return False
        s = s + 1
    return s



def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([1, -5, 6, -3, 8]) == 4
    assert get_longest_alternating_signs([6, 6]) == 0
    assert get_longest_alternating_signs([21, -3, 4, -3]) == 3
def test_get_longest_prime_digits():
    assert get_longest_prime_digits([2, 3, 7, 4]) == False
    assert get_longest_prime_digits([2, 2, 2, 2]) == 4
    assert get_longest_prime_digits([2, 3, 5, 7]) == 4
def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([1, 2, 5, 6]) == 4
    assert get_longest_sorted_asc([1, 2, 5, 3]) == False
    assert get_longest_sorted_asc([2, 2, 3]) == 3


def main():

    while True:
        print("Optiuni: ")
        print("1. Numerele au semne alternante. ")
        print("2. Toate numerele sunt formate din cifre prime.")
        print("3. Numerele sunt ordonate crescător.")
        print("4. Terminarea programului")
        option = input("scrie nr. optiuni: ")
        if option == 1:
            list = []
            get_longest_alternating_signs(list)
        if option == 2:
            list = []
            get_longest_prime_digits(list)
        if option == 2:
            list = []
            get_longest_prime_digits(list)
        if option == 4:
            break



if __name__ == '__main__':
    test_get_longest_alternating_signs()
    test_get_longest_prime_digits()
    test_get_longest_sorted_asc()
    main()




