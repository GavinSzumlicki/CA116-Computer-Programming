#!/usr/bin/env python3

n = int(input())
i = 0
while i < 5:
  prev = n
  n = int(input())
  curr = n
  if prev < curr:
    print("higher")
  elif curr < prev:
    print("lower")
  else:
    print("equal")
  i = i + 1
