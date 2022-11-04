#!/usr/bin/env python3

n = input()
state_code = ",WI"

total = 0

while n != "end":
  i = 0
  while i < len(n):
    if n[i:i + len(state_code)] == state_code:
      total = total + 1
    i = i + 1
  n = input()

print(total)
