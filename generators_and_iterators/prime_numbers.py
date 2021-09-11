def check_if_prime(num):
    factor = 2
    if num > 1:
        while factor < num:
            if num % factor == 0:
                return False
            factor += 1
        return True


def get_primes(list_given):
    list_of_all_primes = [el for el in list_given if check_if_prime(el)]
    index = 0
    while index < len(list_of_all_primes):
        yield list_of_all_primes[index]
        index += 1

print(list(get_primes([0,2, 4, 3, 5, 6, 9, 1, 0])))

