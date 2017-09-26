#Encryption method using the Affine scheme
#Michael Kirby
#9/16/17

import sys
import fractions

textfile = open(sys.argv[1], 'r')
alpha = int(sys.argv[2]) % 26
beta = int(sys.argv[3]) % 26

def verifyAlpha(alpha):
    if(fractions.gcd(alpha, 26) == 1):
        return alpha
    else:
        sys.exit("Error: Invalid alpha value. Alpha must be relatively prime to 26.")

plaintext = textfile.read()
textfile.close()

alpha = verifyAlpha(alpha)  #check that alpha is relatively prime to 26 (gcd(alpha, 26) = 1)

invalid_chars = ' \n,./<>?;:\'"[]{}\|-=_+!@#$%^&*()1234567890'
plaintext = plaintext.translate(None, invalid_chars)  #remove invalid characters from string
plaintext = plaintext.upper()   #convert all letters to uppercase
print plaintext
plaintext = map(lambda x: ord(x) - ord('A'), plaintext)  #convert plaintext into ASCII values, then to mod 26 by subtracting 'A' value
#print plaintext
ciphertext = map(lambda x: (alpha*x + beta) % 26, plaintext)  #convert plaintext into ciphertext by applying algorithm to map numbers
#print ciphertext
ciphertext = map(lambda x: chr(x + ord('A')), ciphertext)  #convert new numbers to respective characters
#print ciphertext
ciphertext = "".join(ciphertext)  #join all letters from ciphertext list into one string
print ciphertext

#open a new file and write encrypted messsage to file
secretfile = open('secretmsg.txt', 'w')
secretfile.write(ciphertext)
secretfile.close()
