#!/usr/bin/env python3

with open("a.txt") as f:
  a = f.readlines()

with open("b.txt") as f:
  b = f.readlines()

data = a + b

out = []
i = 0
while i < len(a) + len(b):
  if data[i] in a and data[i] in b and data[i] not in out:
    out.append(data[i])
  i = i + 1
if 0 < len(out):
  print("".join(out).rstrip())
