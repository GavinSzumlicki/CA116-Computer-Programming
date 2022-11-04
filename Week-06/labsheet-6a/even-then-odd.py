#!/usr/bin/env python3

n = input()
odds = []

while n != "end":
  n = int(n)
  if n % 2 == 0:
    print(n)
  else:
    odds.append(n)
  n = input()

i = 0
while i < len(odds):
  print(odds[i])
  i = i + 1
