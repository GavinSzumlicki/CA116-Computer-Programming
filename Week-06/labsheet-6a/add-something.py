#!/usr/bin/env python3

s = input()
a = []

while s != "end":
  n = int(s)
  a.append(n)
  s = input()

n = int(input())
i = 0
while i < len(a):
  print(a[i] + n)
  i = i + 1
