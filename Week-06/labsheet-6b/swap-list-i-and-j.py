#!/usr/bin/env python3

if __name__ == "__main__":
  a = ["dog", "cat", "mouse"]
  i = 1
  j = 2

tmp = a[i]
a[i] = a[j]
a[j] = tmp
