#!/usr/bin/env python3

attribute = " City,"

n = input()
while n != "end":

  i = 0
  while i < len(n):
    if n[i:i + len(attribute)] == attribute:
      print(n[0:i + len(attribute) - 1])
    i = i + 1
  n = input()
