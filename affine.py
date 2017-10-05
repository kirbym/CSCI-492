# Encryption and Decryption methods using the Affine shift scheme
# Michael Kirby
# 10/4/17

import sys
import fractions

def verifyAlpha(a):
    if(fractions.gcd(a, 26) == 1):
        return True
    else:
        return False

def findMultInverse(a):
    for i in xrange(26):
        if((a * i) % 26 == 1):
            return i

def encrypt(plaintext, alpha, beta):
    if verifyAlpha(alpha):  #check that alpha is relatively prime to 26 (gcd(alpha, 26) = 1)
        invalid_chars = ' \n,./<>?;:\'"[]{}\|-=_+!@#$%^&*()1234567890'
        plaintext = plaintext.translate(None, invalid_chars)  #remove invalid characters from string
        plaintext = plaintext.upper()   #convert all letters to uppercase
        #print plaintext
        plaintext = map(lambda x: ord(x) - ord('A'), plaintext)  #convert plaintext into ASCII values, then to mod 26 by subtracting 'A' value
        #print plaintext
        ciphertext = map(lambda x: (alpha*x + beta) % 26, plaintext)  #convert plaintext into ciphertext by applying algorithm to map numbers
        #print ciphertext
        ciphertext = map(lambda x: chr(x + ord('A')), ciphertext)  #convert new numbers to respective characters
        #print ciphertext
        ciphertext = "".join(ciphertext)  #join all letters from ciphertext list into one string
        #print ciphertext
        return ciphertext
    else:
        sys.exit("Error: Invalid alpha value. Alpha must be relatively prime to 26.")


def decrypt(ciphertext, alpha, beta):
    if verifyAlpha(alpha):  #check that alpha is relatively prime to 26 (gcd(alpha, 26) = 1)
        mult_inverse = findMultInverse(alpha)  #find multiplicative inverse in mod 26 for decryption (division doesn't exist in modular arithmatic)
        invalid_chars = ' \n,./<>?;:\'"[]{}\|-=_+!@#$%^&*()1234567890'
        ciphertext = ciphertext.translate(None, invalid_chars)  #remove invalid characters from string
        ciphertext = ciphertext.upper()   #convert all letters to uppercase
        #print ciphertext
        ciphertext = map(lambda x: ord(x) - ord('A'), ciphertext)  #convert ciphertext into ASCII values, then to mod 26 by subtracting 'A' value
        #print ciphertext
        plaintext = map(lambda x: (mult_inverse*(x - beta)) % 26, ciphertext)  #convert ciphertext into plaintext by applying algorithm to map numbers
        #print plaintext
        plaintext = map(lambda x: chr(x + ord('A')), plaintext)  #convert new numbers to respective characters
        #print plaintext
        plaintext = "".join(plaintext)  #join all letters from plaintext list into one string
        #print plaintext
        return plaintext
    else:
        sys.exit("Error: Invalid alpha value. Alpha must be relatively prime to 26.")


if __name__ == "__main__":

    if (len(sys.argv) < 5):
        sys.exit("Too few arguments. Use \"-h\" command for help.\npython affine.py -h <text.txt> <alpha> <beta>")
    elif (len(sys.argv) > 5):
        sys.exit("Too many arguments. Use \"-h\" command for help.\npython affine.py -h <text.txt> <alpha> <beta>")

    command = sys.argv[1]

    if command == "-e":
        textfile = open(sys.argv[2], 'r')
        alpha = int(sys.argv[3]) % 26
        beta = int(sys.argv[4]) % 26
        input_text = textfile.read()
        textfile.close()

        plaintext = input_text
        ciphertext = encrypt(plaintext, alpha, beta)

        #open a new file and write encrypted messsage to file
        secretfile = open('secretmsg.txt', 'w')
        secretfile.write(ciphertext)
        secretfile.close()
    elif command == "-d":
        textfile = open(sys.argv[2], 'r')
        alpha = int(sys.argv[3]) % 26
        beta = int(sys.argv[4]) % 26
        input_text = textfile.read()
        textfile.close()

        ciphertext = input_text
        plaintext = decrypt(ciphertext, alpha, beta)

        #open a new file and write decrypted messsage to file
        publicfile = open('publicmsg.txt', 'w')
        publicfile.write(plaintext)
        publicfile.close()
    elif command == "-h":
        print "This program uses the Affine cipher to encrypt or decrypt a given\ntext file with a given multiplicative value and shift value.\n"
        print "usage: python affine.py <command> <text.txt> <alpha> <beta>\n"
        print "Command Options:"
        print "\t\"-h\" : Display command options and the order of arguments."
        print "\t\"-e\" : Encrypt the given text file with the given values."
        print "\t\"-d\" : Decrypt the given text file with the given values."
        sys.exit()
    else:
        print "Use \"-h\" command for help."
        print "python affine.py -h <text.txt> <alpha> <beta>"
