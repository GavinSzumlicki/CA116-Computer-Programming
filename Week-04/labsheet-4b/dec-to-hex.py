#!/usr/bin/env python3

digits = "0123456789abcdef"

base = 16

n = int(input())
output = ""

while 0 < n:
  output = digits[n % base] + output
  n = n // base

if len(output) == 0:
  output = "0"

print(output)
