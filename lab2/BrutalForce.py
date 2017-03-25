import sys, math, time
from Crypto.Cipher import ARC4
from itertools import *

if len(sys.argv) == 3:
    start_time = time.time()
    cryptogram_file = open(sys.argv[1])
    entropy_level = float(sys.argv[2])
    max_key_length = 3
    cryptogram = cryptogram_file.read()
    key = "!"
    alphabet = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    found_entropy_level = 0.0
    lowest_entropy_level = 10.0
    lowest_decoded = ''
    lowest_key = ''
    decoded = ''
    found = 0


    for i in range(1, max_key_length + 1):
        if (found == 1):
            break
        key_combinations = product(alphabet, repeat=i)
        for temp_key in key_combinations:
            key = ''.join(temp_key)
            encrypter = ARC4.new(key)
            encrypted = encrypter.encrypt(cryptogram)
            #print encrypted
            # Zliczanie znakow
            stat = {}
            chars_number = 0.0
            encrypted = encrypted.lower()
            for znak in encrypted:
                if znak in stat:
                    stat[znak] += 1
                else:
                    stat[znak] = 1
                chars_number += 1
            # Przeliczanie na prawdopodobienstwo
            for znak in stat:
                stat[znak] = stat[znak] / chars_number

            # Obliczanie entropi
            entropy = 0.0

            for znak in stat:
                entropy += stat[znak] * math.log(stat[znak], 2)
            entropy *= -1.0

            if (entropy < entropy_level):
                found_entropy_level = entropy
                decoded = encrypted
                found = 1
                break

            if (entropy < lowest_entropy_level):
                lowest_entropy_level = entropy
                lowest_decoded = encrypted
                lowest_key = key


            # Wypisz
            #print "Entropia dla klucza \"" + key + "\": " + str(entropy)
    end_time = time.time()
    elapsed = end_time - start_time
    if (found_entropy_level != 0.0):
        print "Time: " + str(elapsed) + " Key: \"" +str(key)+ "\" entropy: " + str(found_entropy_level) + " Text: " + decoded
    else:
        print "Time: " + str(elapsed)+ " Key: \"" +str(key) + " Entropy: " + str(lowest_entropy_level) + " Text: " + lowest_decoded




