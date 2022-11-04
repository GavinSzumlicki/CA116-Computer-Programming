#!/usr/bin/env python3

s = input()
t = ""

i = 0
while i < len(s):
  n = s[i]
  if n == " ":
    t = t + ""
  else:
    t = t + n
  i = i + 1
print(t)
