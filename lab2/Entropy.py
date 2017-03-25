import sys, re, math

for i in range(1,len(sys.argv)):
    #Zliczanie z plikow
    stat = {}
    chars_number = 0.0
    test_file = open(sys.argv[i])
    for line in test_file.readlines():
            line = re.sub(r'\s', '', line)
            line = line.lower()
            for znak in line:
                    if znak in stat:
                            stat[znak] += 1
                    else:
                            stat[znak] = 1
                    chars_number += 1
    #Przeliczanie na prawdopodobienstwo
    for znak in stat:
        stat[znak] = stat[znak]/chars_number

    #Obliczanie entropi
    entropy = 0.0

    for znak in stat:
        entropy += stat[znak] * math.log(stat[znak], 2)
    entropy *= -1.0

    #Wypisz
    print "Entropia pliku \""+ sys.argv[i]+ "\": " + str(entropy)

