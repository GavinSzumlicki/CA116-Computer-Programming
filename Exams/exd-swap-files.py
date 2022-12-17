#!/usr/bin/env python3

import sys
file_1 = sys.argv[1]
file_2 = sys.argv[2]

with open(file_1, "r") as f:
  file_1_text = f.read()

with open(file_2, "r") as f:
  file_2_text = f.read()

with open(file_1, "w") as f:
  f.write(file_2_text)

with open(file_2, "w") as f:
  f.write(file_1_text)
