#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
  a = f.readlines()

with open(sys.argv[2]) as f:
  b = f.readlines()

data = a + b

if len(a) <= len(b):
  shorter = a
  longer = b
else:
  shorter = b
  longer = a

i = 0
while i < len(shorter):
  j = 0
  while j < len(shorter[i]):
    if a[i][j] != b[i][j]:
      print(i, j)
      j = len(shorter[i])
    j = j + 1
  i = i + 1
if len(shorter) != len(longer):
  print(len(shorter), "0")
