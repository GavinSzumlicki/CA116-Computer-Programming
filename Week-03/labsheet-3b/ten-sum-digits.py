#!/usr/bin/env python3

total = 0

i = 0
while i < 10:
  n = int(input())
  if n < 0:
    n = n * - 1
    total = total + n % 10
  else:
    total = total + n % 10
  i = i + 1
print(total)
