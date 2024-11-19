# El'Gamal Digital Signature Algorithm.
### Parameter Calculation:
1. Choose a prime $p$. (This will provide the main security against brute-force attacks)
2. Select a generator $g$ such that $g$ generates the whole residue class $&integers;^{*}_{p}$.
3. Pick an $x\ s.t.\ 1 < x < p-1$.
4. Compute the public key $K_{pub} \equiv g^{x} \mod p$
5. Publish the parameters: $(p,g,K_{pub})$


### Digital signing process:
1. Calculate $m_{hashed} \equiv H(m)$, where $H()$ is a cryptographic hash function that outputs an integer lesser than $p$.
2. Pick a random $k\ s.t.\ 1 < k < p-1 $ that is relatively co-prime to $p$. Which means $gcd(k,p-1)=1$, which means $\exists k^{-1} \in &integers;^{*}_{p}$
3. Compute $r_{verifier} \equiv g^k \mod p$
4. Compute: $k^{-1} \mod p\ s.t.\ k*k^{-1} \equiv 1 \mod (p-1)$
5. Compute: $ s_{ignature} \equiv k^{-1}(m_{hashed} - x* r_{verifier}) \mod (p-1) \equiv k^{-1}*(m_{hashed} - x * g^{k})$
6. The signed document is represented by: $D = (m_{hashed},r_{verifier},s_{ignature})$

### Checking the signature:
Using the available parameters: $(p,g,K_{pub})$ are the published parameters, and $D=(m_{hashed}, r_{verifier}, s_{ignature})$ is the document sent to be verified.

In order to verify the signed document one performes a check and only accepts the document if the equation is correct:
$$ g^{m_{hashed}} \equiv K_{pub}^{r_{verifier}}*r_{verifier}^{s_{ignature}} \mod p \Rightarrow The\ signature\ is\ valid.$$

****

### Mathematical reasoning of Elgamal DS Algorithm:
If the signature is shown to be correct, that would mean: 
$$ K_{pub}^{r_{verifier}} * r_{verifier}^{s_{ignature}} \equiv (g^{x})^{r_{verifier}}*(g^k)^{s_{ignature}} \mod p \equiv (g^{x})^{g^{k}} * (g^{k})^{k^{-1} *(m_{hashed} -x*r_{verifier})} \mod p$$\
$$ g^{x*g^{k}} * g^{m_{hashed} - x*r_{verifier}} \mod p \equiv g^{x*g^{k} * m_{hashed} -x* g^{k}} \mod p \equiv g^{m_{hashed}} \mod p$$


****

### Attacks against ElGamal DSA.
**Finding $k$, will grant you a linear congruence to the other parameters.**
$$ x*r_{verifier} \equiv m-k*s_{ignature} \mod p-1 \Leftrightarrow x * g^k \equiv m-(k^{-1}*(m-x*g^k)) \mod p-1$$
Although knowing $(m,r_{verifier}, s_{ignature})$ leaves you with: $gcd(a,p-1)=l$ different variants for calculating the private key:
$$ x_1 \equiv x \mod (\frac{p-1}{l}) $$

**Knowing this we can consider the attack applied in case the same $k$ are used for different messages $m_1$ and $m_2$.**\
If the same $k$ is used twice, that will also generate similar $r_{verifier}$ since, $r_{verifier} \equiv g^k \mod p$.\
Therefore: From $k_1=k_2=k \Rightarrow r_{verifier_{1}}=r_{verifier_{2}}=r_{verifier}$ 

This creates a system of two linear congruences:
$$ x*r_{verifier_{1}} \equiv m_1 -k*s_{ignature_{1}} \mod p-1$$
$$ x*r_{verifier_{2}} \equiv m_2 -k*s_{ignature_{2}} \mod p-1$$

Which gives us the following congruence: 
$$ k*(s_{ignature_{1}} - s_{ignature_{2}}) \equiv m_1 - m_2 \mod p-1 $$

Solving this equation yields several different solutions. The correct one is found by testing all of them with:
$$r_{verifier} \equiv g^k \mod p$$

After finding $k$ it should be trivial to use one of the above equations to calculate $x$.



