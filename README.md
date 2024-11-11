# Cryptography
The practical cryptographical algorithms and tools.

## List of Content:
* Required Python packages.
* Implementing RSA Cryptosystem.

### Required Python packages:
1. sympy



### Implementing RSA Cryptosystem.  &larr; In Progress... 
### Process...:
1. Started implementing RSA.
2. Decided that I want to program an algorithm that will produce prime numbers up to n for me.
   1. I found Miller-Rabin test, which is not for generating primes but for testing a given number if it's a prime. 
      1. *Comment:* Using a number testing algorithm to generate a list of primes gave me a proper headache. I need to learn to research more before jumping into implementing.
   2. I searched for effective prime generation algorithms and "Sieve of Eratosthenes" came up. 
      1. *Comment:* Still I did not use as much time as I would like to ensure that I am implementing the algorithm correctly. 
3. I used the primes that I generated in file Sieve_of_Eratosthenes. Since all primes are coprime to each other I can now pick the greates two and get p * q.
4. Now I can actually implement the RSA algorithm!
   1. **Next &rarr;** Make it handle encryption and decryption of numbers.
   2. Extend it to handle characters.

#### Extra for RSA:
* I implement my own gcd instead of using an library. 

### Coming next:
* Implement the Miller-Rabin test, and use it to check if a large number is a prime.
* Algorithms for Discrete Logarithm calculation. 
* Digital Signature protocols.


