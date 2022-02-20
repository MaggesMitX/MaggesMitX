#!/usr/bin/env python3
# coding: utf-8

#Libarys zum installieren:
#pikepdf und tqdm/(pip install ...)

import pikepdf
from tqdm import tqdm

passwords= [line.strip() for line in open("wordlist.txt")]
#benötigt vorhandene Wordlist.txt
for password in tqdm(passwords, "Decypting PDF"):
    try:
        with pikepdf.open("sample.pdf", password=password) as pdf:
            print("\n[+] Password found:", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        #bei falschen password soll der Loop weiterlaufen
        continue
