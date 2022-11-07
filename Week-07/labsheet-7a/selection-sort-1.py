#!/usr/bin/env python3

n = input()
a = []

while n != "end":
  a.append(n)
  n = input()

p = 0
i = p + 1
while i < len(a):
  if int(a[i]) < int(a[p]):
    p = i
  i = i + 1
print(p)
