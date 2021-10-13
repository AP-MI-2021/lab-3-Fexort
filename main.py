def citire():
    list = []
    givenstring = input("datele problemei separat prin virgula")
    numersasstring = givenstring.split(",")
    for x in numersasstring:
        list.append(int(x))
    return list
'''
Numerele au semne alternante.
'''

def max_get_longest_alternating_signs(list):
    maxList=[]
    for i in range (len(list)):
        for j in range (i, len(list)):
            if get_longest_alternating_signs(list[i:j+1]) and len(list[i:j+1])>len(maxList):
                maxList = list[i:j+1]
def get_longest_alternating_signs(list):
    for i in range (0, len(list)-1):
        if list[i] >= 0 and list[i+1] >= 0:
            return False
        elif list[i] < 0 and list[i+1] < 0:
            return False
    return True



'''
Toate numerele sunt formate din cifre prime.
'''

def max_get_longest_prime_digits(list):
    maxList=[]
    for i in range (len(list)):
        for j in range (i, len(list)):
            if get_longest_prime_digits(list[i:j+1]) and len(list[i:j+1])>len(maxList):
                maxList = list[i:j+1]
def get_longest_prime_digits(list):
    for i in list:
        if list[i]%10 != 2:
            return False
        elif list[i]%10 != 3:
            return False
        elif list[i] % 10 != 5:
            return False
        elif list[i] % 10 != 7:
            return False
    return True

'''
Numerele sunt ordonate crescător.
'''
def max_get_longest_sorted_asc(list):
    maxList=[]
    for i in range (len(list)):
        for j in range (i, len(list)):
            if get_longest_sorted_asc(list[i:j+1]) and len(list[i:j+1])>len(maxList):
                maxList = list[i:j+1]
def get_longest_sorted_asc(list):
    for i in range (0, len(list)-1):
        if (list[i] > list[i+1]):
            return False
    return True

def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([3, -5, 6, -3, 2]) == True
    assert get_longest_alternating_signs([6, 6]) == False
    assert get_longest_alternating_signs([21, -3, 4, -3]) == True
def test_get_longest_prime_digits():
    assert get_longest_prime_digits([2, 3, 7, 4]) == False
    assert get_longest_prime_digits([2, 2, 2, 2]) == False
    assert get_longest_prime_digits([2, 3, 5, 7]) == False
def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([1, 2, 5, 6]) == True
    assert get_longest_sorted_asc([1, 2, 5, 3]) == False
    assert get_longest_sorted_asc([2, 2, 3]) == True


def main():

    while True:
        print("Optiuni: ")
        print("1. Numerele au semne alternante. ")
        print("2. Toate numerele sunt formate din cifre prime.")
        print("3. Numerele sunt ordonate crescător.")
        print("4. Terminarea programului")
        option = input("scrie nr. optiuni: ")
        if option == 1:
            get_longest_alternating_signs(list)
        if option == 2:
            get_longest_prime_digits(list)
        if option == 3:
            get_longest_prime_digits(list)
        if option == 4:
            break



if __name__ == '__main__':
    test_get_longest_alternating_signs()
    test_get_longest_prime_digits()
    test_get_longest_sorted_asc()
    main()




