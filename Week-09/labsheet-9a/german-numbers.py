#!/usr/bin/env python3

import sys
a = sys.stdin.readlines()

translation = {
  "one": "eins",
  "two": "zwei",
  "three": "drei",
  "four": "vier",
  "five": "funf",
  "six": "sechs",
  "seven": "sieben",
  "eight": "acht",
  "nine": "neun",
  "ten": "zehn",
}


i = 0
while i < len(a):
  print(translation["".join(a[i]).rstrip()])
  i = i + 1
