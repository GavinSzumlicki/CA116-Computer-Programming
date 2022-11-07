#!/usr/bin/env python3

import sys
args = sys.argv[1]

n = int(args)

half = n // 2

i = 0
while i < n:
  j = half - i
  if j < 0:
    j = -j
  print(" " * j + "*" * (n - 2 * j))
  i = i + 1
