#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Usage:",sys.argv[0],"MESSAGE-ENC.TXT\n")
    sys.exit()

alfaL = []
for i in range(65, 91):
    alfaL.append(chr(i))
alfa = ''.join(alfaL)

banfot = "=" * int(70) #BANNER FOOTER

#enfreq  = 'ETAOINSHRDLCUMWFGYPBVKJXQZ' #The words more frequency in english languagem.
enfreq = 'AOESMRUILZDTHNCYBXVKGFPWQJ' #As letras com mais frequencia na linguem portuguesa

ltcount = {'A': 0,'B': 0,'C': 0,'D': 0,'E': 0,'F': 0,'G': 0,'H': 0,'I': 0,'J': 0,'L': 0,'K': 0,'M': 0,'N': 0,'O': 0,'P': 0,'Q': 0,'R': 0,'S': 0,'T': 0,'U': 0,'V': 0,'W': 0,'X': 0,'Y': 0,'Z': 0}

f = open(sys.argv[1], 'r').read().upper()

print(banfot)
print("== [*] FA (Frequency Analysis) >>>[<<< V1.0 >>>]<<< [*] |--->  <x><  ")
print(banfot+'\n')


for c in f:
    if c in alfa.upper():
        ltcount[c] += 1

order = []
score = 0

for w in sorted(ltcount, key=ltcount.get, reverse=True):
    print(w, ltcount[w])
    order.append(w)

order = ''.join(order)

for clt in enfreq[:6]:
    if clt in order[:6]:
        score += 1

for ult in enfreq[-6:]:
    if ult in order[-6:]:
        score += 1

print("\n[*] Score = ",score,"out of 12")
print(banfot)