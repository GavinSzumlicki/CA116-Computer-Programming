#!/usr/bin/env python3

n = int(input())
while n != 0:
  prev = n
  n = int(input())
  curr = n
  if prev < curr and curr != 0:
    print("higher")
  elif curr < prev and curr != 0:
    print("lower")
  elif prev == curr and curr != 0:
    print("equal")
