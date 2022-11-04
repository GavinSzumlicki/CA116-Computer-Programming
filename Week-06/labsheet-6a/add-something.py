#!/usr/bin/env python3

n = input()
a = []

while n != "end":
  n = int(n)
  a.append(n)
  n = input()

n = int(input())
i = 0
while i < len(a):
  print(a[i] + n)
  i = i + 1
