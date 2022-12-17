#!/usr/bin/env python3

import os
files = os.listdir(".")

i = 0
while i < len(files):
  N = len(files[i])
  if files[i][N - 4:N] == ".bak" and os.path.isfile(files[i]) is True:
    os.unlink(files[i])
  i = i + 1
