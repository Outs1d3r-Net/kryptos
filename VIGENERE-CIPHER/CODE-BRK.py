#!/usr/bin/env python3

import sys

#BANNER
#print(len(sys.argv))
if len(sys.argv) != 3:
    print("[*] CODEBREAKER (vigenere cipher) v1.0 [*]\n\n")
    print("Usage:",sys.argv[0],"MESSAGE-FILE.txt WORDLIST.txt")
    print("eX:",sys.argv[0],"Message.txt enc")
    print("[=================================================]")
    sys.exit()

alfaL = []
for i in range(65, 91):
    alfaL.append(chr(i))
alfa = ''.join(alfaL)

f = open(sys.argv[1], 'r').read().lower()
r = ''
kID = 0
k = open(sys.argv[2], 'r')

for p in k:
    for c in f:
        if c in alfa.lower():
            pt = alfa.lower().find(c)
            pt = pt - alfa.lower().find(p[kID%len(p)])
            r = r + alfaL[pt%26]
        else:
            r = r + c

print(r,)

    