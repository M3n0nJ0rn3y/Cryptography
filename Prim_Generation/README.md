# Algorithms for generating large prime numbers efficiently.

## List of content:
* Sieve of Eratosthenes.

### Sieve of Eratosthenes.
**Time complexity:**\
$O(n*log(log(n)))$

**The Algorithm:**
1. List instantiation:\
Start by instantiating a list of all numbers starting from 2 up to n. Each number will have a boolean value true or false (true for prime and false for composite).
Which we will initialize with setting all values to true for all numbers up to n.\
*Example:* ``[2:true, 3:true, 4:true, 5:true, ..., n:true]``

2. List iteration:
   1. During the process of elimination, simply pick the first true value in the list (which in our case is 2), and set that to our current prime.\
   *Example:* $(2*p, 3*p, 4*p, \dots ,n*p)$
   2. With the current p iterate through all multiples of p up to n and set them to false (These are our composite numbers which can be divided by our current prime).
   *Example:* For $i=2,3,4, \dots, n$ ``list[i*p]=False``
   3. Move to next prime (next index with a true value), and repeat the same process.
3. Follow this iteration process until $p^2>n$. Then you will have a list of only primes.\
*Example:* ``[2:true, 3:true, 4:false, 5:true, 6:false, ..., n:true]``

