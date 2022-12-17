#!/usr/bin/env python3

import os
files = os.listdir(".")

curr = "start.txt"
while curr in files:
  with open(curr) as f:
    data = f.readlines()
  curr = ("".join(data).rstrip())
print(curr)
