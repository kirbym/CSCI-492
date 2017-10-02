# Brute force method to break Caesar cipher by using frequence analysis of letters and digrams
# Michael Kirby
# 10/1/17

# Monogram and digram frequencies given by the following website
# http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/

monogram_freq = {
"A" :  8.55,        "K" :  0.81,        "U" :  2.68,
"B" :  1.60,        "L" :  4.21,        "V" :  1.06,
"C" :  3.16,        "M" :  2.53,        "W" :  1.83,
"D" :  3.87,        "N" :  7.17,        "X" :  0.19,
"E" : 12.10,        "O" :  7.47,        "Y" :  1.72,
"F" :  2.18,        "P" :  2.07,        "Z" :  0.11,
"G" :  2.09,        "Q" :  0.10,
"H" :  4.96,        "R" :  6.33,
"I" :  7.33,        "S" :  6.73,
"J" :  0.22,        "T" :  8.94}  #values are in percents

digram_freq = {
"TH" :  2.71,        "EN" :  1.13,        "NG" :  0.89,
"HE" :  2.33,        "AT" :  1.12,        "AL" :  0.88,
"IN" :  2.03,        "ED" :  1.08,        "IT" :  0.88,
"ER" :  1.78,        "ND" :  1.07,        "AS" :  0.87,
"AN" :  1.61,        "TO" :  1.07,        "IS" :  0.86,
"RE" :  1.41,        "OR" :  1.06,        "HA" :  0.83,
"ES" :  1.32,        "EA" :  1.00,        "ET" :  0.76,
"ON" :  1.32,        "TI" :  0.99,        "SE" :  0.73,
"ST" :  1.25,        "AR" :  0.98,        "OU" :  0.72,
"NT" :  1.17,        "TE" :  0.98,        "OF" :  0.71}  #top 30 digrams, values are in percents

for key in monogram_freq.keys():
    monogram_freq[key] = round(monogram_freq[key] / 100, 5)
#print monogram_freq
for key in digram_freq.keys():
    digram_freq[key] = round(digram_freq[key] / 100, 5)

import sys

if (len(sys.argv) < 2):
    sys.exit("Too few arguments. python <script> <text.txt>")
elif (len(sys.argv) > 2):
    sys.exit("Too many arguments. python <script> <text.txt>")

textfile = open(sys.argv[1], 'r')
text = textfile.read()
textfile.close()

invalid_chars = ' \n,./<>?;:\'"`[]{}\|-=_+!@#$%^&*()1234567890'
text = text.translate(None, invalid_chars)
text = text.upper()

letter_count = {}
for i in xrange(len(text)):
    if text[i] in letter_count.keys():
        letter_count[text[i]] += 1
    elif text[i] not in letter_count.keys():
        letter_count[text[i]] = 1

letter_freq = {}
for key in letter_count.keys():
    letter_freq[key] = round(float(letter_count[key]) / len(text), 5)

digram_count = {}
n = 0
while n < len(text):
    if text[n:n+2] in digram_count.keys():
        digram_count[text[n:n+2]] += 1
    elif text[n:n+2] not in digram_count.keys():
        digram_count[text[n:n+2]] = 1
    n += 2

print digram_count
#need a variable name for digram freq

def meanSquaredError(actual, observed):
    accumulator = 0
    for key in actual:
        tmp = pow(float(actual[key] - observed[key]), 2)
        accumulator += tmp

    return float(accumulator) / len(actual.keys())

monogram_error = round(meanSquaredError(monogram_freq, letter_freq), 5)

#print monogram_error
#print text[:50]
#print text[-50:]
#print letter_count
#print letter_freq
