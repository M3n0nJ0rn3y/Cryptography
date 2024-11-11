## Diffie Hellman Key Exchange Methods:

The Diffie-Hellman Algorithms helps establish a symmetric key over an insecure network, without the need of encrypting the communication before the exchange.
The algorithm can be divided into two parts: **The Setup**, and the **Key Exchange**. Which happens in the following procedure:

### The Setup:
One of the parts should establish the finite group ($&integers;$) that they will be using for the key establishment. In order to ''establish'' the group,
one will pick a large prime $p$ and a generator of the field $g$ such that:
$$
\sum_{i=1}^{p-1} g^i\ iterates\ through\ the\ set\ &integers;_p\
$$

Publish: $(p, g)$

### The Key Exchange process:
| Alice                                                            |                                                             Bob | 
|:-----------------------------------------------------------------|----------------------------------------------------------------:|
| $Pick\ a\in &integers;^{*}_{p}\ s.t.\ a\not\equiv \pm 1 \mod p $ | $Pick\ b\in &integers;^{*}_{p}\ s.t.\ b\not\equiv \pm 1 \mod p$ |
| $Calculate:A \equiv g^a \mod p$                                  |                                $Calculate: B \equiv g^b \mod p$ |
| $Send: A \to Bob$                                                |                                              $Send:B \to Alice$ |
| $Calculate: K \equiv B^a\mod p \equiv g^{ba} \mod p $            |           $Calculate: K \equiv A^b \mod p \equiv g^{ab} \mod p$ |

Now Bob and Alice can use the Symmetric key in a Symmetric key algorithm in order to exchange information safely over unsafe channel. 