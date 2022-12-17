#!/usr/bin/env python3

import sys

tokens = sys.stdin.read().split()
N = 20
points = {}

i = 0
while i < len(tokens) // 2:
  x = tokens[i * 2]
  y = tokens[i * 2 + 1]
  i = i + 1

  key = x + "/" + y
  points[key] = True
print(" " + N * "-")

y = 0
while y < N:
  line = ["|"]
  x = 0
  while x < N:
    key = str(x) + "/" + str(N - y - 1)

    if key in points:
      line.append("*")

    else:
      line.append(" ")

    x = x + 1

  line.append("|")
  print("".join(line))
  y = y + 1
print(" " + N * "-")
