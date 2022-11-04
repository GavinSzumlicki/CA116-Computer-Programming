#!/usr/bin/env python3

n = int(input())
output = ""
base = 2

while 0 < n:
  output = str(n % base) + output
  n = n // base
print(output)
