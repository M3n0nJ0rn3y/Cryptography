#Libraries:
import random
from Cryptography.Prim_Generation.Sieve_of_Eratosthenes import primes_up_to


#PHASE 0:
# Generates a list of prime numbers and picks the greatest two that are relatively co prime.
def g_of_primes():
    list_of_primes = primes_up_to(2**50) # Creates a list of primes up to binary length 50.
    p, q = list_of_primes[-1], list_of_primes[-2]

    return p, q

#PHASE 1:
# Calculates fi(N) explained in README file in the current directory.
def eulers_function(p, q):
    return (p-1) * (q-1)

def find_inverse_in_mod(mod):


    return e, d

# Calculates the Private and Public keys using the g_of_primes to pick primes.
def keys():
    p, q = g_of_primes()
    N = p * q
    fi_n = eulers_function(p, q)
    e, d = find_inverse_in_mod(mod)



#PHASE 2:
#PHASE 3: