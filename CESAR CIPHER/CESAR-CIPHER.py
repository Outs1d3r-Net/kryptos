#!/usr/bin/env python3

#LIBRARIES
import sys

#BANNER
#print(len(sys.argv))
if len(sys.argv) != 3:
    print("[*] CESAR-CIPHER v1.0 [*]\n\n")
    print("Usage:",sys.argv[0],"MESSAGE-FILE.txt OPERATION")
    print("eX:",sys.argv[0],"Message.txt enc")
    print("[=================================================]")
    sys.exit()
    
#ALPHABET
alfaL = []
for i in range(65, 91): alfaL.append(chr(i))
alfa = ''.join(alfaL)

#GET THE MSG FOR ENCRYPT
f = open(sys.argv[1], 'r').read().lower()
k = int(3)
m = sys.argv[2] #ENCRYPT OR DECRYPT INPUT

#RESULT
r = ''

#ALGORITHM
for c in f: 
    if c in alfa.lower():
        pt = alfa.lower().find(c)
        if m == 'enc':
            pt = (pt + k) % 26
        elif m == 'dec':
            pt = (pt - k) % 26
        else:
            print("[*] Error ! Invalid Operation !\n")
            print("enc for ENCRIPTION\ndec for DECRYPTION\n")
            sys.exit()
            
        r = r + alfaL[pt]
    else:
        r = r + c 
    
#RESULT
print(r,)