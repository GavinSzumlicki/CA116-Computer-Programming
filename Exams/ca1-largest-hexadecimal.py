#!/usr/bin/env python3

s = input()
t = input()

if len(s) < len(t):
  print(t)
elif len(t) < len(s):
  print(s)
elif t < s:
  print(s)
else:
  print(t)
