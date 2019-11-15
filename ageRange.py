#!/usr/bin/env python3
import sys

a = int(sys.argv[1])

if a in range(0,10):
    print("you belong to kids")
elif a in range(10,18):
   print("you belong to teenager")
elif a in range(18,30): 
    print("you belong to adult")
elif a in range (30,60):
   print("you belong to older")
elif a in range(60,120):
   print("you belong to oldest")
