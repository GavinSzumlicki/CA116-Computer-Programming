#!/usr/bin/env python3

if __name__ == "__main__":
  a = ["", "", "12345", "123456", "1234567"]
  s = "1234"

i = 0
while i < len(a):
  if s == a[i][:len(s)]:
    print(a[i])
  i = i + 1
