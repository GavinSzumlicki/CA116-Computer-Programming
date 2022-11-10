#!/usr/bin/env python3

s = input()
odds = []

while s != "end":
  n = int(s)
  if n % 2 == 0:
    print(n)
  else:
    odds.append(n)
  s = input()

i = 0
while i < len(odds):
  print(odds[i])
  i = i + 1
