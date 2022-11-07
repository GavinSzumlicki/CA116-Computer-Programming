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
    if int(a[j][6:8]) < int(a[p][6:8]):
      p = j
    elif int(a[j][6:8]) == int(a[p][6:8]):
      if int(a[j][3:5]) < int(a[p][3:5]):
        p = j
      elif int(a[j][3:5]) == int(a[p][3:5]):
        if int(a[j][0:2]) < int(a[p][0:2]):
          p = j
    j = j + 1

  tmp = a[i]
  a[i] = a[p]
  a[p] = tmp
  print(a[i][9:])
  i = i + 1
