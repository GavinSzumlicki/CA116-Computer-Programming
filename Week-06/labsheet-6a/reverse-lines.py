#!/usr/bin/env python3

n = input()
a = []

while n != "end":
  a.append(n)
  n = input()

i = 0
while i < len(a):
  print(a[len(a) - i - 1])
  i = i + 1
