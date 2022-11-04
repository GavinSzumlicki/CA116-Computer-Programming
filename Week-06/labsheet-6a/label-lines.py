#!/usr/bin/env python3

a = []
n = input()

while n != "end":
  a.append(n)
  n = input()

i = 0
while i < len(a):
  print(i, len(a), a[i])
  i = i + 1
