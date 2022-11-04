#!/usr/bin/env python3

s = input()

i = 0
while i < len(s):
  t = s[i]
  if "A" <= t and t <= "Z":
    print(i)
    s = " "
  i = i + 1
