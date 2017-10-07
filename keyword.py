# Encryption and Decryption methods using the Keyword scheme
# Michael Kirby
# 9/16/17

import sys
from string import ascii_uppercase

def removeDuplicates(keyword):
    seen = set()
    unique = []
    for item in keyword:
        if item not in seen:
            seen.add(item)
            unique.append(item)

    return "".join(unique)

def createEncryptionList(keyword):
    bad = []
    letters = [ascii_uppercase[c] for c in xrange(26)]
    for l in letters:
        if l in keyword:
            bad.append(l)

    for b in bad:
        letters.remove(b)

    keyword_l = [keyword[k] for k in xrange(len(keyword))]
    encryption_l = keyword_l + letters
    return encryption_l

def encrypt(plaintext, keyword):
    invalid_chars = ' \n,./<>?;:\'"[]{}\|-=_+!@#$%^&*()1234567890'
    plaintext = plaintext.translate(None, invalid_chars)  #remove invalid characters from string
    plaintext = plaintext.upper()   #convert all letters to uppercase
    keyword = keyword.translate(None, invalid_chars)
    keyword = keyword.upper()
    keyword = removeDuplicates(keyword)
    #print "keyword:", keyword
    #print plaintext

    encryption_list = createEncryptionList(keyword)

    plaintext = map(lambda x: ord(x) - ord('A'), plaintext)
    #print plaintext
    ciphertext = map(lambda x: encryption_list[x], plaintext)
    #print ciphertext
    ciphertext = "".join(ciphertext)
    #print ciphertext
    return ciphertext


def decrypt(ciphertext, keyword):
    invalid_chars = ' \n,./<>?;:\'"[]{}\|-=_+!@#$%^&*()1234567890'
    ciphertext = ciphertext.translate(None, invalid_chars)  #remove invalid characters from string
    ciphertext = ciphertext.upper()   #convert all letters to uppercase
    keyword = keyword.translate(None, invalid_chars)
    keyword = keyword.upper()
    keyword = removeDuplicates(keyword)
    #print "keyword:", keyword
    #print ciphertext

    letters = [ascii_uppercase[c] for c in xrange(26)]
    encryption_list = createEncryptionList(keyword)

    plaintext = map(lambda x: letters[encryption_list.index(x)], ciphertext)
    #print plaintext
    plaintext = "".join(plaintext)
    #print plaintext
    return plaintext



if __name__ == "__main__":

    if (len(sys.argv) < 4):
        sys.exit("Too few arguments. Use \"-h\" command for help.\npython keyword.py -h <text.txt> <keyword>")
    elif (len(sys.argv) > 4):
        sys.exit("Too many arguments. Use \"-h\" command for help.\npython keyword.py -h <text.txt> <keyword>")

    command = sys.argv[1]

    if command == "-e":
        textfile = open(sys.argv[2], 'r')
        keyword = sys.argv[3]
        input_text = textfile.read()
        textfile.close()

        plaintext = input_text
        ciphertext = encrypt(plaintext, keyword)

        #open a new file and write encrypted messsage to file
        secretfile = open('secretmsg.txt', 'w')
        secretfile.write(ciphertext)
        secretfile.close()
    elif command == "-d":
        textfile = open(sys.argv[2], 'r')
        keyword = sys.argv[3]
        input_text = textfile.read()
        textfile.close()

        ciphertext = input_text
        plaintext = decrypt(ciphertext, keyword)

        #open a new file and write encrypted messsage to file
        publicfile = open('publicmsg.txt', 'w')
        publicfile.write(plaintext)
        publicfile.close()
    elif command == "-h":
        print "This program uses the Keyword cipher to encrypt or decrypt a given text file with a given keyword.\n"
        print "usage: python keyword.py <command> <text.txt> <keyword>\n"
        print "Command Options:"
        print "\t\"-h\" : Display command options and the order of arguments."
        print "\t\"-e\" : Encrypt the given text file with the keyword."
        print "\t\"-d\" : Decrypt the given text file using the keyword."
        sys.exit()
    else:
        print "Use \"-h\" command for help."
        print "python keyword.py -h <text.txt> <keyword>"
