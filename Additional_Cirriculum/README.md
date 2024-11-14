# Cryptographic Functions.
## List of content:
* Legandre / Jacobi Symbol

## Legandre symbol:
Legandre symbol in cryptographic context helps to find whether a residue is a quadratic residue of a residue class or not.
Sometimes when the modulo $p$ is composite we call the symbol the Jacobi symbol which allows us to use the extra properties that Jacobi symbol follows.
Either way if the symbol is a Jacobi or Legandre symbol I will refer to it as a Legandre symbol. It might sound complicated but it isn't the description is as following:

$a \mod p$ is a quadratic residue and can be represented as: $x^2 \equiv a \mod p$, if the Legandre symbol: $( \frac{a}{p}) = 1$

During the calculation of the symbol I will make use of the following Theorems, Laws and properties of both Legandre and Jacobi symbol:
****
**Properties of Legandre symbol:**\
Let p bean odd prime number and a,b be integers.
1. The number of solutions to the congruence $x^2 \equiv a \mod p = 1 + (\frac{a}{p})$
2.  $(\frac{a}{p}) \equiv a^{(\frac{p-1}{2})}$
3. $(\frac{a*b}{p}) \equiv (\frac{a}{p})*(\frac{b}{p})$
4. $if\ a \equiv b \mod p,\ then\ (\frac{a}{p}) = (\frac{b}{p})$
5. $(\frac{1}{p}) = 1\ and\ (\frac{-1}{p})= (-1)^{(\frac{(p-1)}{2})}$. Which means that, $-1$ is a quadratic residue modulo p, 
$(e.g\ x^2 \equiv -1 \mod p)$, iff $p \equiv 1 \mod 4$.
6. if $p$ does not divide $a$, then $(\frac{a^2}{p}) = 1\ \&\  (\frac{a^2*b}{p})=(\frac{b}{p})$

****

**Properties of Jacobi Symbol:**\
Let $n,m$ be an odd positive integers and $a,b$ be integers.
1. $if a \equiv b \mod n,\ then\ \frac{a}{n} = \frac{b}{n}$
2. $\frac{a*b}{n} = \frac{a}{n}* \frac{b}{n}$
3. $\frac{a}{n*m} = \frac{a}{n} * \frac{a}{m}$
4. $if\ gcd(a,n)=1,\ then\ \frac{a^2}{n} = \frac{a}{n^2} = 1,\ \frac{a^2*b}{n} = \frac{b}{n},\ and\ \frac{b}{m^2*n} = \frac{b}{n}$

****

**The Law of Quadratic Reciprocity.**
1. $(\frac{p}{q}) * (\frac{q}{p}) = (-1)^{ \frac{p-1}{2} * \frac{q-1}{2}}$
2. $( \frac{2}{p} ) = (-1)^{ \frac{p^2-1}{8} }$
****


### Legandre /Jacobi symbol use case:
Often in cryptography one establish some finite group $&integers;^{*}_{p}$ where $p$ is an integer, and all encryptions and decryptions
happens with the use of this finite group. Here is one of the scenarios where Legandre symbol can help us to crack a crypto-algorithm.

**Example.1:**

Imagine that you managed to intercept the $\varphi(N)=39$ and the prime used for establishing the finite field $p = 65$ for an RSA encryption system.

We could set the equation in the following way: $39 \mod 65$ and convert this into the Legandre symbol: $(\frac{39}{65})$.
Then with the help of the Legandre symbol we can check whether there exists any factorization for $a$ in $p$ or not.

1. I begin by checking whether the modulo is a composite number or a prime by Trial Division:
   $$ 65 = 5 * 13 \Rightarrow It's\ composite.$$
2. I apply the Jacobi symbol property:
$$ \frac{39}{65} = \frac{39}{5} * \frac{39}{13} \Leftrightarrow \frac{4}{5}* \frac{0}{13}$$
3. It is obvious that $ 0 \mod 13 \equiv 0 \mod 13$ which yields $\frac{0}{13} = 0$
4. This guarantees that the symbol $\frac{39}{65} = 0$, which means that $39 \mod 65$ is neither an quadratic residue class nor a non-residue class. 
This means that there is no way for factoring this $\phi(N)$ into smaller factors. Which makes this equation pretty cryptographically secure.


**Example.2:**
Let's try with a better example:\
We intercept the $\phi(N) = 11$ and we know the $p = 43 \Rightarrow 11 \mod 43$

1. Evaluate the primality of the modulos: $\sqrt{43} \approx 7 \Rightarrow$ 43 should be dividable into factors of up to 7. But it isn't. Which means that 43 is prime. 
2. Since $43$ is not composite we should be able to evaluate whether the Legandre symbol is a quadratic residue $x^2 \equiv 11 \mod 43$.
3. I start by rewriting the legandre symbol:
$$(\frac{11}{43}) \Rightarrow (\frac{11}{43}) (\frac{43}{11}) \Leftrightarrow (\frac{11}{43}) (\frac{43}{11}) = (-1)^{ \frac{11 - 1}{2} * \frac{43-1}{2} } = (-1)^{ \frac{10}{2} * \frac{42}{2} } = (-1)^{ 5 * 21 } = (-1)$$
4. Now I know that the symbol $(\frac{11}{43})$ can be rewritten as $(\frac{11}{43}) = (-1)* (\frac{43}{11}) = -(\frac{43}{11}) = -(\frac{10}{11})$
5. Then I can factor out the equation and solve each part separately:
$$ (\frac{11}{43}) = -(\frac{10}{11}) \Leftrightarrow (-1)*(\frac{5}{11})*(\frac{2}{11})$$
6. Evaluating: $(\frac{5}{11})$:
    $$ (\frac{5}{11}) \Rightarrow (\frac{5}{11})*(\frac{11}{5}) \Leftrightarrow  (\frac{5}{11})*(\frac{11}{5}) = (\frac{5}{11})*(\frac{1}{5}) = (-1)^{ \frac{5-1}{2}* \frac{1-1}{2}} = 1 \Rightarrow (\frac{5}{11}) = (\frac{1}{5})$$
7. Now I evaluate $(\frac{5}{11})$ as $(\frac{1}{5}) = 1$
8. Evaluating: $(\frac{2}{11}) = (-1)^{ \frac{11^2 - 1}{8}} = (-1)^{ \frac{120}{8}} = (-1)^{15} = (-1)$
9. Now I can evaluate the Legandre symbol $(\frac{11}{43})$:
$$ (\frac{11}{43}) \Leftrightarrow -(\frac{10}{11}) = (-1)*(\frac{5}{11})*(\frac{2}{11}) = (-1)*1*(-1) = 1 $$

Which means: $ \exists x\ s.t.\ x^2 \equiv  11 \mod 43$
