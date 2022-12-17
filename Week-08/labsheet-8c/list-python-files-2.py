#!/usr/bin/env python3

import sys
import os
files = os.listdir(".")

i = 0
while i < len(files):
  with open(files[i]) as f:
    data = f.readlines()
  if files[i][len(files[i]) - 3:len(files[i])] == ".py" and 0 < len(data):
    print(files[i])
  i = i + 1
