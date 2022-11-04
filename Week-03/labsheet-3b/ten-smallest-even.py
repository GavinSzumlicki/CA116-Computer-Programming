#!/usr/bin/env python3

smalleven = 0

i = 0
while i < 10:
  n = int(input())
  if smalleven == 0 and n % 2 == 0:
    smalleven = smalleven + n
  elif n < smalleven and n % 2 == 0:
    smalleven = n
  i = i + 1
print(smalleven)
