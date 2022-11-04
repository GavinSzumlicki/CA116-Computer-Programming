#!/usr/bin/env python3

n = 5
total = 0
start = 0

sum = input()

i = 0
while i < n:
  j = start
  while j < len(sum) and sum[j] != "+":
    j = j + 1

  total = total + int(sum[start:j])
  start = j + 1

  i = i + 1

print(total)
