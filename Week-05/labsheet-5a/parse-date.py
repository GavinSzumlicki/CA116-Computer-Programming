#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and not (s[i] == " "):
  i = i + 1
s = s[i:] + " " + "(" + s[0:i] + ")"

i = 1
while i < len(s) and not (s[i] == " "):
  i = i + 1
j = i + 1
while j < len(s) and not (s[j] == " "):
  j = j + 1
s = s[i:j - 1] + s[0:i] + "," + s[j:]
s = s[1:len(s)]
print(s)
