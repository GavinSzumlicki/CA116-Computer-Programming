#!/usr/bin/env python3

total = 0

n = int(input())
while n != 0:
  if n < 0:
    n = n * - 1
  total = total + n
  n = int(input())
print(total)
