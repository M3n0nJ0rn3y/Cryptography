#Libraries:
from Cryptography.Modular_Arithmatics.Square_n_Multiply import square_n_multiply
from Cryptography.Prim_Generation.Sieve_of_Eratosthenes import pick_p_q
from sympy import mod_inverse
from math import gcd

#PHASE 0:
# Generates a list of prime numbers and picks the greatest two that are relatively co prime.
def g_of_primes():
    p, q = pick_p_q(2**50) # Creates a list of primes up to binary length 50.
    print("Generation of Primes Completed!!")

    return p, q

#PHASE 1:
# Calculates fi(N) explained in README file in the current directory.
def eulers_function(p, q):
    return (p-1) * (q-1)

def find_inverse_in_mod(mod):
    print("Searching for an appropriate integer with an inverse.")

    for num in range(2, mod):
        has_inv = gcd(num, mod)
        if has_inv == 1:
            return num, mod_inverse(num, mod)
    return 0


# Calculates the Private and Public keys using the g_of_primes to pick primes.
def keys():
    p, q = g_of_primes()
    n = p * q
    fi_n = eulers_function(p, q)
    e, d = find_inverse_in_mod(fi_n)

    print("Keys calculated!!")

    return (n, e), (n, d)

# Test if the input is the same as output:
def test(input_m, output_m):
    if input_m == output_m:
        return True
    else:
        print(f'Wrong!: {input_m} != {output_m}')
        return False


#PHASE 2:
# The Encryption algorithm pub_k = (n, e):
def rsa_encrypt(message:int, pub_k:tuple):
    print("Calculating the encryption.")
    e = pub_k[1]
    mod = pub_k[0]
    ciphertext = square_n_multiply(message, e, mod)

    return ciphertext


#PHASE 3:
# The Decryption algorithm priv_k = (n, d):
def rsa_decrypt(ciphertext:int, priv_k:tuple):
    print("Calculating the decryption.")
    d = priv_k[1]
    mod = priv_k[0]

    original_message = square_n_multiply(ciphertext, d, mod)

    return original_message


if __name__ == '__main__':
    the_message = 42
    # Calculate the Public and Private keys.
    pub_k, priv_k = keys()

    # Calculate the encryption of your message:
    C = rsa_encrypt(the_message, pub_k)

    # Calculate the decryption of your message:
    M = rsa_decrypt(C, priv_k)

    # Test the calculation.
    print(test(the_message, M))



