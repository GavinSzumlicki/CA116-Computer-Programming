#!/usr/bin/env python3

import sys

a = sys.stdin.readlines()

total = 0

i = 0
while i < len(a):
  total = total + int(a[i])
  i = i + 1
print(total)
