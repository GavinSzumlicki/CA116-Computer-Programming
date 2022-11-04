#!/usr/bin/env python3

s = input()
prev = ""
curr = ""
t = ""
i = 0
while i < len(s):
  curr = s[i]
  if i == 0:
    if curr < "A" or ("Z" < curr and curr < "a") or "z" < curr:
      t = t + curr
      prev = "N"
    elif curr <= "Z" and "A" <= curr:
      curr = chr(ord(curr) + ord("a") - ord("A"))
      t = t + curr
      prev = "n"
    else:
      t = t + curr
      prev = "n"
  elif curr < "A" or ("Z" < curr and curr < "a") or "z" < curr:
    t = t + curr
  elif prev <= "Z" and "A" <= prev and curr <= "Z" and "A" <= curr:
    curr = chr(ord(curr) + ord("a") - ord("A"))
    t = t + curr
    prev = "n"
  elif prev <= "Z" and "A" <= prev and curr <= "z" and "a" <= curr:
    t = t + curr
    prev = "n"
  elif prev <= "z" and "a" <= prev and curr <= "Z" and "A" <= curr:
    t = t + curr
    prev = "N"
  elif prev <= "z" and "a" <= prev and curr <= "z" and "a" <= curr:
    curr = chr(ord(curr) + ord("A") - ord("a"))
    t = t + curr
    prev = "N"
  i = i + 1
print(t)
