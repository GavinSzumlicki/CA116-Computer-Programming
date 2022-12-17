#!/usr/bin/env python3

import sys

file_name = sys.argv[1]

a = []
i = 0
while i < len(sys.argv) - 2:
  a.append(sys.argv[i + 2] + "\n")
  i = i + 1

with open(file_name, "w") as f:
  f.write("".join(a))
