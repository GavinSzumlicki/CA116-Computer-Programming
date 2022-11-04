#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and not (s[i] <= "9" and "0" <= s[i]):
  i = i + 1

j = i
while j < len(s) and (s[j] <= "9" and "0" <= s[j]):
  j = j + 1

if i < len(s):
  print(s[i:j], i)
