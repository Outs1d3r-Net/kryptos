#!/usr/bin/env python3

import sys
#BANNER
#print(len(sys.argv))
if len(sys.argv) != 4:
    print("[*] VIGENERE-CIPHER v1.0 [*]\n\n")
    print("Usage:",sys.argv[0],"MESSAGE-FILE.txt PASSWORD OPERATION")
    print("eX:",sys.argv[0],"Message.txt password enc")
    print("[=================================================]")
    sys.exit()

alfaL = []
for i in range(65, 91):
    alfaL.append(chr(i))
alfa = ''.join(alfaL)

f = open(sys.argv[1], 'r').read().lower()

k = sys.argv[2].lower()

kID = 0

m = sys.argv[3]

r = ''

for c in f:
    if c in alfa.lower():
        pt = alfa.lower().find(c)
        if m == 'enc':
            pt = pt + alfa.lower().find(k[kID%len(k)])
            #ptbn = "[*] Encript MSG>>  "
        elif m == 'dec':
            pt = pt - alfa.lower().find(k[kID%len(k)])
            #ptbn = "[*] Decript MSG>>  "
        r = r + alfaL[pt%26]
    else:
        r = r + c
        
print(r,)
#print('\n',str(ptbn),r,'\n')