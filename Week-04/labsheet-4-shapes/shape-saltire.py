#!/usr/bin/env python3

#n = int(input())
#
#i = 0
#while i < n:
#  if i + 1 < n / 2:
#    print(" " * i + "*" + " " * (n - 2 - (2 * i)) + "*")
#  elif i + 0.5 == n / 2:
#    print(" " * i + "*")
#  else:
#    print(" " * ((n - i) - 1) + "*" + (" " * (i * 2 - n)) + "*")
#  i = i + 1


n = int(input())
half = n // 2

i = 0
while i < n:
  j = half - i
  if j < 0:
    j = -j
  if j == 0:
    print(half * " " + "*")
  else:
    print((half - j) * " " + "*" + (2 * j - 1) * " " + "*")
  i = i + 1
