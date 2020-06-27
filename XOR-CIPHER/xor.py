#!/usr/bin/env python2

#LIBRARIES
import sys
import binascii

#BANNER
banhed = 'Msg[>>> '
banfot = '=' * 70
#print len(sys.argv)
if len(sys.argv) != 4:
    print "Usage:",sys.argv[0],"MESSAGE PASSWORD OPERATION\neX:",sys.argv[0],"'message' 'secret' enc\n"
    sys.exit()

#VARIABLES
k = sys.argv[2]
m = sys.argv[3]
kID = 0
xored = ''

#ALGORITHM
if m == 'enc':
    msg = sys.argv[1]
elif m == 'dec':
    msg = binascii.unhexlify(sys.argv[1])

#XOR CALC
for c in msg:
    xored += chr(ord(k[kID%len(k)]) ^ ord(c))
    kID += 1

if m == 'enc':
    xored = binascii.hexlify(xored)
    banfot
    print banhed, xored
    banfot
elif m == 'dec':
    banfot
    print banhed, xored
    banfot
