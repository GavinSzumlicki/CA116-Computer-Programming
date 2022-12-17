#!/usr/bin/env python3

import sys

a = sys.stdin.readlines()

i = 0
while i < len(a):
  a[i] = a[i].split("/")
  file = a[i][len(a[i]) - 1]
  print(file[0:len(file) - 1])
  i = i + 1
