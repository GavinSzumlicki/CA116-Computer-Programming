#!/usr/bin/env python3

largest = 0

i = 0
while i < 10:
  n = int(input())
  if largest == 0 or largest < n:
    largest = n
  i = i + 1
print(largest)
