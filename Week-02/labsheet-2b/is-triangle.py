#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

if a + b <= c or a + c <= b or b + c <= a:
  print("no")
else:
  print("yes")
