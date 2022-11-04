#!/usr/bin/env python3

s = input()
t = ""

i = 0
while i < len(s):
  if s[i] <= "z" and "a" <= s[i]:
    t = t + chr(ord(s[i]) - ord("a") + ord("A"))
  else:
    t = t + s[i]
  i = i + 1
print(t)
