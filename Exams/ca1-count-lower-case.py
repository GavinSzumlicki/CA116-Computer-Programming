#!/usr/bin/env python3

s = input()

count = 0

i = 0
while i < len(s):
  if s[i] <= "z" and "a" <= s[i]:
    count = count + 1
  i = i + 1
print(count)
