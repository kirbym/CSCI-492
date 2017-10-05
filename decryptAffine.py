#Decryption method using the Affine scheme
#Michael Kirby
#9/16/17

import sys
import fractions

if (len(sys.argv) < 4):
    sys.exit("Too few arguments. python <script> <text.txt> <alpha> <beta>")
elif (len(sys.argv) > 4):
    sys.exit("Too many arguments. python <script> <text.txt> <alpha> <beta>")

textfile = open(sys.argv[1], 'r')
alpha = int(sys.argv[2]) % 26
beta = int(sys.argv[3]) % 26

ciphertext = textfile.read()
textfile.close()

def verifyAlpha(alpha):
    if(fractions.gcd(alpha, 26) == 1):
        return alpha
    else:
        sys.exit("Error: Invalid alpha value. Alpha must be relatively prime to 26.")

def findMultInverse(a):
    for i in xrange(26):
        if((a * i) % 26 == 1):
            return i

alpha = verifyAlpha(alpha)  #check that alpha is relatively prime to 26 (gcd(alpha, 26) = 1)
mult_inverse = findMultInverse(alpha)  #find multiplicative inverse in mod 26 for decryption (division doesn't exist in modular arithmatic)
#print alpha, mult_inverse

invalid_chars = ' \n,./<>?;:\'"[]{}\|-=_+!@#$%^&*()1234567890'
ciphertext = ciphertext.translate(None, invalid_chars)  #remove invalid characters from string
ciphertext = ciphertext.upper()   #convert all letters to uppercase
print ciphertext
ciphertext = map(lambda x: ord(x) - ord('A'), ciphertext)  #convert ciphertext into ASCII values, then to mod 26 by subtracting 'A' value
#print ciphertext
plaintext = map(lambda x: (mult_inverse*(x - beta)) % 26, ciphertext)  #convert ciphertext into plaintext by applying algorithm to map numbers
#print plaintext
plaintext = map(lambda x: chr(x + ord('A')), plaintext)  #convert new numbers to respective characters
#print plaintext
plaintext = "".join(plaintext)  #join all letters from plaintext list into one string
print plaintext

#open a new file and write decrypted messsage to file
publicfile = open('publicmsg.txt', 'w')
publicfile.write(plaintext)
publicfile.close()
