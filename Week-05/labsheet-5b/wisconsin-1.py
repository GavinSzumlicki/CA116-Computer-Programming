#!/usr/bin/env python3

n = input()
state_code = ",WI"

while n != "end":
  i = 0
  while i < len(n):
    if n[i:i + len(state_code)] == state_code:
      print(n[0:i])
    i = i + 1
  n = input()
