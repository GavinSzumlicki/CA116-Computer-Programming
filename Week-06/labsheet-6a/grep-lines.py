#!/usr/bin/env python3

import sys
pattern = sys.argv[1]

s = input()
a = []
while s != "end":
  a.append(s)
  s = input()

i = 0
while i < len(a):
  j = 0
  while j < len(a[i]) and a[i][j:j + len(pattern)] != pattern:
    j = j + 1
  if a[i][j:j + len(pattern)] == pattern:
    print(a[i])
  i = i + 1
