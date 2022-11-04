#!/usr/bin/env python3

s = input()

i = 0
while i < len(s):
  t = s[i]
  if "a" <= t and t <= "g":
    print(t)
    s = " "
  i = i + 1
