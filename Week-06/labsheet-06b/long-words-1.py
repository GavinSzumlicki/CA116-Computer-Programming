#!/usr/bin/env python3

if __name__ == "__main__":
  a = ["dog", "cat", "mouse"]

i = 0
while i < len(a):
  if 6 <= len(a[i]):
    print(a[i])
  i = i + 1
