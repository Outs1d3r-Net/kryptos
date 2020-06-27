#!/usr/bin/env python3

#LIBRARIES
import sys

#BANNER
#print(len(sys.argv))
if len(sys.argv) != 2:
    print("[*] CODEBREAKER v1.0 (cesar cipher)[*]\n\n")
    print("Usage:",sys.argv[0],"MESSAGE-FILE.txt")
    print("eX:",sys.argv[0],"Message.txt")
    print("[=================================================]")
    sys.exit()

#ALPHABET
alfaL = []
for i in range(65, 91): alfaL.append(chr(i))
alfa = ''.join(alfaL)

#GET THE MSG FOR ENCRYPT
f = open(sys.argv[1], 'r').read().lower()

#COUNT
k = 27

#ALGORITHM
bp = 1
while bp < k:
    r = ''
    for c in f:
        if c in alfa.lower():
            ct = alfa.lower().find(c)
            ct = (ct - bp) % 26
            r = r + alfaL[ct]
        else:
            r = r + c

    bp = bp + 1
	#RESULT
    print("Key = ",(bp-1),"[-->> ",r.rstrip("\n"))
