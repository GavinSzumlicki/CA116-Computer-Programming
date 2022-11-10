#!/usr/bin/env python3

import sys
n = int(sys.argv[1])

half = n // 2

i = 0
while i < n:
  j = half - i
  if j < 0:
    j = -j
  print(" " * j + "*" * (n - 2 * j))
  i = i + 1
