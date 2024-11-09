def sieve_of_eratos(input_n:int):
    calc_n = input_n//2
    p_squared = (calc_n**2)+1
    list_of_primes = [[i, True] for i in range(p_squared)] # 0 and 1 are added in order to align indexes with the values.
    print("Generating list of primes!!")

    for number_tuple in list_of_primes[2:]: # Skip 0 and 1.

        number, prime = number_tuple[0], number_tuple[1]

        if number >= calc_n: # When you have iterated through n items you're done.
            break

        if not prime: # If the value is composite.
            continue # Skip to next number.

        for i in range(2, calc_n):
            composite = number * i # p * i.
            list_of_primes[composite] = [composite, False] # Remove the product of p*i which is a composite number.

    return list_of_primes[2:]

def primes_up_to(n):
    sieve_list = sieve_of_eratos(n)
    print("Formating list of primes!!")

    prime_list = [prime_num for prime_num, statement in sieve_list if statement] # I went wild.

    return prime_list

def pick_p_q(n):
    sieve_list = sieve_of_eratos(n)
    print("Picking the last two integers.")

    p, q = sieve_list[-2], sieve_list[-1]

    return p, q

if __name__ == '__main__':
    print(primes_up_to(10))