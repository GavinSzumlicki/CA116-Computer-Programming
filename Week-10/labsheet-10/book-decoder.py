#!/usr/bin/env python3

import sys
encrypt = sys.stdin.readlines()

pages_dict = {
  0: "page-0.txt",
  1: "page-1.txt",
  2: "page-2.txt",
  3: "page-3.txt",
  4: "page-4.txt",
  5: "page-5.txt",
  6: "page-6.txt",
  7: "page-7.txt",
  8: "page-8.txt",
  9: "page-9.txt",
  10: "page-10.txt",
}

decoded = []

i = 0
while i < len(encrypt):
  page = int(encrypt[i].split(" ")[0])
  line = int(encrypt[i].split(" ")[1])
  char = int(encrypt[i].split(" ")[2])

  with open(pages_dict[page]) as f:
    curr_page = f.readlines()

  decoded.append(curr_page[line][char])
  i = i + 1

print("".join(decoded).rstrip())
