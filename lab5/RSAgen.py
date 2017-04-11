import sys
from Crypto.PublicKey import RSA


if (len(sys.argv) == 4):

    leng = int(sys.argv[1])
    file_pub = open(sys.argv[2], 'w')
    file_priv = open(sys.argv[3], 'w')


    rsa_keys = RSA.generate(leng)
    pub_key = rsa_keys.publickey().exportKey()
    priv_key = rsa_keys.exportKey()

    file_pub.write(pub_key)
    file_priv.write(priv_key)
else:
    print "Zla ilosc argumentow"



