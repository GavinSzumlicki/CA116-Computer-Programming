#!/usr/bin/env python3

p = 0
c = 0

i = 1
while i != 0:
  p = c
  c = int(input())
  if p % 2 == 0 and p // 2 == c:
    i = - 1
  elif p % 2 == 1 and p * 3 + 1 == c:
    i = - 1
  i = i + 1
print(p, c)
