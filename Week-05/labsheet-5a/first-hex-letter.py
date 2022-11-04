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

i = 0
while i < len(output):
  if output[i] <= "f" and "a" <= output[i]:
    output = output[i]
    print(output)
    i = len(output)
  i = i + 1
