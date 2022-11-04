#!/usr/bin/env python3

home = int(input())
away = int(input())

if home < away:
  print("Away win.")
elif away < home:
  print("Home win.")
else:
  print("Draw.")
