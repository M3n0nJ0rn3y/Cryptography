#Libraries:
import random
from Cryptography.Efficiency_Algorithms.Square_n_Multiply import square_n_multiply


#Phase 0:
# Prime Generation.
def mr_prime_generator() -> int:
    d, exponent, perf_modulo = mr_function()
    prime_sus = Miller_Rabin_test(d, exponent, perf_modulo)

    while not prime_sus:
        print("--------------------------------------------------------------------")
        print("------------------------Generating Prime----------------------------")
        print("--------------------------------------------------------------------")

        d, exponent, modulos = mr_function()
        prime_sus = Miller_Rabin_test(d, exponent, perf_modulo)

    return perf_modulo


def Miller_Rabin_test(m, r, n) -> bool:
    a = random.randint(2, n-2)
    x = square_n_multiply(a, m, n)

    while x == 1 or x == n - 1:
        a = random.randint(2, n-2)
        x = square_n_multiply(a, m, n)

    for i in range(r-1):
        x = square_n_multiply(x, 2, n)

        if x == n - 1:
            a = random.randint(2, n - 2)
            x = square_n_multiply(a, m, n)

        if x == n - 1:
            return True

    return False


def mr_function():
    # The first and the last int s.t. len(bin(int))=50
    #n = random.randint(2 ** 50, (2 ** 51) - 1)
    n = random.randint(200, 500)
    m = n - 1
    r = 0

    # While m is dividable by 2, count the number of times we can divide m by two.
    # After this function n - 1 = m * 2^r
    while m % 2 == 0:
        m = m // 2
        r += 1

    return int(m), r, n

#Phase 1:
#Phase 2:
#Phase 3:


if __name__ == "__main__":
    print(mr_prime_generator())
