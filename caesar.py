# Encryption and Decryption methods using the Caesar shift scheme
# Michael Kirby
# 9/15/17

import sys

def encrypt(plaintext, offset):
    invalid_chars = ' \n,./<>?;:\'"[]{}\|-=_+!@#$%^&*()1234567890'
    plaintext = plaintext.translate(None, invalid_chars)  #remove invalid characters from string
    plaintext = plaintext.upper()   #convert all letters to uppercase
    #print plaintext
    plaintext = map(lambda x: ord(x) - ord('A'), plaintext)   #convert plaintext into ASCII values, then to mod 26 by subtracting 'A' value
    #print plaintext
    ciphertext = map(lambda x: (x + offset) % 26, plaintext)  #convert plaintext into ciphertext by applying offset
    #print ciphertext
    ciphertext = map(lambda x: chr(x + ord('A')), ciphertext)  #convert new numbers to respective characters
    #print ciphertext
    ciphertext = "".join(ciphertext)  #join all letters from ciphertext list into one string
    #print ciphertext
    return ciphertext

def decrypt(ciphertext, offset):
    invalid_chars = ' \n,./<>?;:\'"[]{}\|-=_+!@#$%^&*()1234567890'
    ciphertext = ciphertext.translate(None, invalid_chars)  #remove invalid characters from string
    ciphertext = ciphertext.upper()   #convert all letters to uppercase
    #print ciphertext
    ciphertext = map(lambda x: ord(x) - ord('A'), ciphertext)  #convert ciphertext into ASCII values, then to mod 26 by subtracting 'A' value
    #print ciphertext
    plaintext = map(lambda x: (x - offset) % 26, ciphertext)  #convert ciphertext into plaintext by applying offset
    #print plaintext
    plaintext = map(lambda x: chr(x + ord('A')), plaintext)  #convert new numbers to respective characters
    #print plaintext
    plaintext = "".join(plaintext)  #join all letters from plaintext list into one string
    #print plaintext
    return plaintext

if __name__ == "__main__":

    if (len(sys.argv) < 4):
        sys.exit("Too few arguments. Use \"-h\" command for help.\npython caesar.py -h <text.txt> <offset>")
    elif (len(sys.argv) > 4):
        sys.exit("Too many arguments. Use \"-h\" command for help.\npython caesar.py -h <text.txt> <offset>")

    command = sys.argv[1]

    if command == "-e":
        textfile = open(sys.argv[2], 'r')
        offset = int(sys.argv[3]) % 2
        input_text = textfile.read()
        textfile.close()

        plaintext = input_text
        ciphertext = encrypt(plaintext, offset)

        #open a new file and write encrypted messsage to file
        secretfile = open('secretmsg.txt', 'w')
        secretfile.write(ciphertext)
        secretfile.close()
    elif command == "-d":
        textfile = open(sys.argv[2], 'r')
        offset = int(sys.argv[3]) % 2
        input_text = textfile.read()
        textfile.close()

        ciphertext = input_text
        plaintext = decrypt(ciphertext, offset)

        #open a new file and write encrypted messsage to file
        publicfile = open('publicmsg.txt', 'w')
        publicfile.write(plaintext)
        publicfile.close()
    elif command == "-h":
        print "This program uses the Caesar cipher to encrypt or decrypt a given text file with a given offset value.\n"
        print "usage: python caesar.py <command> <text.txt> <offset>\n"
        print "Command Options:"
        print "\t\"-h\" : Display command options and the order of arguments."
        print "\t\"-e\" : Encrypt the given text file with the offset value."
        print "\t\"-d\" : Decrypt the given text file with the offset value."
        sys.exit()
    else:
        print "Use \"-h\" command for help."
        print "python caesar.py -h <text.txt> <offset>"
