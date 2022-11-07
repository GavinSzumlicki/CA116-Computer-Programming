#!/usr/bin/env python3

n = input()
a = []

while n != "end":
  a.append(n)
  n = input()

i = 0
while i < len(a):
  p = i
  j = p + 1
  while j < len(a):
    if int(a[j]) < int(a[p]):
      p = j
    j = j + 1

  tmp = a[i]
  a[i] = a[p]
  a[p] = tmp
  i = i + 1
print(a[len(a) // 2])
