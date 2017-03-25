import sys, math

if (len(sys.argv) == 2):
    alpha_length = int(sys.argv[1])
    entropy_level = 128
    k = 0
    current_entropy = 0
    while (current_entropy < entropy_level):
        k += 1
        current_entropy = k * math.log(alpha_length, 2)
    print "Do alfabetu " + str(alpha_length) + " znakowego haslo musi byc conajmniej " + str(k) + " znakowe"