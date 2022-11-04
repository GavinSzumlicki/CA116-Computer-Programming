#!/usr/bin/env python3

f = input()
s = ""

i = 0
while i < len(f) and not f[i] == ".":
  s = s + f[i]
  i = i + 1

print(s)
print(f[i + 1:])
