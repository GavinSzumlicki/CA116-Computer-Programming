#!/usr/bin/env python3

s = input()
t = 0

i = 0
while i < len(s):
  t = int(s[i]) + t
  i = i + 1
print(t)
