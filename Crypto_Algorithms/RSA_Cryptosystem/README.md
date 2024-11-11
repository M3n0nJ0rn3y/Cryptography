# The RSA Cryptosystem. 
*Explained and implemented by me.*

### Phase 1: Public Key Generation.
The application of the algorithm begins by calculating your RSA Public Key that the receiver of your message will use to "Unlock" your message.
The security of RSA lies within the complexity of factoring large prime numbers, therefore it is important to choose prime that is large enough.


1. Use an algorithm to calculate two large prime numbers p and q.
2. Use these large primes to calculate N which will be a part of your Public Key (PB). N will also work as our modulos 
to make encryption and decryption possible. 
3. Use Eulers Totient function (Which I will referee to as function $fi(x)$). Where $fi(N) = (p-1)(q-1)$.
In the next step we will find an integer $e$ such that $GCD(e, fi(N)) == 1$ & $1 < e < fi(N)$. 
Thanks to this structure we ensure that $fi(N)$ does not divide $e$ and therefore $e$ has an inverse in $fi(N)$, so when we encrypt our message $M$ with $e$ we will be able to decrypt it with the use of $e^{-1}$.
4. Pick an integer $e\ s.t. 1 < e < fi(N)$ & $GCD(e, fi(N)) == 1$.
5. Calculate the inverse of $d \equiv e^{-1} (mod\ fi(N))$. ($d$ is the Private Key that should be kept secret.)

Now we have calculated both the Public Key and the Private Key.\
$K_{Pub} = (N, e)$, $K_{Priv} = (N, d)$\
If anyone wants to send you an encrypted message they simply use your public key, and thanks to the mathematical correlation between $e$ & $d$ you will be able to decrypt the message.


### Phase 2: The Encryption
Each message that is sent is converted to binary strings and represented as a number. (This is to apply the modular arithmetic as an encryption mechanic.)
Therefor the message M will represent an integer.

Ciphertext calculation happens as follows:\
$C \equiv M^{e}\ (\textrm{mod}\ N)$ 

$C$ can safely be sent to you through an unsecure channel.

### Phase 3: The Decryption
When you receive the ciphertext $C$ you will use the following formula to remove the encryption from $M$:\
$M \equiv C^{d}\ (\textrm{mod}\ N)$\
and you can convert the message back to the original ASCII representation. (Normal language)

**Why you are able to decrypt $C$ with $d$ is explained below:**\
$Since\ d\ \equiv e^{-1}\ (\textrm{mod}\ fi(N))$ & $C \equiv M^{e}\ (\textrm{mod}\ N),$\
$then\ C^{d} \equiv M^{-e\ *\ e}\ (\textrm{mod}\ N)\ \equiv M\ (\textrm{mod}\ N)$ 



