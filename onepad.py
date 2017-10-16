# Encryption and Decryption methods using the One-Time Pad scheme
# Michael Kirby
# 10/15/17

import sys

def encrypt(ptext, key):
    invalid_chars = ' \n,./<>?;:\'"[]{}\|-=_+!@#$%^&*()1234567890'
    ptext = ptext.translate(None, invalid_chars)  #remove invalid characters from string
    ptext = ptext.upper()
    key = key.translate(None, invalid_chars)
    key = key.upper()

    ptext = map(lambda x: ord(x) - ord('A'), ptext)
    key = map(lambda x: ord(x) - ord('A'), key)

    n = 0
    ctext = []
    while n < len(ptext):
        ctext.append((ptext[n] + key[n % len(key)]) % 26)
        n += 1

    ctext = map(lambda x: chr(x + ord('A')), ctext)
    ctext = "".join(ctext)

    #print "plaintext", ptext
    #print "key", key
    #print "ciphertext", ctext

    return ctext

def decrypt(ctext, key):
    invalid_chars = ' \n,./<>?;:\'"[]{}\|-=_+!@#$%^&*()1234567890'
    ctext = ctext.translate(None, invalid_chars)  #remove invalid characters from string
    ctext = ctext.upper()
    key = key.translate(None, invalid_chars)
    key = key.upper()

    ctext = map(lambda x: ord(x) - ord('A'), ctext)
    key = map(lambda x: ord(x) - ord('A'), key)

    n = 0
    ptext = []
    while n < len(ctext):
        ptext.append((ctext[n] - key[n % len(key)]) % 26)
        n += 1

    ptext = map(lambda x: chr(x + ord('A')), ptext)
    ptext = "".join(ptext)

    #print "ciphertext", ctext
    #print "key", key
    #print "plaintext", ptext

    return ptext


if __name__ == "__main__":
    textfile = open(sys.argv[1], 'r')
    keyfile = open(sys.argv[2], 'r')
    text = textfile.read()
    key = keyfile.read()
    textfile.close()
    keyfile.close()

    ciphertext = encrypt(text, key)
    print "ciphertext", ciphertext
    plaintext = decrypt(ciphertext, key)
    print "plaintext", plaintext
