#!/usr/bin/env python3

s = 0

i = 0
while i < 10:
  n = int(input())
  s = s + (n * (10 ** i))
  i = i + 1
i = 0
while i < 10:
  s = s % (10 ** (10 - i))
  print(s // 10 ** (9 - i))
  i = i + 1
