#!/usr/bin/env python3

import sys

total = 0

i = 0
while i < len(sys.argv[1:]):

  with open(sys.argv[i + 1]) as f:
    lines = f.readlines()

  j = 0
  while j < len(lines):
    total = total + int(lines[j])
    j = j + 1

  i = i + 1

print(total)
