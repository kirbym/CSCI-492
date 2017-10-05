# Brute force method to break Caesar cipher by using frequence analysis of letters and digrams
# Michael Kirby
# 10/1/17

# Monogram and digram frequencies given by the following website
# http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/

import sys
import caesar

#Find the mean squared error of a set of data
#actual: dictionary object containing the theoretical data value
#observed: dictionary object containing the experimental data value
def meanSquaredError(actual, observed):
    accumulator = 0
    for key in observed.keys():
        tmp = pow(float(actual[key] - observed[key]), 2)
        accumulator += tmp

    return float(accumulator) / len(observed.keys())

#Find the minimum value of a list of data and the index associated with it
#listData: list object containing data values
def findMinOfList(listData):
    index = 0
    minimum = listData[0]
    for i in xrange(len(listData)):
        if listData[i] < minimum:
            minimum = listData[i]
            index = i

    return index, minimum

#Method to brute force the Caesar cipher testing all 26 possibilities and predicting the offset value
def etTuBrute(raw_text):
    stats = []  #will hold the error statistics
    for c in xrange(26):
        text = caesar.decrypt(raw_text, c) #decrypt the text with each offset

        #count the number of occurances of each unique letter
        letter_count = {}
        for i in xrange(len(text)):
            if text[i] in letter_count.keys():
                letter_count[text[i]] += 1
            elif text[i] not in letter_count.keys():
                letter_count[text[i]] = 1

        #calculate the frequency of the letters
        letter_freq = {}
        for key in letter_count.keys():
            letter_freq[key] = round(float(letter_count[key]) / len(text) * 100, 5)

        #count the number of occurances of digrams in the text
        digram_count = {}
        n = 0
        while n < len(text):
            if text[n:n+2] in digram_count.keys():
                digram_count[text[n:n+2]] += 1
            elif text[n:n+2] not in digram_count.keys():
                digram_count[text[n:n+2]] = 1
            n += 2

        #calculate the frequency of the digrams
        digram_freq = {}
        for key in digram_count.keys():
            digram_freq[key] = round(float(digram_count[key]) / len(text) / 2 * 100, 5)

        #calculate errors
        monogram_error = round(meanSquaredError(monogram_freq, letter_freq), 5)
        digram_error = round(meanSquaredError(bigram_freq, digram_freq), 5)

        print c , (monogram_error + digram_error) / 2
        stats.append((monogram_error + digram_error) / 2)  #track average of monogram error and digram error

    #make a prediction about which offset was used to encrypt the text
    predicted_offset, predicted_min = findMinOfList(stats)
    print "Predicted Key:", predicted_offset, "Error:", predicted_min

if __name__ == "__main__":

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

    #read all 26^2 = 676 possible bigrams and the number of times they occured from a file
    bigramfile = open("bigram-data.txt", 'r')
    lines = bigramfile.readlines()
    bigramfile.close()
    value = []
    count = []
    total = 0
    for l in xrange(len(lines)):
        value.append(lines[l][:2])  #getting the bigram from the string (the first two letters in the string)
        occurances = int(lines[l][2:].strip())  #getting the number of occurances the bigram appeared (the remainder of the string)
        count.append(occurances)
        total += occurances  #total the amount of bigrams for frequency calculation

    #organizing the bigrams into a dictionary object
    bigram_count = {}
    for k in xrange(len(value)):
        bigram_count[value[k]] = count[k]

    #find the frequency (in percents) of each bigram
    bigram_freq = {}
    for key in bigram_count.keys():
        bigram_freq[key] = round(bigram_count[key] / float(total) * 100, 5) #frequencies are in percents

    #verify correct number of arguments given on the command line
    if (len(sys.argv) < 2):
        sys.exit("Too few arguments. python <script> <text.txt>")
    elif (len(sys.argv) > 2):
        sys.exit("Too many arguments. python <script> <text.txt>")

    #open the file and read the text
    textfile = open(sys.argv[1], 'r')
    input_text = textfile.read()
    textfile.close()

    #brute force the encrypted text using the Caesar shift scheme
    #determine what offset value was used to encrypt text
    etTuBrute(input_text)
