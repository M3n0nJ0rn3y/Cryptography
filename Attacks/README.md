# Attacks against Cryptographic Algorithms:
## List of Content:
* Pollards $\rho $-method.


### Pollards $\rho $-method.
This is a probabilistic Algorithm which can be used for both factorization and for calculating the discrete logarithm.
Here I will only focus on the property of calculating Discrete Logarithms, and I will explain how this can be used against cryptographic algorithms.

In most cases of Cryptographic algorithms, some integers are chosen from a finite group $&integers;^{*}_{p}$, where $p$ is a large prime.
Pollard $\rho$-method makes use of multiple laws that finite groups are enclosed under in order to find a collision in the set, and then use that collision to find private integers used for decryption. In order to be effectively ''guess'' the collision it makes use of an iterative method often referred to as ''Hare and Tortoise Iteration'' (Which will be demonstrated through the algorithm).
#### The Algorithm:
The Algorithm can be divided into 3 sub-steps:
Consider an intercepted ciphertext $C \equiv g^d \mod p$ (Where $g$ is a generator of &integers;^{*}_{p}). Often the private exponent $d$ for a Symmetric Encryption Algorithm is chosen from the set $&integers;^{*}_{p} $.
$$ d \in &integers;^{*}_{p} $$
Now in order to be able to decrypt the ciphertexts that we intercepted or will intercept we need to know the exponent $d$ such that we can calculate: $d^{-1} \mod p$ for decryption purposes. In order to successfully find $d$ we will apply Pollards $\rho$-method as follows.
1. **Dividing the finite field into pseudo random subsets**\
   1. Choose $S_1, S_2, S_3$ s.t. $ S_1 \cap S_2 \cap S_3 \subseteq &integers;^{*}_{p} $, where (as an example):
   $$ if\  x_i \equiv 0 \mod 3,\ then\ x_i \in S_1 $$
   $$ if\  x_i \equiv 1 \mod 3,\ then\ x_i \in S_2 $$
   $$ if\  x_i \equiv 2 \mod 3,\ then\ x_i \in S_3 $$
   2. Then we define a function $f(x)$ which will map the different $x_i$ to one of the set in a pseudo-random fashion.
   $$f(x) = x * g \mod p,\  if\ x_i \in S_1$$
   $$f(x) = x^2 \mod p,\ if\ x_i \in S_2    $$
   $$f(x) = x * h \mod p,\ if\ x_i \in S_3$$
   3. Finally, we instantiate our ''Hare and Tortoise iterators'':
      1. Initialize bases as follows:
   $$ x_{hare} \equiv x_{tortoise} \equiv g \mod p $$
      2. Initialize exponent variables:
      $$ a_{hare}, b_{hare}\ \& \ a_{tortoise}, b_{tortoise}\ s.t.$$ 
      $$ x_{hare} \equiv g^{a_{hare}}*h^{b_{hare}} \mod p\ \& \ x_{tortoise} \equiv g^{b_{tortoise}}*h^{b_{tortoise}} \mod p $$
2. **Iterating between the subsets**
   1. Iterate $x_{hare}$ and $x_{tortoise}$ interchangeably moving the $x_{hare}$ twice as fast as $x_{tortoise}$:
   $$ f(x_{hare}) = f(f(x_{hare}))$$
   2. For each iteration check if:
   $$ x_{hare} \equiv x_{tortoise} \Leftrightarrow  g^{a_{hare}}*h^{b_{hare}} \equiv g^{b_{tortoise}}*h^{b_{tortoise}} \mod p$$
   $$ g^{a_{hare} - a_{tortoise}} \equiv h^{{b}_{tortoise}-b_{hare}} \mod p$$
   Therefore at each iteration one should also check that: $a_{hare} \not= a_{tortoise}$ and if $a_{hare} = a_{tortoise}$, then one must find another $x_{hare}\ \&\ x_{tortoise}$.
3. **Solving the equation**
   1. If $a_{hare} \not= b_{tortoise},\ then:\ d \equiv (a_{hare}-a_{tortoise}) * (b_{tortoise}-b_{hare})^{-1} \mod p $