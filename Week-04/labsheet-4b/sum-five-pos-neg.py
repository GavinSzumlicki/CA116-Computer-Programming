#!/usr/bin/env python3

totalpos = 0
totalneg = 0

i = 0
while i < 5:
  n = int(input())
  if n < 0:
    totalneg = totalneg + n
  else:
    totalpos = totalpos + n
  i = i + 1
print(totalneg, totalpos)
