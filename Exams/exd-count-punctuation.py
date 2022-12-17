#!/usr/bin/env python3

import sys
text = sys.stdin.read()

total = 0
i = 0
while i < len(text):
  if text[i] == ".":
    total = total + 1
  if text[i] == ",":
    total = total + 1
  if text[i] == "?":
    total = total + 1
  if text[i] == "!":
    total = total + 1

  i = i + 1

print(total)
