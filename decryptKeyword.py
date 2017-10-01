# Decryption method using the Keyword scheme
# Michael Kirby
# 9/16/17

import sys
from string import ascii_uppercase

if (len(sys.argv) < 3):
    sys.exit("Too few arguments. python <script> <text.txt> <keyword>")
elif (len(sys.argv) > 3):
    sys.exit("Too many arguments. python <script> <text.txt> <keyword>")

textfile = open(sys.argv[1], 'r')
keyword = sys.argv[2]
#print type(keyword), keyword

ciphertext = textfile.read()
textfile.close()

def removeDuplicates(keyword):
    seen = set()
    unique = []
    for item in keyword:
        if item not in seen:
            seen.add(item)
            unique.append(item)

    return "".join(unique)

invalid_chars = ' \n,./<>?;:\'"[]{}\|-=_+!@#$%^&*()1234567890'
ciphertext = ciphertext.translate(None, invalid_chars)  #remove invalid characters from string
ciphertext = ciphertext.upper()   #convert all letters to uppercase
keyword = keyword.translate(None, invalid_chars)
keyword = keyword.upper()
keyword = removeDuplicates(keyword)
#print "Keyword:", keyword
print ciphertext

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

letters = [ascii_uppercase[c] for c in xrange(26)]
encryption_list = createEncryptionList(keyword)
#print encryption_list, len(encryption_list)

plaintext = map(lambda x: letters[encryption_list.index(x)], ciphertext)
#print plaintext
plaintext = "".join(plaintext)
print plaintext

#open a new file and write encrypted messsage to file
publicfile = open('publicmsg.txt', 'w')
publicfile.write(plaintext)
publicfile.close()
