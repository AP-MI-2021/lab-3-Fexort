'''
Numerele au semne alternante.
'''


def get_longest_alternating_signs(n):

    s = 0
    z = n
    while n:
        n = input
        if z * n > 0:
            return s
        s = s + 1
    return s





'''
Toate numerele sunt formate din cifre prime.
'''


def get_longest_prime_digits(n):
    s = 0
    while n:
        if   n%10 != 2:
            return False
        elif n%10 != 3:
            return False
        elif n % 10 != 5:
            return False
        elif n % 10 != 7:
            return False
        s = s + 1
        n = n//10
    return s




def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs(1) == 5
    assert get_longest_alternating_signs(6) == 3
    assert get_longest_alternating_signs(21) == 7
def test_get_longest_prime_digits():
    assert get_longest_prime_digits(237) == 3
    assert get_longest_prime_digits(2222) == 4
    assert get_longest_prime_digits(2357) == 4
def main():

    while True:
        print("Optiuni: ")
        print("1. Numerele au semne alternante. ")
        print("2. Toate numerele sunt formate din cifre prime.")
        print("4. Terminarea programului")
        option = input("scrie nr. optiuni: ")
        if option == 1:
            n = input("introdu numarul")
            get_longest_alternating_signs(n)
        if option == 2:
            n = input("introdu numarul")
            get_longest_prime_digits(n)
        if option == 4:
            break



if __name__ == '__main__':
    test_get_longest_alternating_signs()
    test_get_longest_prime_digits()
    main()




