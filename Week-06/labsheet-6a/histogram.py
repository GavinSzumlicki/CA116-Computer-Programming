#!/usr/bin/env python3

n = input()
a = []

while n != "end":
  a.append(n)
  n = input()

count = 0
i = 0
while i < 10:
  j = 0
  while j < len(a):
    if i == int(a[j]):
      count = count + 1
    j = j + 1
  print(i, "*" * count)
  count = 0
  i = i + 1
