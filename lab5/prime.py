import sys, math, timeit

def SuperPower(x, n):
    if (n==0):
        return 1
    if (n%2==1):
        return x * (SuperPower(x, (n - 1)/2) * SuperPower(x, (n - 1)/2))
    else:
        return (SuperPower(x, n/2)) * (SuperPower(x, n/2))

if (len(sys.argv) == 2):
    start = timeit.default_timer()
    n = int(sys.argv[1])

    sqn = int(math.floor(math.sqrt(n)))

    is_prime = True

    for i in range (1, sqn):
        if (SuperPower(i, n-1) % n != 1):
            is_prime = False

    stop = timeit.default_timer()

    print is_prime
    print "Time: " + str(stop-start)









