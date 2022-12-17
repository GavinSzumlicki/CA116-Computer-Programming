#!/usr/bin/env python3

import os
files = os.listdir(".")

backedup = []

i = 0
while i < len(files):
  N = len(files[i])
  if files[i][N - 4:N] == ".bak" and files[i] not in backedup:
    backedup.append(files[i])
  elif os.path.isfile(files[i]) is True:
    with open(files[i]) as f:
      data = f.readlines()
      data = "".join(data)
      newfile = files[i] + ".bak"
    with open(newfile, "w") as f:
      f.write(data)
  i = i + 1
