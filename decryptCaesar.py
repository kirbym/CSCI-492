# Decryption method using the Caesar shift scheme
# Michael Kirby
# 9/16/17

import sys

if (len(sys.argv) < 3):
    sys.exit("Too few arguments. python <script> <text.txt> <offset>")
elif (len(sys.argv) > 3):
    sys.exit("Too many arguments. python <script> <text.txt> <offset>")

textfile = open(sys.argv[1], 'r')
offset = int(sys.argv[2]) % 26
#print type(offest)

ciphertext = textfile.read()
textfile.close()
#print ciphertext
invalid_chars = ' \n,./<>?;:\'"[]{}\|-=_+!@#$%^&*()1234567890'
ciphertext = ciphertext.translate(None, invalid_chars)  #remove invalid characters from string
ciphertext = ciphertext.upper()   #convert all letters to uppercase
print ciphertext
ciphertext = map(lambda x: ord(x) - ord('A'), ciphertext)  #convert ciphertext into ASCII values, then to mod 26 by subtracting 'A' value
#print ciphertext
plaintext = map(lambda x: (x - offset) % 26, ciphertext)  #convert ciphertext into plaintext by applying offset
#print plaintext
plaintext = map(lambda x: chr(x + ord('A')), plaintext)  #convert new numbers to respective characters
#print plaintext
plaintext = "".join(plaintext)  #join all letters from plaintext list into one string
print plaintext

#open a new file and write decrypted messsage to file
publicfile = open('publicmsg.txt', 'w')
publicfile.write(plaintext)
publicfile.close()
