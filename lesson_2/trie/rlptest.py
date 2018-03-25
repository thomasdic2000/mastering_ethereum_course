#!/usr/bin/python

import plyvel

db = plyvel.DB('triedb')

for k, v in db:
    print("the key = 0x"+k.encode("hex"))
    print("the value = 0x"+v.encode("hex"))
    print("-------------------------------------------")



