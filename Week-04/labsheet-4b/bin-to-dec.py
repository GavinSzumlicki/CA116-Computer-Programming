#!/usr/bin/env python3

total = 0
s = input()

i = 0
while i < len(s):
  n = int(s[((len(s) - 1) - i)])
  total = total + (n * 2 ** i)
  i = i + 1
print(total)
