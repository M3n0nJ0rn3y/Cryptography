# El'Gamals Encryption System.
ElGamals encryption system is very similar to the known Diffie Hellman Key Exchange algorithm. In fact it emplyees a very similar method for establishing encryption and decryption keys through sending the keys as plaintext through an insecure network. 
The algorithm can be divided into three sub-parts: **Key Generation and Exchange**, **The Encryption** and **The Decryption**. 
In order to keep it intuitive and understandable I will refer to the _Receiver_ and the _Sender_ as Bob and Alice respectively.
## The Key Generation and Exchange:
1. **Establishing the group:**\
One of the parts establishes the finite group ($&integers;$) that they will be using for the key establishment. In order to ''establish'' the group,
one will pick a large prime $p$ and a generator of the field $g$ such that:
$$
\sum_{i=1}^{p-1} g^i\ iterates\ through\ the\ set\ &integers;_p\
$$

2. **Bob _(The Receiver)_:**
   1. Picks a secret integer $d\ \in &integers;^{*}_{p},\ s.t.\ d\not\equiv \pm1 \mod p $.
   2. Uses $d$ to Calculate: $\beta \equiv g^d$.
   3. Sends: $\beta \to Alice$

## The Encryption:

**Alice _(The Sender)_:**
   1. Receives: $\beta \to Alice$
   2. Picks: $i \in &integers;^{*}_{p},\ s.t. i \not\equiv \pm 1 \mod p$
   3. Calculates the **Ephemeral Key**: $K_{e} \equiv g^{i} \mod p$
      1. (_**Ephemeral** is from greek, meaning: ''Lasting for a very short duration''. Which is interesting because the Ephemeral Key in ElGamal cryptosystem is ment to be calculated for each new conversation._):
   4. Uses $\beta$ to calculate the **Masking Key**: $K_{m} \equiv \beta^{i} \mod p \equiv g^{d*i} \mod p$
   5. Computes the ciphertext C by calculating: $C\equiv M*K_{m} \mod p$
   6. Sends the pair: $(K_{e}, C) \to Bob$


## The Decryption:
**Bob:**
1. Receives: $(K_{e}, C) \to Bob$
2. Computes the **Masking Key**: $K_m \equiv (K_{e})^d \mod p \equiv (g^i)^d \mod p \equiv g^{i*d} \mod p$
3. Calculates: $K_{m}^{-1} \mod p$
3. Decrypt the message by calculating: $M \equiv C*K_{m}^{-1} \mod p$