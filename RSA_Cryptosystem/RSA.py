#Libraries:
import random
from Cryptography.Modular_Arithmatics.Square_n_Multiply import square_n_multiply

#Initialization of lists:
def initialize_list_n():
    print("Initializing random sample lists of probable primes...")
    n_list = random.sample(range(2 ** 50 + 1, 2 ** 51 - 1), 1000000)
    print("List n initialization Complete!")

    return n_list


def initialize_list_base(n:int):
    print("Initializing random sample lists of bases a...")
    base_list = random.sample(range(2, n-1), n-2)
    print("List of bases initialization Complete!")

    return base_list


#Phase 0:
# Prime Generation.
def main_prime_generation(list_n, list_a) -> int:
    confidence = 0
    # This method is inneficient.
    n_list = initialize_list_n()# Initialize list of n's
    prim_n = pick_n(n_list)# Pick an initial n to test for primality.
    base_list = initialize_list_base(prim_n)# Initialize list of bases from 2 to n-2
    base_a = pick_a(base_list)# Pick an initial base a.

    # Convert the n to the correct format of: d * 2^exponent (mod prim_n)
    d, exponent = n_decomposition(prim_n)

    # Calculate x = a^d (mod n)
    x = square_n_multiply(base_a, d, prim_n)

    # Run Miller-Rabin test r-1 times.


    prime_sus = Miller_Rabin_test(d, exponent, prim_mod)





    while not prime_sus:
        print("--------------------------------------------------------------------")
        print("------------------------Generating Prime----------------------------")
        print("--------------------------------------------------------------------")

        d, exponent, prim_mod = n_decomposition()
        prime_sus = Miller_Rabin_test(d, exponent, prim_mod)

    return prim_mod


def Miller_Rabin_test(d, r, n) -> bool:
    print("Testing...")
    a = random.randint(2, n-2)
    x = square_n_multiply(a, d, n)

    while x == 1 or x == n - 1:
        a = random.randint(2, n-2)
        x = square_n_multiply(a, d, n)

    print("An appropriate base has been chosen...")

    for i in range(r-2): # Iterate up to r-1 times.
        x = square_n_multiply(x, 2, n)

        if x == n - 1:
            a = random.randint(2, n - 2)
            x = square_n_multiply(a, 2, n)

    return True if confidence == 40 else False

# This function keeps track of how many times it was called.
# That is in order to always return unique random elements.
def pick_n(list_of_num):
    i[0] += 1
    index = i[0]

    try:
        n = list_of_num[index]
        return n
    except IndexError as e:
        print(f'Extend the n searching list! Error:\ {e}')


def pick_a(base_list):
    j[0] += 1
    index = j[0]

    try:
        a = base_list[index]
        return a
    except IndexError as e:
        print(f'Extend the base searching list! Error:\ {e}')


def n_decomposition(n: int):
    d = n - 1
    r = 0

    # While m is dividable by 2, count the number of times we can divide m by two.
    # After this function n - 1 = m * 2^r
    while d % 2 == 0:
        d = d // 2
        r += 1

    return int(d), r


# Global function counters:
i = [-1]
j = [-1]


#Phase 1:
#Phase 2:
#Phase 3:
