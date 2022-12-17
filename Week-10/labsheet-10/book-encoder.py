#!/usr/bin/env python3

import sys
message = sys.stdin.read()

book = {
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

seen = []

i = 0
while i < len(message):
  found = False
  while found is False:
    j = 0
    while j < len(book) and found is not True:
      with open(book[j]) as f:
        page = f.readlines()
      k = 0
      while k < len(page) and found is not True:
        loop = 0
        while loop < len(page[k]) and found is not True:
          triplet = j, k, loop
          if message[i] == page[k][loop] and triplet not in seen:
              found = True
              seen.append(triplet)
          loop = loop + 1
        k = k + 1
      j = j + 1
  i = i + 1

i = 0
while i < len(seen):
  print(seen[i][0], seen[i][1], seen[i][2])
  i = i + 1
