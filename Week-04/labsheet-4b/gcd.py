#!/usr/bin/env python3

a = int(input())
b1 = int(input())

while b1 != 0:
  b2 = a % b1
  a = b1
  b1 = b2
print(a)
