#!/usr/bin/env python3

smallest = 0

i = 0
while i < 10:
  n = int(input())
  if smallest == 0:
    smallest = n
  elif 0 < n and n < smallest:
    smallest = n
  i = i + 1
print(smallest)
