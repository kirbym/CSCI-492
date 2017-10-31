# Exploring the RSA algorithm
# Michael Kirby
# 10/29/17

#input string (as numbers) must be less than n?
#if input is relatively prime to n, msg gets encrypted to itself?

import sys
import fractions

def checkPrimality(num):
    isPrime = True
    if num % 2 == 0:
        return False
    else:
        for i in xrange(3, num, 2):
            if i*i <= num:
                if num % i == 0:
                    isPrime = False
                    break

        return isPrime

def encrypt(n, e, m):    #step 5
    return pow(m, e) % n

def decrypt(n, d, c):    #step 6
    return pow(c, d) % n

if __name__ == "__main__":
    #textfile = open(sys.argv[1], 'r')
    #text = textfile.read()
    #textfile.close()
    m = int(sys.argv[1])
    p = int(sys.argv[2])
    q = int(sys.argv[3])

    if checkPrimality(p) and checkPrimality(q):
        n = p*q  #step 1

        pq = (p-1)*(q-1)
        x = pq + 2*p - 2*q
        e = None
        while e is None:
            x += 1
            if fractions.gcd(x, pq) == 1:
                e = x        #step 2

        d = None
        y = pq + 2*q - 2*p
        while d is None:
            y += 1
            #print "y:", y, "ye:", y*e, "ye mod pq:", (y*e) % pq
            if (y*e) % pq == 1:
                d = y     #step 3


        c = encrypt(n, e, m)
        z = decrypt(n, d, c)
        print "input:", m
        print "p:", p
        print "q:", q
        print "n:", n
        print "pq:", pq
        print "e:", e
        print "d:", d
        print "encrypted:", c
        print "decrypted:", z
