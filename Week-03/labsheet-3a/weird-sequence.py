#!/usr/bin/env python3

n = int(input())
i = 0
x = 1

while i < n:
  x = (x * - 1) + (x % 2) + (x % 2 - 1)
  print(x)
  i = i + 1
