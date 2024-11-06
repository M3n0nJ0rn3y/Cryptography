def sieve_of_eratos(n):
    p_squared = (n**2)+1
    list_of_primes = [[i, True] for i in range(p_squared)] # 0 and 1 are added in order to align indexes with the values.

    for number_tuple in list_of_primes[2:]: # Skip 0 and 1.

        number, prime = number_tuple[0], number_tuple[1]

        if number >= n: # When you have iterated through n items you're done.
            break

        if not prime: # If the value is composite.
            continue # Skip to next number.

        for i in range(2, n):
            composite = number * i # p * i.
            list_of_primes[composite] = [composite, False] # Remove the product of p*i which is a composite number.

    return list_of_primes[2:]

def primes_up_to(n):
    sieve_list = sieve_of_eratos(n)

    prime_list = [prime_num for prime_num, statement in sieve_list if statement] # I went wild.

    return prime_list


print(primes_up_to(10))
