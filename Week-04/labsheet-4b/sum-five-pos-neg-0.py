#!/usr/bin/env python3

totalpos = 0
totalneg = 0

n = int(input())
while n != 0:
  if n < 0:
    totalneg = totalneg + n
  else:
    totalpos = totalpos + n
  n = int(input())
print(totalneg, totalpos)
