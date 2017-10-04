# Encryption method using the Caesar shift scheme
# Michael Kirby
# 9/15/17

import sys
#from string import ascii_uppercase


#print type(offset)


#print plaintext
def caesarEncrypt(plaintext, offset):
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

if __name__ == "__main__":
  # This is being run on its own
  if (len(sys.argv) < 3):
      sys.exit("Too few arguments. python <script> <text.txt> <offset>")
  elif (len(sys.argv) > 3):
      sys.exit("Too many arguments. python <script> <text.txt> <offset>")

  textfile = open(sys.argv[1], 'r')
  offset = int(sys.argv[2]) % 26
  
  plaintext = textfile.read()
  textfile.close()
  
  ciphertext = caesarEncrypt(plaintext, offset)
  #open a new file and write encrypted messsage to file
  secretfile = open('secretmsg.txt', 'w')
  secretfile.write(ciphertext)
  secretfile.close()
