#!/usr/bin/env python3

s = input()
a = []

while s != "end":
  a.append(s)
  s = input()

p = int(input())
i = p + 1
while i < len(a):
  if int(a[i]) < int(a[p]):
    p = i
  i = i + 1
print(p)
