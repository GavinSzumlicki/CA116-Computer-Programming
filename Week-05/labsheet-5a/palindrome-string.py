#!/usr/bin/env python3

w = input()

i = 0
while i < len(w) and (w[(len(w) - 1) - i] == w[i]):
  i = i + 1

if i == len(w):
  print("palindrome")
