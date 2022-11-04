#!/usr/bin/env python3

s = input()
neg = ""

i = 0
while i < len(s):
  if s[0] == "-":
    neg = "-"
    s = s[1:]
  elif s[0] == ".":
    s = "0" + s
  i = i + 1

i = 0
while i < len(s) and s[i] != ".":
  if s[i] == s[len(s) - 1]:
    s = s + "." + "0"
  i = i + 1

if s[len(s) - 1] == ".":
  s = s + "0"

i = 0
while i < len(s) and not (s[i] == "."):
  i = i + 1

j = i + 1
while j < len(s) and not (s[j] == "."):
  j = j + 1

print(neg + s[0:j])
