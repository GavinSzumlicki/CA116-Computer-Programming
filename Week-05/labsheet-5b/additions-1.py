#!/usr/bin/env python3

first = 0
second = 0

i = 0
while i < 10:

  n = input()

  j = 0
  while j < len(n):
    if n[j] == "+":
      first = int(n[0:j])
      second = int(n[j + 1:])
      j = len(n)
    j = j + 1

  print(first + second)
  i = i + 1
