# Exploring the RSA algorithm
# Michael Kirby
# 10/29/17

#input string (as numbers) must be less than n? yes, otherwise must chunk msg
#if input is relatively prime to n, msg gets encrypted to itself?

import sys
import fractions

def isPrime(num):   #checking if a number is prime
    valid = True
    if num <= 1:
        return False
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, num, 2):
            if i*i <= num:
                if num % i == 0:
                    valid = False
                    break

        return valid

def encrypt(n, e, m):    #step 5
    return pow(m, e) % n

def decrypt(n, d, c):    #step 6
    return pow(c, d) % n

if __name__ == "__main__":
    # get input values
    m = int(sys.argv[1])  #message entered as number
    p = int(sys.argv[2])  #prime #1  =/= q
    q = int(sys.argv[3])  #prime #2  =/= p

    if p == q:
        sys.exit("Must enter two distinct prime numbers")
    else:
        if not isPrime(p) or not isPrime(q):
            print "One or both of the numbers are not prime"
            if not isPrime(p):
                print "%d is not prime" % (p)
            if not isPrime(q):
                print "%d is not prime" % (q)
            sys.exit(1)
        else:
            n = p*q  #step 1
            if m > n:
                print "Message is too large, must be less than %d*%d = %d" % (p, q, n)
                sys.exit(1)
            else:
                prod = (p-1)*(q-1)
                x = prod + 2*p + 2*q    #starting value when searching for 'e'
                e = None            #encryption exponent
                while e is None:
                    x += 1
                    if fractions.gcd(x, prod) == 1:     #'e' and (p-1)(q-1) must be relatively prime
                        e = x        #step 2

                y = prod + 2*p + 2*q   #starting value when searching for 'd'
                d = None     #decryption exponent
                while d is None:
                    y += 1
                    if (y*e) % prod == 1:       #'de' congruent to 1 mod (p-1)(q-1)
                        d = y     #step 3


                c = encrypt(n, e, m)
                z = decrypt(n, d, c)
                print "input:", m
                print "p:", p
                print "q:", q
                print "n:", n
                print "(p-1)(q-1):", prod
                print "e:", e
                print "d:", d
                print "encrypted:", c
                print "decrypted:", z
